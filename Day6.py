# Day 6 - Functions + Loops

def describe_field(name, size):

    if size >= 50:
        x = "large field"
    elif size >= 20:
        x = "medium field"
    else:
        x = "small field"
    
    return (f"{name} is a {size} hactare {x}")

fields = [("F1", 63),("F2", 25),("F3", 12)]
for id,val in fields:
    y = describe_field(id, val)
    print(y)


#  Rewrite the grade program from the previous chapter using a function called computegrade 
#  that takes a score as its parameter and returns a grade as a string.
# Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
#  < 0.6     F

def computegrade(score):
    if score >= 0.9:
        return "A"       # No print - it will give None
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        return "F"

try:
    scores = float(input("Enter your score: "))
    if scores < 0.0 or scores > 1.0:
        print("Invalid grade")
    else:
        grade = computegrade(scores)
        print(f"You got a {grade} grade.")

except ValueError:
    print("Invalid Grade")






























