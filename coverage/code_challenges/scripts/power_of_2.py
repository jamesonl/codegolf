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

def recurse_power(res):
    quotient = res[0] / 2
    distance = quotient / 2
    derivative = distance / 2
    return [quotient, distance, derivative]

def is_power2(num):
    modulus = num % 2
    counter = 1
    if modulus == 0:
        quotient = num / 2
        distance = quotient / 2
        derivative = distance / 2

        res = [quotient, distance, derivative]

        while res != [2, 1, 0]:
            if res == [0, 0, 0]:
                break
            else:
                res = recurse_power(res)
                counter += 1

        if res == [0, 0, 0]:
            return False
        elif res == [2, 1, 0]:
            comp = [num, counter, quotient, distance, derivative]
            # answer = (2**(comp[1] * 2 - abs(comp[4] - counter)))
            answer = True if 2**(comp[1]+1) == num else False
            return answer
        else:
            return False
    else:
        return False



check_4 = is_power2(4)
check_3 = is_power2(3)

print(check_3, check_4)
