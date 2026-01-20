class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
    def get_info(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"

    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email

    @classmethod
    def from_dict(cls, data):
        return cls(id=data.get('id'), name=data.get('name'), email=data.get('email'))
    
class Student(User):
    def __init__(self, id, name, email, grade_level):
        super().__init__(id, name, email)
        self.grade_level = grade_level

    def get_role(self):
        return "student"

    def get_access_level(self):
        return "access to lessons"
    
class Teacher(User):
    def __init__(self, id, name, email, subject):
        super().__init__(id, name, email)
        self.subject = subject

    def get_role(self):
        return "teacher"

    def get_access_level(self):
        return "access to editing"
