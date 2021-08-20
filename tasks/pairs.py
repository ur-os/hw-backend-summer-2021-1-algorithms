from typing import Any

__all__ = (
    'corresponding_pairs',
)


def corresponding_pairs(arr1: list[Any], arr2: list[Any]) -> list[tuple[Any, Any]]:
    """
    Функция должна возвращать соответствующие элементы двух массивов:
    corresponding_pairs([1, 2], [3, 4]) == [(1, 3), (2, 4)]
    """

    result = list(tuple())

    if len(arr1) <= len(arr2):
        iterator = 0
        for i in arr1:
            result.append((i, arr2[iterator]))
            iterator += 1
    else:
        iterator = 0
        for i in arr2:
            result.append((arr1[iterator], i))
            iterator += 1

    return result

