from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def abstractmethod(self):
        pass

    def conceretemethod(self):
        print("Message from conceretemethod")


class Triangle(Polygon):
    def abstractmethod(self):
        print("Message from Triangle")


class Square(Polygon):
    def abstractmethod(self):
        print("Message from Square")


class Pentagon(Polygon):
    def abstractmethod(self):
        print("Message from Pentagon")


obj1 = Triangle()
obj1.abstractmethod()

obj2 = Square()
obj2.abstractmethod()

obj3 = Pentagon()
obj3.abstractmethod()

obj4 = Polygon() # TypeError: Can't instantiate abstract class Polygon with abstract method abstractmethod
#obj4.abstractmethod()

#print(Polygon.conceretemethod())
