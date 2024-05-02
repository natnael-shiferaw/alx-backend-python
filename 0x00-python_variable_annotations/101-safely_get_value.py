#!/usr/bin/env python3
"""Module containing a method for safely retrieving
values from a dictionary."""
from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """Safely retrieves value from a dictionary.
    Args:
        dct (Mapping): The dictionary to retrieve value from.
        key (Any): The key to retrieve value for.
        default (Optional[T], optional): The default value to return if key
                                        is not found. Defaults to None.
    Returns:
        Union[Any, T]: The value from the dictionary, or the default value
                       if key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
