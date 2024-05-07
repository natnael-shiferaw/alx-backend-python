#!/usr/bin/env python3
""" Module for generating asynchronous random numbers."""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Generates random floating-point numbers asynchronously.
    This function loops 10 times, waiting for 1 second between each iteration
    and yields a random floating-point number between 0 and 10.
    Returns:
        A generator yielding random floating-point numbers.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
