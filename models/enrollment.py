class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.__progress = 0

    def get_progress(self):
        return self.__progress
    
    def update_progress(self, new_progress):
        if 0 <= new_progress <= 100:
            self.__progress = new_progress
    
    def __str__(self):
        return f"Enrollment(student={self.student.name}, course={self.course.title}, progress={self.__progress}%)"