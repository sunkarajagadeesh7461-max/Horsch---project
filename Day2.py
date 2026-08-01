# Day2: practicing list operations

# creating a List 
crop_names = ["Rice","Wheat","Maize","Barley","Oats"] 

# first and last value in the list 
first_crop = crop_names[0]
last_crop = crop_names[-1]
print(f"The first crop is {first_crop}")
print(f"The last crop is {last_crop}")

# adding a new crop
crop_names.append("Sorghum")
print(f"The new crop list: {crop_names}")

# removing a crop and final crop list 
removing_crop = crop_names.pop(2)
updated_crop_list = crop_names
print(f"Removed crop is {removing_crop}")
print(f"The final crop list: {updated_crop_list}")
 