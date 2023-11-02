# I can keep my object STATE (properties and values) in here and their BEHAVIOR (methods)
class Dog:
# __init__ is my constructor method.
# It runs whenever an isntance of my class is created.
# It is mainly used to assign values to my properties.
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print("dog initialized")

    # Methods are defined as thier own named functions inside the class.
    def sic(self):
        print(f'{self.name} woofs!') 

    def sit(self):
        print(f'{self.name} sits')

    def roll_over(self):
        print(f'{self.name} rolls over')

