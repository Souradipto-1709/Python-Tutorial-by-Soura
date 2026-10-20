# -----------------------------------
# Lists in Python
# -----------------------------------

# Lists are like containers in Python, capable of storing any data type, inside third brackets. For Example:
l1 = ['Soura', 2, 4.98, True, 'Python'] # Can store any data type
print(type(l1)) # => List

l = [] # An empty list

# --------------------
# List Slicing and Indexing
# --------------------

# A list in Python can be sliced and indexed just like strings. For Example:
l2 = ['Soura', 9, 3.69, False, 'Python', 'Java']
# Here, the data types can be indexed as 0, 1, 2, 3, 4, 5, and negative indexing can also be done here.
# Eg:
print(l2[0])
print(l2[5])
print(l2[3])

# Output:
# Soura
# Java
# False

# Also, the list can be sliced using the same syntax as strings.
# Eg:
print(l2[1:4])

# Output:
# [9, 3.69, False]

# --------------------
# List Methods 
# --------------------

# There are numerous list methods in python, which help us to perform various operations on lists. Let's learn some of them:

l = [2, 0.45, 9, 9, 5, 10, 6.73]

# 1. sort() = Updates the list to ascending order.
l.sort()
print(l)

# 2. reverse() = Updates the list to descending order.
l.reverse()
print(l)

# 3. append() = Adds a item to the last.
l.append(56)
print(l)

# 4. pop() = Removes a specific item at the given index.
l.pop(5)
print(l)

# 5. insert() = Adds a item in the specific index.
l.insert(1, 3)
print(l)

# 6. count() = Counts number of occurences of a specific item of the list.
print(l.count(9))

# Output:
# [0.45, 2, 5, 6.73, 9, 9, 10]
# [10, 9, 9, 6.73, 5, 2, 0.45]
# [10, 9, 9, 6.73, 5, 2, 0.45, 56]
# [10, 9, 9, 6.73, 5, 0.45, 56]
# [10, 3, 9, 9, 6.73, 5, 0.45, 56]
# 2

# Now let's move to our next coding lesson...