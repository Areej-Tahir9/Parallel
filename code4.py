# Basic Python Calculator

print("Welcome to the Basic Calculator!")

# Input: Ask the user for two numbers and an operation
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Choose an operation: +, -, *, /")
operation = input("Enter your choice: ")

# Perform the calculation based on the operation
if operation == "+":
    result = num1 + num2
    print(f"The result of {num1} + {num2} is {result}")
elif operation == "-":
    result = num1 - num2
    print(f"The result of {num1} - {num2} is {result}")
elif operation == "*":
    result = num1 * num2
    print(f"The result of {num1} * {num2} is {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is {result}")
    else:
        print("Division by zero is not allowed!")
else:
    print("Invalid operation. Please try again.")

print("Thank you for using the calculator!")
