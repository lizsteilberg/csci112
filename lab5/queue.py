"""
File: Queue.py
Author: Lizzie Steilberg
"""
from node import Node


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def isEmpty(self):
        return self.front is None

    def pop(self):
        data = self.front.data
        self.front = self.front.next
        return data

    def add(self, item):
        node = Node(item, None)
        if self.isEmpty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node


if __name__ == '__main__':
    print("Test case for queue class (expect a b c d): ")
    s = Queue()

    s.add('a')
    s.add('b')
    s.add('c')
    s.add('d')

    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
