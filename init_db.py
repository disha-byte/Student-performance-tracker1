import sqlite3

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
                FOREIGN KEY(roll_number) REFERENCES students(roll_number)
            )''')

print("✅ Database and tables created successfully!")

conn.commit()
conn.close()
