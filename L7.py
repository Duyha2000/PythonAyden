"""
🔢 Exercise 1 — Stop at Zero
Write a loop that keeps asking the user for integers.
Stop immediately when the user enters 0.
Print a message saying the loop has ended.
Example Input:
5
12
7
0
Example Output: Loop ended because you entered 0.
while True:
    y = int(input("Enter a number")) # what is the data type of y variable:
    if y == 0:
        print("Loop ended because you entered 0")
        break
🚫 Exercise 2 — Skip All Odd Numbers
Task: Print numbers from 1 to 20, skipping all odd numbers.
Expected Output:
2 4 6 8 10 12 14 16 18 20
Hint: using "continue"
for i in range(1,20+1):
    if i % 2 != 0:
        continue
    else:
        print(i)

🧮 Exercise 3 — Sum Until Over 100
Task: Keep reading integers and stop when 'total > 100'.
Example Input:
20
50
40
Example Output:
Total exceeded 100. Loop stopped.
sum = 0
while True:
    if sum > 100:
        print("Total exceeded 100. Loop stopped.")
        break
    else:
        x = int(input("Num"))  # 70
        sum += x
print(sum)
🔄 Exercise 6 — Skip Blank Input
Task:
empty → skip
“stop” → break
otherwise print the word
Example Input:
hello

hi
stop

Example Output:
You entered: hello
You entered: hi
while True:
    x = input("Input")
    if x == "stop":
        break
    elif x == "":
        continue
    else:
        print(x)

🧲 Exercise 7 — First Number Divisible by 9
Task: Loop 1–100, stop at the first number divisible by 9.
Expected Output:
First divisible-by-9 number found: 9
for i in range(1,100+1):
    if i % 9 == 0:
        print("First divisible-by-9 number found:" , i)
        break

🎰 Exercise 10 — Multiple Skips
Task:
Skip numbers divisible by 4
Stop if number divisible by 9
Expected Output:
1 2 3 5 6 7
Loop ended at a number divisible by 9.
n+=1 -> where
n = 0
while True:
    n+=1
    if n % 4 == 0:
        continue
    elif n % 9 == 0:
        break
    else:
        print(n)

📌 Exercise 12 — Print Characters Except Vowels
Example Input:
hello world
Expected Output:
hll wrld
x = input("")
for i in range(0,len(x)):
    if x[i] == "a" or x[i] == "e" or x[i] == "i" or x[i] == "o" or x[i] =="u":
        continue
    else:
        print(x[i], end="")
🎯 Exercise 15 — First Number > 500
Ask user 8 integers; stop early if >500.
Example Input:
100
250
600
Example Output:
Large number found. Loop stopped early.
for i in range(0,8+1):
    x = int(input("num"))
    if x > 500:
        print("Large number found. Loop stopped early.")
        break

Exercise 20 — Sum of Digits (Loop)
Task: Ask user for a number as a string, then print the sum of digits.
Example Input: 5029
Expected Output: Sum of digits = 16
x = input("Input num")
sumA = 0 # data type: inter
for i in x:
    sumA += int(i) # character
print(sumA)

Exercise 24 — Search for Letter 'a' in Text
Task: Loop through characters and stop when encountering 'a'.
Example Input: hello mango
Example Output: Found 'a' at position 7 (index can be 0-based or 1-based tùy học sinh)
x = input("")
for i in range(0,len(x)):
    if x[i] == "a":
        print("Found 'a' at position", i)
Exercise 31 — First Repeated Character
Task:
Given a string, find the first character that appears more than once.
Example Input: abcaef
Example Output: First repeated character: a
x = input("") # ubcabf
for i in range(0,len(x)): #  x[i] -> 'b'
    count = 0
    for j in range(i+1,len(x)): # x[j] -> b c a e f
        if x[j] == x[i]:
            print("First repeated character at position", j, x[j])
            count+=1
    if count == 1:
        break

TODO: Exercise 32 — Digital Root (Sum Until One Digit)
Task:
Repeatedly sum the digits of a number until only one digit remains.
Print all intermediate results.
Example Input: 9875
Example Output:
Intermediate: 29 (9+8+7+5 = 29)
Intermediate: 11 (2 + 9 = 11)
Final result: 2 ( 2 < 10 -> stop)
x = input("Num")
sumA = 0
for i in x:
    sumA += int(i)
# Continue summing until total becomes a single digit
while sumA >= 10: # 2
    sumB = 0
    print("Intermediate" , sumA)
    for i in str(sumA):
        sumB += int(i) # 2
    sumA = sumB # 2
print("Final result:", sumA)
"""

















