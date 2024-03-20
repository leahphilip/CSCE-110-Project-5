# File: q2.py
# Author: Leah Philip
# Date: 03/20/2024
# Section: 505
# Email: leahephilip@tamu.edu
# Description: This program takes two numbers as input from the user, and outputs whether the numbers are prime numbers or not with some additional conditions.

start, end = map(int, input("Enter the start and end values: ").split())


def isValid(num):
    return isinstance(num, int) and num > 0


def isPrime(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):

        if num % i == 0:
            return False

    return True


def printPrimes(start, end):
    prime_numbers = []

    for num in range(start, end + 1):

        if isPrime(num):
            prime_numbers.append(num)

    if len(prime_numbers) == 0:

        print("No prime number found in the given range.")

    else:

        print(*prime_numbers)
        print("Total prime numbers:", len(prime_numbers))


try:

    if not isValid(start) or not isValid(end):

        print("The input is invalid")

    else:

        if isPrime(start):

            print(start, "is a prime number")

        else:

            print(start, "is not a prime number")

        if isPrime(end):

            print(end, "is a prime number")

        else:

            print(end, "is not a prime number")

        printPrimes(start, end)

except ValueError:

    print("The input is invalid")
