
from domains.student import Student
from domains.course import Course
import numpy as np
def input_students(school):
    num_student = int(input("Enter number of students: "))
    for _ in range(num_student):
        student_id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student dob: ")
        school.students.append(Student(student_id, name, dob))

def input_courses(school):
    num_course = int(input("Enter number of courses: "))
    for _ in range(num_course):
        course_id = input("Enter course id: ")
        name = input("Enter course name: ")
        credit = int(input("Enter course credit: "))
        school.courses.append(Course(course_id, name, credit))
    
    school.credits_array = np.array([course.credit for course in school.courses])

def input_marks(school):
    marks_matrix = []
    for course in school.courses:
        course_marks = []
        print(f"\nCourse: {course.name} (id: {course.id})")
        for student in school.students:
            mark = float(input(f"Enter mark for student {student.name} (id: {student.id}): "))
            course_marks.append(mark)
        marks_matrix.append(course_marks)
    school.marks_array = np.array(marks_matrix)
