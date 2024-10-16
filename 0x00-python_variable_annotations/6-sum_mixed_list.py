#!/usr/bin/env python3
"""Task 6 Module
"""
from typing import Union


def some_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    """Complex types - mixed list
    """
    return sum(mxd_lst)
