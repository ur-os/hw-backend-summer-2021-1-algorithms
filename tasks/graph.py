from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:
        result = [self._root]

        for node in self._root.outbound:
            traceback = Graph(node).dfs()


            for element in traceback:
                if element in result:
                    traceback.remove(element)  # concatenation of lists
            result += traceback
        return result

    def bfs(self) -> list[Node]:
        raise NotImplementedError
