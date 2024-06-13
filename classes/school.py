
class School:

    def __init__(self, name):

        self.name = name
        self.student = []
        self.staff = []

    def __repr__(self):
        return f"{self.name}"
     