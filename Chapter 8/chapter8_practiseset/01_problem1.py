def greatest(a,b,c):
     if(a>b and a>c):
         return a
     if(b>c and b>a):
         return b
     if(c>b and c>a):
         return c
     
a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
c = int(input("Enter the 3rd number: "))

print(f"The greatest number of all three is: {greatest(a,b,c)}")