import sys
from database import create_connection, create_tables
from models.user import Student, Teacher
from models.cours import Course
from services.enrollment_service import EnrollmentService

def main():
    conn = create_connection()
    if conn is not None:
        create_tables(conn)
    else:
        print("Ошибка подключения к БД")
        return

    while True:
        print("1. Добавить студента")
        print("2. Добавить курс")
        print("3. Записать студента на курс")
        print("4. Показать все курсы")
        print("5. Выход")
        
        choice = input("Выберите действие: ")

        if choice == '1':
            name = input("Имя студента: ")
            email = input("Email: ")
            
            if Student.validate_email(email):
                cursor = conn.cursor()
                try:
                    cursor.execute("INSERT INTO users (name, email, role, extra_info) VALUES (?, ?, ?, ?)", 
                                   (name, email, "student", "Grade 1"))
                    conn.commit()
                    print("Студент добавлен!")
                except Exception as e:
                    print(f"Ошибка при добавлении: {e}")
            else:
                print("Некорректный email!")

        elif choice == '2':
            title = input("Название курса: ")
            desc = input("Описание: ")
            price = float(input("Цена: "))
            
           
            temp_course = Course(0, title, desc, price) 
            
            cursor = conn.cursor()
            cursor.execute("INSERT INTO courses (title, description, price) VALUES (?, ?, ?)", 
                           (title, desc, price))
            conn.commit()
            print(f"Курс '{title}' создан. Всего курсов в памяти: {Course.get_total_courses()}")

        elif choice == '3':
            s_id = input("ID студента: ")
            c_id = input("ID курса: ")
            EnrollmentService.enroll_student(conn, s_id, c_id)

        elif choice == '4':
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM courses")
            rows = cursor.fetchall()
            print("\nСписок курсов:")
            for row in rows:
                print(f"ID: {row[0]} | Название: {row[1]} | Цена: {row[3]}")
                
        elif choice == '5':
            print("Выход...")
            break
        else:
            print("Неверный выбор")

    conn.close()

if __name__ == '__main__':
    main()