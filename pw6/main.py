import os
import json
import zipfile
from domains.school import School
from domains.student import Student
from domains.course import Course
import numpy as np
import input as inp_module
import output

# Ensure the pw6 folder exists
BASE_DIR = "pw6"
os.makedirs(BASE_DIR, exist_ok=True)

def compress_files():
    """Compress students.txt, courses.txt, and marks.txt into pw6/students.dat."""
    filepath = os.path.join(BASE_DIR, "students.dat")
    with zipfile.ZipFile(filepath, "w") as zipf:
        for filename in ["students.txt", "courses.txt", "marks.txt"]:
            file_to_zip = os.path.join(BASE_DIR, filename)
            if os.path.exists(file_to_zip):
                zipf.write(file_to_zip, os.path.basename(file_to_zip))

def decompress_files():
    """Decompress pw6/students.dat and extract its content into pw6."""
    filepath = os.path.join(BASE_DIR, "students.dat")
    if os.path.exists(filepath):
        with zipfile.ZipFile(filepath, "r") as zipf:
            zipf.extractall(BASE_DIR)
    pass
def load_data(school):
    """Load data from decompressed files into the school object."""
    for filename, loader in [("students.txt", load_students), 
                             ("courses.txt", load_courses), 
                             ("marks.txt", load_marks)]:
        filepath = os.path.join(BASE_DIR, filename)
        if os.path.exists(filepath):
            loader(filepath, school)
    pass
def load_students(filepath, school):
    """Load students data into the School object."""
    with open(filepath, "r") as file:
        students_data = json.load(file)
        for student in students_data:
            school.students.append(Student(student["id"], student["name"], student["dob"]))

def load_courses(filepath, school):
    """Load courses data into the School object."""
    with open(filepath, "r") as file:
        courses_data = json.load(file)
        for course in courses_data:
            school.courses.append(Course(course["id"], course["name"], course["credit"]))
    school.credits_array = np.array([course.credit for course in school.courses])

def load_marks(filepath, school):
    """Load marks data into the School object."""
    with open(filepath, "r") as file:
        marks_data = json.load(file)
        marks_matrix = []
        for course in school.courses:
            course_marks = [mark["mark"] for mark in marks_data if mark["course_id"] == course.id]
            marks_matrix.append(course_marks)
        school.marks_array = np.array(marks_matrix)

def main():
    school = School()

    # Decompress and load data if available
    if os.path.exists(os.path.join(BASE_DIR, "students.dat")):
        print("Detected students.dat.")
        choice = input("Would you like to (1) Display data, (2) Input new data, or (3) Overwrite data? Enter 1, 2, or 3: ")
        
        if choice == "1":
            decompress_files()
            load_data(school)
            school.calculate_gpa()
            school.sort_students_by_gpa()
            output.list_students(school)
            output.list_courses(school)
            return
        elif choice == "2":
            decompress_files()
            load_data(school)
        elif choice == "3":
            pass
        else:
            print("Invalid choice. Exiting.")
            return
    else:
        print("'students.dat' was not found.")

    # Input new data if necessary
    inp_module.input_students(school)
    inp_module.input_courses(school)
    inp_module.input_marks(school)

    # Process and output data
    school.calculate_gpa()
    school.sort_students_by_gpa()
    output.list_students(school)
    output.list_courses(school)
    
if __name__ == "__main__":
    main()
