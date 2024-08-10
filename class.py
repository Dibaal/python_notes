# OOP is a programming paradigm based on the concept of "objects", which can contain data
# and code to manipulate that data.ie the objects contain the data and the code to manipulate the data.

#CLASS: Is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.ie in the class we define the methods and the attributes that the object will have.

class Car: #This line defines a new class named Car. Car here is the blueprint for creating Car objects. 
    def __init__(self, make, model, year): # Constructor method/initializer. It's a special method that gets called when a new instance of the class is created. Self parameter refers to the instance of the class being created.
        self.make = make #Assigns the value of the make parameter to the instance variable self.make
        self.model = model #Assigns the value of the model parameter to the instance variable self.model
        self.year = year #Assigns the value of the year parameter to the instance variable self.year

    def display_info(self): # Is a method(function) defined inside the class Car.Is intended to operate on instances of the class car(in this case) because it is created within the class Car block as shown from the indentation.Method is the logic for manipulating data provided by the instance(object). The method is where we set the logic for manipulating the data that comes with the object.
        print(f"{self.year} {self.make} {self.model}")


#Class Keywors: The 'class Car:' Indicates the start of the class definition.
#Indentation: The __init__ and display_info methods are indented under the Car class, showing they are part of the class.
#Method is the logic for manipulating data provided by the instance(object), this logic is stated in the method.
#Instance(object):An individual object created from a class, containing its own data (attributes)
#To call a method for reusability within the code, you create an instance of the class and then call the method on the instance.

# Creating instances of the Car class
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2018)

# Calling the display_info method on each instance
car1.display_info()  # Output: 2020 Toyota Corolla
car2.display_info()  # Output: 2018 Honda Civic

#FOUR PILLARS OF OOP

# 1. ENCAPSULATION: Is the bundling of data and methods that operate on that data within one unit e.g a class. It restricts direct access to some of the object's components.
#Private attributes: In python, private attributes are indicated by prefixing the attribute name with double underscores(__).
#Private attributes restrict direct access to these attributes from outside the class
#Benefits of Enpcapsulation: Data Hiding, Controlled Access, Modularity. 
#Example of encapsulation is as below

class Person: #Defines a new class named person
    def __init__(self, name, age): #This is the constructor method that initializes new instance of the person class. Takes name and age as the parameters.
        self.__name = name  # Assigns the name parameter to a Private attribute __name. The double underscore (__) prefix makes the attribute private.
        self.__age = age    # Private attribute

    def get_name(self):#This method returns the value of the private attibute __name
        return self.__name 

    def get_age(self): # Returns the value of the private attribute __age
        return self.__age

person = Person("Alice", 30)
print(person.get_name())  # Output: Alice. Accessed the private attributes via Getter methods as shown here,

#2. INHERITANCE: Is a way to form new classes using classes that have already been defined. It helps to reuse the code. See example below:

class Animal: #Defines a base class named Animal
    def __init__(self, name): # The constructor method of the animal class. It initializes the name attribute
        self.name = name #Assigns the name parameter to the instance attribute name

    def speak(self):#Method named speak, defined in the Animal class.
        pass

class Dog(Animal): #Defines a derived class named Dog that inherits from the Animal class. This means Dg will inherit all attributes and methods from Animal.This is the derived class definition.What makes this a derived class from the class Animal? class Dog(Animal): This line indicates that Dog is inherited from Animal. The Animal class is specified in parenthesis. Which means Dog will inherit all attributes and methods from Animal.By inheriting from Animal, the Dog class automatically has access to all the attributes and methods defined in the Animal class, unless they are overriden as below.
    def speak(self): # This overrides the method above as it provides it's own implementation of the speak method which overrides the speak method in Animal above. 
        return "Woof!"

dog = Dog("Buddy")
print(dog.speak())  # Output: Woof!
# This inheritance relationship allows Dog to reuse and extend the functionality of Animal, making it a derived class.

#POLYMORPHISM: allows methods to do different things based on the object it is acting upon, even though they(methods) share the same name.

