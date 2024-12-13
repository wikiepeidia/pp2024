class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.gpa = 0.0

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, DOB: {self.dob}, GPA: {self.gpa:.1f}"