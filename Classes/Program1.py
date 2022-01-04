class Car:
    def __init__(self, modelName, Year):
        self.modelName = modelName
        self.Year      = Year

    def display(self):
        print("Model Name ", self.modelName)
        print("Year ", self.Year)

obj = Car("Toyota", 2022)
obj.display()