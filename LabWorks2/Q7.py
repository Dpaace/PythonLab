'''
7.Given a positive real number, print its fractional part.

'''

num = float(input("Enter any positive: "))
import math
val = math.modf(num)

print(val)