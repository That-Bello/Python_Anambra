#
# Python Boot Camp Week 3
# TASK 3.
#
# Write a function that takes a list of numbers and returns the largest number.


def largst_num(num_list):
    bigst_num = num_list[0]

    for nulist in num_list:
        if nulist > bigst_num:
            bigst_num = nulist

    return bigst_num


print(largst_num([23, 54, 6, 56, 76, 21, 333, 73, 90, 109]))
