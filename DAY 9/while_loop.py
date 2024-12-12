''' A while loop is a block of code to be executed repeatedly as long as a certain condition is true.
    Its useful when u dont noe in advance how many times the loop will run but have a condition to continue looping
    
    Synthax of while loop
    while condition:
        code to be executed repeatedly
        
    CONDITION: - A boolean expression that is checked before every iteration of the loop.
                If true the loop continue, if false the loop stop.'''

# EXAMPLE
'''The loop will print the value of counter and increases it by one after each iteration
The loop will stop when counter is greater than 5'''

counter = 1
while counter <= 5:
    print(f'Counter is : {counter}')
    counter += 1

# USER INPUT WHITH WHILE LOOP : Using a while loop to ask user for input repeatedly until they give a specific response

response = ''
while response != 'yes':
    response = input('Type yes to exit : ')
print('GoodBye!')