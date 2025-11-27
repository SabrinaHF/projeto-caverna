import random
from typing import Optional


def roll(min_v: int, max_v: int, rng: Optional[random.Random] = None) -> int:
    if min_v > max_v:
        raise ValueError("min_v must be <= max_v")

    if rng is None:
        rng = random

    return rng.randint(min_v, max_v)