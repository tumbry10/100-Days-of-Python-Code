def d():
    color = "green"
    def e():
        nonlocal color
        color = "yellow"
    e()
    print("Color: " + color)
    color = "red"
color = "blue"
d()

#Find the output of the code below
num = 9
class Car:
    num = 5
    bathrooms = 2

def cost_evaluation(num):
    num = 10
    return num

class Bike():
    num = 11

cost_evaluation(num)
car = Car()
bike = Bike()
car.num = 7
Car.num = 2
print(num)

'''Which of the following is the correct implementation that will return True if there is a parent class P, with an object p and a sub-class called C, with an object c?


print(issubclass(P,C))



print(issubclass(p,C))



print(issubclass(C,P))



print(issubclass(C,c))


1 point
'''

'''Which of the following is not true about Integration testing:


It combines unit tests.



Tests the flow of data from one component to another.



Primarily dealt by the tester.



It is where the application is tested as a whole.


1 point
'''

#What will be the output 
class A:
   def a(self):
       return "Function inside A"

class B:
   def a(self):
       return "Function inside B"

class C:
   pass

class D(C, A, B):
   pass

d = D()
print(d.a())

'''
What will be the type of time complexity for the following piece of code:


def bigo(numbers):
    for i in numbers:
        print(numbers)

bigo([1, 7, 13, 19])


Linear Time



Constant Time



Logarithmic Time



Quadratic Time


1 point
'''