#!/usr/bin/env python3
"""Module containing a function for summing a list of floats."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums a list of floats.
    Args:
        input_list (List[float]): A list of floats to be summed.
    Returns:
        float: The sum of the floats in the list.
    """
    if input_list is None:
        return 0
    else:
        return sum(input_list)
