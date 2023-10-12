#Python Classes:
"""
A class is considered as a blueprint of objects.We use the class keyword to create a class in Python. For example,

class ClassName:
    # class definition """
class Bike:
    name = ""
    gear = 0
"""
Bike - the name of the class
name/gear - variables inside the class with default values "" and 0 respectively.
The variables inside a class are called attributes.
"""
#Python Objects:
"""
An object is called an instance of a class. For example, suppose Bike is a class then we can 
create objects like bike1, bike2, etc from the class
"""
class Bike:
    name = ""
    gear = 0

# create objects of class
bike1 = Bike()

#Access Class Attributes Using Objects:
"""
We use the . notation to access the attributes of a class. 
"""
# modify the name attribute
bike1.name = "Mountain Bike"

# access the gear attribute
bike1.gear

#EXAMPLE 1 :

class Bike:
    name = ""
    gear = 0

bike1 = Bike()

# access attributes and assign new values
bike1.gear = 11
bike1.name = "Mountain Bike"

print(f"Name: {bike1.name}, Gears: {bike1.gear} ")

#EXAMPLE 2 :
#Create Multiple Objects of Python Class:

class Employee:
    employee_id = 0

employee1 = Employee()
employee2 = Employee()

employee1.employee_id = 1001
print(f"Employee ID: {employee1.employee_id}")

employee2.employee_id = 1002
print(f"Employee ID: {employee2.employee_id}")
#Output
# Employee ID: 1001
# Employee ID: 1002

#Python Methods:
"""We can also define a function inside a Python class. 
A Python Function defined inside a class is called a method."""
#Example:
class Point:
    def move(self):
        print("move..")
    def draw(self):
        print("draw") 
point1=Point()
point2=Point()
point1.draw()
point2.move() 
point2.x=1
print(point2.x)

#Example:

class Room:
    length = 0.0
    breadth = 0.0
    
    def calculate_area(self):
        print("Area of Room =", self.length * self.breadth)

study_room = Room()
 
study_room.length = 42.5
study_room.breadth = 30.8

study_room.calculate_area()     

#Python Constructors:
"""
__init__() is the constructor function that is called whenever a new object of that class is instantiated."""
#Example:
class Person:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print(f"Hi I am {self.name}.")   
person1=Person("Nuzhat Fatima")
person1.talk()  

person2=Person("Hamza Khan")
person2.talk()


