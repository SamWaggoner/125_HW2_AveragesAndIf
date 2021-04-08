# File: hw2b.py
# Author: Sam Waggoner
# Date: 09/18/2020
# Section: 1006
# E-mail samuel.waggoner@maine.edu
# Description:
# We calculate the a weighted grade based off different categories.
# Collaboration:
# I did not collaborate with anyone.

def main():
    whw = float(input("Homework weight:", ))
    hw = float(input("Homework grade:", ))
    wproj = float(input("Project weight:", ))
    proj = float(input("Project grade:", ))
    wengage = float(input("Engagement Activities Weight:", ))
    engage = float(input("Engagement Activities Grade:", ))
    wlab = float(input("Lab weight:", ))
    lab = float(input("Lab grade:", ))
    whrxam = float(input("Hourly Exam weight:", ))
    hrxam = float(input("Hourly Exam grade:", ))
    wfxam = float(input("Final Exam weight:", ))
    fxam = float(input("Final Exam grade:", ))
    final_grade = int(whw * hw + wproj * proj + wengage * engage + wlab * lab \
        + whrxam * hrxam + wfxam * fxam)
    print("Your final grade is ",final_grade,".",sep="")
main()


