#!/usr/bin/python3
# 0-add_integer.py

# Made By ME

"""Defines intg addit funct"""


def add_integer(a, b=98):
    """Return the intg"""
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
