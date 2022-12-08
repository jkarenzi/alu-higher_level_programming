#!/usr/bin/python3
"""adding two integers"""


def add_integer(x=0, y=98):
    """ a function that adds integers """
    if type(x) is not int and type(x) is not float:
        raise TypeError("x must be an integer")
    if type(y) is not int and type(y) is not float:
        raise TypeError("y must be an integer")

    if type(x) is float:
        x = int(x)
    if type(y) is float:
        y = int(y)
    return x + y
