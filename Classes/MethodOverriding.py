class Bank:
    def getROI (self):
        print("Bank Rate of Interest is ",10)

class SBI (Bank):
    def getROI(self):
        print("SBI Rate of Interest is ", 8)

class ICICI (Bank):
    def getROI(self):
        print("ICICI Rate of Interest is ", 12)

class HDFC (Bank):
    def getROI(self):
        print("HDFC Rate of Interest is ", 7)

obj1 = Bank()
obj1.getROI()

obj2 = SBI ()
obj2.getROI()

obj3 = ICICI()
obj3.getROI()

obj4 = HDFC()
obj4.getROI()