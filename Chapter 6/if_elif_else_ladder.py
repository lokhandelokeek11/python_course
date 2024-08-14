age = int(input("Enter your age: "))

if(age>=18):
    print("You can drive a car..")
elif(age==0):
    print("Please enter valid age..")
elif(age<0):
    print("Negative age not allowed...")
else:
    print("You are below the age to drive a car")