import os
import numpy as np
import json
from domains.student import Student
from domains.course import Course


BASE_DIR = "pw5"
os.makedirs(BASE_DIR, exist_ok=True)

def save_to_file(filename, data):
    """Utility function to save data to a file in the pw5 folder."""
    filepath = os.path.join(BASE_DIR, filename)
    with open(filepath, 'w') as file:
        json.dump(data, file)

def input_students(school):
    """Input student information and save to students.txt."""
    students_data = []
    num_student = int(input("Enter number of students: "))
    for _ in range(num_student):
        student_id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student dob: ")
        student = Student(student_id, name, dob)
        school.students.append(student)
        students_data.append({'id': student_id, 'name': name, 'dob': dob})
    save_to_file("students.txt", students_data)

def input_courses(school):
    """Input course information and save to courses.txt."""
    courses_data = []
    num_course = int(input("Enter number of courses: "))
    for _ in range(num_course):
        course_id = input("Enter course id: ")
        name = input("Enter course name: ")
        credit = int(input("Enter course credit: "))
        course = Course(course_id, name, credit)
        school.courses.append(course)
        courses_data.append({'id': course_id, 'name': name, 'credit': credit})
    school.credits_array = np.array([course.credit for course in school.courses])
    save_to_file("courses.txt", courses_data)

def input_marks(school):
    """Input marks for students and save to marks.txt."""
    marks_data = []
    marks_matrix = []
    for course in school.courses:
        course_marks = []
        print(f"\nCourse: {course.name} (id: {course.id})")
        for student in school.students:
            mark = float(input(f"Enter mark for student {student.name} (id: {student.id}): "))
            course_marks.append(mark)
            marks_data.append({'course_id': course.id, 'student_id': student.id, 'mark': mark})
        marks_matrix.append(course_marks)
    school.marks_array = np.array(marks_matrix)
    save_to_file("marks.txt", marks_data)
