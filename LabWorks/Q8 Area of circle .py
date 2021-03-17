'''
Write a Python program which accepts the radius of a circle from the user and compute the area.
Area of circle = PI * r ^ 2
'''

radius = int(input("Enter the radius of the circle:"))
pi = 22 / 7
area = pi * (radius ** 2)
print(f"The area of the circle is {area}")

