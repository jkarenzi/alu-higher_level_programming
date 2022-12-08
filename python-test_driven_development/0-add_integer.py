#!/usr/bin/python3
"""adding two integers"""

def add_integer(x, y=98):
    if type(x) != int:
        raise TypeError("a must be an integer")
    if type(y) != int:
        raise TypeError("b must be an integer")
    if type(x) == float or type(y) == float:
        x = int(x)
        y = int(y)
    return x + y
