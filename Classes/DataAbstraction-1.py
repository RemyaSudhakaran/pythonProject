from abc import ABC, abstractmethod

class BaseClass(ABC):
    def abstractmethod(self):
        pass

class DerivedClass1 (BaseClass):
    def abstractmethod(self):
        print("Message from Derived Class 1")

class DerivedClass2 (BaseClass):
    def abstractmethod(self):
        print("Message from Derived Class 2")

class DerivedClass3 (BaseClass):
    def abstractmethod(self):
        print("Message from Derived Class 3")

obj1 = DerivedClass1()
obj1.abstractmethod()

obj2 = DerivedClass2()
obj2.abstractmethod()

obj3 = DerivedClass3()
obj3.abstractmethod()
