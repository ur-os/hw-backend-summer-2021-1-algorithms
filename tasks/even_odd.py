__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:

    even_slice = (2*i for i in arr)
    odd_slice = (2*i + 1 for i in arr)

    return sum(even_slice) / sum(odd_slice)
