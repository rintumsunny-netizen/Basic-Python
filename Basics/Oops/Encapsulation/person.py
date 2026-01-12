class Person:
    def __init__(self,name,age,job):

        self.name=name
        self.__age=age #it is a private variable
        self._job=job
    def get_age(self): # it is used to retrieve
        return self.__age
    def set_age(self,age): #it is used to update
        self.__age=age