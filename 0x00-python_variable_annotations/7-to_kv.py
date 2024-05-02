#!/usr/bin/env python3
"""Module containing a function for converting a Python variable
to a key-value pair."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts a Python variable to a key-value pair.
    Args:
        k (str): The key for the key-value pair.
        v (Union[int, float]): The value for the key-value pair.
    Returns:
        Tuple[str, float]: The key-value pair.
    """
    return k, v ** 2
