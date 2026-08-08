# Loops 

crop_list = ["Rice", "Maize", "Wheat", "Sorghum", "Barley"]

for i in range(len(crop_list)):
    # print(i, crop_list[i]) # computer counting  
    print(f"{i+1} {crop_list[i]}") # By using simple math in the f string we can get the normal human count 


# Intersting Exercises on loops:

# Exercise 1: 
# Repeatedly read integers until user enters "done".
# Print total, count, and average.
# Use try/except to catch invalid (non-integer) input, print error, and continue.

total = 0
count = 0 

while True:
    num = input("Please enter the number: ")

    if num == "done":
        break

    try:
        val = float(num)
    except ValueError:
        print("Enter a valid number !!")
        continue

    total = total + val
    count = count + 1
    
if count == 0:
    print("Enter atleast one number")
else:
    average = total/count
    print("Total:", total, "Count:", count, "Average:", average)


#Exercise 2:Same as above, but print max and min instead of average.

# Write a program that prompts for a list of numbers as above (reading
# integers repeatedly until the user enters "done", using try/except to
# catch invalid input) and at the end prints out both the maximum and
# minimum of the numbers instead of the average.

minimum = None    # we choose none instead of '0', None ha no value and '0' has a value
maximum = None 

while True:
    number = input("Enter a number: ")

    if number == "enough":
        break        # stop's when the user type this key

    try:
        value = float(number)
    except ValueError:
        print("Enter a valid number !!")
        continue        # skip the bad input and again go back to the top, ask the input

    if maximum is None or maximum < value:
        maximum = value

    if minimum is None or minimum > value:
        minimum = value

print("Maximium:", maximum, "Minimum:", minimum)
