zz = 10 #int
my_name = "Erik" #string    
height = 188.5 #float
is_cool = True #boolean
is_ready = False #boolean
print(my_name)

my_name = 40 #int
print(my_name);

p, y, z = "HEJ", 200, 1000
print(p)
print(y)
print(z)

# *, +, -, /, 

a = 5**2 #25
b = 3**3 #27
c = 5/ 2 #2.5 float
d = 5//2 #2 int-division
print(a,b,c,d) 
print(a + b)

age = 28
name = "Erik"
print("hello my name is {} and i am {} years old.".format(name,age))

print("hello, my name is {1} and i am {0} years old".format(age, name))
print("this awesome guys' name is {1}. {1} is {0} years old".format(age, name))
print("this boring dudes' name is {name} and i think he is {age} years old".format(age = 50, name = "Erik"))
print(f'hello, my name is {name} and i am {age} years old') #by prefixinf  the string with an "f". pythin understands it as a formatted string and lets u infuse variables inot the string
a = 10
b = 43
print(f"what is {a} times {b}? it's {a*b} ofcourse!")

# username = input("what is your username?")
# print(username)

# int() - casts to an int
# float() - casts to float
# str() casts to string
age= int(input("what is your age"))
print(type(age))
print(age)


