'''
Weight Converter:
    Input the weight of a person in either kg or lbs.
If the person provides his/her weight in kg then convert it into lbs else convert it to kg
'''

select = input("(kg) or in (lbs): ")
weight = int(input("Enter the weight: "))
if select == "kg":
    weight_lbs = weight * 2.20462
    print(f"Converted weight in lbs is {weight_lbs} lbs")
elif select == "lbs":
    weight_kg = weight / 2.20462
    print(f"Converted weight in kg is {weight_kg} kg")
else:
    print("Not valid selection")
