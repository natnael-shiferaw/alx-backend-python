#!/usr/bin/env python3
"""Contains a method that spawns asyncio Tasks n times
with a specified delay between each call."""

import asyncio
from typing import List

# Importing task_wait_random from the specified module
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns asyncio Tasks n times with a specified
    delay between each call.
    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): Maximum delay between each call.
    Returns:
        List[float]: List of delays.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
