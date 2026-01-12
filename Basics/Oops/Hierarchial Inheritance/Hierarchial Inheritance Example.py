class Vehicle:
    def vehicle_Details(self,wheels):
        print("Vehicle contains", wheels)
class Bike(Vehicle):
    def bike_Details(self,wheels,model):
        super().vehicle_Details(wheels)
        print("Bike model is", model)
bike1=Bike()
bike1.bike_Details(2,"Honda")

class Car(Vehicle):
    def car_Details(self,wheels,model):
        super().vehicle_Details(wheels)
        print("Car model is", model)
car1=Car()
car1.car_Details(4,"Maruti")
#For testing purpose, only single level inheritance are used:


