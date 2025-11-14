# For - loop
# Print number from 1 -> 5
# Output: ->'1 2 3 4 5'
# for(int i = 1 ; i <= 5 ; i++){
#     System.out.println(i)
# }
# for i in range(1,5 + 1):
#     print(i,end=" ")

"""
Exercise 1: Display Even Numbers and Calculate Their Sum. Task:
Write a program that takes an integer n as input, displays all even numbers from n up to 100, and calculates the sum of these even numbers.
Input:
An integer n (e.g., 90).
Output:
All even numbers from n to 100 (e.g., 90 92 94 96 98 100).
-> 'The sum' of these even numbers (e.g., sum = 570).
n = int(input("Num"))
sumEvenNumbers = 0
# i: n -> 100
for i in range(n,100 + 1):
    if i % 2 == 0:
        print(i)
        sumEvenNumbers +=i
print(sumEvenNumbers)
Exercise 2: Numbers Divisible by 3 and 5
Task: Write a program that "takes two integers a and b" and displays all numbers between them divisible by both 3 and 5.
Steps:
Input two integers a and b.
Loop through numbers ‘from a to b’.
Check if each number is divisible by both 3 and 5.
Print the valid numbers.
Input: Two integers a and b (e.g., 1 and 50).
Output: All numbers = divisible by both 3 and 5 (e.g., 15 30 45).
a = int(input("Num1"))
b = int(input("Num2"))
for i in range(a,b + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end = " ")
--
print numbers from 5 -> -5
5 4 3 ... -5 -4 -3
Ex2.2: how many even numbers are there from 1 to 10? -> 5 (count)
count = 0
for i in range(1,10 + 1):
    if i % 2 == 0:
        count += 1
print(count)
Ex2.3: print numbers from 5 -> -5
Example: [5 4 3 ... -5 -4 -3]
for i in range(5,-5 - 1, -1):
    print(i, end=" ")

Exercise 3: Count Numbers Divisible by X
Write a program to 'count how many numbers' are divisible by X in the range from A to B, where A <= B, and X is a positive integer. Use a for loop to check each number in the range.
Example: If A = 1 , B = 50, and X = 5, there are 10 numbers divisible by 5
Note: for i in range(start, end + 1, step):
        default step's value is + 1
        x = int(input("Num"))
a = int(input("Num2"))
b = int(input("Num3"))
count = 0
if x > 0:
    for i in range(a,b + 1):
        if i % x == 0:
            count += 1
print(count)

Exercise 5: Calculate the Product of Numbers from 1 to M
Write a program to calculate the product of all integers from 1 to M, where M is a positive integer.
Use a for loop to multiply each number in the range and store the result in a variable.
Note: If M is too large, the result may exceed the limits of the data type.
Example: If M = 5, the product is 1 × 2 × 3 × 4 × 5 = 120
m = int(input("Num"))
product = 1

if m > 0:
    for i in range(1,m + 1):
        product *= i
#        sum += i
print(product)

Exercise 6: Count Divisors
Task: Write a program that inputs an integer n and displays the number of its divisors.
Steps:
Input an integer n.
Loop through numbers from 1 to n.
Check if each number divides n evenly.
Count and print the divisors.
Input:
An integer n (e.g., 12).
Output:
Number of divisors (e.g., 6 for 12).
n = int(input("Num"))
count = 0
for i in range(1,n + 1):
    if n % i == 0:
        count += 1
print(count)

Exercise 13: Validate User Input
Write a program in Python that uses a while loop to validate user input for entering a valid age.
The program should ensure that the age entered is between 0 and 120 (inclusive). If the user enters an invalid value,
the program should display an error message and prompt the user to re-enter the age.
hint: while true -> condition -> break
while True:
    a = int(input("Age"))
    if 0 <= a <= 120:
        print("Valid age")
        break
    else:
        print("Re-enter age")

Exercise 14: Guess the Number Game
Write a program to simulate a number guessing game:
The program randomly selects a number between 1 and 100. // 57
The user repeatedly enters guesses.
Use a while loop to keep asking for input until the user guesses the correct number.
The program should provide hints like "Too high!" or "Too low!" after each guess.
Extension: Count the number of guesses and display it when the user wins.
x = 57

while True:
    a = int(input("Num"))
    if a == x:
        print("Correct guess")
        break
    elif a < x:
        print("Too low")
    elif a > x:
        print("Too high")
Exercise 15: Print 'the first number' divisible by 3 in the range from 1 -> 10
Output: 3
for i in range(1,10 + 1):
    if i % 3 == 0:
        print(i)
        break

Exercise 16: Print out the first 3 numbers divisible by 3 and 5 in the range a,b entered from the keyboard
For example: a = 1, b = 100 -> print: 15 30 45
a = int(input("Num1"))
b = int(input("Num2"))
count = 0
for i in range(1,100 + 1):
    if i % 3 == 0 and i % 5 == 0:
        count += 1
        print(i)
    elif count == 3:
        break
"""

"""
🧩 Exercise 1: Personal Introduction
Task: Ask for your name and age, then display a sentence.
Example Input:
Name: Hoa
Age: 19
Example Output:
My name is Hoa and I am 19 years old.
name = input("Name:")
age = input("Age:")
print("My name is " + name + " and I am " + age + " years old")
🧮 Exercise 2: Sum and Difference
Task: Ask for two numbers, then print their sum and difference.
💡 Hint: Use two variables to store the inputs.
Example Input:
8
3
Example Output:
Sum: 11
Difference: 5
 a = int(input("Num1"))
b = int(input("Num2"))
print("Sum" ,( a + b))
print("Difference: " ,(a - b))
 📏 Exercise 3: Area of a Circle
Task: Ask for the radius, then calculate area = 3.14 × r × r.
Example Input:
5
Example Output:
The area of the circle is 78.5
r = int(input("Radius"))
print("The area of the circle is " ,(3.14 * r * r))

💵 Exercise 9: Simple Tax Calculator
Task: Ask for income.
If < 10 million → “Low income”
If 10–30 million → “Medium income”
If > 30 million → “High income”
Example Input:
25000000
Example Output:
Medium income.
income = float(input("Whats your income:"))
if income < 10000000:
    print("Low income")
elif income <= 30000000:
    print("Medium income")
else:
    print("High income")
    
🧾 Exercise 10: Password Checker
Task: Ask for a password and compare it with a stored one (e.g.,
Print “Access granted” if correct, otherwise “Access denied.
”
Example Input:
python123
Example Output:
Access granted.
"""
x = "python123"
y = input()
if x == y:
    print("Access granted")
else:
    print("Access denied")





