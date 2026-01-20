class Course:
    total_courses = 0

    def __init__(self, id, title, description, price):
        self.id = id
        self.title = title
        self.description = description
        self.price = price
        self.lessons = []
        Course.total_courses += 1

    def __str__(self):
        return f"Course(title='{self.title}', description='{self.description}', price={self.price})"
    
    def __len__(self):
        return len(self.lessons)

    def __eq__(self, other):
        if not isinstance(other, Course):
            return False
        return self.id == other.id

    @classmethod
    def get_total_courses(cls):
        return cls.total_courses

    @staticmethod
    def check_difficulty(lessons_count):
        if lessons_count > 10:
            return "Hard"
        return "Easy"
