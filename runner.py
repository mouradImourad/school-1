from classes.school import School 
from classes.student import Student
from classes.staff import Staff

"""
x. school class 
2. student class
3. staff class 
4. user class
5. load students from csv
6. make cli 
7. 

"""
ridgemont = School('Ridgemont High') 

print(ridgemont)
momo = Student("mourad", 43, "student", 656, "mmm")
jordan = Staff("jordan", 30, "TA", 898, "ssss" )
print(momo)
print(jordan)

# student_info = {'name' : 'Diana', 'password' : 'password', 'school_id' : 12345, 'age' : 17, 'role' : 'Student'}
all_students = Student.loading_all_student()

print(all_students)
new_student = { 
    "name": "mmm",
    "age": 40,
    "role": "student",
    "school_id": 98997,
    "password": "ccc"  }
print(School.student)
School.add_student(new_student)
print(School.student)