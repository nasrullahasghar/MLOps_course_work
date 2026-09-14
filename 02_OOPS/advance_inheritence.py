# <==============> 1. Single Inheritence <==============>
# class Parent:
#     def __init__(self,name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, my name is {self.name}")


# class Child(Parent):
#     def play(self):
#         print(f"{self.name} is playing")


# # Create an object of the class
# child = Child("Rizwan")
# child.greet()
# child.play()

# # <==============> 2. Multi-level Inheritence <==============>

# # Base Class
# class Grandparent:
#     def __init__(self,name):
#         self.name = name

#     def tell_story(self):
#         print(f"{self.name} tells a story.")

# # Intermediat Class
# class Parent(Grandparent):

#     def work(self):
#         print(f"{self.name} is working.")

# # Drived Class
# class Child(Parent):
    
#     def play(self):
#         print(f"{self.name} is playing")


# # Create an object of the class
# child = Child("Rizwan")
# child.tell_story()
# child.work()
# child.play()


# <==============> 3. Hierarchical Inheritence <==============>

# class Parent:
#     def __init__(self,name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, my name is {self.name}")


# class Child1(Parent):
#     def play(self):
#         print(f"{self.name} is playing")

# class Child2(Parent):
#     def study(self):
#         print(f"{self.name} is studying")

# child1 = Child1("Kashif")
# child2 = Child2("Ahmad")

# child1.greet()
# child1.play()

# child2.greet()
# child2.study()


# <==============> 4. Multiple Inheritence (Diamond Problem)<==============>
# class A:
#     def __init__(self,name):
#         self.name = name

#     def greet(self):
#         print(f"Hello from A, {self.name}.")

# class B(A):
#     def greet(self):
#         print(f"Hello from B, {self.name}.")
#         super().greet()

# class C(A):
#     def greet(self):
#         print(f"Hello from C, {self.name}.")
#         super().greet()

# class D(B,C):
#     def greet(self):
#         print(f"Hello from D, {self.name}.")
#         super().greet()

# d = D("Mirza")
# d.greet()

# <==============> 5. Hybrid Inheritence<==============>
# Hybrid Inheritance

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound.")

# Intermediate class 1 (Hierarchical)
class Mammal(Animal):
    def feed(self):
        print(f"{self.name} is feeding milk.")

# Intermediate class 2 (Multiple)
class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying.")

# Derived class (Multiple Inheritance)
class Bat(Mammal, Bird):
    def __init__(self, name):
        Mammal.__init__(self, name)  # Explicitly calling the constructor

    def nocturnal(self):
        print(f"{self.name} is nocturnal.")

# Create an instance of Bat
bat = Bat("Bruce")
bat.sound()     # Output: Bruce makes a sound.
bat.feed()      # Output: Bruce is feeding milk.
bat.fly()       # Output: Bruce is flying.
bat.nocturnal() # Output: Bruce is nocturnal.