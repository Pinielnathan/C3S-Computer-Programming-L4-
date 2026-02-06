import os
from user_base import DataHandler

class DatabaseManager(DataHandler):
    def __init__(self, filename="institution_db.txt"):
        self.filename = filename

    def save(self, data):
        with open(self.filename, "a") as f:
            f.write(data + "\n")

    def read_all(self):
        if not os.path.exists(self.filename): return "No database found."
        with open(self.filename, "r") as f:
            content = f.read()
            return content if content.strip() else "Database is empty."

    def delete_record(self, name):
        if not os.path.exists(self.filename): return False
        with open(self.filename, "r") as f:
            lines = f.readlines()
        found = False
        with open(self.filename, "w") as f:
            for line in lines:
                if name.lower() not in line.lower():
                    f.write(line)
                else:
                    found = True
        return found

    def clear_database(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
            return True
        return False
