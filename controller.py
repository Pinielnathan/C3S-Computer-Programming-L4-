from person import Student
from account import StudentAccount
from course import Course, IntensiveCourse, get_catalog
from database_manager import DatabaseManager

class SystemController:
    def __init__(self):
        self.db = DatabaseManager()

    def run(self):
        while True:
            print("\n" + "="*45)
            print("   INSTITUTION MANAGEMENT SYSTEM ")
            print("="*45)
            print("1. [Enrollment]   Register New Student")
            print("2. [Courses]      View Course Catalog")
            print("3. [Records]      View Registration Database")
            print("4. [Manage]       Edit/Delete Records")
            print("5. [Security]     Check User Permissions")
            print("6. [System]       Exit")
            
            choice = input("\nSelect a system option (1-6): ")

            if choice == "1":
                name = input("Enter Full Name: ")
                s_id = input("Assign Student ID: ")
                while True:
                    print("\nSelect Type: 1. Standard | 2. Intensive")
                    c_choice = input("Choice: ")
                    if c_choice in ["1", "2"]:
                        student = Student(name)
                        acc = StudentAccount(s_id)
                        crs = IntensiveCourse("Course") if c_choice == "2" else Course("Course")
                        # Delegation: Formatting handled by the Student class
                        self.db.save(student.get_record_format(acc.get_secure_id(), crs.get_duration()))
                        print(f"\nSUCCESS: {name} enrolled.")
                        break
                    print("Invalid selection.")
            elif choice == "2":
                print("\n" + "="*15 + " CATALOG " + "="*15)
                for i, c in enumerate(get_catalog(), 1):
                    print(f"{i}. {c.name:25} | {c.get_duration()}")
            elif choice == "3":
                print("\n" + "="*15 + " RECORDS " + "="*15)
                print(self.db.read_all())
            elif choice == "4":
                sub = input("\n1. Delete Student | 2. Clear Database: ")
                if sub == "1":
                    print("Removed." if self.db.delete_record(input("Name: ")) else "Not Found.")
                elif sub == "2":
                    print("Database Cleared." if self.db.clear_database() else "Empty.")
            elif choice == "5":
                u = Student("Security_Audit")
                print(f"User: {u.name} | {u.get_access_level()}")
            elif choice == "6":
                print("System offline. Goodbye!")
                break
            input("\nPress Enter to continue...")