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