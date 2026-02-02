class Course:
    def __init__(self, name):
        self.name = name
    
    def get_duration(self):
        return "12 Weeks (Standard)"

class IntensiveCourse(Course):
    def get_duration(self): 
        # Polymorphism: 
        return "8 Weeks (Intensive)"

def get_catalog():
    return [
        Course("Web Development"),
        IntensiveCourse("Data Science Boot Camp"),
        Course("Cyber Security"),
        IntensiveCourse("AI & Machine Learning"),
        Course("Software Engineering"),
        IntensiveCourse("Cloud Computing Sprint"),
        Course("Digital Marketing"),
        IntensiveCourse("UX/UI Design Intensive")
    ]