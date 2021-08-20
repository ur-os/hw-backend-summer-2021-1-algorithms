__all__ = (
    'is_prime',
)


def is_prime(n: int) -> bool:
    if n in [0, 1]:
        return False

    i, j = 2, 0
    while i**2 <= n and j != 1:
        if n % i == 0:
            j = 1
        i += 1
    if j == 1:
        return False
    else:
        return True
