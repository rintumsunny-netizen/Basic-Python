from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):

        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Instantiate the subclass, not the abstract class
obj = Rectangle(5, 3)
print(obj.area())  # Output: 15
