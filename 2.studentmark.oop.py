class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, DOB: {self.dob}"


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
        self.mark = mark


class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

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

    def input_marks(self):
        print("\nEnter marks for each student in a selected course: ")
        for course in self.courses:
            print(f"\nCourse: {course.name} (id: {course.id})")
            for student in self.students:
                while True:
                    try:
                        mark = float(input(f"Enter mark for student {student.name} (id: {student.id}): "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                self.marks.append(Mark(course.id, student.id, mark))

    def list_students(self):
        print("\nList of students: ")
        for student in self.students:
            print(student)

    def list_courses(self):
        print("\nList of courses: ")
        for course in self.courses:
            print(course)

    def show_student_marks(self):
        student_id = input("Enter student id: ")
        for course in self.courses:
            for mark in self.marks:
                if mark.course_id == course.id and mark.student_id == student_id:
                    print(f"Course: {course.name}, Mark: {mark.mark}")

    def main(self):
        self.input_student_info()
        self.input_course_info()
        self.input_marks()
        self.list_students()
        self.list_courses()
        self.show_student_marks()


if __name__ == "__main__":
    school = School()
    school.main()