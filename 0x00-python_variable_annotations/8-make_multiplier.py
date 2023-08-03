#!/usr/bin/env python3

"""8. Complex types - functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a
    float by the given multiplier."""
    def multiply_by_multiplier(x: float) -> float:
        return x * multiplier
    return multiply_by_multiplier
