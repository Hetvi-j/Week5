# Python uses indentation to define blocks of code.

# Standard: 4 spaces
# Avoid tabs (recommended)
from ast import With


if True:
    print("Correct indentation")
    print("Still inside if block")

print("Outside block")
# A colon(:) is required after statements that start a block.
# Usue after if, else, for, while, def, class, try, except
# like this
age = 22
if age > 18:
    print("Adult")

for i in range(5):
    print(i)

def greet():
    print("Hello")

# Python does not require semicolons (;) at the end of lines.

# //////////////////////////////////////    Strings

# Python supports:

# Single quotes ' '
# Double quotes " "
# Triple quotes ''' ''' or """ """

# ///////////////////////////////////////    f-Strings

# Used for formatting strings easily.

name = "Hetvi"
age = 21

print(f"My name is {name} and I am {age} years old.")
# output: My name is Hetvi and I am 21 years old.
print(f"Hello {name!r}")    # Hello 'Hetvi' 
# !r uses the object representation

# ////////////////////////////////////////     None vs null
# Python uses None instead of null.
data = None # instead of null

# //////////////////////////////////////////     Boolean Values
# Python booleans start with capital letters.
is_valid = True
is_admin = False
# instaed of is_admin = true



# /////////////////////////////////////////     Variables ad data types
# Python is dynamically typed, so you don't need to declare variable types.
# A variable stores data in memory.
############## int, float
############## complex numbers : Stores complex numbers
# format: a + bj
z = 2 + 3j
print(z)  # Output: (2+3j)
############### string 
name = "Hetvi"
message = 'Python is easy'
################ boolean
is_valid = True
is_admin = False
################ bytes : Used to store binary data
data = b'Hello'
print(data)  # Output: b'Hello'
# used in files , networking, imgs , encoded data

# //////////////////////////////////////////////  Type Checking
# Use type() to check the type of a variable.
print(type(name))  # Output: <class 'str'>  
print(type(age))   # Output: <class 'int'>
print(type(is_valid))  # Output: <class 'bool'>

# ///////////////////////////////////////////////    Using isinstance()
# Checks whether an object belongs to a specific type
# it supports inheritance, so it can check for subclasses as well.
print(isinstance(name, str))  # Output: True
print(isinstance(age, int))   # Output: True
print(isinstance(is_valid, bool))  # Output: True

# ////////////////////////////////////////////////     Type Conversion
# Python allows converting one data type into another.
# Convert Integer to String
age_str = str(age)  # Convert int to str
print(age_str)  # Output: '22'
# Convert String to Integer
age_int = int(age_str)  # Convert str to int
print(age_int)  # Output: 22
# Convert Float/String to Float
pi = float("3.14")
print(pi)  # Output: 3.14

# /////////////////////////////////////////////////////     id() Function
# Returns the unique identifier of an object (its memory address)
x = 10
print(id(x))    # 140732563201232
# Output will be a large integer representing the object's memory identity.

# Everything in Python is an Object
# numbers are objects
# strings are objects
# functions are objects
# classes are objects
x = 10
print(x.bit_length())  # Output: 4
# This shows that integers behave like objects with methods.

# /////////////////////////////////////////////////////     Operators in Python
# Operators are symbols used to perform operations on variables and values
# Arithmetic Operators: +, -, *, /, //(floor division), %, **
# Floor Division //: Returns the integer part only.
# Comparison Operators: ==, !=, >, <, >=, <=
# Logical Operators: and, or, not
# Assignment Operators: =, +=, -=, *=, /=, //=, %=, **=
# Bitwise Operators: &, |, ^, ~, <<, >>
y = 5
print(x > y)

# Identity Operators
# Checks whether two variables refer to the same object in memory.

a = [1, 2]
b = [1, 2]
print(a == b) # Output: True (values are equal)
print(a is b) # Output: False (different objects in memory)

a = [1, 2]
b = a
print(a is b) # Output: True (both variables refer to the same object in memory)

# Membership Operators
# Checks if a value is present in a sequence (like lists, strings, etc.)
text = "Python"
print("P" in text)  # Output: True
print("z" in text)  # Output: False

numbers = [1, 2, 3]
print(2 in numbers)  # Output: True
print(5 not in numbers)  # Output: True

