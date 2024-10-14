#!/usr/bin/env python3

"""
Multiple coroutines running concurrently
"""

import asyncio
import random

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """
    waits for a random delay between 0 and max_delay
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
