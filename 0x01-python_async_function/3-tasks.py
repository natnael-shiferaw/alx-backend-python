#!/usr/bin/env python3
"""Contains a method that creates and returns an asyncio task."""

import asyncio

# Importing wait_random from the specified module
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio task that waits for
    a random number of seconds.
    Args:
        max_delay (int): The maximum number of seconds
        that the task will wait.
    Returns:
        asyncio.Task: An asyncio Task object.
    """
    return asyncio.create_task(wait_random(max_delay))
