
# ========================================
#       VARIABLES AND DATA TYPES
# ========================================

# 1. WHAT IS A VARIABLE?
# A variable is a name used to store information.
# Variables can store numbers, text, and other values.

name = "Soura"
age = 12
marks = 95

print(name)
print(age)
print(marks)

# ========================================
# 2. RULES FOR NAMING VARIABLES
# ========================================

# Variable names can contain letters, numbers, and underscores.
# A variable name cannot start with a number.
# Variable names cannot contain spaces.
# Python keywords like if and for cannot be variable names.
# Variable names are case-sensitive.

student_name = "Soura"
student_age = 12
marks1 = 95

# Examples of invalid variable names:
# 1name = "Soura"
# student age = 12

# ========================================
# 3. WHAT IS A DATA TYPE?
# ========================================

# A data type tells us what kind of information a variable stores.
# Let's explore four common Python data types.

# ========================================
# 4. INTEGER (int)
# ========================================

# An integer is a whole number without a decimal point.

age = 12
temperature = -5
number = 100

print(age)
print(type(age))
# Note: The type() is used to statw the type of the data.

# Output:
# 12
# <class 'int'>

# ========================================
# 5. FLOAT (float)
# ========================================

# A float is a number that contains a decimal point.

price = 25.50
height = 1.65
temperature = -2.5

print(price)
print(type(price))

# Output:
# 25.5
# <class 'float'>

# ========================================
# 6. STRING (str)
# ========================================

# A string is text written inside quotation marks.

name = "Soura"
city = "Kolkata"
message = "Hello, World!"

print(name)
print(type(name))

# Output:
# Soura
# <class 'str'>

# ========================================
# 7. BOOLEAN (bool)
# ========================================

# A Boolean stores one of two values: True or False.
# Remember to capitalize the first letter.

is_student = True
is_raining = False
learning_python = True

print('Learning Python:', learning_python)
print(is_student)
print(type(is_student))

# Output:
# True
# <class 'bool'>

# ========================================
# 8. CHECKING DATA TYPES
# ========================================

# The type() function tells us the data type of a value.

a = 10
b = 3.14
c = "Python"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Output:
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'bool'>

# ========================================
# 9. CHANGING DATA TYPES
# ========================================

# Type conversion changes a value from one data type to another.

number = "25"
number = int(number)

print(number + 5)

# Output:
# 30

# Useful type conversion functions:
# int()   - Converts a compatible value to an integer.
# float() - Converts a compatible value to a float.
# str()   - Converts a value to a string.
# bool()  - Converts a value to a Boolean.

# ========================================
# 10. A SMALL PRACTICE PROGRAM
# ========================================

# Let's use variables and different data types together.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
favourite_language = "Python"
is_learning = True

print("Name:", name)
print("Age:", age)
print("Favourite language:", favourite_language)
print("Learning Python:", is_learning)

# Example input:
# Enter your name: Soura
# Enter your age: 12

# Example output:
# Name: Soura
# Age: 12
# Favourite language: Python
# Learning Python: True

# Note: Enter a valid whole number for age.

# ========================================
#              CONCLUSION
# ========================================

# Variables store information.
# Data types tell us what kind of information is stored.
#
# int   - Whole numbers
# float - Decimal numbers
# str   - Text
# bool  - True or False values
#
# Keep practising and keep coding! 🚀


# Stay tuned for new lessons...