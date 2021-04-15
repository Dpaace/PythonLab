'''
5.For given integer x, print ‘True’ if it is positive, print ‘False’
if it is negative and print ‘zero’ if it is 0.

'''
x = int(input("Enter any number: "))
if x > 0:
    value = True
elif x < 0:
    value = False
elif x == 0:
    value = "zero"

print(value)