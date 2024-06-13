class Person:
    def __init__(self, name, age, password, role):
        self.name = name
        self.age = age
        self.password = password
        self.role = role 

    def __repr__(self):
        return f"{self.name} {self.age} {self.password} {self.role}"
                

    
