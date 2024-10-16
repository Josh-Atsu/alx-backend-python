#!/usr/bin/env python3
""" Async Generator
"""
import asyncio
#from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """Loop 10 times
    Yield random number between 0 and 10
    """
    for _ in range(10):
        i = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield i
