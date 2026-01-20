import sqlite3

class EnrollmentService:
    @staticmethod
    def enroll_student(conn, student_id, course_id):
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO enrollments (student_id, course_id, progress) VALUES (?, ?, ?)", 
                           (student_id, course_id, 0))
            conn.commit()
            print(f"Студент {student_id} успешно записан на курс {course_id}.")
        except sqlite3.IntegrityError:
            print("Ошибка: Студент уже записан на этот курс или курс/студент не существует.")
