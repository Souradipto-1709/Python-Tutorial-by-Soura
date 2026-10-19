# ---------------------------
# Operations Using Strings
# ---------------------------

# 1. Take a string as 'Good Afternoon, Soura', and replace 'Soura' with your name.
str = 'Good Afternoon, Soura'
print(str.replace('Soura', 'John'))

# 2. Take a input from the user to check that the input starts with 'hello' or not.
text = input('Write Something: ')
print(text.startswith('hello'))

# 3. Take a input from the user and change it to uppercase.
text = input('Write Something: ')
print(text.upper())

# 4. Write a program to detect the word 'Java' in a string, and replace it with the word 'Python'.
str = 'I love Java'
if('Java' in str):
    print('Word Detected')
    print(str.replace('Java', 'Python'))
else:
    print('No Word Detected')
    
# 5. Using the escape sequence characters, modify the text: 'Hello, I love Python.'
print('Hello,\nI love \'Python\'.')


# Keep Practising and Coding

# HAPPY CODING! 🚀