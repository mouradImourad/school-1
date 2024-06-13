from .student import Student
class School:

    def __init__(self, name):

        self.name = name
        self.student = []
        self.staff = []

    def __repr__(self):
        return f"{self.name}"
     
    def add_student(self, new_student):
        self.student.append(Student(**new_student))


        