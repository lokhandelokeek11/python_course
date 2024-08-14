# 1. sorting list (ascending order)

eg_color = ["violet", "red", "yellow"]
eg_color.sort()
print(eg_color)

num = [1,89,77,54,6,19]
num.sort()
print(num)

# sorting list (descending order)
number = [56,78,99,14,67]
number.sort(reverse=True)
print(number)

# 2. reverse (this method reverses the order)

divison = ["a", "c", "h", "j"]
divison.reverse()
print(divison)

# 3. index (this method tells you the index of the string or num)

smartphone_brands = ["samsung", "apple", "xiomi", "micromax", "motorola"]
print(smartphone_brands.index("motorola"))

# List Method - count (this method gives us the count of the no of items in the list)
colorr = ["blue", "white", "green","blue","violet"]
print(colorr.count("blue"))

num_ber = [5,6,7,3,7,9,7,0,5,7]
print(colorr.count(7))

# List Method - copy (this method copies the list)
names = ["lokeek","rishi","santosh","kamlesh"]
newlist = names.copy()
print(names)
print(newlist)