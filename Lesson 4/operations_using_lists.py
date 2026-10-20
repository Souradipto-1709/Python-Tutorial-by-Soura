# -------------------------------
# Operations Using Lists
# -------------------------------

# 1. Take a empty list as variable 'l'. Take 5 numbers as a input from the user and add them to the list. At last, sort them and print the list.
l = []
n1 = int(input('Enter Number 1: '))
n2 = int(input('Enter Number 2: '))
n3 = int(input('Enter Number 3: '))
n4 = int(input('Enter Number 4: '))
n5 = int(input('Enter Number 5: '))
l.append(n1)
l.append(n2)
l.append(n3)
l.append(n4)
l.append(n5)
l.sort()
print(l)

# 2. Take a list and reverse it.
l = [3, 9, 6, 21, 0, 47]
l.reverse()
print(l)

# 3. Count the occurence of the number 10 in the list: [2, 6, 10, 7, 0.8, 11.7, 10].
l = [2, 6, 10, 7, 0.8, 10, 11.7, 10]
print(l.count(10))

# 4. Perform list slicing on the list as per your choice. List: [9, 3.5, 'Soura', False, 'Java']
l = [9, 3.5, 'Soura', False, 'Java']
print(l[1:4])

# Keep Practising and Coding

# HAPPY CODING! 🚀