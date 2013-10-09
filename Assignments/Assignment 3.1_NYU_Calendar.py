'''
This is Assignment 3 for Introduction to Computer Programming
by Craig Kapp @ NYU 

Sep 28
'''
'''
NYU Academic Calendar For Fall 2013

This program will tell the user whether he/she
has the date off for a specific day during the
semester of Fall 2013.

Semester begins: Sep 3
Semester ends  : Dec 14
Fall break     : Oct 14 - Oct 15
Thanksgiving   : Nov 28 - Dec 1

Firstly, this program tests whether the user entered a valid date, e.g., September 31 would not be a valid date.
Secondly, this program tests if the date is within semester of Fall 2013.
Then, it will tests if the date is a holiday day. 
Weekends will not be considered as holiday days.
'''

# Prompt the user to enter the month, using the number to stand for month
mon = int(input("Please enter the month in number format, e.g. 10 for October: "))
day = int(input("Please enter the day: "))

# If the month is 9, test the date is before semester or not a valid date.
if mon==9:
    if day<4:
        print("September",day,'is before the Fall 2013 term.')
    elif day>30:
        print("Sorry, it is not a valid date.")
    else:
        print('September',day,'is not a school holiday at NYU.')
        
# If the month is 10, test whether the date is a holiday day or not a valid date
if mon==10:
    if day>31:
        print('Sorry, it is not a valid date.')
    elif day==14 or day ==15:
        print("October",day,"is Fall Break. This is a school holiday at NYU.")
    else:
        print('October',day,'is not a school holiday at NYU.')

# If the month is 11, test whether the date is Thanksgiving or not a valid date
if mon ==11:
    if day>30:
        print("This is not a valid date.")
    elif day>=28 and day<=30:
            print("November",day,'is Thanksgiving. This is a school holiday at NYU.')
    else:
        print("November",day,"is not a school holiday at NYU.")

# If the month is 12, test whether the date is Thanksgiving or after the semester or not a valid date
if mon == 12:
    if day == 1:
          print("December 1 is Thanksgiving Recession. This is a school holiday at NYU.")
    elif day>31:
          print("Sorry, it is not a valid date.")
    elif day<31 and day>14:
          print("December",day,"is after the Fall 2013 term.")
    else:
          print("December",day,"is not a school holiday at NYU.")

