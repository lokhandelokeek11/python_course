marks1 = (int(input("Enter your DSA marks: ")))
marks2 = (int(input("Enter your MA marks: ")))
marks3 = (int(input("Enter your Kotlin marks: ")))

percentage = (100*(marks1 + marks2 + marks3))/300

if (percentage>=40 and marks1>=33 and marks2 >= 33 and marks3 >= 33):
    print("You are passed....", percentage)
    
else:
    print("You are failed",percentage)