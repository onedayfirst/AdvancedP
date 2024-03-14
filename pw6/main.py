from math import floor
import input_function as i_f
from zipfile import ZipFile
import os
import pickling as pl

def get_all_file_paths(directory):
    file_paths = []

    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    return file_paths

def main():
    students = []
    i_f.input_student(students)
    courses = []
    i_f.input_course(courses)
    select_course = input("Enter your desired course: ")
    i_f.add_student_mark_in_course(select_course, courses, students)
    pl.storeData(students, courses)
    pl.loadData()
    sorted(students, key = lambda x: x.GPA)
    with open("mark.txt", "w") as mark_file:
        for course in courses:
            mark_file.write(f"Course: {course.get_name()}\n")
            for student in students:
                for cour, mark in student.course_mark.items():
                    if cour.get_name() == course.get_name():
                        mark_file.write(f"\t{student.name} : {mark}")

    directory = '/home/vietah/Documents/AdvancedP/pw5'
    file_paths = get_all_file_paths(directory)
    print('Following files will be zipped:')
    for file_name in file_paths:
        print(file_name)
main()