from student import Student
from person import Person
from car import Car

student = Student("erik", 28)
print(type(student))

volvo = Car("Volvo", 2016)
volvo.to_string()
volvo.check_condition_of_wheels()

