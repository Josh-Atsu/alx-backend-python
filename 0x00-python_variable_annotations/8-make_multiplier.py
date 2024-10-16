#!/usr/bin/env python3
"""task 8
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Complex types - function
    """
    def multiplier_func(value: float) -> float:
        """callable function
        """
        return value * multiplier
    return multiplier_func
