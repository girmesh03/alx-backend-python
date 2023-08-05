#!/usr/bin/env python3
"""A module that returns a asyncio.Task."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Regular function to create an asyncio.Task from wait_random."""
    return asyncio.create_task(wait_random(max_delay))
