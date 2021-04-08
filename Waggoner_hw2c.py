# File: hw2c.py
# Author: Sam Waggoner
# Date: 09/19/2020
# Section: 1006
# E-mail samuel.waggoner@maine.edu
# Description:
# This made recommendations about bottle recycling based off inputs, and also
# reminded the user to vote!
# Collaboration:
# I did not collaborate with anyone.

print("You've come to the right place for some recycling tips!")
used = int(input("How many disposable cans or bottles did you use today? ", ))
if used == 0 :
    print("Great, you didn't use any bottles or cans!")
if used != 0 :
    recycled = int(input("Of that number, how many did you recycle? ", ))
    if used > recycled :
        print("""Help the earth! You should try to recycle all the recyclable bottles
    that you use!""")
    if used < recycled :
        print("Did you recycle someone else's cans or bottles? Thanks!")
    if used == recycled :
        print("Great job! Thanks for recycling.")
    if used > 4 :
        print("You could also try using a reusable bottle--you will need fewer bottles!")
print("Remember to vote on November 3rd or earlier by mail!")
