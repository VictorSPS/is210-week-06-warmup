#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Concept of looping lists with a (for)loops
   with our data module
"""


def process_data(data):
    """Function takes only one argument named data and
       uses a for loop
    Arg:
        total(int): total sum of the input data.
        average(float): average of input data.
    Return:
        returns a tuple providing sum and average of
        input data.
    Examples:
        >>> process_data([1, 2, 3])
        (6, 2.0)
    """
    value = 0
    for total in data:
        value += total

    average = (value/float(len(data)))
    return value, average
