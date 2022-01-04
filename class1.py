class Student:
    def __init__(self, id, name, age, gender):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender


st = Student(100, "Ancy",28, "F")
print(st.id, st.name)
