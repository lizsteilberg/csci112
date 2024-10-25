"""
File: Stack.py
Author: Lizzie Steilberg
"""
from node import Node


class Stack:

    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def __iter__(self):
        cursor = self.head
        while cursor is not None:
            yield cursor.data
            cursor = cursor.next

    def __len__(self):
        return self.size

    def pop(self):
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1


if __name__ == '__main__':
    print("Test case for stack class (expect c b a): ")
    s = Stack()

    s.push('a')
    s.push('b')
    s.push('c')

    print(s.pop())
    print(s.pop())
    print(s.pop())
