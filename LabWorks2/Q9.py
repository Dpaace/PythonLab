'''
9.Check whether the given year is leap year or not. If year is leap print ‘LEAP YEAR’ else print ‘COMMON YEAR’.
Hint: •a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100•
a year is always a leap year if its number is exactly divisible by 400

'''

year_days = int(input("Enter the number of days: "))
if year_days == 365:
    print("COMMON YEAR")
elif year_days == 366:
    print("LEAP YEAR")