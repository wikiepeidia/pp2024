import numpy as np
from .student import Student
from .course import Course
from .mark import Mark

class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []  # List of Mark objects
        self.marks_array = None
        self.credits_array = None

    def calculate_gpa(self):
        if self.marks_array is None or self.credits_array is None:
            print("Marks or credits data is missing.")
            return

        weighted_marks = self.marks_array.T @ self.credits_array
        total_credits = np.sum(self.credits_array)
        gpas = weighted_marks / total_credits

        for student, gpa in zip(self.students, gpas):
            student.gpa = gpa

    def sort_students_by_gpa(self):
        sorted_indices = np.argsort([-student.gpa for student in self.students])
        self.students = [self.students[i] for i in sorted_indices]
