class Greetings:
    def hello(self,name=None):
        if name:
            print("Hello",name)
        else:
            print("Hello")
greetings=Greetings()
greetings.hello("Bob")
greetings.hello()

