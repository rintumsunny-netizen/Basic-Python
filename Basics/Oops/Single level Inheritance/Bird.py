class Bird:
    def __init__(self,sound):
        self.sound=sound
    def speak(self):
        print(self.sound)
        

class Parrot(Bird):
    def __init__(self,food,sound):
        super().__init__(sound)
        self.food=food
    def speak(self):
        super().speak()
        print(self.sound)
        print(self.food)
parrot1=Parrot("grains",'keke')
parrot1.speak()