class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show(self):
        print(self.name, self.age, self.gender)

obj = Person("Mathew",47, "M")
obj.show()

print(getattr(obj,'name'))

setattr(obj,"age",10)
print(getattr(obj,'age'))

delattr(obj,"age")
#print(getattr(obj,'age'))

print(hasattr(obj,"name"))
print(hasattr(obj,"forename"))