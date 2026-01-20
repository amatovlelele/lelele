class Lesson:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
    def __repr__(self):
        return f"Lesson(title='{self.title}', duration={self.duration})"