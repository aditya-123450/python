class Animal:

    # attribute and method of the parent class
    
    def eat(self):
        print("I can eat")

# inherit from Animal
class Dog(Animal):

    # new method in subclass
    def display(self):
        # access name attribute of superclass using self
        print("My name is ")
a=Dog()
a.eat()       