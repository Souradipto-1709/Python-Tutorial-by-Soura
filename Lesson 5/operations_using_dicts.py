# --------------------------------
# Operations Using Dictionaries
# --------------------------------

# 1. Take a dictionary, take 5 names of student as keys, and provide names for their 5 favourite, unique laptop brands. When the user enters the name of each student, it will show his/her favourite laptop brand.

name_laptop = {
    'Soura':'HP',
    'John':'Lenovo',
    'Tom':'MacBook',
    'Rahul':'Dell',
    'Anna':'Asus'
}

name = input('Enter Student Name: ')
if('Soura' in name):
    print(name_laptop.get('Soura'))
elif('John' in name):
    print(name_laptop.get('John'))
elif('Tom' in name):
    print(name_laptop.get('Tom'))
elif('Rahul' in name):
    print(name_laptop.get('Rahul'))
elif('Anna' in name):
    print(name_laptop.get('Anna'))
else:
    print('No Student!')
# A simple if-elif-else conditional program

# 2. Create a empty dictionary. Allow the user to give input for names of 5 friends and also their favourite languages. Fill the empty dictionary with these names and their favourite languages and print it.

d = {}
name1 = input('Enter the name: ')
lang1 = input('Enter the favourite language: ')
name2 = input('Enter the name: ')
lang2 = input('Enter the favourite language: ')
name3 = input('Enter the name: ')
lang3 = input('Enter the favourite language: ')
name4 = input('Enter the name: ')
lang4 = input('Enter the favourite language: ')
name5 = input('Enter the name: ')
lang5 = input('Enter the favourite language: ')

d.update({
    name1:lang1,
    name2:lang2,
    name3:lang3,
    name4:lang4,
    name5:lang5
})
print(d)

# 3. Build a grade detector system using dictionaries, where take 4 keys as grades, and 4 values as the marks. Take the input from the user as a grade, and print that inputed grade means how much marks.

grade_marks = {
    'A':'90-100',
    'B':'75-89',
    'C':'60-74',
    'D':'Fail'
}

grade = input('Enter the grade: ')
if('A' in grade):
    print(grade_marks.get('A'))
elif('B' in grade):
    print(grade_marks.get('B'))
elif('C' in grade):
    print(grade_marks.get('C'))
elif('D' in grade):
    print(grade_marks.get('D'))
else:
    print('Wrong Grade entered!')
# A simple if-elif-else conditional program

# Keep Practising and Coding

# HAPPY CODING! 🚀