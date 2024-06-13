from .person import Person

class Staff(Person):
    def __init__(self, name, age, role, employee_id, password):
        super().__init__(name, age, password, role)
        self.employee_id = employee_id

    def __repr__(self):

        return f"{self.name} {self.age} {self.role} {self.employee_id} {self.password}"
    


