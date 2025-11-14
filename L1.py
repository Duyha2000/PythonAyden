# https://docs.google.com/document/d/1pENdmsUGyAYbQezTJNoBo5FmLNruk7G4wu1vx8Qhfz0/edit?tab=t.6qky7ohf67bw
# How many data types in java?
# int, float, double, String,  "Hello" -> String  'H' -> char  true/false -> boolean
# a = 4 -> print(a)
# name = "Ayden"
# age = 23
# height = 173
# print("Full name: " + name + " age: " + str(age) + " height: " + str(height) )
# a = input("Enter a number: ")
# print(a)
# Ex: input a, b -> int
# print sum (a + b)
# a = int(input("Num a")) # "2"
# b = int(input("Num b")) # "3"
# c = float(input("Num c")) #
# d = bool(input("Num d"))
# print(a + b) # "23"
# a = int(input("Num a")) # 31
# b = int(input("Num b")) # 4
# print(a + b) # 35
# print(a - b) # 27
# print(a * b)
# print(a / b) # 7.75 ( return an original value)
# print(a // b) # int(7.75) -> 7
# print(a % b) # modulo: 3
# c = float(input("Celsius"))
# f = (c * (9 / 5) + 32)
# print(f)
# w = float(input("Width"))
# h = float(input("Height"))
# print(w * h)
# currYear = 2025
# a = int(input("Year born"))
# print(currYear - a)
# Ex9:
# x = int("25")
# print(x + 10)
# https://docs.google.com/document/d/1n4n52y7RjgHDgp8qLMpNg1Fqi0CQp2zodFrFjWFNrOk/edit?tab=from
# a = int(input("Num a"))
# if a % 2 == 0: # 90% -> '%'
#     print("Even number")
# else:
#     print("Odd number")
# a = int(input("Salary 1")) # 50
# b = int(input("Salary 2")) # 50
# if a > b:
#     print("Person 1")
# elif a == b:
#     print("Same salary")
# else:
#     print("Person 2")
#a = int(input("Score"))
# -5 | 105
# and or -> && ||
# if a <= 0 or a >= 100:
#     print("Invalid input")
# elif a <= 50:
#     print("Weak score")
# elif a <= 60:
#     print("Average score")
# elif a <= 75:
#     print("Good")
# elif a <= 90:
#     print("Very good")
# else:
#     print("Excellent")
# a = int(input("Year"))
# if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
#     print(a , " is a leap year")
# else:
#     print(a , " is not a leap year")
a = int(input("Num"))
if a < 0 or a > 6:
    print("Invalid input")
elif a == 0:
    print("Sunday")
elif a == 1:
    print("Monday")
elif a == 2:
    print("Tuesday")
elif a == 3:
    print("Wednesday")
elif a == 4:
    print("Thursday")
elif a == 5:
    print("Friday")
else:
    print("Saturday")
