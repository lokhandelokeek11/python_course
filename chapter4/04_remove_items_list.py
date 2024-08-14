#1. removing list items (pop) - removes last element of the list
print("Removing list items - Pop() ")
car_companies = ["mahindra", "tata", "suzuki"]
car_companies.pop()
print(car_companies)

#2. removing list items (remove) - removes any item from the list
print("Removing list items - remove() ")
students = ["aditya", "swayam", "kaustubh", "lokeek"]
students.remove("aditya")
print(students)

#3. removing list items (del) - removes any list item from specific location
print("Removing list items - del()")
apps = ["insta", "facebook", "google", "twitter"]
del apps[0]
print(apps)

#4. removing list items(clear)- clears all the list items
things = ["pen", "book", "eraser"]
things.clear()
print(things)

#5. change list items (add) 
name = ["Sakshi", "Rohini","Rishi", "Rohan","ayush","harshal"]
name[2:5] = ["Zeeshan","Khush"]
print(name)