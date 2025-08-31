import sqlite3

DB_NAME = "students.db"

def init_db():
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    # Create table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            roll TEXT,
            name TEXT,
            subject TEXT,
            score INTEGER,
            class_name TEXT
        );
    """)
    con.commit()
    con.close()


def get_subjects():
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute("SELECT DISTINCT subject FROM students;")
    subjects = [row[0] for row in cur.fetchall()]
    con.close()
    return subjects


def get_toppers(subject):
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute("""
        SELECT roll, name, score 
        FROM students 
        WHERE subject = ?
        ORDER BY score DESC
        LIMIT 3;
    """, (subject,))
    toppers = cur.fetchall()  # [(roll, name, score), ...]
    con.close()
    return toppers

    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute("SELECT DISTINCT subject FROM grades;")

    toppers = cur.fetchall()  # [(roll, name, score), ...]
    con.close()
    return toppers
