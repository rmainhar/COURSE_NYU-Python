'''
Assignment 9

Part2: Sales for this week

'''

day_num = 7

# Create a list for weekly sales
daily_sales = [0] * day_num

# Ask the user to enter valid sales for this week
for x in range (day_num):

    flag = True
    # continuous input
    # Sales for day 1: ; Sales for day 2: ; ...
    print("Sales for day", (x+1),end = '')
    sales = input(": ")

    # Make sure input is a number and
    # is greater than 0
    while (flag):
        if sales.isdigit() and int(sales)>0:
            daily_sales[x] = int(sales)
            flag = False
        else:
            print()
            print("Sorry, that is not a valid number. Please try again.")
            print()
            print("Sales for day", (x+1),end = '')
            sales = input(": ")


# print the total sales for this week
sum_sales = sum(daily_sales)
print(format("Total sales","18s"),":",float(sum_sales))

# print the average daily sales for this week
print(format("Total sales","18s"),":",format(sum_sales/day_num, ".2f"))

# print the highest sales in this week
print(format("Highest sales day","18s"),":",format(max(daily_sales), ".1f"))

# print the lowest sales in this week
print(format("Lowest sales day","18s"),":",format(min(daily_sales), ".1f"))


