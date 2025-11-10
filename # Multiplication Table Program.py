# Multiplication Table Program

# Ask the user for a number
num = int(input("Enter a number: "))

print(f"\nMultiplication Table for {num}:\n")

# Loop through numbers 1 to 10
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
