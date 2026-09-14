# Simple Inheritence

# # Base class
# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound.")

# # Drived Class
# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} barks")

# animal = Animal("Genric Animal")
# animal.speak()

# dog = Dog("Tommy")
# dog.speak()

# <=====> Super Keyword <=====>
# Base class
class Animal:
    def __init__(self):
        self.name = "Jackey"

    def speak(self):
        print(f"{self.name} makes a sound.")

# Drived Class
class Dog(Animal):
    def __init__(self, breed,behaviour):
        super().__init__()  # To inherit parent class constructor
        self.breed = breed
        self.behaviour = behaviour

    
    def speak(self):
        super().speak() # To inherit the Parent Class Method
        print(f"{self.name} barks in {self.behaviour} mood. It is a {self.breed} Dog.")

dog = Dog("German Shepherd","Angry")
dog.speak() 

