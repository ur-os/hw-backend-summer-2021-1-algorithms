from typing import Any

__all__ = (
    'cartesian_product',
)


def cartesian_product(arr1: list[Any], arr2: list[Any]) -> list:
    result = list(tuple())
    for i in arr1:
        for j in arr2:
            result.append((i, j))
    return result
