'''
Assignment 6 Part 1
for Introduction to Computer Programming
by Kapp Craig @ NYU.
Date: Oct 27, 2013

This part aims at practicing 'defining functions'
'''

import math
# Prompt to input radius between 1 and 50
while (True):
    radius = int(input("Enter a radius (1-50): "))
    if (radius >=1) and (radius <= 50):
        break
    print("Sorry, that's not between 1 and 50.")
    
# Def: compute the area
# Input: the radius
def area(x):
    # Process: calculate the area
    circle_area = format(math.pi * x **2,".2f")
    # Output: the area
    print("The area of your circle is ", circle_area)

# Def: compute the circumference
# Input: the radius
def circumference(x):
    # Process: calculate the circumference
    circle_circum = format(2*math.pi*x, ".2f")
    # Output: the circumference
    print("The circumference of your circle is ", circle_circum)
    
area(radius)
circumference(radius)
