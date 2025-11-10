# Program to convert temperature from Fahrenheit to Celsius and Kelvin

# Get input from the user
fahrenheit = float(input("Enter temperature in Fahrenheit (°F): "))

# Convert to Celsius
celsius = (fahrenheit - 32) * 5 / 9

# Convert to Kelvin
kelvin = celsius + 273.15

# Display results
print(f"\nTemperature Conversions:")
print(f"{fahrenheit}°F = {celsius:.2f}°C")
print(f"{fahrenheit}°F = {kelvin:.2f} K")

