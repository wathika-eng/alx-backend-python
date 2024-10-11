#!/usr/bin/env python3

"""
Use mypy to validate the following piece of code and apply any necessary changes.
"""

from typing import Tuple, List

def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Given a tuple, returns a list with the same elements
    repeated a specific number of times
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
