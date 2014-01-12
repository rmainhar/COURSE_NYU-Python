
# Prompt the user to enter a lower boundary between 1 and 500 inclusive
while (True):
    lower_bound = int(input("Lower Boundary: enter a number between 1 and 500: "))
    if (lower_bound >=1 and lower_bound <= 500):
        break
    print("* Invalid, try again!")

# Prompt the user to enter an upper boundary between 501 and 999 inclusive
while(True):
    upper_bound = int(input("Upper Boundary: enter a number between 501 and 999: "))
    if (upper_bound >= 501 and upper_bound <= 999):
        break
    print("* Invalid, try again!")

# Prompt the user to enter a skip value between 1 and 10 inclusive
while (True):
    skip = int(input("Skip: enter a number between 1 and 10: "))
    if ( skip >= 1 and skip <= 10):
        break
    print("* Invalid, try again!")

# How many numbers per line does the user want?
number_per_line = int(input("How many numbers per line? "))

# Calculate how many numbers will be in layout
total_num = (upper_bound - lower_bound) // skip + 1
# Calculate the number of rows
rows = total_num // number_per_line
if (total_num % number_per_line != 0):
    rows += 1

# Number that is going to be printed
num = lower_bound

print("")
# For each row
for row in range(rows):
    # For each column
    for column in range(number_per_line):
        if(num <= upper_bound):
            print(format(num, ">4d"), end='')
            num += skip
    print("")

