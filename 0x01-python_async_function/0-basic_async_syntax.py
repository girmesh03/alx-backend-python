#!/usr/bin/env python3
"""
A asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random
that waits for a random delay between 0 and max_delay
(included and float value) seconds and eventually returns it.

"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that takes in an integer argument
    and waits for a random delay between 0 and max_delay
    before returning it."""

    # define how long to wait
    wait = random.random() * max_delay
    # sleep for that amount of time
    await asyncio.sleep(wait)
    # return the amount of time waited
    return wait
