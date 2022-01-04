class Person:
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

    def show(self):
        print(self.name, self.age)

obj1 = Person("Mathew",47)
obj2 = Person("Sibi",47)
obj3 = Person("Teena",47)
print("Number of Objects of a class ", Person.count)

print(obj1.__dict__)
print(obj1.__doc__)
print(obj1.__module__)
