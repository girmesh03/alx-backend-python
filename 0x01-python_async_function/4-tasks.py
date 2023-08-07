#!/usr/bin/env python3
"""
Takes the code from wait_n and alter it into a new
function ask_wait_n. The code is nearly identical
to wait_n except task_wait_random is being called.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Takes in 2 int arguments (n and max_delay, respectively).
    Returns a list of all the delays (float values)."""

    # Create an empty list to store the results
    delays = []

    # Create a list of tasks
    tasks = [task_wait_random(max_delay) for i in range(n)]

    # Iterate over the tasks as they are completed
    for task in asyncio.as_completed(tasks):
        # Await the task and store the result
        result = await task
        # Append the result to the list of results
        delays.append(result)
    # Return the list of results
    return delays
