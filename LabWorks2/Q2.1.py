'''
Price of a house is $1M. If buyer has good credit, they need to put down by 10%
otherwise they need to put down by 20%
Print the down payment.
'''

house_price = 1000000
good_credit = True
if good_credit == True:
    down_payment = (10 / 100) * house_price
else:
    down_payment = (20 / 100) * house_price

print(f"The down payment is {down_payment}")