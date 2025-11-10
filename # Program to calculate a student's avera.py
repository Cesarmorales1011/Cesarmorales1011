# Program to calculate a student's average and determine if they are approved

# Input: exam scores
A = float(input("Enter the score for Exam A: "))
B = float(input("Enter the score for Exam B: "))
C = float(input("Enter the score for Exam C: "))

# Calculate the average
average = (A + B + C) / 3

# Display the average
print(f"\nAverage score: {average:.2f}")

# Determine approval status
if average >= 7.0:
    print("Status: Approved ✅")
else:
    print("Status: Not Approved ❌")

