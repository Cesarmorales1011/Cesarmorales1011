# Program to convert hours to minutes and seconds

# Get input from the user
hours = float(input("Enter the number of hours: "))

# Conversion calculations
minutes = hours * 60
seconds = hours * 3600

# Display the results
print(f"{hours} hour(s) is equivalent to:")
print(f"{minutes} minute(s)")
print(f"{seconds} second(s)")
