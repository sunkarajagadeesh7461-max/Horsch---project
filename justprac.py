
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
    print("Enter at least one number!!")
else:
    average = total / count
    print("Total:", total, "Count:", count, "Average:", average)