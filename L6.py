"""
1. Keep Only Digits
Description: Remove every non-digit character from the input string and print the resulting string that contains only digits (preserve order).
Input: A single line string s.
Output: A string containing only digits from s. If no digits, print an empty line.
Example:
Input:
Phone: +1 (234) 567-8900
Output: 12345678900
-> Hint: for loop + isDigit
s = input() # +1 (234) 567-8900
result =""
for i in s:
    if i.isdigit():
        result +=i
print(result)
2. Replace Vowels With *
Description: Replace each vowel (a, e, i, o, u) with the * character. Keep other characters unchanged.
Input: A single line string s.
Output: Modified string with vowels replaced.
Example:
Input: Hello World
Output: H*ll* W*rld
Hint: for each + replace method(old, new)
s = input("")
result = ""

for i in s:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        result += "*"
    else:
        result +=i
print(result)

10. Join Words with a Dash
Task: Convert a space-separated string into a dash-separated one
Example Input:
s =
"Python is fun"
Example Output:
"Python-is-fun"
Hint: replace
For loop
s = input("")
result =""
for i in s:
    if i == " ":
        result += "-"
    else:
        result += i
print(result)

3. Remove First and Last Character

Description: Print the string without its first and last character. If the string has length ≤ 2, print an empty string.
Input: A single line string s.
Output: The trimmed string.
Example:
Input: example
Output: xampl
s = input("")
result = ""
for i in range(1,len(s)-1):
    if len(s) > 2:
        result += s[i]
    else:
        print("")
print(result)
4. Count Uppercase Letters

Description: Count and print the number of uppercase alphabetic letters in the string.
Input: A single line string s.
Output: An integer — the count of uppercase letters.
Example:
Input: Hello World! THIS is Fun.
Output: 7
s = input("")
count = 0
for i in s:
    if i.isalpha() and i.isupper():
        count += 1
print(count)
5. Duplicate Every Character

Description: Create a new string where every character from the original appears twice consecutively.
Input: A single line string s.
Output: The duplicated-character string.
Example:
Input: abc
Output: aabbcc
s = input("")
result = ""
for i in s:
    result += i*2
print(result)
6. Last 3 Characters Repeated
Description: Print the last three characters of the string repeated 5 times. If the string has fewer than 3 characters, repeat the whole string 5 times.
Input: A single line string s.
Output: A string formed by 5 repetitions (or full s if len<3).
Example:
Input: Python
Output: honhonhonhonhon
s = input("")
result = ""
for i in range(len(s)-3,len(s)):
    result += s[i]
print(result*5)
8. Remove All Spaces

Description: Remove all space characters ' ' from the input (do not use replace — use loop or other methods).
Input: A single line string s.
Output: s without spaces.
Example:
Input: Python is fun
Output: Pythonisfun
s = input("")
result = ""
for i in s:
    if i != ' ':
        result += i
print(result)

9. Insert * Between Characters
Description: Insert the character * between every pair of adjacent characters in the string. For an empty string or 'single char', output it unchanged.
Input: A single line string s.
Output: The transformed string with * separators.
Example:
Input: hello
Output: h*e*l*l*o
s = input("")
result = ""
if s == "" or len(s) == 1:
    print(s)
else:
    for i in range(0,len(s)-1):
        result += s[i] + '*'
print(result + s[-1])
11. First Half vs Second Half

Description: If the string has even length, print Yes if the first half equals the second half; otherwise print No. If the string has odd length, print No.
Input: A single line string s.
Output: Yes or No.
Example:
Input: abcabc
Output: Yes
s = input("")
if len(s) % 2 == 0:
    print("Yes")
else:
    print("No")

12. Move First 3 Characters to the End
Description: Create a new string by moving the first 3 characters of s to the end. -> 'If len(s) < 3, return the original string.'<=
Input: A single line string s.
Output: The rotated string.
Example:
Input: Python
Output: honPyt
s = input("")
result = ""
firstOf3 = ""
lastOf3 = ""
if len(s) < 3:
    print(s)
else:
        firstOf3 = s[0] + s[1] + s[2]
        lastOf3 = s[-3]+s[-2]+s[-1]
        result = lastOf3 + firstOf3
print(result)
16. Print Characters at Even Indexes

Description: Print characters that are at even indices (0, 2, 4, ...) concatenated into a new string.
Input: A single line string s.
Output: The resulting string.
Example:
Input: Python
Output: Pto
s = input("")
x = ""
for i in range(0,len(s)):
    if i % 2 == 0:
        x += s[i]
print(x)

18. Replace Every 3rd Character With #

Description: Replace every 3rd character (1-based indexing: positions 3, 6, 9, ...) with #. Keep length same.
Input: A single line string s.
Output: Modified string.
Example:
Input: abcdefghi
Output: ab#de#gh#

for i in s:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        result += "*"
    else:
        result +=i
print(result)
"""
s = input("")
result = ""
for i in range(0,len(s)):
    if (i+1) % 3 == 0:
        result += "#"
    else:
        result += s[i]

print(result)