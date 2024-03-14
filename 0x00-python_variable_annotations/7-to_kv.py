#!/usr/bin/env python3
from typing import Tuple, Union
"""
Compute the square of an int/float
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Compute the square of v."""
    return k, v ** 2
