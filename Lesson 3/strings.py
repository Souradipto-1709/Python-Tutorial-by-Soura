# -----------------------------
# Strings in Python
# -----------------------------

# A string is a data type in python which is a collection of characters within single, double and triple quotes.
# Eg:

a = 'Hello' # Single-quoted
b = "I love" # Double-quoted
c = '''Python''' # Tripple-quoted

# Now, we will learn about them in detail...

# -------------
# String Slicing
# -------------

# A string can be sliced or divided in python to get individual parts of it. For Example:
string = 'Python'
print(len(string)) # len() is a string function in Python which tells us the length of the string.
# Output: 6

# Here, the word 'Python' can be indexed as: 0, 1, 2, 3, 4, 5, where the numbers identify the letters p, y, t, h, o, n respectively.
# Also, the word 'Python' can be indexed as: -6, -5, -4, -3, -2, -1 where the numbers identify the letters p, y, t, h, o, n respectively
# String Index in Python starts from 0, and since the word 'Python' had 6 letters, it gave the length as 6.

# To slice a string in Python, we follow the following syntax:
# slicing = string[index_starting:index_ending] Note: The last index in not included. For Example:
slicing = string[2:5]
print(slicing) # return 'tho', did not return the last index 'n'.
# Note: Negative slicing can also be done by using the negative indexes.

# --------------------
# String Functions
# --------------------

# There are numerous string functions in Python, which help us to perform various operations on strings. Let's list some of them:

# 1. upper(): Capitalizes the string.
str = 'hello python'
print(str.upper())
# Output: HELLO WORLD

# 2. lower(): Converts all letters to lowercase.
str = 'HELLO WORLD'
print(str.lower())
# Output: hello world

# 3. capitalize(): Converts the first letter to uppercase.
str = 'heLLO worlD'
print(str.capitalize())
# Output: Hello world

# 4. title(): Converts the first letter of each word to uppercase.
str = 'heLLO worlD'
print(str.title())
# Output: Hello World

# 5. startswith(): Check whethers the string begins with the specific combination of characters.
str = 'hello World'
print(str.startswith('he'))
# Output: True

# 6. endswith(): Check whethers the string ends with the specific combination of characters.
str = 'Hello World'
print(str.endswith('ab'))
# Output: False

# 7. replace(): Replaces the text of the string with another text.
str = 'Hello World'
print(str.replace('World', 'Python'))
# Output: Hello World

# There are many other important and less-important string functions, but we will not learn them now. If you want, you can learn them by your own, by using the internet, or any other method.

# --------------------
# Escape Sequence Characters
# --------------------

# These are sequence of characters, after a backslash(\), these represent various functions when used in a string.
# For Example:

# \': Used to insert single quotes('').
# \n: Used to insert a new line.
# \\: Used to insert a backslash.
# Eg:
print('This is a\nnew line using \'Escape Sequence Charaters\'.')

# Output:
# This is a
# new line using 'Escape Sequence Characters'.

# Now let's move to out next coding lesson...