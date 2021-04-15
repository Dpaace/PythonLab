'''
If name is less than 3 characters long -
name must be at least 3 characters otherwise if it's more the 50 characters -
name must be of maximum 50 characters -
otherwise name looks good!
'''

name = input("Enter the name: ")
name_length = len(name)
if name_length < 3:
    print("Your name is very short")
elif name_length > 50:
    print("Your name is very long")
else:
    print("Your name looks good")