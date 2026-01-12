class Student:#class definition
    schoolname="MKMHSS" #it is a class variable or global variable
    def __init__(self,name,age):#self is used for each objects to distinguish and to focus
        #init is called constructor- it is used for the creation of object
       print("Student object created")
       self.name=name
       self.age=age #these are parameterized constrcutor:#self.name and self.age are instance variable
    def display(self):
        print(self.name,self.age,Student.schoolname)
student1=Student("anu",25)
student1.display()

#imp
#python contain default constructor, but its not mandatory inorder to perform some manipulation when the object is created
