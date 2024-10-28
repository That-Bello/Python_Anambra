#
# Python Boot Camp Week 3
# TASK 1.
#
# Write a function to check if a number is prime.


import math


def its_prime(choose_num):
    if choose_num <= 1:
        return False
    for i in range(2, int(math.sqrt(choose_num)) + 1):
        if choose_num % i == 0:
            return False
    return True


choose_num = int(input("Enter a number: "))
if its_prime(choose_num):
    print("It's Prime!")
else:
    print("Not Prime!")
