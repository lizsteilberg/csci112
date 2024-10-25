"""
Class 10/14/24
"""
from node import Node


class LinkedStack:
    def __init__(self):
        self.head = None

    def push(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

    def pop(self):
        if self.head is None:
            return None # or could raise an exception ig
        item = self.head.data
        self.head = self.head.next
        return item
# he doesn't like iterating over stacks
