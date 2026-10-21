# -----------------------------
# Dictionaries In Python
# -----------------------------

# Dictionaries are mutable data types in Python, inside 2nd brackets({}), which are collections of key-value pairs, seperated by a colon. Note: Mutable means which can be changed after written.
# Eg:
a = {
    'Name':'Soura',
    'Language':'Python'
}
# Here, 'Name' and 'Language; are keys, whereas 'Soura' and 'Python' are values.
print(type(a)) # => Dictionary

d = {} # Empty Dictionary

# Dictionaries are:
# - mutable
# - unordered
# - indexed
# and also, cannot contain keys of smae name or duplicated keys.

# ---------------------
# Dictionary Methods
# ---------------------

# There are numerous dictionary methods to perform operations on dictionaries. Let's list some of them:
# Let's take the same dictionary 'a'.

# 1. get(): Returns the value of the key.
print(a.get('Name'))

# 2. keys(): Return all the keys of the dictionary.
print(a.keys())

# 3. values(): Returns all the values of the dictionary
print(a.values())

# 4. items(): Returns all the pairs of the dictionary.
print(a.items())

# 5. update(): Adds or updates the pairs of the dictionary.
a.update({'Language': 'Java'})
print(a)

#. pop(): Removes the pair from the dictionary and returns its value.
a.pop('Name')
print(a)

# Output:
# Soura
# dict_keys(['Name', 'Language'])
# dict_values(['Soura', 'Python'])
# dict_items([('Name', 'Soura'), ('Language', 'Python')])
# {'Name': 'Soura', 'Language': 'Java'}
# {'Language': 'Java'}

# Now let's move to our next coding lesson...