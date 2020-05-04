# Date: May 4th, 2020

# Objective: Write a program that checks if the integer is a power of 2.
# Rules:
# - Don't use +,- operations.
# - Use some sort of input stream to get the number. Input is not supposed to be initially stored in a variable.
# - The shortest code (in bytes) wins.
# - You can use any truthy/falsy response (for instance, true/false). You may assume that input number is greater than 0.

# Additional Reading
# - https://realpython.com/python-main-function/

from math import sqrt

def is_power2(num):
    modulus = num % 2
    if modulus > 0:
        return False
    else:
        quotient = num / 2
        distance = quotient / 2
        derivative = distance / 2
        if quotient < 2:
            answer = 2**quotient
        elif quotient == 2:
            answer = 2/derivative
        elif quotient > 2:
            answer = 2**(distance - (derivative - 1))

        print(num, quotient, distance, derivative, answer)

        if answer == num:
            return True
        else:
            return False

is_power2(2)
is_power2(4)
is_power2(16)
is_power2(32)
is_power2(64)
is_power2(20)
