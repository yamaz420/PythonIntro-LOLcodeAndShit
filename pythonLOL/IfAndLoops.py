#-----------!!!INDENTATION!!!-----------

# age = int(input("What is your age?"))
# if age >= 20: 
#   print("You are grown up, you can go to Systemet!")
# else: 
#     print("you are to young for systemet...")

# if age >= 20:
#   if age >= 30:
#     print("Allright, you can go to systemet for me, i hate showing ID")
#   else:
#       print("you can fo to systemet, just don't forget your ID...")
#     else: 
#         print("you are too young for systemet")

### "or" = "||"       "and" = "&&"
# if (day == "friday" or day == "Saturday") and age >= 18: 
#   print("is is a foot day to hit the club")
# elif day == "monday" or day == "tuseday":
#     print("noooo, i hate these days")

# numbers = [1,2,3,45]
# if 45 in numbers:
#   print("exists")
# else:
#   print("no existo")

# truthy and falsy values also exist in python. 
my_list = []
if my_list: # my_list.size() > 0 - in Java"
  print(my_list)
else:
  print("the list is empty")

i = 0   ## while-LOOP
while i < 10: 
  print (i, end = " ")
  i += 1

# for-each-LOOP
names = ["hej", "niklas", "Erik"]
for name in names:
  print(name, end = " ")
print(i, end = "\U0001F606") #Smiley ahahah #tackPelle

for i in range(10):
  print(i, end = " ")

for i in range (1,20,2):
  print (i, end= " ")

numbers = [1,24,12,52,26]
for i in range(len(numbers)):
  print(numbers[i], end = " ")

persons = [ #list=arraylist of persons
  {
    "name": "Erik",
    "age": 28
  },
  {
    "name": "Martin",
    "age": 34
  },
  {
    "name": "Louise",
    "age": 30
  }
]
for person in persons:
  print(person)

'''
multi-line-Commment
lalala
hahahahhahahahahahaHAH.
'''
just_names = [person["name"] for person in persons]
print(just_names)

over_30 = [person for person in persons if person["age"] >= 30] ##sortera persons-lista över 30
print(over_30)
