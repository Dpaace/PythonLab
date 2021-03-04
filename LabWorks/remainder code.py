'''
N students take k apples and distribute them among each other evenly.
The remaining (the undivisible) part remains in the basket.
How many apples will each student get?
How many apples will remain in the basket?
The programmers reads the numbers N and K.
It should print the two answers for the questions above.
'''

apple_value = int(input("Enter number of apples:"))
student_number = int(input("Enter the number of students:"))
divid = apple_value//student_number
remain = apple_value%student_number
print("each student=",divid)
print("remain=",remain)
#Command Test