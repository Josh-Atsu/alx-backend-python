#!/usr/bin/env python3
import asyncio
import random
"""an asynchronous coroutine
"""


async def wait_random(max_delay=10):
    """
    takes in an integer argument
    waits for a random delay between 0 and max_delay seconds
    and eventually returns it.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
