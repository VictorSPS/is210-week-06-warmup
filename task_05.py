#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Mutabiity differences between strings and the tuple"""


def flip_keys(to_flip):
    """Function takes one argument, uses a for loop,
       and returns the original list with its inner elements reversed.
    Args:
        counter(int): the variable to increment the index
                      while using for loop.
        to_flip(mixed): the input immutable, nested list.
    Returns:
        the original list with its inner elements reversed
    Examples:
        >>> LIST = [(1, 2, 3), 'abc']
        >>> NEW = flip_keys(LIST)
        >>> LIST is NEW
        True
        >>> print LIST
        [(3, 2, 1), 'cba']
    """
    counter = 0
    for item in to_flip:

        to_flip[counter] = item[::-1]

        counter += 1

    return to_flip
