#!/usr/bin/env python3
""" Async Generator
"""
import asyncio
#from typing import
import random


async def async_generator():
    """Loop 10 times
    Yield random number between 0 and 10
    """
    for _ in range(10):
        i = random.uniform(0, 10)
        yield i
