# STRINGS
'''
    A string is a collection of one or more xtersput in single, double, or even tripple quotes.

'''

# Creating  A string
name = 'Nyasha'
age = 30

#Concatenate
#Remember age is an int, we have to cast it to a string b4 concatenating it

print('My name is ' +name+ ' and I am ' +str(age)+ 'years old.')

# String Formatting
#A better method of concatinating than the above. Methods of string formating are : 

#ARGUMENTS BY POSITION
print('My name is {name}, and I am {age}years old.'.format(name=name, age=age))

#F-Strings -- Only available from python 3.6 upwards
print(f'My name is {name}, and I am {age}years old.')

# String Methods
s = 'hello world'

#capitalize string : - It capitalizes the first xter of the string
print(s.capitalize())

#Make all xters Uppercase
print(s.upper())

# Make all xters lower case 
print(s.lower())

#Swap-case
print(s.swapcase())

# Get The length of the string
print(len(s))

# Replace : - replace the word world with everyone in the string
print(s.replace('world', 'everyone'))

# Count - Count the number of sub-strings in the string
sub = 'h'
print(s.count(sub))  #count the number of h's in the string

#Start with & end with - Boolean True or False

# split(), find() e.t.c 