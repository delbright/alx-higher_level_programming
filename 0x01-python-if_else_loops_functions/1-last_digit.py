#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    a = number % 10
else:
    a = ((number * -1) % 10) * -1
add_string = "and is less than 6 and not 0"
if a > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, a))
elif a == 0:
    print("Last digit of {} is {} and is 0".format(number, a))
elif a < 6 and a != 0:
    print("Last digit of {} is {} {}".format(number, a, add_string))
