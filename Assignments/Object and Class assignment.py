#Class Creation
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        print(self.brand,self.model)
#Creating two car objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")
#Display the details
car1.display()
car2.display()
#Create a class calculator with methods
class calculator:
    def addition(self,a,b):
      return a + b
    def subtraction(self,a,b):
       return a - b
calc=calculator()
print(calc.addition(10,20))
print(calc.subtraction(10,20))