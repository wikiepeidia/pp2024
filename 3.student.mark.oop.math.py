#is having problem with CURSE module.
import math
import numpy as np
try:
    import curses
except ImportError:
    import windows_curses as curses # type: ignore

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
        self.mark = mark


class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def input_student_info(self, stdscr):
        curses.echo()
        stdscr.clear()
        stdscr.addstr(2, 0, "Enter number of students: ")
        stdscr.refresh()
        num_student = int(stdscr.getstr().decode('utf-8'))
        for i in range(num_student):
            stdscr.addstr(4 + i * 3, 0, f"Enter student {i + 1} id: ")
            stdscr.refresh()
            student_id = stdscr.getstr().decode('utf-8')
            stdscr.addstr(5 + i * 3, 0, f"Enter student {i + 1} name: ")
            stdscr.refresh()
            name = stdscr.getstr().decode('utf-8')
            stdscr.addstr(6 + i * 3, 0, f"Enter student {i + 1} dob: ")
            stdscr.refresh()
            dob = stdscr.getstr().decode('utf-8')
            self.students.append(Student(student_id, name, dob))
        curses.noecho()

    def input_course_info(self, stdscr):
        curses.echo()
        stdscr.clear()
        stdscr.addstr(2, 0, "Enter number of courses: ")
        stdscr.refresh()
        num_course = int(stdscr.getstr().decode('utf-8'))
        for i in range(num_course):
            stdscr.addstr(4 + i * 3, 0, f"Enter course {i + 1} id: ")
            stdscr.refresh()
            course_id = stdscr.getstr().decode('utf-8')
            stdscr.addstr(5 + i * 3, 0, f"Enter course {i + 1} name: ")
            stdscr.refresh()
            name = stdscr.getstr().decode('utf-8')
            stdscr.addstr(6 + i * 3, 0, f"Enter course {i + 1} credit: ")
            stdscr.refresh()
            credit = int(stdscr.getstr().decode('utf-8'))
            self.courses.append(Course(course_id, name, credit))
        curses.noecho()

    def input_marks(self, stdscr):
        curses.echo()
        stdscr.clear()
        stdscr.addstr(2, 0, "\nEnter marks for each student in a selected course: ")
        stdscr.refresh()
        for course in self.courses:
            stdscr.addstr(4, 0, f"\nCourse: {course.name} (id: {course.id})")
            stdscr.refresh()
            for student in self.students:
                stdscr.addstr(5, 0, f"Enter mark for student {student.name} (id: {student.id}): ")
                stdscr.refresh()
                mark = float(stdscr.getstr().decode('utf-8'))
                mark = math.floor(mark * 10) / 10.0  # Round down to 1-digit decimal
                self.marks.append(Mark(course.id, student.id, mark))
        curses.noecho()

    def list_students(self, stdscr):
        stdscr.clear()
        stdscr.addstr(2, 0, "\nList of students: ")
        for i, student in enumerate(self.students):
            stdscr.addstr(3 + i, 0, str(student))
        stdscr.refresh()

    def list_courses(self, stdscr):
        stdscr.clear()
        stdscr.addstr(2, 0, "\nList of courses: ")
        for i, course in enumerate(self.courses):
            stdscr.addstr(3 + i, 0, str(course))
        stdscr.refresh()

    def show_student_marks(self, stdscr):
        curses.echo()
        stdscr.clear()
        stdscr.addstr(2, 0, "Enter student id: ")
        stdscr.refresh()
        student_id = stdscr.getstr().decode('utf-8')
        for course in self.courses:
            for mark in self.marks:
                if mark.course_id == course.id and mark.student_id == student_id:
                    stdscr.addstr(3, 0, f"Course: {course.name}, Mark: {mark.mark}")
        stdscr.refresh()
        curses.noecho()

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

    def curses_main(self, stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, "Welcome to the School Management System")
        stdscr.refresh()
        curses.napms(2000)
        stdscr.clear()

        self.input_student_info(stdscr)
        self.input_course_info(stdscr)
        self.input_marks(stdscr)
        self.calculate_gpa()
        self.sort_students_by_gpa()
        self.list_students(stdscr)
        self.list_courses(stdscr)
        self.show_student_marks(stdscr)

        stdscr.addstr(0, 0, "Press any key to exit...")
        stdscr.refresh()
        stdscr.getch()


if __name__ == "__main__":
    school = School()
    curses.wrapper(school.curses_main)