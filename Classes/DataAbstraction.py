class Employee:
    __salary = 120000
    def getSalary(self):
        print("Salary is ",Employee.__salary)

obj = Employee()
obj.getSalary()

#print(Employee.__salary) #AttributeError: type object 'Employee' has no attribute '__salary'