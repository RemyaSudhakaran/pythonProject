#Type 1
class Person:
    def __init__(self):
        self.name = "John"
        self.age = 45

    def show(self):
        print(self.name, self.age)

obj = Person()
obj.show()

#Type 2
class Color:
    def __init__(self):
        print("Non-Parametrized Constructor - init() method")
    def show(self):
        print("Non-Parametrized Constructor - show() method")

obj1 = Color()
obj1.show()