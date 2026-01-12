message="hai world"
print(message[1])
print(message[-1])
#Slicing
print(message[:5])
print(message[2:7]) #starting from index value 2 to 6
#concatennation
concat = "Hello "+message
print(concat)
#Case Changing->upper case to lower case or lower case to upper case or camel case
print(message.upper())
print(message.lower())
print(message.title())#camel case
#Searching
print("Hello " in concat)#in is called membership operator, is is identity operator
#Replacing
new = message.replace("hai","hey")
print(new)
#Comparison-> to compare the sting
s1 = "hello"
s2 = "hai"
print(s1==s2)# it is to check only the content of two text and compares
print(s1 is s2) #is is identity operator and it will identify both the memory location and its content