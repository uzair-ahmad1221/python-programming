# Ask the user to enter their mark
mark = float(input("Enter your mark: "))

# Determine the grade
if mark >= 90:
    grade = "A"
elif mark >= 80:
    grade = "B"
elif mark >= 70:
    grade = "C"
elif mark >= 60:
    grade = "D"
else:
    grade = "Fail"

# Display the result
print(f"With a mark of {mark}, your grade is: {grade}")