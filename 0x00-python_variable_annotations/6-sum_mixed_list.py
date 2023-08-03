#!/usr/bin/env python3

"""6. Complex types - mixed list"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of the elements in the
    mixed list of integers and floats."""
    return sum(mxd_lst)
