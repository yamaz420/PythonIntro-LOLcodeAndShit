from wheel import Wheel
import random

class Car:

    nr_of_wheels = 4

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.wheels = []
        self.install_wheels()

    def install_wheels(self):
        for i in range(self.nr_of_wheels):
            condition = random.randint(40-100)
            self.wheels.append(Wheel(condition)) #here we append an instande of the class wheel in every iteration

    def to_string(self):
        print(f"Car: {self.model} from the year {self.year}.")

    def check_condition_of_wheels(self):
        positions = ("From left", "From right", "rear left", "rear Right")
        print("Condition of wheels: ")
        for i in range(self.nr_of_wheels):
            print(f"{positions[i]}: {self.wheels[i].condition}.)


