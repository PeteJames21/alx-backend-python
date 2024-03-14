#!/usr/bin/env python3
"""
Define a function that returns the first element in a list.
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element in lst."""
    if lst:
        return lst[0]
    else:
        return None
