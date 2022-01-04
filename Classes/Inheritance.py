class Animal:
    def run (self):
        print("Animal is running...")

class Dog (Animal):
    def bark (self):
        print("Dog is barking")

obj = Dog()
obj.bark()
obj.run()