class Bird:#Defines a base class named Bird
    def fly(self):#This is a method within the Bird class. Here we did not use the initializer (__init__), but it is still valid. We mostlu use the initializer when we want to ensure that the object starts with a specific state or when we want to pass parameters to the object upon creation. Here we did not pass any parameters.
        return "Flying high!"

class Penguin(Bird):#This is a subclass from the Bird class bc (Bird).It is named Penguin, it inherits from the Bird class.
    def fly(self): #This method is defined within the Penguin class, overriding the fly method of the Bird class.
        return "I can't fly!"

bird = Bird()
penguin = Penguin()
print(bird.fly())    # Output: Flying high!
print(penguin.fly()) # Output: I can't fly!

#Polymorphism allows objects of different classes to be treated as objects of a common superclass.
#In this example when calling the fly method on instances of Bird and Penguin, the appropriate method for each class is executed, showcasing polymorphism.

#4. ABSTRACTION: Is the concept of hiding the complex implementation details and showing only the necessary features of the object.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height): # The init method initializes width and height attributes of the Rectangle instance
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(10, 20)
print(rect.area())  # Output: 200




# #OOP: Object Oriented Programming

# #CONCEPTS OF OOP
# #CLASS: A blueprint for creating objects. 
# #OBJECT: A particular instance of a class.
# #INHERITANCE: MECHANISM WHERE A NEW CLASS CAN INHERIT ATTRIBUTES AND METHODS FROM AN EXISTING CLASS, BASE OR PARENT CLASS.
# #POLYMORPHISM: Allows object of different classes to be treated as objects of a common superclass


# class Car:
#     def __init__(self, make, model): # Class (blue print), defining attributes make and model
#         self.make = make
#         self.model = model

#     def drive(self): # method (function) drive behaviour
#         print(f'Driving the {self.make} {self.model}')
    
#     def sound(self):
#         print(f'The {self.make} {self.model} makes a vroom sound')

# # TO INHERIT A CLASS AND CREATE OUR OWN CLASS, WE USE THE FOLLOWING SYNTAX

# class ElectricCar(Car): # Creating electricCar(child class) inheriting the behaviuor of our car(parent class) above
#     def charge(self): 
#         print('Charging the {self.make} {self.model}') #Inherits the attributes

# tesla = ElectricCar('Tesla', 'model S') #Creating a copy of ElectricCar. It inherits the behavious of base and subbase classes above.

# # tesla.charge() 
# # tesla.drive()
# # tesla.sound()



# #Polymorphism
# class Animal: # Blue print to demonstrate polymorphism
#     def make_sound(self): # Came with no default, just make sound behavious. Allows us to customise the attributes to suite our need.
#         pass #Means don't return anything, just pass.

# class Dog(Animal): # Show the concept of polymorphism as we override the attribute from the parent class to create what we need
#     def make_sound(self):
#         print('woof') # The default from the parent class is pass, but we want print('woof) in here. Once we specify it as shown, it ignores the default. That is polymorphism

#     def make_sound(self):
#         print('A dog makes a woof sound') # This will override the parent attribute.
    
# # dog = Dog() # To run the instance of a dog

# # dog.make_sound() # if we run this we would get woof and not just the pass

# class Cat(Animal): # Show the concept of polymorphism as we override the attribute from the parent class to create what we need
#     def legs(self): # Created my own animal but inherited from the base class(Inheritance)
#         print('A cat has fore legs')
    
#     def make_sound(self):
#         print("A cat makes a meew sound") # This overrides the defaulf (polymophism)

# # cat = Cat()
# # cat.makesound()

# class Cow(Animal): # Show the concept of polymorphism as we override the attribute from the parent class to create what we need
#     def legs(self): # Created my own animal but inherited from the base class(Inheritance)
#         print('A caw has fore legs')
    
#     def make_sound(self):
#         print("A cow makes a moo sound") 
    






 

