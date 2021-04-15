'''
Solve each of the following problems using Python Scripts.
Make sure you use appropriate variable names and comments.
When there is a final answer have Python print it to the screen.
A person's body mass index (BMI) is defined as:
    BMI = mass in KG / (height in m)^2
'''


mass = int(input("Enter mass in KG:"))
height = int(input("Enter height in meter:"))
bmi = mass / (height) ** 2
print(f"A person's Body Mass Index is {bmi}")
