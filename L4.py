#https://docs.google.com/document/d/1ri43FlfIQl6SHRHKf61_60nOvmuiozLrxNnH3gtuXWA/edit?tab=t.0#heading=h.9y7mdpbwh327
# String:
# https://meet.google.com/zph-tgjp-ndq

# upper():
"""
replace(old, new): Replaces all occurrences of a substring with another substring.
-> Example: x.replace("apple", "cherry") returns "cherry pie".
Output: Hello Hi
x = "Hello world"
print(x.replace("world", "Hi"))
print(x.upper())

EX1: Manipulation:
Step 1: Convert the string to lowercase.
Step 2: Replace all occurrences of the substring "hello" with "python".
x = input("") # HELLO WORLD
x = x.lower() #      x  = hello world
x = x.replace("hello", "python") #   x = python world
print(x)

EX2: Information Retrieval:
Step 1: Find and return the index of the first occurrence of the substring "Python".
Step 2: Check if the string starts with "WELCOME".
Hint:
-> find(sub): Returns the index of the first occurrence of a substring. Returns -1 if not found.
Example: x.find("world") returns 6.
-> startswith(prefix): Checks if a string starts with a specific prefix. Returns True or False.
Example: x.startswith("hello") returns True.
x = input("")
y = x.find("python")
print(y)
z = x.startswith("WELCOME")
print(z)

Ex3: Validation:
Check if the string contains only alphabetic characters.
Check if the string contains only digits.
Hint:
text = "HelloWorld" -> print(text.isalpha())   # True
text2 = "Hello123" -> print(text2.isalpha())  # False
num = "12345" -> print(num.isdigit())    # True
num2 = "12a45" -> print(num2.isdigit())   # False

TODO: Splitting and Joining: Split the string into a list of words (use space as a delimiter). Join the list of words into a single string separated by commas.
1.split(delimiter): Splits a string into a list based on a delimiter.
Example: "apple,banana,orange".split(",") returns ['apple', 'banana', 'orange'].
2.join(iterable): Joins elements of an iterable (e.g., list) into a single string with a specified delimiter.
Example: ", ".join(['apple', 'banana', 'orange']) returns "apple, banana, orange".
x = input("")
print(x.split(","))
"""
x = "hello world"
# index: 0 -> -1 last index
print(x[-1])
"""
1. Print all characters in string: h e l l o w o r l d -> for loop
x = input("")
print(len(x)) # 5
# 1: for i in range
# for i in range(0, len(x)):
#     print(x[i], end=" ")

# for each:
for i in x:
    print(i, end =" ")
2. Count Vowels
Given a string, count how many vowels (a, e, i, o, u) it contains.
The program must work correctly even if the string contains uppercase letters.
x = input("")
count = 0
for i in x:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        count += 1
print(count)

3. Reverse Each Word
Write a program that reverses every word in a sentence individually but keeps the word order the same.
Example: "hello" → "olleh".
h e l l o
0 1 2 3 4 

o l l e h
4 3 2 1 0
# for i in range(5,-3 - 1, -1):
#     print(i,end=" ")

x = input("")
for i in range(len(x)-1,-1,-1 ):
    print(x[i], end="") # hello -> 5
    Print: 0 1 2 3 4 for loop:
-> Print: 5 4 3 2 1 0 -1 -2 -3 
4. Remove Spaces
Given a string, remove all spaces from it.
Example: "a b c" → "abc".
#        i: index or x[i]:value(character, number...)
x = input("")
# i: stands for a character in string - for each
for i in x:
    if i != " ":
        print(i, end="")
8. Character Category Counter
Write a program that counts how many of the characters in a string are:
+alphabetic letters -> str.isalpha() 
+digits -> str.isdigit()
+whitespace -> str.isspace()
+other special characters 
=> Print the result, for each         
x = input("")
count = 0
count2 = 0
count3 = 0
countSpecial = 0
for i in x:
    if i.isalpha():
        count += 1
    elif i.isdigit():
        count2 += 1
    elif i.isspace():
        count3 += 1
    else:
        countSpecial += 1
print(count)
print(count2)
print(count3)
print(countSpecial)
https://teams.live.com/meet/9371991082198?p=yWeifyAXcGGr2tUJ6N

Question 1. Student alias
A student's alias is created by concatenating their last name with the last two digits of
their birth year.
Write a Python program that:
1.Asks the user to enter their last name (a string).
2.Asks the user to enter their birth year (a 4-digit number).
3.Prints out the student's alias.
Examples:
Input:
Last name: Nguyen
Birth year: 2003
Output:
Nguyen03
x = input("Last name ") # Nguyen
y = input("Birth year ")  # 20[03]
print(x+y[2]+y[3])

Question 2. Timestamp reformat
A timestamp is encoded as a single 9-digit integer in the following format: HHMMSSDDD
Where:
● HH = hours (00–23)
● MM = minutes (00–59)
● SS = seconds (00–59)
● DDD = the number of milliseconds (000–999)
Task:
Write a program that:
1.Asks the user to enter a timestamp in this 9-digit code.
2.Prints the input timestamp in the following format: SS:MM:HH-DDD
"""
x = input("Timestamp") # 9 digit code: HHMMSSDDD (232323444)
hh = x[0]+x[1]            # 23 -> get letter 0 1
mm = x[2]+x[3]           # 23
ss = x[4]+x[5]           # 23
ddd = x[6]+x[7]+x[8]           # 444
print(ss+":"+mm+":"+hh+"-"+ddd)
