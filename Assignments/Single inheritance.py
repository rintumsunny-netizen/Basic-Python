# Part 1: Company and Employee classes
class Company:
    def __init__(self, company_name):
        self.company_name = company_name

    def display_company(self):
        print(self.company_name)


class Employee(Company):
    def __init__(self, company_name, employee_name):
        # Call parent constructor
        super().__init__(company_name)
        self.employee_name = employee_name

    def display_employee(self):
        print(self.employee_name,self.company_name)


# Creating objects
emp1 = Employee("Microsoft", "Alice")
emp2 = Employee("Google", "Boby")
emp1.display_employee()
emp2.display_employee()


# Part 2: Vehicle and Bike classes
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def display_vehicle(self):
        print(self.vehicle_type)


class Bike(Vehicle):
    def __init__(self, brand):
        # Call parent constructor using super()
        super().__init__("Two-Wheeler")
        self.brand = brand

    def display_bike(self):
        print(self.brand, self.vehicle_type)


# Creating Bike object
bike1 = Bike("Yamaha")
bike2 = Bike("Royal Enfield")

bike1.display_bike()
bike2.display_bike()
