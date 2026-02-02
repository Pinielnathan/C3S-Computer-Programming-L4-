class StudentAccount:
    def __init__(self, student_id): 
        self.__student_id = student_id 
        self.__status = "Active"

    def get_secure_id(self):
        return f"ID-{self.__student_id}"

    def get_status(self):
        return self.__status