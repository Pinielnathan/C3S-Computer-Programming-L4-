class Student:
    def __init__(self, name):
        self.name = name

    def get_record_format(self, account_id, duration):
        return f"STU: {self.name} | {account_id} | DUR: {duration}"
