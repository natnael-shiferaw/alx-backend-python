#!/usr/bin/env python3
"""
Module containing a function that takes a mixed list of integers and
floats and returns the sum of all the numbers in the list as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Takes a mixed list of integers and floats and returns the
    sum of all the numbers in the list as a float.
    Args:
        mxd_lst (List[Union[int, float]]): A mixed list of integers and floats.
    Returns:
        float: The sum of all the numbers in the list as a float.
    """
    return sum(mxd_lst)
