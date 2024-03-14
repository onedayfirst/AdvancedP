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