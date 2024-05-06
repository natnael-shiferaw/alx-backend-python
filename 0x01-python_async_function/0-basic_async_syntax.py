#!/usr/bin/env python3
"""Module containing a coroutine that introduces
a random delay and returns it."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Return a random float between 0 and max_delay after a delay.
    Args:
        max_delay (int): The maximum delay to return.
    Returns:
        float: A random float between 0 and max_delay.
    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
