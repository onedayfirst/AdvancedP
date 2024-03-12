# Ask user the number of student
while True:
    num_student = input("Enter the number of student: ")
    try:
        num_student = int(num_student)
        if num_student >= 0:
            break
        else:
            print("\nNumber of student can't be less than 0.\n")
    except ValueError:
        print("\nYour input is not a number.\n")

# Ask user information of student
students = []
student = {}
for i in range(num_student):
    print(f"Student {i + 1}")
    id = input("\tEnter student id: ")
    name = input("\tEnter student name: ")
    dob = input("\tEnter student DoB: ")
    students.append({"id": id, "name": name, "DoB": dob})

print(students)
courses = []


# Ask user the number of course
while True:
    num_course = input("Enter the number of course: ")
    try:
        num_course = int(num_course)
        if num_course >= 0:
            break
        else:
            print("\nNumber of course can't be less than 0.\n")
    except ValueError:
        print("\nYour input is not a number.\n")

# Ask user the information of course
for i in range(num_course):
    print(f"Course {i+1}")
    id = input("\tEnter course id: ")
    name = input("\tEnter course name: ")
    list_student = students
    courses.append({"id": id, "name": name})


# Ask the course that the user want to interact
selected_course = input("Enter a name of course that you want: ")
for index,cou in enumerate(courses):
    print(cou['name'])
    if selected_course.lower() == cou['name'].lower():
        cou['list_student']= list_student
        for stu in cou['list_student']:
            stu['mark']= input(f"Enter mark for {stu['name']}: ")

            
print(f"{student.name}: {student.mark}")      
#Print student mark
for cou in courses:
    if cou['name'] == selected_course:
        print(f"Course: {cou['name']}")
        for stu in cou['list_student']:
            print(f"\t{stu['name']}: {stu['mark']}")
