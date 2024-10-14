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
    wait_random = random.uniform(0, max_delay)
    await asyncio.sleep(wait_random)
    return wait_random

if __name__ == "__mian__":
    asyncio.run(wait_random())
