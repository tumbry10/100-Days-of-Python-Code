# A function is a block of code which only runs when it is called

# Create a fn
def sayHello(name):
    print(f'Hello, {name}')
sayHello('Nyasha')

#Function Return Value
def getSum(num1, num2):
    total = num1 + num2
    return total
num = getSum(3, 4)
print(num)  #To output the returned value to the console

#LAMBPA FUNCTIONS
# Its a small anonymous fn tt takes any number of arguments but can only have one expression

getSum = lambda num1, num2 : num1 + num2
print(getSum(10, 3))
    