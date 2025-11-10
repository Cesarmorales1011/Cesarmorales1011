# Program to check if a number 'a' is a multiple of another number 'b'

# Ask the user for input and convert to float
a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))

# Check for division by zero
if b == 0:
    print("Error: Division by zero is not allowed.")
else:
    # Use the modulo operator to check if a is a multiple of b
    if a % b == 0:
        factor = a / b
        print(f"{a} is a multiple of {b}. The factor is {factor}.")
    else:
        print(f"{a} is NOT a multiple of {b}.")
