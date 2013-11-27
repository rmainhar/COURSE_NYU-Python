'''
Assignment 9

Part II: Sales for this week

'''

import math

# Create a daily_sales list with zeros
daily_sales = [0] * 7
index = 0

#Input   : User's input (String)
#Process : if it is a valid input, return "True"
#          otherwise, print the reason and return "False"
#Output  : True or False (boolean)
def isSales(num):
    if num.isdigit() and int(num) > 0:
        return True
    else:
        # print the reason
        print("\nSorry, that is not a valid number. Please try again. ","\n")
        return False


        
# Test sales for day 1
flag = True
while( flag ):
    sales1 = input("Sales for day 1: ")
    if isSales(sales1):
        daily_sales[0] = int(sales1)
        flag = False
    

# Test sales for day 2
flag = True
while( flag ):
    sales2 = input("Sales for day 2: ")
    if isSales(sales2):
        daily_sales[1] = int(sales2)
        flag = False

# Test sales for day 3
flag = True
while( flag ):
    sales3 = input("Sales for day 3: ")
    if isSales(sales3):
        daily_sales[2] = int(sales3)
        flag = False

# Test sales for day 4
flag = True
while( flag ):
    sales4 = input("Sales for day 4: ")
    if isSales(sales4):
        daily_sales[3] = int(sales4)
        flag = False

# Test sales for day 5
flag = True
while( flag ):
    sales5 = input("Sales for day 5: ")
    if isSales(sales5):
        daily_sales[4] = int(sales5)
        flag = False

# Test sales for day 6
flag = True
while( flag ):
    sales6 = input("Sales for day 6: ")
    if isSales(sales6):
        daily_sales[5] = int(sales6)
        flag = False

# Test sales for day 7
flag = True
while( flag ):
    sales7 = input("Sales for day 7: ")
    if isSales(sales7):
        daily_sales[6] = int(sales7)
        flag = False

# 1. Calculate the sum of this week's sales
sales_sum = 0
for n in range(0,7):
    sales_sum += daily_sales[n]
print("Total sales: ", float(sales_sum))

# 2. Calculate the average sales of this week
sales_ave = float(sales_sum/7)
print("Average sales per day: ", format(sales_ave, ".2f"))

# 3. Highest sales in this week
highest = float(max(daily_sales))
highest = format(highest, ".2f")
print("Highest sales: ", highest)

# 4. Lowest sales in this week
lowest = float(min(daily_sales))
print("Lowest sales: ", lowest)
