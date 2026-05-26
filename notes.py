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





#****************************************************************************************
#////////////////////////////////////////////////////////////////////////////////////////
#                                   Day 2
#////////////////////////////////////////////////////////////////////////////////////////
#****************************************************************************************






#/////////////////////////////////  Python Functions — Deep Dive
# Functions are reusable blocks of code that perform a specific task.
def greet():
    print("Hello")

# Function Parameters and Arguments
def add(a, b):
    return a + b

result = add(5, 3)
print(result)

# Default Parameters: If no value is passed, default is used.
def greet(name="Guest"):
    print(f"Hello {name}")

greet()              # Output: Hello Guest
greet("Hetvi")       # Output: Hello Hetvi

# Arbitrary Positional Arguments
# Used when you don’t know how many positional arguments will come
def total(*args):
    print(args)
    return sum(args)
print(total(1, 2, 3, 4))
# Output:
# (1, 2, 3, 4)
# 10
# args becomes a tuple
# You can loop through it like this
def show(*args):
    for item in args:
        print(item)
show("apple", "banana", "mango")

# ////////////////////////////////  Arbitrary Keyword Arguments — **kwargs
# Used when unknown keyword arguments are passed
def student_info(**kwargs):
    print(kwargs)
student_info(name="Hetvi", age=21, city="Bharuch")
# Output: {'name': 'Hetvi', 'age': 21, 'city': 'Bharuch'}

