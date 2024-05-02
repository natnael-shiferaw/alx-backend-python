#!/usr/bin/env python3
"""Module containing a function with annotated parameters and return
values with appropriate types."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]
                   ) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples with the length of each element.
    Args:
        lst (Iterable[Sequence]): An iterable containing sequences.
    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple
                                    contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