# ////////////////////////////////////////////   Walrus Operator :=
# Introduced in Python 3.8, 
# Assigns a value while evaluating an expression.
# without walrus operator
name = input("Enter name: ")

if name:
    print(name)


# with walrus operator
if (name := input("Enter name: ")):
    print(name)
# This:

# takes input
# assigns it to name
# checks condition

# ////////////////////////////////////////////   String Operations in Python
text = "Python"
# Strings are immutable, meaning they cannot be changed directly.
# .upper(): Converts all characters to uppercase.
# .lower(): Converts all characters to lowercase.
# .strip(): Removes spaces from beginning and end.
text = "   hello   "
print(text.strip()) # Output: 'hello'

# .split(): Splits a string into a list.
text = "Python is easy"
print(text.split()) # Output: ['Python', 'is', 'easy']
data = "a,b,c"
print(data.split(","))   #split by comma, Output: ['a', 'b', 'c']

# .join(): Joins elements into a single string.
words = ["Python", "is", "easy"]
result = " ".join(words)
print(result)

# .replace(): Replaces part of a string.
text = "Python is easy"
print(text.replace("easy", "powerful"))  # Output: 'Python is powerful'

# .startswith(): Checks starting characters.
text = "Python is easy"
print(text.startswith("Python"))  # Output: True
print(text.startswith("python"))  # Output: False

# .endswith(): Checks ending characters.
text = "Python is easy"
print(text.endswith("easy"))  # Output: True
print(text.endswith("Easy"))  # Output: False

# .find(): Finds the index of a substring of first occurrence.
text = "Python is easy"     
print(text.find("is"))  # Output: 7
print(text.find("easy"))  # Output: 10

# .count(): Counts occurrences of a substring.
text = "Python is easy and Python is popular"   
print(text.count("Python"))  # Output: 2

# String Slicing: string[start:end:step]
text = "Python"
print(text[0:6])  # Output: 'Python' 
print(text[:3])   # Output: 'Pyt' 
print(text[3:])   # Output: 'hon' 
print(text[::2])  # Output: 'Pto' 
print(text[::-1]) # Output: 'nohtyP' (reversed string)

# Multiline Strings
multiline = """This is a multiline
string in Python."""    

# String Formatting Deep Dive
# Concatenation
name = "Hetvi"
print("Hello " + name)

# format() Method
# The format() method is used to insert values into a string dynamically.
# It replaces {} placeholders with values.
name = "Hetvi"
age = 22
print("My name is {} and I am {} years old".format(name, age))
# output: My name is Hetvi and I am 22 years old

# Positional Formatting
# You can specify positions manually.
print("{1} is learning {0}".format("Python", "Hetvi"))
# output: Hetvi is learning Python
print("{0} scored well. {0} is happy.".format("Hetvi"))
# reusing same value

# Named Arguments
print("Name: {name}, Age: {age}".format(name="Hetvi", age=21))
# output: Name: Hetvi, Age: 21

# Accessing Dictionary Values
student = {
    "name": "Hetvi",
    "marks": 95
}
print("Name: {name}, Marks: {marks}".format(**student))

# Accessing List Values
data = ["Hetvi", 21]
print("Name: {0}, Age: {1}".format(data[0], data[1]))

# Formatting Numbers
# Decimal Precision
pi = 3.14159265
print("{:.2f}".format(pi))   # Output: 3.14 (2 decimal places)

# Width Formatting
print("{:10}".format("Python"))  # Output: 'Python    ' (10 characters wide, right-aligned)
print("{:<10}".format("Python")) # Output: 'Python    ' (10 characters wide, left-aligned)
print("{:>10}".format("Python")) # Output: '    Python' (10 characters wide, right-aligned)
print("{:^10}".format("Python")) # Output: '  Python   ' (10 characters wide, centered)
print("{:*^10}".format("Python")) # Output: '**Python**' (10 characters wide, centered, filled with '*')
print("{:05}".format(42))  # Output: '00042' (5 characters wide, zero-padded)
# Comma Separator : Useful for large numbers.
num = 1000000
print("{:,}".format(num))
# 1,000,000

# Percentage Formatting
score = 0.85
print("{:.2%}".format(score))  # Output: '85.00%'

