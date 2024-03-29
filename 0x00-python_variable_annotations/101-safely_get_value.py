#!/usr/bin/env python3
"""
Retrieve a value from a dict using its key.
"""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> T:
    """Get a value from a dict."""
    if key in dct:
        return dct[key]
    else:
        return default
