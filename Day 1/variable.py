# A variable is a container for a value, which can be of various types
#Commenting in Python, u use #
'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
#Creating Variables
x, y, name, is_cool = (1, 2.5, 'John', True)
a = x+y
print(x, y, name, is_cool)
print(a)

#Casting : - Changing the type of a variable
#Initially our variable x is an Integer. Lets change it to a string as below

x = str(x)
print(type(x))

y = int(y)
print(type(y), y)