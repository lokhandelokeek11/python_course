
#add list items
#1. append - add data at the end of the list
print("Adding List items - Append() ")
colors = ["violet","red", "blue"]
colors.append("reddish blue")
print(colors)
print()


#2. extend - add list to list
print("Adding list items - Extend() ")
sample_cars = ["bmw", "audi", "range rover"]
sample_colors = ["cameron green", "blue", "red"]
sample_cars.extend(sample_colors)
print (sample_cars)
print()

#3. insert - inserts the data at specific any location in the existing list
print("Adding list items - Inserting() ")
animals = ["dog", "cat", "rhino", "hippo"]
animals.insert(3, "giraffe")
print(animals)