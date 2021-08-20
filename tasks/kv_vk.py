from typing import TypeVar

__all__ = (
    'flip_kv_vk',
    'flip_kv_vk_safe',
)

KT = TypeVar('KT')
KV = TypeVar('KV')


def flip_kv_vk(d: dict[KT, KV]) -> dict[KV, KT]:
    return {d[i]: i for i in d}


def flip_kv_vk_safe(d: dict[KT, KV]) -> dict[KV, list[KT]]:
    return {d[i]: [j for j in d if d[j] == d[i]] for i in d}
