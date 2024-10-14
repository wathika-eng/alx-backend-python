#!/usr/bin/env python3

"""
basics of asyncio
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    waits for a random delay between 0 and max_delay
    """
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
