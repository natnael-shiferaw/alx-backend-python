#!/usr/bin/env python3
"""A Python module for measuring the execution time
of asynchronous operations."""

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of asynchronous operations.
    This function executes the async_comprehension() function
    4 times concurrently
    using asyncio.gather(), and calculates the total execution time.
    Returns:
        The total execution time in seconds.
    """
    t_start = time.perf_counter()
    task = [async_comprehension() for i in range(4)]
    await asyncio.gather(*task)
    t_end = time.perf_counter()
    return (t_end - t_start)
