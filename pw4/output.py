import curses

def list_students(stdscr, school):
    stdscr.clear()
    stdscr.addstr(2, 0, "\nList of students: ")
    for i, student in enumerate(school.students):
        stdscr.addstr(3 + i, 0, str(student))
    stdscr.refresh()

def list_courses(stdscr, school):
    stdscr.clear()
    stdscr.addstr(2, 0, "\nList of courses: ")
    for i, course in enumerate(school.courses):
        stdscr.addstr(3 + i, 0, str(course))
    stdscr.refresh()

def show_student_marks(stdscr, school):
    curses.echo()
    stdscr.clear()
    stdscr.addstr(2, 0, "Enter student id: ")
    stdscr.refresh()
    student_id = stdscr.getstr().decode('utf-8')
    for course in school.courses:
        for mark in school.marks:
            if mark.course_id == course.id and mark.student_id == student_id:
                stdscr.addstr(3, 0, f"Course: {course.name}, Mark: {mark.mark}")
    stdscr.refresh()
    curses.noecho()