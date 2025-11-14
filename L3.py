# https://teams.live.com/meet/9366262663734?p=Gx7DGX5pO57t8AMpAO
'''
🧩 Exercise 1: Count to Ten
Task: Use a for loop to print the numbers from 1 to 10.
Expected Output:
1 2 3 4 5 6 7 8 9 10
for i in range(1,10 + 1, +1):
    print(i , end = " ")

🔢 Exercise 3: Sum of First N Numbers
Task: Ask for a number n, then use a loop to calculate the sum of all numbers 'from 1 to n'.
Example Input:
5
Example Output:
The sum is 15.
n = int(input("Num1"))
sum = 0
for i in range(1,n + 1):
    sum += i
print(sum)

💬 Exercise 4: Repeat a Word
Task: Ask for a word and a number, then print the word that many times in one line.
Example Input:
Word: hi
Times: 3
Example Output:
hi hi hi
x = input("Word")
n = int(input("Num"))
for i in range(1,n + 1):
    print(x , end = " ")

🔁 Exercise 5: Countdown
Task: Ask for a starting number and use a while loop to count down to 1.
Example Input:
5
Example Output:
5 4 3 2 1 Blast off!
x = int(input("Num"))
for i in range(x,1-1,-1):
    print(i , end = " ")
print("Blast off!")
🎲 Exercise 9: Guessing Game (Simple)
Task: The program keeps asking for a number until the user enters 7.
Example Input:
3
9
7
Example Output:
Correct!
Hint: while (loop)
while True:
    x = int(input("Num"))
    if x == 7:
        print("Correct!")
        break
    else:
        print("Guess again")

🧠 Exercise 10: Sum Until Zero
Task: Keep asking for numbers and add them up. Stop when the user enters 0, then show
the total.
Example Input:
5
8
3
0
Example Output:
Total sum = 16
sum = 0
while True:
    x = int(input("Num"))
    if x == 0:
        print(sum)
        break
    else:
        sum += x
🧮 Exercise 1: Sum of Odd Numbers
Task: Ask for n and calculate the sum of all odd numbers from 1 to n.
Example Input: 10
Example Output: Sum of odd numbers = 25
n = int(input("Num"))
sum = 0
for i in range(1,n+1):
    if i % 2 != 0:
        sum += i
print(sum)

💰 Exercise 3: Smallest Multiple Finder
Task: Use a while loop to find the smallest number greater than 0 that is divisible by both 3
and 5.
Expected Output: 15
Steps:
+Initialize a variable n = 1.
+Use if to check divisibility by 3, 5
+Stop when a number satisfying the condition is found.
+Print the result.
Input:
None (the calculation is fixed).
Output:
The smallest positive number divisible by 3, 5 (15).
n = 1
while True:
    if n % 3 == 0 and n % 5 == 0:
        print(n)
        break
    else:
        n += 1

🔁 Exercise 5: Sum Until Negative
Task: Keep asking for numbers and add them up.
Stop when a negative number is entered, then print the total.
Example Input: 5 → 8 → 3 → −1
Example Output: Total = 16
sum = 0
while True:
    x = int(input("Num"))
    if x < 0:
        break
    else:
        sum += x
print(sum)

📏 Exercise 6: Factorial Calculator
Task: Ask for n and compute n! using a for loop.
💡 Hint: Multiply a running product from 1 to n.
Example Input: 4
Example Output: Factorial = 24 (1*2*3*4)
n = int(input("Num"))
factorial = 1
for i in range(1,n+1):
    factorial *= i
print(factorial)

🔠 Exercise 8: Count Vowels in a Word
Task: Ask for a word and count how many vowels (a, e, i, o, u) it has.
💡 Hint: Use a for loop and a counter variable.
Example Input: python
Example Output: Number of vowels = 1
w = input("Word")
count = 0
for i in w:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count += 1
print(count)

🧾 Exercise 9: Collatz Step Counter
Task: Ask for a positive integer n. Repeat these rules until n becomes 1:
+ If n is even -> 'divide by 2'
+ If n is odd -> 'multiply by 3 and add 1'
Count how many steps it takes.
-Example Input: 6
-Example Output: It took 8 steps to reach 1.
count = 0
n = int(input("Num"))
while True:
    if n % 2 == 0:
        n = n // 2
        count += 1
    else:
        n = (n * 3) + 1
        count += 1
    if n == 1:
        break
print(count)
🔢 Exercise 2: Skip Multiples of 3
Task: Use a for loop to print numbers from 1 to 10, 'skipping multiples of 3.'
Expected Output:
1 2 4 5 7 8 10 (exclude 3 6 9)
for i in range(1,10+1):
    if i % 3 != 0:
       print(i , end = " ")

🧮 Exercise 3: 'Count' Until Limit
Task: Ask the user for a maximum number, then print from 1 upward. Stop early if the total
sum exceeds 50.
💡 Hint: Use break inside a for loop.
x = int(input("Num"))
sum = 0
for i in range(1,x+1):
    sum += i
    if sum > 50:
        break
    else:
        print(i , end = " ")

💬 Exercise 6: Skip Empty Input
Task: Keep asking for a name.
If the user enters an empty string, skip and ask again.
If the user enters “exit”, stop.
💡 Hint: Combine continue and break.
while True:
    n = input("Name")
    if n == '':
        continue
    elif n == "exit":
        break
📦 Exercise 7: Find First Even Number
Task: Ask for 5 integers (using a loop).
Stop the loop when the first even number is found and print it.
for i in range(1,5+1):
    x = int(input("Int"))
    if x % 2 == 0:
        print(x)
        break

for i in range(1,5 + 1): # row
    for j in range(1,3 + 1): # column
        print(i, end = " ")
    print()
🎯 Exercise 5: Multiplication Table (Nested Loop)
Task: Use nested loops to print a multiplication table from 1 to 3.
Expected Output:
1×1=1 1×2=2 1×3=3
2×1=2 2×2=4 2×3=6
3×1=3 3×2=6 3×3=9
for i in range(1,3+1,+1):
    for j in range(1,3+1,+1):
        print(i , '*' , j, '=',i * j ,end = " ")

    print() # print new line

🧠 Exercise 4: Placeholder Example
Task: Create a loop that runs five times but does nothing inside it.
💡 Hint: Use pass inside the loop.
Expected Output:
(no visible output, but no errors either)
'''
for i in range(1,5+1):
    pass
x = 4

if x % 2 == 0:
    pass







