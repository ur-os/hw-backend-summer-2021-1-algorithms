__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    try:
        even_slice = (2*i for i in arr)
        odd_slice = (2*i + 1 for i in arr)
        result = sum(even_slice) / sum(odd_slice)

    except ZeroDivisionError:
        return 1.0
    return result

