__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    intervals = (
        ('d', 86400),    # 60 * 60 * 24
        ('h', 3600),    # 60 * 60
        ('m', 60),
        ('s', 1),
    )

    result = []
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)

    result = str()
    if d != 0:
        result += f'{d:02d}'
        result += 'd'
        result += f'{h:02d}'
        result += 'h'
        result += f'{m:02d}'
        result += 'm'
        result += str(f'{s:02d}')
        result += 's'
        return result

    if h != 0:
        result += f'{h:02d}'
        result += 'h'
        result += f'{m:02d}'
        result += 'm'
        result += str(f'{s:02d}')
        result += 's'
        return result

    if m != 0:
        result += f'{m:02d}'
        result += 'm'
        result += str(f'{s:02d}')
        result += 's'
        return result

    result += str(f'{s:02d}')
    result += 's'

    return result




