# variables
name = "Alex"
car = "BMW"
age = 23
occupation = "Digital Agronomist"
salary = 10000

print(f"A guy name {name} has a new {car} at a age {age} his occupation is {occupation} with a monthly salary {salary} Euros.")

# lists
favourate_cars = ["BMW", "Volkswagen", "Audi", "Porsche", "Mercedes Benz"]
print(favourate_cars[0:3])
print(favourate_cars[3:])

my_first_car = favourate_cars[1]
print(f"My first car is {my_first_car}")

dream_car = favourate_cars[-1]
print(f"My dream car is {dream_car}")

favourate_cars.append("Ferrari")
print(favourate_cars)

reducing = favourate_cars.pop(2)
print(reducing)


#dictionary
seeds_required = {"rice":100,"maize":150,"wheat":125,"rapeseed":200}
print(seeds_required)
print(seeds_required.keys())
print(seeds_required.values())

print(len(seeds_required))

seed_for_rice = seeds_required["rice"]
print(seed_for_rice)

seeds_required["barley"] = 50
print("A new seed is added and updated dict:",seeds_required)

del seeds_required["rapeseed"]
print(seeds_required)