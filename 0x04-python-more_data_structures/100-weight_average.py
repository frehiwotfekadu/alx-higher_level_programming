#!/usr/bin/python3
# 100-weight_average.py


def weight_average(my_list=[]):
    """Returns the weighted average of all integers tuple."""
    if len(my_list) == 0:
        return 0
    return sum([x*y for (x, y) in my_list]) / sum([y for (x, y) in my_list])
