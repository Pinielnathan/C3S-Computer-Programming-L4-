from user_base import User

class Student(User):
    def __init__(self, name):
        self.name = name

    def get_access_level(self):
        return "Student Access: View-Only Course Materials"

    def get_record_format(self, account_id, duration):
        return f"STU: {self.name} | {account_id} | DUR: {duration}"