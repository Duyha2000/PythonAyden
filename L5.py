import math
"""
Question 3. Masked credit card number
Write a Python program that:
1. Asks the user to enter a credit card number as a string (it may contain 16 digits).
2.  Your program should mask the credit card number:
- Keep only the first 2 digits and the last 4 digits visible.
- Replace all digits in between with the * character.
3. Display the masked result using an f-string.
Rules / Requirements:
● Do not use loops.
● Do not change the length of the string.
Example 1
Input:
123456720202812345678
Output:
12************5678
Hint: using replace method
x = input("") # 1234567812345678
result = x[0]+x[1] + (len(x)-6) *  "*" + x[-4] + x[-3]+ x[-2] + x[-1]
print(result) # '12**********5678'
# How to print 12 stars  * in a line in python
# x = "*"
# print(x * 12)
# How to print 10 % in a line: '%%%%%%%%%%'
# a = "%"
# print(a * 10)
TODO: Question 4. PI’s first digits
Write a program that:
1. Asks the user to enter a positive integer D — the number of digits to display after the decimal.
2. Prints π rounded/truncated to exactly D decimal places using f-string formatting.
Important Requirements:
● Use the value of π available from Python (do not manually type digits).
● Use f-string formatting to control the number of digits.
● The output should not include extra trailing zeros or scientific notation.
● Assume D ≥ 1.
Example:
Input: 5
Output: Pi to 5 decimal places is: 3.14159
->Explanation
.{x}f inside the f-string means:
Format as a floating-point number (x)
With exactly x digits after the decimal.
x = int(input("Num"))
print(f"{math.pi:.{x}f}") #3.14159|2653589793

1. Extract Middle Character(s)
Task: Print the 2 middle characters of the input string
Example Input:
s =
"Python"
Example Output:
"th"
x = input("")
print( x[len(x)//2 -1] + x[len(x)//2])
# # 7 : 2 = 3
# print(7//2) # 3

2. Swap First and Last Characters
Task: Create a new string by swapping the first and last characters of the input string.
Example Input:
s =
"world"
Example Output:
"dorlw"
"""
# x = input("") # world
# last = x[-1]
# first = x[0]
# result = ""
# middle = ""
# for each ->
# put letters: o r l into middle string
# for i in range(1,len(x)-1):
#     middle += x[i]
# result = last + middle + first
# print(result)
# calc sum of all numbers from 0 -> 5
# sumA = 0
# for i in range(0,5,+1):
#     sumA += i
# print(sumA)


# x = x.replace(x[-1], x[0])
# x = x.replace(y, x[0])
# print(x)
"""
3. Reverse a String Using Slicing
Task: Reverse the string using for loop.
Example Input:
s =
"banana"
Example Output:
"ananab"
"""
x = input("")




