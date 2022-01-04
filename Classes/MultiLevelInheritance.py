class Animal:
    def run (self):
        print("Animal is running...")

class Dog (Animal):
    def bark (self):
        print("Dog is barking")

class Puppy (Dog):
    def jump (self):
        print("Puppy is jumping")

#Single Level Inheritance
obj = Dog()
obj.bark()
obj.run()

#Multi Level Inheritance
obj1 = Puppy()
obj1.jump()
obj1.bark()
obj1.run()
