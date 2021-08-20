import re

from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    minimum = text.split()
    maximum = text.split()

    if len(minimum) <= 0:
        minimum = None
    else:
        minimum = min(minimum, key=len)

    if len(maximum) <= 0:
        maximum = None
    else:
        maximum = max(maximum, key=len)

    return minimum, maximum
