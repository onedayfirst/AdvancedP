from math import floor

class Person:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

    def work():
        print("A person need to work.")

class Student(Person):
    def __init__(self, id, name, dob):
        super().__init__(id, name, dob)
        self.course_mark = {}
        self.GPA = None
    # Polyorphism
    def work(self):
        print('Student need to take the course')

class Course:
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__list = None
        self.__credit = None

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_list_students(self, list):
        self.__list = list

    def set_credit(self, credit):
        self.__credit = credit

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name

    def get_list_students(self):
        return self.__list
    
    def get_credit(self):
        return self.__credit
    
students = []
num_student = int(input("Enter the number of student: "))
for i in range(num_student):
    print(f"Student {i + 1}")
    id = input("\tEnter student's id: ")
    name = input("\tEnter student's name: ")
    dob = input("\tEnter student's DoB: ")
    student = Student(id, name, dob)
    students.append(student)

courses = []
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

select_course = input("Enter your desired course: ")
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

for student in students:
    total_mark = 0
    total_credit = 0
    for course, mark in student.course_mark.items():
        total_mark += mark * course.get_credit()
        total_credit += course.get_credit()
    student.GPA = total_mark / total_credit
    print(f"{student.name} has GPA: {student.GPA}")

sorted(students, key = lambda x: x.GPA)
