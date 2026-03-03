import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

cursor.execute("INSERT INTO students (name, age) VALUES ('Alice', 23)")

conn.commit()

cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

conn.close()