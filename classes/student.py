from .person import Person
import csv 
class Student(Person):
        all_students = []

        def __init__(self, name, age, role , school_id, password):
            super().__init__(name, age, password, role)
            self.school_id = school_id

        def __repr__(self):
            return f"{self.name} {self.age} {self.school_id} {self.password} {self.role}"

        @classmethod
        def loading_all_student(cls):
        #    csvfile = with open('./data/students.csv', 'r', newline='')
           with open('./data/students.csv' ,'r', newline='') as csvfile :
                reader = csv.DictReader(csvfile)
                for raw in reader:
                     cls.all_students.append(Student(**raw))
                return cls.all_students
           
           
           
        

    
