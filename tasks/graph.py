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
    def __init__(self, root: Node, visited_list=None):
        if visited_list is None:
            self.visited_list = []
        else:
            self.visited_list = visited_list
        self._root = root

    def dfs(self) -> list[Node]:
        result = [self._root]

        for node in self._root.outbound:
            if node not in self.visited_list:
                self.visited_list.append(node)
                traceback = Graph(node, self.visited_list).dfs()

                for element in traceback:
                    if element in result:
                        traceback.remove(element)
                result += traceback  # concatenation of lists
        return result

    def bfs(self, queue=None, result=None) -> list[Node]:
        if queue is None:
            queue = []
        if result is None:
            result = []

        #  append root vertex
        if self._root not in result:
            result.append(self._root)

        # parse in queue
        for node in self._root.outbound:
            if node not in result:
                result.append(node)
                queue.insert(0, node)

        if queue:
            return Graph(queue.pop(), self.visited_list).bfs(queue, result)
        else:
            return result
