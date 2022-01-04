class Student:
    def __init__(self, name, age, gender, percent):
        self.name = name
        self.age  = age
        self.gender = gender
        self.percent = percent

    def showStudentDetails(self):
        print("Name of Student is - ", self.name)
        print("Age of Student is - ", self.age)
        print("Gender of Student is - ", self.gender)
        print("Percentage - ", self.percent)

obj = Student("Tina", 15, "Female", 98 )
obj.showStudentDetails()
