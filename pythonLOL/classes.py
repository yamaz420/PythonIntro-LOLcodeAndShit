class Car:
    def __init__(self, model, top_speed):
        self.model = model
        self.top_speed = top_speed

    def to_string(self):
        print(f"Model: {self.model}. top speed: {self.top_speed} km/h")


class Student:
    school = "Handelsakademin"
    subjects = []

    def __init__(self, name):
        self.name = name

    def to_string(self):
        print(f"name: {self.name}. School: {self.school}" )

    def show_subjects(self):
        print(f"{self.name}: ", end="")
        for subject in self.subjects:
            print(f"{subject}", end=" ")
        print()

student = Student("erik")
student1 = Student("louise")
student2 = Student("martin")

student.to_string()
student1.to_string()
student2.to_string()
