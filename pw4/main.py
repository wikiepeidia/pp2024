import curses
from domains.school import School
import input as inp
import output as out

def curses_main(stdscr):
    school = School()
    stdscr.clear()
    stdscr.addstr(0, 0, "Welcome to the School Management System")
    stdscr.refresh()
    curses.napms(2000)
    stdscr.clear()

    inp.input_student_info(stdscr, school)
    inp.input_course_info(stdscr, school)
    inp.input_marks(stdscr, school)
    school.calculate_gpa()
    school.sort_students_by_gpa()
    out.list_students(stdscr, school)
    out.list_courses(stdscr, school)
    out.show_student_marks(stdscr, school)

    stdscr.addstr(0, 0, "Press any key to exit...")
    stdscr.refresh()
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(curses_main)