# Binary, Octal, Hexadecimal
num = 10
print("{:b}".format(num))
print("{:o}".format(num))
print("{:x}".format(num))
# Output:
# 1010
# 12
# a

# Using Expressions
a = 5
b = 3
print("Sum = {}".format(a + b)) # Output: Sum = 8

# Escaping Curly Braces
print("{{}} is used in format") # Output: {} is used in format

# Nested Formatting
value = 3.14159
width = 10
precision = 2

print("{:{width}.{precision}f}".format(
    value,
    width=width,
    precision=precision
))

# /////////////////////////////////// diff between format() and f-strings

name = "Hetvi"
print("Hello {}".format(name))
print(f"Hello {name}")
# f-strings are:

# shorter
# faster
# more readable

# But format() is still widely used and useful.

# Control Flow in Python
# Control flow decides how a program executes code based on conditions and loops.

# ///////////////////////////////    if + elif + else
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# ///////////////////////////////    Nested if
age = 20
citizen = True
if age >= 18:
    if citizen:
        print("Eligible to vote")

# ///////////////////////////////    Ternary Operator: 
# Short form of if-else.
age = 20
result = "Adult" if age >= 18 else "Minor"
print(result)

# ////////////////////////////////    for Loop
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

# //////////////////////////////////  range(): Generates numbers
for i in range(5):
    print(i) # Output: 0, 1, 2, 3, 4

for i in range(2, 6):
    print(i) # Output: 2, 3, 4, 5

for i in range(1, 10, 2):
    print(i) # Output: 1, 3, 5, 7, 9

# ////////////////////////////////  enumerate()
# Provides: index, value

# Without enumerate()
fruits = ["apple", "banana"]
index = 0
for fruit in fruits:
    print(index, fruit)
    index += 1

# With enumerate()
fruits = ["apple", "banana"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

# ////////////////////////////////   zip(): 
# Combines multiple sequences.

names = ["Hetvi", "Rahul"]
marks = [95, 88]

for name, mark in zip(names, marks):
    print(name, mark)
# Output:
# Hetvi 95
# Rahul 88

# ////////////////////////////////   while Loop: 
# Runs while condition is True
count = 1
while count <= 5:
    print(count)
    count += 1

# ////////////////////////////////   break: 
# Stops loop immediately.
for i in range(10):
    if i == 5:
        break
    print(i)
# Output: 0, 1, 2, 3, 4

# ////////////////////////////////   continue: 
# Skips current iteration.
for i in range(10):
    if i == 5:
        continue
    print(i)
# Output: 0, 1, 2, 3, 4, 6, 7, 8, 9

#////////////////////////////////   pass: 
# Placeholder that does nothing.
for i in range(5):
    pass

# Useful for:

# empty functions
# unfinished code

#////////////////////////////////   else with Loops
# Runs only if loop finishes normally.
# It does NOT run if break occurs.
for i in range(3):
    print(i)
else:
    print("Loop completed")
# 0
# 1
# 2
# Loop completed

# else will not run because of break
for i in range(5):

    if i == 3:
        break
    print(i)
else:
    print("Completed")
# 0
# 1
# 2

# ///////////////////////////////////   List Comprehension
# Compact way to create lists.
# Basic Syntax: [expression for item in iterable]
squares = [x * x for x in range(5)]
print(squares)
# Output: [0, 1, 4, 9, 16]

# With Condition
numbers = [x * 2 for x in range(10) if x % 2 == 0]
print(numbers)
# Output: [0, 4, 8, 12, 16]
# Explanation:

# iterate from 0–9
# keep even numbers
# multiply by 2

# ///////////////////////////////    Equivalent Normal Loop
result = []
for x in range(10):
    if x % 2 == 0:
        result.append(x * 2)
print(result)

# ////////////////////////////////    Nested List Comprehension
pairs = [(x, y) for x in range(2) for y in range(2)]
print(pairs)
# Output: [(0, 0), (0, 1), (1, 0), (1, 1)]

# ////////////////////////////////    Dictionary Comprehension
squares = {x: x * x for x in range(5)}
print(squares)
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# ////////////////////////////////    Set Comprehension
unique_squares = {x * x for x in range(5)}
print(unique_squares)
# Output: {0, 1, 4, 9, 16}

