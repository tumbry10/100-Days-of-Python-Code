''' The input() fn allows a program to take user input 
    By default, watever the user types is a string'''

name = input('Enter your name: ')
print ('Hello ' + name + '!')

#Converting Inputs to other DataTypes
age = int(input('Enter your Age : '))
print(f'You are {age}years Old')
'''If the user enters something that cannot be converted to a no, python raise an error'''

# Multiple Inpute Statements 
name = input('Enter your name: ')
age = int(input('Enter your age: '))
height = float(input('Enter your height in m: '))

print(f'Hello {name}, you are {age}years old and {height}m tall')