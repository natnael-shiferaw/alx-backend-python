#!/usr/bin/env python3
"""
Module containing a function that returns a list of integers
multiplied by a certain factor.
"""
from typing import Tuple, List


def zoom_array(lst: Tuple[int], factor: int = 2) -> List[int]:
    """Returns a list of integers multiplied by a certain factor.    
    Args:
        lst (Tuple[int]): A tuple of integers.
        factor (int, optional): An integer representing the multiplication
                                factor. Defaults to 2.
    Returns:
        List[int]: A list of integers.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in

array: Tuple[int] = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
