# -------------------------------------
# Operations Using Sets
# -------------------------------------

# 1. Create a empty set 's', and ask the user to input some numbers and then add it to the set, and print it.

s = set()
n1 = int(input('Enter no 1: '))
n2 = int(input('Enter no 2: '))
n3 = int(input('Enter no 3: '))
s.update({n1, n2, n3})
print(s)

# 2. Take two sets, and write a program to find out the similar elements in the two sets.
# s1 = {2, 63, 10, 9, 45}
# s2 = (34, 81, 75, 10, 9, 47)

s1 = {2, 63, 10, 9, 45}
s2 = (34, 81, 75, 10, 9, 47) 
print(s1.intersection(s2))

# 3. Write a program to remove one of the element from the set, but the program shouldn't raise an error, if element not present in the set. s = {21, 87, 90, 63, 101}

s = {21, 87, 90, 63, 101}
n = int(input('Enter a no: '))
s.discard(n)
print(s)

# 4. What will happen if we add two similar elements to a set?

# It will remove one of the same elements as sets are collections of non-repetive elements.
s = {10, 10}
print(s) # Removes one of the 10.

# Keep Practising and Coding

# HAPPY CODING! 🚀