# Neater loops & text -- list comprehensions + string methods

crops = ["  Wheat", "BARLEY  ", " maize", "Sugar Beet ", "RAPESEED"]

clean_lower = [crop.strip().lower()  for crop in crops]  # one line code///
print(clean_lower)



fruit = "banana"

index = 0
while index < len(fruit):    # looping with while
    letter = fruit[index]
    print(letter)
    index = index + 1

indexing = len(fruit) - 1   # Reverse order
while indexing >= 0:
    print(fruit[indexing])
    indexing -= 1

for words in fruit:         # I felt this one is a bit easy 
    print(words)


#Exercise 3: Encapsulate this code in a function named count, 
# and generalize it so that it accepts the string and the letter as arguments.

def count(word,letter):
    counting = 0
    for words in word:
        if words == letter:
            counting += 1
    return counting

w1 = count("apple","p")
print(w1)

w2= count("pppears", "p")
print(w2)