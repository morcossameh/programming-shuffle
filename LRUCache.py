# Problem: https://leetcode.com/problems/lru-cache/
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node

        # Dummy head and tail nodes to avoid edge cases
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # Helper to remove a node from the list
    def _remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    # Helper to insert a node at the tail (most recently used)
    def _add(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move the node to the end (most recently used)
        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove old node
            self._remove(self.cache[key])

        # Add new node
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            # Remove least recently used node (head.next)
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
