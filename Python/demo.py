# name = "Asli"
# age = 26
# print(type(name)) #class string
# print(type(age)) #class integer

# print(name.upper())
# print(dir(name))

#Build your own class, rather than use class string or class int for exmaple
#OOP - Object Oriented Programming, style of programming based on ojects, help us create a blueprint to create the class

#by convention class names start with Uppercase
# We use def in functions, we call it method if it belongs to a class
# init - is to initialise the object
# whenever we want to create the object, we initialise it from the class
# first parameter in the method will be self 
# age and breed are attributes of this method - size, breed, colour, age ect.
# methods / actions - talk, walk, play ect.

class Dog:

    def __init__(self, age, breed):
        #age = 3
        #Jett's age will now be 3 & breed will be a pug
        #this menthod won't return, but others can
        self.age = age
        self.breed = breed

    def talk(self):
        return "Bark"

Jett = Dog(3, "pug")
Jett.talk()


