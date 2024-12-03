'''Write a simple program that calculate the sum of two numbers. The numbers are 2 diff user input
NB: Numbers can be decimals or integers
'''
# SOLUTION 
'''
    First we have to get the user inputs using the input() fn.
    Make sure the inputs are floats.
    Either we can limit the user to only input float numbers OR allow the user to enter strings,
    then cast them to flot'''

'''num_1 = input('Enter the First Number: ')
num_2 = input('Enter the Second Number: ')
add = float(num_1) + float(num_2)
print(f'The sum of {num_1} and {num_2} is : {add}')
'''

num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))
add = num1 + num2
print(f'The sum of {num1} and {num2} is {add}')