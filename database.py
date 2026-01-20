import sqlite3

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('lms.db')
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def create_tables(conn):
    cursor = conn.cursor()
    
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            role TEXT NOT NULL,
            extra_info TEXT
        );
    ''')

   
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price REAL
        );
    ''')

    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lessons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_id INTEGER,
            title TEXT NOT NULL,
            duration INTEGER,
            FOREIGN KEY (course_id) REFERENCES courses (id)
        );
    ''')

    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS enrollments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            course_id INTEGER,
            progress INTEGER DEFAULT 0,
            FOREIGN KEY (student_id) REFERENCES users (id),
            FOREIGN KEY (course_id) REFERENCES courses (id),
            UNIQUE(student_id, course_id)
        );
    ''')
    conn.commit()