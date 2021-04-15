'''
8.Given a three-digit number. Find the sum of its digits.

'''

num = int(input("Enter any number: "))
num_duplicate = num
len = 0
while num > 0:
    len = len + 1
    num = num // 10


if len == 3:
    sum = 0
    digit = 0
    while len > 0:
        digit = num_duplicate % 10
        sum = sum + digit
        num_duplicate = num_duplicate // 10
        digit = 0
        len = len - 1
    print(sum)
else:
    print("Only for 3 digit")
