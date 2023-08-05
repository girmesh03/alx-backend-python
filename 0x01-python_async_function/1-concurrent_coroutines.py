#!/usr/bin/env python3
"""
Execute multiple coroutines at the same time with async.
"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Async routine that spawns wait_random n times
    with the specified max_delay."""

    # create a list of delays
    delays = [wait_random(max_delay) for i in range(n)]

    # create a list of the order in which the delays were completed
    completed_delays = [await delay for delay in asyncio.as_completed(delays)]

    # return the list of completed delays
    return completed_delays
