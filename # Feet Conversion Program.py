# Feet Conversion Program

def convert_from_feet(feet):
    # Conversion factors
    yards = feet / 3
    miles = feet / 5280
    inches = feet * 12
    leagues = feet / 15840  # 1 league = 3 miles = 15840 feet
    meters = feet * 0.3048

    # Return results as a dictionary
    return {
        "yards": yards,
        "miles": miles,
        "inches": inches,
        "leagues": leagues,
        "meters": meters
    }

# Main program
def main():
    print("Feet Conversion Program")
    feet = float(input("Enter the length in feet: "))

    conversions = convert_from_feet(feet)

    print(f"\nConversions for {feet} feet:")
    print(f"Yards: {conversions['yards']:.4f}")
    print(f"Miles: {conversions['miles']:.6f}")
    print(f"Inches: {conversions['inches']:.2f}")
    print(f"Leagues: {conversions['leagues']:.6f}")
    print(f"Meters: {conversions['meters']:.4f}")

if __name__ == "__main__":
    main()
