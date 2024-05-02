#!/usr/bin/env python3
"""Module containing a function for creating a multiplier function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Creates a function that multiplies a float by a specified multiplier.
    Args:
        multiplier (float): The multiplier to use in the created function.
    Returns:
        Callable[[float], float]: A function that multiplies a float
                                 by the specified multiplier.
    """

    def multiplier_func(number: float) -> float:
        """Multiplies a float by the specified multiplier"""
        return multiplier * number

    return multiplier_func
