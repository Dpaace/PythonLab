'''
Write a python program to find sum of the first n positive integers.
    sum = ( n * ( n + 1)) / 2
'''

'''
n = int(input("Enter any number upto which you want to find the sum:"))
sum = int(( n * ( n + 1)) / 2)
print(f"The sum of the given positive integers is {sum}")
'''

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = sum(list)
print(f"The sum of the integers is {total}")
