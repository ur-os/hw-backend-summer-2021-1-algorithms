__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    try:
        even_slice = (x for x in arr if x % 2 == 0)
        odd_slice = (x for x in arr if x % 2 != 0)
        result = sum(even_slice) / sum(odd_slice)

    except ZeroDivisionError:
        return 0

    return result

