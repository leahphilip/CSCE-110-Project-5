# File: q3.py
# Author: Leah Philip
# Date: 03/20/2024
# Section: 505
# Email: leahephilip@tamu.edu
# Description: This program takes two integers as input from the user and finds the permutation of them with some additional conditions as well.

n = int(input("n: "))
k = int(input("k: "))

def isValid(n, k):

    return n >= k >= 0

def getFactorial(num):

    if num == 0:

        return 1

    factorial = 1

    for i in range(1, num + 1):

        factorial *= i

    return factorial

def getPermutation(n, k):

    return getFactorial(n) // getFactorial(n - k)

try:

    if not isValid(n, k):

        print("Invalid input")

    else:

        print("n! =", getFactorial(n))
        print("k! =", getFactorial(k))
        print("The value of P({}, {}) is {}".format(n, k, getPermutation(n, k)))

except ValueError:

    print("Invalid input")
