class Employee:
    name = 'Harry'
    age  = 25
    gender = 'M'
    def displayFunction (self):
        print("Name = %s, Age = %d , Gender = %s  " %(self.name, self.age, self.gender))


obj = Employee()
print(obj.name)

obj.displayFunction()