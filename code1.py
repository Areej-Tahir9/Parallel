# A basic Python program demonstrating fundamental concepts

# Input: Ask the user for their name
name = input("Enter your name: ")

# Output: Greet the user
print(f"Hello, {name}! Welcome to Python programming.")

# Variables and basic arithmetic
a = 10
b = 5
print(f"\nLet's do some basic math with a = {a} and b = {b}:")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")

# Conditional statement
if a > b:
    print("\na is greater than b")
else:
    print("\nb is greater than or equal to a")

# Loop: Print numbers from 1 to 5
print("\nHere are numbers from 1 to 5:")
for i in range(1, 6):
    print(i)

# Function: Define and call a function
def say_goodbye():
    print("\nGoodbye! Have a great day!")

# Call the function
say_goodbye()
