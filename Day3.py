# Dictionary 

#creating a dictionary, crop and typical weed 
crop_mapping = {"Rice":"Wild rice", 
                "Wheat":"Blackgrass", 
                "Maize":"Barnyard grass", 
                "Soyabean":"Amaranthus", 
                "Sugar beet":"Chenopodium album"}


#checking the dict keys and values 
print(crop_mapping)
print(crop_mapping.keys())
print(crop_mapping.values())

#looking up the crop common weeds
crop1 = crop_mapping["Rice"]
crop2 = crop_mapping["Sugar beet"]
print(f"The common weed of Rice: {crop1}")
print(f"The common weed of Sugar beet: {crop2}")

#length of the dictionary 
print(len(crop_mapping))

#iterating using for loop
for keys in crop_mapping:
    print(keys) # print the keys one by one 

for values in crop_mapping:
    x = (crop_mapping[values])
    print(x) # print the values one by one 

#adding a new crop 
crop_mapping["Rapeseed"] = "Cleavers"
print(crop_mapping)

#deleting 
del crop_mapping["Rice"]
print(crop_mapping)