# kwargs becomes a dictionary or we can say it as object
def display(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
display(name="Hetvi", course="CE")
# Output:
# name : Hetvi
# course : CE

# example of both *args and **kwargs together
def demo(a, *args, **kwargs):
    print("a =", a)
    print("args =", args)
    print("kwargs =", kwargs)

demo(10, 20, 30, name="Hetvi", city="Bharuch")
# Output:
# a = 10
# args = (20, 30)
# kwargs = {'name': 'Hetvi', 'city': 'Bharuch'}

# Keyword-Only Arguments (*)
# Arguments after * MUST be passed using keyword.
def person(name, *, age):
    print(name, age)
person("Hetvi", age=21)
# so we cant write it like this
person("Hetvi", 21) # because * makes its keyword mendatory
# it makes code more readable

# Positional-Only Arguments (/)
# Arguments before / can ONLY be positional.
def divide(a, b, /):
    return a / b
print(divide(10, 2))

# ////////////////////////////////   Lambda Functions
# Small anonymous functions.
# Syntax:- lambda arguments: expression
# A lambda function can take any number of arguments, but can only have one expression.
square = lambda x: x * x   # without using def we can create function like this
print(square(5))
# with multiple arguments
add = lambda a, b: a + b
print(add(3, 4))
# with sorting
points = [(1, 2), (3, 1), (0, 0)]
points.sort(key=lambda point: point[1])  # sort by y-coordinate
print(points)
# Output: [(0, 0), (3, 1), (1, 2)]

# //////////////////////////////////////    Recursion
# A function that calls itself.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120

# ///////////////////////////////////////    Decorators
# Decorators modify another function without changing its code
# A decorator is a function that takes another function as input and returns a new function.
# Basic Decorator
def decorator123(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator123
def hello():
    print("Hello")
hello()
# So Our hello function is decorated with the decorator123
# Output:
# Before function  
# Hello
# After function
# it is equivalent to this
# hello = decorator123(hello)

# we can write decorator with argument like this
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Function called")
        return func(*args, **kwargs)
    return wrapper
@decorator
def add(a, b):
    return a + b
print(add(2, 3))

# Multiple Decorators
def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper

@bold
@italic
def text():
    return "Hello"
print(text())

# /////////////////////////////////////   Metadata Means:
# Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.
# Normally, a function's name can be returned with the __name__ attribute:
def myfunction():
  return "Have a great day!"
print(myfunction.__name__) # Output: myfunction
# But, when a function is decorated, the metadata of the original function is lost.

# Things like:

# function name
# docstring
# annotations
# help information


# ///////////////////////////////////////    functools.wraps
# Without wraps, original function metadata is lost.
# example without wraps
def decorator(func):

    def wrapper():
        print("Before function")
        func()

    return wrapper

@decorator
def hello():
    """This is hello function"""
    print("Hello")
print(hello.__name__)  # Output: wrapper  "but the func name is hello so o/p should be hello so solution is wraps"
print(hello.__doc__)   # Output: None

# With wraps
from functools import wraps

def decorator(func):

    @wraps(func)        # used wraps to preserve original function metadata
    def wrapper():
        print("Before function")
        func()

    return wrapper

@decorator
def hello():
    """This is hello function"""
    print("Hello")
print(hello.__name__)  # Output: hello
print(hello.__doc__)   # Output: This is hello function

# ///////////////////////////////////   Higher-Order Functions

# Functions that:
# take functions as arguments
# OR return functions

def greet(func):
    func()
def hello():
    print("Hello")
greet(hello)

# ///////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////
# What is a Module?
# A module is simply a Python file.
# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.

# Create a Module
# To create a module just save the code you want in a file with the file extension .py:
# we can import that file like import filename
# and then we can use the functions of that file like filename.functionname
# /////////////////////or we can rename it also
# like import filename as new_name
# //////////////////////Built-in Modules

# /////////////////////////////////////////////    from X import Y
# Instead of using full module name every time.
# from my_module import add
# print(add(2, 3))
# now no need for my_module.add()

# Import Multiple Things
from math import sqrt, pi

print(sqrt(25))
print(pi)

#//////////////////////////////////////////////    if __name__ == "__main__"
def greet():
    print("Hello")

if __name__ == "__main__":
    greet()
# This code will only run if the file is executed directly like python filename.py
# It will NOT run if the file is imported as a module in another file.
# This is useful for testing code in a module without running it when imported.

# /////////////////////////////////////////////   Package
# A package is a folder containing Python modules
# Packages help:

# organize large projects
# separate features
# avoid naming conflicts
# Which folder has __init__.py that folder is called Package
# this file tells python that treat this folder as a package
# it can even be empty
# mypackage/
# │
# ├── __init__.py
# ├── math_utils.py
# └── calculator.py
# Example Package

# math_utils.py
# def add(a, b):
#     return a + b

# main.py        which is outside the package
# from mypackage.math_utils import add
# print(add(2, 3))

# but if i want to import it in package file like calculator.py then i can do it like this'
# from .math_utils import add   # . means current package
# print(add(5, 3))
# this is called relative imports
# Relative imports are shorter and cleaner inside packages.

# //////////////////////////////////////////////   How Python Finds Modules
# Python searches modules using: sys.path
import sys
print(sys.path)
# Output can be something like this:
# [
#     current_folder,
#     python_installation_folder,
#     site-packages,
# ]

# Python Module Search Process

# ///////////////////////////////////////////////////////  Pip & virtual  environment
# What is pip?
# pip is Python’s package manager.
# It helps install external libraries/packages.
# Why we need? => Python does not include every library by default.
# pip install package_name  Syntax
# pip install numpy==1.26.0 Specific version installation
# pip uninstall numpy       Uninstalling a package
# pip list                  List installed packages
# pip show numpy            Show package details
# pip freeze                shows installed packages with versions in a format suitable for requirements.txt
# requirements.txt: A file storing project dependencies.
# Create It
# pip freeze > requirements.txt
# This saves packages into file.
#  why it is necessary ?requirements.txt
# It allows others to install the same dependencies using:
# pip install -r requirements.txt

# //////////////////////////////////////////   Problem Without Virtual Environment
# suppose our project a needs numpy 1.26.0 and project b needs numpy 1.25.0
# we can not have two versions of same package in same system
# this is called dependency conflict
# solution is virtual environment
# What is Virtual Environment (venv)?

# A virtual environment is:
# isolated Python environment for a project

# Each project gets:
# separate packages
# separate versions

# Without venv: all projects share same Python packages
# With venv: projects stay independent
# Syntax: python -m venv env_name
# activate virtual env: venv\Scripts\activate
# (venv) C:\project> then it will show ssomething like this in terminal
# now install packages here in env
# Deactivate: deactivate

# Without venv packages installed globally.
# All projects affected.

# ////////////////////////////////////////////   python-dotenv for Config
# What is .env File?

# A .env file stores:

# secret keys
# passwords
# API keys
# configuration values
# for ex.,
# API_KEY=abc123
# DB_PASSWORD=mysecret
# DEBUG=True

# Why Use .env?
# Instead of hardcoding secrets inside code 
# Store secrets in .env then load them into Python.
# install package pip install python-dotenv
# this how we can load .env file in python
#///////////////////////////////////////////
# from dotenv import load_dotenv
# import os
# load_dotenv()
# api_key = os.environ.get("API_KEY")
# print(api_key)
#////////////////////////////////////////////

# load_dotenv(): Read .env file and load variables into environment
# os.environ : is like a dictionary containing environment variables
# os.environ.get("KEY") this is its syntax
# os.environ.get("KEY", "default")  we can also provide default value if key is not found
# use thisbecause we hhave uloadee it on github or somewhere so security issue may occure
# What Happens If You Upload .env?

# Anyone can steal:

# database access
# cloud account
# APIs

# /////////////////////////////////////////////////// exception Handling
# Errors that occur during program execution are called exceptions.
# Exception handling prevents program crashes when errors occur.
print(10 / 0) # This will raise ZeroDivisionError 
# this is exception to fix this we can use
#  "try-except block"
# Used to handle errors safely.

# Syntax
# try:
#     # risky code
# except:
#     # error handling code

try:
    num = 10 / 0
except:
    print("Error occurred")
# Output: Error occurred
# program does not crash and we can handle the error gracefully.
# how it works: pyhton tries to execute code in try block, if error occurs it jumps to except block and executes that code.

# ///////////////////////////////////// Catching Specific Exceptions
try:
    number = int("abc")

except ValueError:
    print("Invalid number")
# Output: Invalid number
# Catching specific exceptions allows you to handle different errors differently.
try:
    value = int("abc")

except ValueError:
    print("Value Error")

except TypeError:
    print("Type Error")
# Output: Value Error
# we can have multiple except blocks to catch different types of exceptions.

# here are some common built in exceptions
# Exception	          Meaning
# ValueError	    Wrong value
# TypeError	        Wrong type
# ZeroDivisionError	Division by zero
# IndexError	    Invalid list index
# KeyError	        Missing dictionary key
# FileNotFoundError	File missing

#/////////////////////////////////////////  else Block
# Runs ONLY if no exception occurs.
try:
    num = int("10")

except ValueError:
    print("Invalid")

else:
    print("Conversion successful")
# Output: Conversion successful
# if error occurs run except otherwise run else

# /////////////////////////////////////////// finally Block
# Runs ALWAYS.
# Even if:
# error occurs
# return happens

# Usually used for:
# closing files
# database cleanup
# releasing resources

try:
    print(10 / 2)

except ZeroDivisionError:
    print("Cannot divide")

finally:
    print("Finished")
# Output:
# 5.0
# Finished

# ///////////////////////////////////  Raising Exceptions
# You can create errors manually using raise
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
# So here we gave a condition for creating exception if it is pos no then only work
# Useful for:

# validation
# enforcing rules
# stopping invalid operations

# //////////////////////////////////////////  Custom Exceptions
# You can create your own exception classes.for ex.,
class AppError(Exception):
    pass

# we can use it like this
class AppError(Exception):
    pass

raise AppError("Something went wrong")
# Helps create:
# meaningful errors
# project-specific handling

#//////////////////////////////////////////////////////
# class InvalidAgeError(Exception):
#     pass
# age = -1
# if age < 0:
#     raise InvalidAgeError("Invalid age")
#//////////////////////////////////////////////////////

# Exception hierchy
# All exceptions inherit from BaseException
# Main hierarchy:
# BaseException
#     └── Exception
#           ├── ValueError
#           ├── TypeError
#           ├── IndexError
#           └── ...
# when we write this "except Exception:" then we catch MOST normal exceptions
# But avoid this sometime because it catches EVERYTHING:
# keyboard interrupts
# system exits
# hidden bugs
# Better way : "except Exception as e:"
try:
    int("abc")

except ValueError as e:
    print(e)
# Output; invalid literal for int()
# called "Exception Object"


# /////////////////////////////////  Logging Errors with loguru
# pip install loguru
from loguru import logger

logger.info("Application started")
logger.warning("Low memory")
logger.error("Something failed")
# output:
# INFO     Application started
# WARNING  Low memory
# ERROR    Something failed

# Why Not Just Use print()?
# Problems:
# no timestamp
# no error level
# hard to debug large apps
# cannot save properly to files

# Logging Solves This
# 2026-05-26 10:00:00 | ERROR | Database failed
# contains time, severity, msg
# A logger is an object that records program events.
# used for debuging, monitoring, error tracking

# logger.debug()
# Detailed developer information.
# logger.debug("Variable x = 10")

# logger.info()
# General app information.
# logger.info("Server started")

# logger.warning()
# Something unusual but app still works.
# logger.warning("Disk space low")

# logger.error()
# An operation failed.
# logger.error("Database connection failed")

# logger.critical()
# Serious issue.
# logger.critical("System crashed")

# Logging Exceptions
# from loguru import logger
# try:
#     10 / 0
# except ZeroDivisionError:
#     logger.exception("Division failed")

