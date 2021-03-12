from person import Person

class Student(Person):
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school

    def to_string(self):
        print(f"Name: {self.name}. age: {self.age}. school: {self.school}")

    #--------------------------------------------------------------------------------

    class Student(Person):
        def __init__(self, name, age, school):
            super().__init__(name, age)
            self.school
        def to_string(self):
            print(f"Name: {self.name}. age: {self.age}. school: {self.school}")