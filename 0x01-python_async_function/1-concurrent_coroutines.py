#!/usr/bin/env python3
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
"""
execute multiple coroutines at the same time with async
"""


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Import wait_random from the previous python file
    write an async routine called wait_n; take in 2 int arguments
    (in this order): n and max_delay
    Spawn wait_random n times with the specified max_delay
    return the list of all the delays (float values).
    """

    wait_times = await asyncio.gather(
            *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
