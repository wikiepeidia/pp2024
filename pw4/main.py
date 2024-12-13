from domains.school import School
import input
import output

def main():
    school = School()

    input.input_students(school)
    input.input_courses(school)
    input.input_marks(school)

    school.calculate_gpa()
    school.sort_students_by_gpa()

    output.list_students(school)
    output.list_courses(school)

if __name__ == "__main__":
    main()
