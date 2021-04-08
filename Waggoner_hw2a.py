# File: hw2a.py
# Author: Sam Waggoner
# Date: 09/18/2020
# Section: 1006
# E-mail samuel.waggoner@maine.edu
# Description:
# We calculate the average number of attendees for COS125 labs, then issue a
# warning if they are in-person and could be over capacity.
# Collaboration:
# I looked up how to round down numbers and found the math.floor function
# online, other than that I did not collaborate with anyone.y
import math
def main():
    print("""Hello, I'm here to calculate the average attendance for the first
    four COS125 lab meetings.""")
    labzero = float(input("Number of attendees at Lab 0: ", ))
    labone = float(input("Number of attendees at Lab 1: ", ))
    labtwo = float(input("Number of attendees at Lab 2: ", ))
    labthree = float(input("Number of attendees at Lab 3: ", ))
    average = math.floor((labzero + labone + labtwo + labthree) / 4)
    print("There were an average of ",average,"people in the first four labs.")
    if labzero > 28 or labone > 28 or labtwo > 28 or labthree > 28 :
        yn = input("Is this lab remote? (Type Y or N.): ", )
        if yn != "y" and yn != "Y" and yn != "yes" and yn != "Yes" and yn != "YES" :
            print("Please be mindful of room capacity due to COVID-19.")
main()
# I was testing my code using the second example, and when rounding down to the
# nearest integer, I believe the numbers should yield 23, not 24.