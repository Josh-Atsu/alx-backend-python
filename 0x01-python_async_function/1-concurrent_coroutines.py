#!/usr/bin/env python3
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random
"""
execute multiple coroutines
"""


async def wait_n(n: int, max_delay: int) -> float:
    """Spawn wait_random n times
    """
    delay = []
    for _ in range(n):
        w = asyncio.create_task(wait_random(max_delay))
        delay.append(w)

    results = await asyncio.gather(*delay)
    return sorted(results)
