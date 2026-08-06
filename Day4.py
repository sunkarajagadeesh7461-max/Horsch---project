field_coverage_percentage = input("Enter the how much percentage of field is covered: ")

try:
    val = float(field_coverage_percentage)
except ValueError:
    print("Enter a valid number")
    exit()

if val < 0:
    print("Enter a positive number")
elif val <= 40:
    print("The coverage is low")
elif val >= 40 and val <= 70:
    print("The coverage is medium")
else:
    print("The coverage is High")
