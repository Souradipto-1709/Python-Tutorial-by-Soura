# ----------------------------------
# Sets in Python
# ----------------------------------

# Sets are mutable, unordered, unindexed and mutable data types in python, and is a collection of non repetive elements, within 2nd brackets({}).
# Eg:

s = {'Apple', 'Banana', 'Guava'}
print(type(s)) # => Sets

# We cannot do slicing and indexing with sets unlike lists and tuples.
# Also, we cannot repeat a single same element in a set.
# Also, it has no specific order.

s = set() # An empty set

# -------------------
# Set Methods
# -------------------

# There are numerous Set Methods in Python, which are used to perform operations on sets. Let's list some of them:
s = {1, 2, 3}

# 1. add(): Used to add a single element to the set.
s.add(4)
print(s)

# 2. update(): Used to add multiple elements to the set at once.
s.update([5, 6])
print(s)

# 3. remove(): Removes an element from the set. Returns an error, if element not present.
s.remove(1)
print(s)
# s.remove(10) => Returns error

# 4. discard(): Removes an element from the set. Doesn't return an error, if element not present.
s.discard(2)
print(s)
# s.discard(10) => Returns no error

# 5. pop(): Randomly removes one of the element of the set.
p = s.pop() # Removes an element
print(p) # Prints the removed element
print(s) # Prints the remaining elements

# 6. clear(): Removes all the elements from the set.
s.clear()
print(s)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 7. union(): Combines two sets, by removing the duplicate ones.
print(a.union(b))

# 8. intersection(): Returns the elements which are common to both the sets.
print(a.intersection(b))

# Output:
# {1, 2, 3, 4}
# {1, 2, 3, 4, 5, 6}
# {2, 3, 4, 5, 6}
# {3, 4, 5, 6}
# 3
# {4, 5, 6}
# set()
# {1, 2, 3, 4, 5, 6}
# {3, 4}

# Now, let's move to our next coding lesson...