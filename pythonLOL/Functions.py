### Functions
# typ som static funktioner i java
# functions in python are basically the same as static methos in Java but they have a couple of smsll differences

#syntax for function
# def add_two_numbers(num1, num2):
#     sum = num1 + num2
#     return sum
# print(add_two_numbers(43, 64))#107

# def subtract_two_numbers(num1, num2): return num1 - num2
# print (subtract_two_numbers(68, 34)) #34

def calculate(num1, num2, operator = "+"):
    if operator == "+": 
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
        print("that is not an operator")
print(calculate(34,23))
print(calculate(34,23, "-"))
print(calculate(34,23, "*"))
print(calculate(34,23, "&"))
 