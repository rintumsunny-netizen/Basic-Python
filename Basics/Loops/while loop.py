from Basics.Oops.Encapsulation.person import Person

x="name"
print(x)
length=len(x)
i=0
count=0
while i<length:
    if x[i]=="a" or x[i]=="e" or x[i]=="i" or x[i]=="o" or x[i]=="u":
        count=count+1
    i=i+1
print(count)

person1=Person("James",23,"Python developer")
print(person1.name)
#print(person1.__age)
print(person1.get_age())




