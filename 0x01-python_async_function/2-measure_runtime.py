#!/usr/bin/env python3
"""Contains a method that measures the total
execution time of concurrent coroutines."""

from time import perf_counter
import asyncio

# Importing wait_n from the specified module
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time of concurrent coroutines.
    Args:
        n (int): The number of coroutines to launch.
        max_delay (int): The maximum amount of time to wait for each coroutine.
    Returns:
        float: Elapsed time in seconds.
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = perf_counter() - start
    return elapsed / n
