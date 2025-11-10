# Simple Calculator

# Get the first number
num1 = float(input("Enter the first number: "))

# Get the operation
operation = input("Enter an operation (+, -, *, /): ")

# Get the second number
num2 = float(input("Enter the second number: "))

# Perform the calculation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero!"
else:
    result = "Error: Invalid operation!"

# Display the result
print("Result:", result)

