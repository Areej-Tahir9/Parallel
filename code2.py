# A Python program demonstrating basic concepts with user interaction

# Welcome message
print("Welcome to the Python Basics Program!")

# Input: Ask the user for their favorite number
favorite_number = int(input("Enter your favorite number: "))
print(f"Wow, {favorite_number} is a great choice!")

# Using a list to store numbers
numbers = [1, 2, 3, 4, 5]

# Append the user's favorite number to the list
numbers.append(favorite_number)
print("\nHere's a list of numbers including your favorite:")
print(numbers)

# While loop: Calculate the sum of numbers in the list
print("\nCalculating the sum of the numbers in the list...")
total = 0
i = 0
while i < len(numbers):
    total += numbers[i]
    i += 1

print(f"The total sum of the numbers is: {total}")

# Function: Check if a number is even or odd
def check_even_or_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

# Test the function with the user's favorite number
result = check_even_or_odd(favorite_number)
print(f"Your favorite number, {favorite_number}, is {result}.")

# Goodbye message
print("\nThanks for trying out Python basics. Goodbye!")
