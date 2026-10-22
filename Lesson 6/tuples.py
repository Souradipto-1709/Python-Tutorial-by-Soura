# ---------------------------------
# Tuples in python
# ---------------------------------

# Tuples are a type of immutable data type in python, within first brackets(), which are ordered and indexed.
t = (2, 'Soura')
print(type(t)) # => Tupple

t = (1,) # A tuple containing 1 value is ended with a comma.
t = () # An empty tuple

# -------------------
# Tuple Indexing and Slicing
# -------------------

# Tuples can be indexed:
t = (19, False, 'Python', 5.71)
print(t[2])
print(t[0])

# Output:
# Python
# 19
# Negative Indexing can also be done.

# Tuples can be sliced:
# Let's take the same tuple 't'.
print(t[0:3])
print(t[1:4])

# Output:
# (19, False, 'Python')
# (False, 'Python', 5.71)

# ------------------
# Tuple Methods
# ------------------

# There are a few tuple methods, which we can use to do operations on tuples. Let's list some of them:
t = (10, 20, 10, 30, 10, 40)

# 1. count(): It counts the number of occurences of a specific item in the tuple. 
print(t.count(10))

# 2. index(): It gives the index of the specific item in the tuple.
print(t.index(30))

# Output:
# 3
# 3

# Now, let's move to our next coding lesson...