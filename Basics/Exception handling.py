def division(num1,num2):
    try:
        if num2==0:
            raise ZeroDivisionError("division by zero is not possible")

        return num1/num2
    except ZeroDivisionError as err:
        print("Exception is caught",err)
    finally:
        print("division is performing")
print(division(1,0))
print(division(20,2))
