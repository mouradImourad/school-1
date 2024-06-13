class Student:
    def __init__(self, name, age, school_id, password, role="Student"):
        self.name = name
        self.age = age
        self.school_id = school_id
        self.password = password
        self.role = role 

    def __repr__(self):
        return f"{self.name} {self.age} {self.school_id} {self.password} {self.role}"
                

    
