# List represent by [],it can be eitheb stringb or int or any data
list1=["sikha",2,"Ullas"]
print(list1)
print(list1[0])
#Nagative indexing right to left
print(list1[-1])
#List manipulation methods are (insert,appending,sort ,index)
#1.insert -to add new data to the list where ever user need to add
list1.insert(1,6)
print(list1)

#2.appending data will be add on the end of the list
list1.append(45)
print(list1)
list2=[46,25,32,57]
list2.sort()
print(list2)
list3=["car","bar","tar"]
list3.sort()
print(list3)
list3.reverse()
print(list3)
print(list3.index("car")) # index will give you the value of index to konw the position of index



