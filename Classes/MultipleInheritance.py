class Animal:
    def run (self):
        print("Animal is running...")

class Dog:
    def bark (self):
        print("Dog is barking")

class Puppy (Dog, Animal):
    def jump (self):
        print("Puppy is jumping")
        


#Multiple Inheritance
obj1 = Puppy()
obj1.jump()
obj1.bark()
obj1.run()

print("**** issubclass checking ****  ")

print(issubclass(Puppy,Animal)) #True
print(issubclass(Puppy,Dog))    #True

print(issubclass(Animal, Puppy))#False
print(issubclass(Dog, Puppy))   #False

print("**** isinstance checking ****  ")
print(isinstance(obj1, Puppy))
print(isinstance(obj1, Animal))
print(isinstance(obj1, Dog))