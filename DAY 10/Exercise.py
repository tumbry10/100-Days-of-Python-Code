'''write a function to find the first repeated character in a string.'''

def first_repeated_charecter(s):
    seen = []
    for char in s:
        if char in seen:
            return char
        seen.append(char)
    return None

input_string = input('Enter the string to check for repeated Characters: ')
result = first_repeated_charecter(input_string)
if result:
    print(f'The first repeated character is {result}')
else:
    print('No repeated character found')