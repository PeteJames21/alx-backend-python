#!/usr/bin/env python3
"""
Define an async generator that yields 10 random numbers when looped over.
"""
import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> float:
    """Generate 10 random numbers from 1 to 10."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
