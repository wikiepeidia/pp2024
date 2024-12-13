import math
import numpy as np

class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob
        self.gpa = 0.0

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, DOB: {self.dob}, GPA: {self.gpa:.1f}"


class Course:
    def __init__(self, course_id, name, credit):
        self.id = course_id
        self.name = name
        self.credit = credit

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Credit: {self.credit}"


class Mark:
    def __init__(self, course_id, student_id, mark):
        self.course_id = course_id
        self.student_id = student_id
        self.mark = math.floor(mark * 10) / 10.0



class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []  
        self.marks_array = None 
        self.credits_array = None  

    def input_student_info(self):
        while True:
            try:
                num_student = int(input("Enter number of students: "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
        
        for _ in range(num_student):
            student_id = input("Enter student id: ")
            name = input("Enter student name: ")
            dob = input("Enter student dob: ")
            self.students.append(Student(student_id, name, dob))

    def input_course_info(self):
        while True:
            try:
                num_course = int(input("Enter number of courses: "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
        
        for _ in range(num_course):
            course_id = input("Enter course id: ")
            name = input("Enter course name: ")
            while True:
                try:
                    credit = int(input("Enter course credit: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")
            self.courses.append(Course(course_id, name, credit))
        
       
        self.credits_array = np.array([course.credit for course in self.courses])

    def input_marks(self):
        print("\nEnter marks for each student in a selected course: ")
        marks_matrix = []
        
        for course in self.courses:
            course_marks = []
            print(f"\nCourse: {course.name} (id: {course.id})")
            for student in self.students:
                while True:
                    try:
                        mark = float(input(f"Enter mark for student {student.name} (id: {student.id}): "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                course_marks.append(mark)
            marks_matrix.append(course_marks)
        
      
        self.marks_array = np.array(marks_matrix)

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

    def list_students(self):
        print("\nList of students: ")
        for student in self.students:
            print(student)
    
    def main(self):
        self.input_student_info()
        self.input_course_info()
        self.input_marks()
        self.calculate_gpa()
        self.sort_students_by_gpa()
        self.list_students()
        
        print("\nProgram has ended.")


if __name__ == "__main__":
    school = School()
    school.main()