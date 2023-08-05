#!/usr/bin/env python3
"""
A python script tha measures the runtime
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n."""

    # Start the timer
    start_time = time.time()

    # Run the wait_n coroutine and gather the results
    asyncio.run(wait_n(n, max_delay))

    # Stop the timer and calculate the total time
    end_time = time.time()
    total_time = end_time - start_time

    # Return total execution time divided by n
    return total_time / n
