class Teacher:
    def __init__(self, name, subjects, max_hours):
        self.name = name
        self.subjects = subjects
        self.max_hours = max_hours

    def __str__(self):
        return f"Teacher(name={self.name}, subjects={self.subjects}, max_hours={self.max_hours})"
