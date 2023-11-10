# I keep my object instantiated variables and method calls. 
# Looks for a dog.py file that has the name dog in it.
from dog import Dog

# Instantiation call that creates a Dog odbject:
# I stored my instance in a variable (instance variable).
# Else it just lives in memory and I won't beable to access it.
my_dog = Dog("Torgal", "SuperDog")
my_dog_2 = Dog("Deigo", "Husky")
my_dog_3 = Dog("Stephanie", "Poodle")

# Dog's behavior: instance method
my_dog.sic()
my_dog_2.sit()
my_dog_3.roll_over()


