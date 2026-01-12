try:
    print(10 / 0)
    print("Done")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
finally:
    print("Program execution completed")