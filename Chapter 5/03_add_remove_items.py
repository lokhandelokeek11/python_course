# create a new key and assign a value to it 

student_info = {'name':'rahul','prn_no':'123B1U190','division':'k'}
print(student_info)
student_info['DOB'] = 2005
print(student_info)

# use update() method

student_info = {'name':'rahul','prn_no':'123B1U190','division':'k'}
student_info.update({'name':'kshitij'})
print(student_info)

# removing items
#1. clear() method

student_info = {'name':'rahul','prn_no':'123B1U190','division':'k'}
student_info.clear()
print(student_info)

#2. pop()