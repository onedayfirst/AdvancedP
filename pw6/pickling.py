import pickle

def storeData(students, courses):
    with open('students', 'ab') as file:
        pickle.dump(students, file)
    with open('courses', 'ab') as course_file:
        pickle.dump(courses, course_file)

def loadData():
    with open('students', 'rb') as student_list:
        students = pickle.load(student_list)
        for student in students:
            print(student)


