import curses
from domains.student import Student
from domains.course import Course
from domains.mark import Mark
import math
def input_student_info(stdscr, school):
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
        school.add_student(Student(student_id, name, dob))
    curses.noecho()

def input_course_info(stdscr, school):
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
        school.add_course(Course(course_id, name, credit))
    curses.noecho()

def input_marks(stdscr, school):
    curses.echo()
    stdscr.clear()
    stdscr.addstr(2, 0, "\nEnter marks for each student in a selected course: ")
    stdscr.refresh()
    for course in school.courses:
        stdscr.addstr(4, 0, f"\nCourse: {course.name} (id: {course.id})")
        stdscr.refresh()
        for student in school.students:
            stdscr.addstr(5, 0, f"Enter mark for student {student.name} (id: {student.id}): ")
            stdscr.refresh()
            mark = float(stdscr.getstr().decode('utf-8'))
            mark = math.floor(mark * 10) / 10.0  # Round down to 1-digit decimal
            school.add_mark(Mark(course.id, student.id, mark))
    curses.noecho()