# Lexus = Car("Toyota", "Lx470") # Object (Subclass copy of the class) of Car. Inherit the attributes of the class Car (ie make, model)
# BMW = Car("BMW", "X6")       # Object (Subclass) of Car. Inherit the attributes of the class Car (ie make, model)




# Lexus.drive() # Calling the behaviour of the blueprint drive behaviour
# BMW.drive() #Calling the behavious of the blueprint

# Goat.sound()
# Cow.sound()

# #WHEN WE HAVE A PROGRAM THAT USERS WILL NEED TO EXTEND AND CREATE THEIR'S, WE CAN USE OOP TO DEFINE A CLASS THAT WILL BE USED TO CREATE OBJECTS THAT WILL INHERIT THE ATTRIBUTES AND BEHAVIOURS OF THE CLASS. THIS WILL HELP US TO AVOID WRITING THE SAME CODE MULTIPLE TIMES.
#REASON FOR OOP: When we have multiple objects that share the same attributes and behaviours, we can use OOP to define a class that will be used to create objects that will inherit the attributes and behaviours of the class. This will help us to avoid writing the same code multiple times.

# import re

# #A valid MasterCard number starts with 51 through 55 and is 16 digits long. 
# def valid_mastercard(number):
#     pattern = r'^(5[1-5][0-9]{14})$'


#     if re.match(pattern, number):
#         print("Valid mastercard number")
#     else:
#         print("Invalid mastercard number")

# mastercard_number = "5391234567891299"



# print(valid_mastercard(mastercard_number))  
# # C

# a = "Hello, World!"
# print(a[12])

# 1, -5, 0, 10 

# a = int('10') #10
# b = 3.14
# b = int(3.14) # 3
# print(b)



# float(2) #2.0


# strings = 'abc1952'
# print(strings[0])


# greeting = "Hello, " + "World!" # Concatenation
# print(greeting)


# print(greeting[12])

# #SLICING
# S = "Hello World!"
# # print(S[7:12]) # orld!
# # print(S[3:5]) # lo
# print(S[:-1]) # Hello World

# print(S[2:-2])
# print(S[-3]) #r

# print(len(S))

# list
# name = ["Alice", "Bob", "Charlie"]

# print(name[0])

# #insert
# name.insert(1 , "Eve")
# print(name)

#Add
# name[1] = "Beatrice"
# print(name)

#Remove
# name.remove('Bob')
# print(name)

# name.pop(0)
# print(name)

# del name[2]
# print(name)

#Tuples

# a = ("apple", "banana", "cherry")
# print(a[0])
# b = list(a)
# b.remove('apple')
# b.pop(2)
# del b[0]
# print(b)

# a = tuple(b)
# print(a)

# for x in range(6):
#      print(x)

#List comprihension

# squares of numbers from 1 to 10

# squares = [x**2 for x in range(0,10)]
# print(squares)


# string = "Hello World"

# upper_case = [x.upper() for x in string]
# print(upper_case)

# a = [x for x in range(6)]
# print(a)

# persons = {
#      "name": "John",
#      "age": 30,
#      "city": "New York"
#  }

# print(person["city"]) 

# person["age"] = 31

# print(person)

# print(person['name'])
# print(person['sex'])

# print(person.get('sex'))

# print(person.get('sex', 'not provided'))

# print(person.get('Country', 'Country not on the List '))

for key,value in persons.items():
    print(f"{key}:{value}")
    # print(value)
    # print(f"key: {'name'}")


     






# persons = [
#     {"name": "John", "age": 30, "city": "New York"},
#     {"name": "Mark", "age": 50, "city": "PH"}
# ]

#  To change John's age to 31
# for y in persons:
#     if y["name"] == "John":
#         y["age"] = 31


# print(persons)

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)

aliens = []
for alien_number in range(30): #Returns series of numbers which just tells python how many times we want the loop to repeat
   new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
   aliens.append(new_alien) #We append each new alien to the empty list
#To show the 1st 5 aliens out of the 30 created with slicing
for alien in aliens[:5]:
    print(alien)







