import math
from .student import Student
from .course import Course
from .mark import Mark

class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)

    def add_mark(self, mark):
        self.marks.append(mark)

    def calculate_gpa(self):
        for student in self.students:
            total_credits = 0
            total_weighted_marks = 0
            for mark in self.marks:
                if mark.student_id == student.id:
                    course = next(course for course in self.courses if course.id == mark.course_id)
                    total_credits += course.credit
                    total_weighted_marks += mark.mark * course.credit
            if total_credits > 0:
                student.gpa = total_weighted_marks / total_credits

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda student: student.gpa, reverse=True)