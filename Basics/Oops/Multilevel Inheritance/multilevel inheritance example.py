class Animal:
    def __init__(self,sound):
        self.sound=sound
    def speak(self):
        print(self.sound)

class Dog(Animal):
    def __init__(self,food,sound):
        super().__init__(sound)
        self.food=food
    def speak(self):
        super().speak()
        print(self.sound)
        print(self.food)
class Puppy(Dog):
    def __init__(self,food,sound,walk):
        super().__init__(food,sound)
        self.walk=walk
    def weep(self):
        print(self.walk)
        print("Puppy Weep")
Puppy1=Puppy("bone","bark","Yes")
Puppy1.weep()
Puppy1.speak()