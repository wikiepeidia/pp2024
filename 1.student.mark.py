'''
recommendation: use IF-ELSE: detect student whether exist, couse whether exist,etc. Do a huge while loop.
can use: https://github.com/LezardValeth97/pp2024
'''

def studentinfo():
    student=[]
    numstdnt=int(input("Enter number of student: "))
    for _ in range(numstdnt):
        while True:
            try:
                stdntid=int(input("Enter student id: "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer for student id.")
        name=input("Enter student name: ")
        dob=input("Enter student date of birth: ")
        student.append({"id":stdntid,"name":name,"dob":dob})
    return student

def coruseinfo():
    course=[]
    numcourse=int(input("Enter number of course: "))
    for _ in range(numcourse):
        while True:
            try:
                courseid = int(input("Enter course id: "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer for course id.")
        coursename=input("Enter course name: ")
        course.append({"id":courseid,"name":coursename})
    return course


def markforcouse(student,course):
    mark=[]
    for i in student:
        for j in course:
            while True:
                try:
                    mark.append({"student":i,"course":j,"mark":int(input(f"Enter mark for student {i['name']} in course {j['name']}: "))})
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer for mark.")
    return mark

def courselist(course):
    print("Course list: ")
    for i in course:
        print(f"ID: {i['id']}, Name: {i['name']}")

def liststudent(student):
    print("Student list: ")
    for i in student:
        print(f"ID: {i['id']}, Name: {i['name']}, DOB: {i['dob']}")

def showmarks(course,students,mark):
    print("Student marks: ")
    for i in mark:
        for j in course:
            if i['course']['id']==j['id']:
                for k in students:
                    if i['student']['id']==k['id']:
                        print(f"Student: {k['name']}, Course: {j['name']}, Mark: {i['mark']}")
#implement
students=studentinfo()

course=coruseinfo()

courselist(course)

liststudent(students)

mark=markforcouse(students,course)

showmarks(course,students,mark)


