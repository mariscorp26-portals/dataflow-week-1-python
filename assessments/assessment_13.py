# Assessment 13 - Python Exceptions

# An exception is an error that happens while a program is running.

try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    result = number1 / number2

    print("Result:", result)

except ZeroDivisionError:
    print("You cannot divide by zero.")