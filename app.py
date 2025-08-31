from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "vault_secret"

# Initialize Database
def init_db():
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students (
                    roll_number TEXT PRIMARY KEY,
                    name TEXT NOT NULL
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS grades (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    roll_number TEXT,
                    subject TEXT,
                    marks INTEGER,
                    FOREIGN KEY (roll_number) REFERENCES students(roll_number)
                )''')
    conn.commit()
    conn.close()

init_db()

# Home Page
@app.route("/")
def home():
    return render_template("home.html")

# Add Student
@app.route("/add_student", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        roll = request.form["roll_number"]
        name = request.form["name"]
        subjects = request.form.getlist("subject[]")
        marks = request.form.getlist("marks[]")

        conn = sqlite3.connect("students.db")
        c = conn.cursor()
        try:
            c.execute("INSERT INTO students (roll_number, name) VALUES (?, ?)", (roll, name))
            for i in range(len(subjects)):
                if subjects[i] and marks[i]:
                    c.execute("INSERT INTO grades (roll_number, subject, marks) VALUES (?, ?, ?)",
                              (roll, subjects[i], int(marks[i])))
            conn.commit()
            flash("Student added successfully!", "success")
        except sqlite3.IntegrityError:
            flash("Roll Number already exists!", "danger")
        finally:
            conn.close()
        return redirect(url_for("home"))
    return render_template("add_student.html")

# View Students with average marks
@app.route("/view_students")
def view_students():
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    students = c.fetchall()
    student_data = []
    for student in students:
        c.execute("SELECT subject, marks FROM grades WHERE roll_number=?", (student[0],))
        grades = c.fetchall()
        avg_marks = None
        if grades:
            avg_marks = sum([g[1] for g in grades]) / len(grades)
        student_data.append({
            "roll_number": student[0],
            "name": student[1],
            "grades": grades,
            "avg_marks": avg_marks
        })
    conn.close()
    return render_template("view_students.html", students=student_data)

# Delete Student
@app.route("/delete_student/<roll>")
def delete_student(roll):
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("DELETE FROM grades WHERE roll_number=?", (roll,))
    c.execute("DELETE FROM students WHERE roll_number=?", (roll,))
    conn.commit()
    conn.close()
    flash("Student deleted successfully!", "success")
    return redirect(url_for("view_students"))

# Edit Student
@app.route("/edit_student/<roll>", methods=["GET", "POST"])
def edit_student(roll):
    conn = sqlite3.connect("students.db")
    c = conn.cursor()

    if request.method == "POST":
        name = request.form["name"]
        subjects = request.form.getlist("subject[]")
        marks = request.form.getlist("marks[]")

        c.execute("UPDATE students SET name=? WHERE roll_number=?", (name, roll))
        c.execute("DELETE FROM grades WHERE roll_number=?", (roll,))
        for i in range(len(subjects)):
            if subjects[i] and marks[i]:
                c.execute("INSERT INTO grades (roll_number, subject, marks) VALUES (?, ?, ?)",
                          (roll, subjects[i], int(marks[i])))
        conn.commit()
        conn.close()
        flash("Student details updated successfully!", "success")
        return redirect(url_for("view_students"))

    c.execute("SELECT name FROM students WHERE roll_number=?", (roll,))
    student = c.fetchone()
    c.execute("SELECT subject, marks FROM grades WHERE roll_number=?", (roll,))
    grades = c.fetchall()
    conn.close()
    return render_template("edit_student.html", roll=roll, student=student, grades=grades)

# Subject-wise Topper (one topper per subject)
@app.route("/subject_topper")
def subject_topper():
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("SELECT DISTINCT subject FROM grades")
    subjects = [row[0] for row in c.fetchall()]
    toppers = []

    for subj in subjects:
        c.execute('''SELECT students.name, grades.marks 
                     FROM grades 
                     JOIN students ON grades.roll_number = students.roll_number 
                     WHERE grades.subject=? 
                     ORDER BY grades.marks DESC, students.name ASC LIMIT 1''', (subj,))
        result = c.fetchone()
        if result:
            toppers.append((subj, result[0], result[1]))

    conn.close()
    return render_template("subject_topper.html", toppers=toppers)

# Overall Topper
@app.route("/overall_topper")
def overall_topper():
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute('''SELECT students.roll_number, students.name, AVG(marks) as avg_marks 
                 FROM students 
                 JOIN grades ON students.roll_number = grades.roll_number 
                 GROUP BY students.roll_number 
                 ORDER BY avg_marks DESC LIMIT 1''')
    topper = c.fetchone()
    conn.close()
    return render_template("overall_topper.html", topper=topper)

if __name__ == "__main__":
    app.run(debug=True)
