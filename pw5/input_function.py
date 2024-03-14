from domains.person import Student
from domains.course import Course

from math import floor
def input_student(students):
    num_student = int(input("Enter the number of student: "))
    for i in range(num_student):
        print(f"Student {i + 1}")
        id = input("\tEnter student's id: ")
        name = input("\tEnter student's name: ")
        dob = input("\tEnter student's DoB: ")
        student = Student(id, name, dob)
        students.append(student)

    with open("student.txt", "w") as student_file:
        student_file.write("id, name, DoB\n")
        for student in students:
            student_file.write(f"{student.id}, {student.name}, {student.dob}\n")    

def input_course(courses):
    num_course = int(input("Enter the number of courses: "))
    for i in range(num_course):
        print(f"Course {i + 1}")
        id = input("\tEnter course id: ")
        name = input("\tEnter course name: ")
        list = []
        credit = int(input("\tEnter course credit: "))
        course = Course()
        course.set_id(id)
        course.set_name(name)
        course.set_list_students(list)
        course.set_credit(credit)
        courses.append(course)
    with open("course.txt", "w") as course_file:
        course_file.write("id, name, list,credit\n")
        for course in courses:
            course_file.write(f"{course.get_id()}, {course.get_name()}, {course.get_list_students()}, {course.get_credit()}\n")

def add_student_mark_in_course(select_course, courses, students):
    for course in courses:
        if select_course.lower() == course.get_name():
            for student in students:
                mark = floor(float(input(f"\tEnter mark for {student.name}: ")))
                student.course_mark[course] = mark

            print(f"\nCourse: {course.get_name()}")
            course.set_list_students(students)
            for student in course.get_list_students():
                for course, mark in student.course_mark.items():
                    if course.get_name() == select_course:
                        print(f"\t{student.name}: {mark}")

def print_GPA(students):
    for student in students:
        total_mark = 0
        total_credit = 0
        for course, mark in student.course_mark.items():
            total_mark += mark * course.get_credit()
            total_credit += course.get_credit()
        student.GPA = total_mark / total_credit
        print(f"{student.name} has GPA: {student.GPA}")

        