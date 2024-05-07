#!/usr/bin/env python3
"""Module for asynchronously generating random numbers."""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Generates 10 random floating-point numbers asynchronously
    using async comprehension.
    This function utilizes async comprehension to generate 10
    random floating-point numbers
    by iterating over the async generator function `async_generator()`.
    Returns:
        A list containing 10 random floating-point numbers.
    """
    rslt = [i async for i in async_generator()]
    return rslt
