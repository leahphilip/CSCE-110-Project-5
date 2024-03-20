#File: q1.py
 #Author: Leah Philip
 #Date: 03/20/2023
 #Section: 506
 #E-mail: leahephilip@tamu.edu
 #Description: e.g. This program that has a function BuzzSaw() that takes a positive integer n as the input and performs the following operations for every number in range [1,n]
n = int(input("Enter a number: "))

for i in range(1, n):
    if i % 3 == 0 and i % 5 == 0:
        print("BUZZSAW")
    elif i % 3 == 0:
        print("BUZZ")
    elif i % 5 == 0:
        print("SAW")
    else:
        print(i)
