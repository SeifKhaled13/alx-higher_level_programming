#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number in range(-11, 0):
    print(str(number) + " is negative")
elif number == 0:
    print(str(number) + " is zero")
elif number in range(0, 11):
    print(str(number) + " is positive")
