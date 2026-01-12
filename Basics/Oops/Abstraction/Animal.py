from abc import ABC, abstractmethod


class Animal(ABC):#ABC is builtin abstarct class
    @abstractmethod
    def sound(self):
        pass
    def eat(self):
        print("Animal Eats")
class Cat(Animal):
    def sound(self):
        print("Cat makes sound Meow")
cat1= Cat()
cat1.sound()
cat1.eat()