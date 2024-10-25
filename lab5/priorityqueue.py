"""
File: PriorityQueue.py
Author: Lizzie Steilberg
"""
from node import Node
from queue import Queue
from counter import Counter


class PriorityQueue(Queue):
    """
    Instantiate from parent class Queue
    """
    def __init__(self):
        Queue.__init__(self)

    def add(self, item):
        """
        Redefine add method for priority queue
        """
        counter = Counter()
        counter.increment()
        if self.isEmpty() or item >= self.rear.data:
            Queue.add(self, item)
            counter.increment() if self.isEmpty()\
                else counter.increment(self.size)
        else:
            """
            Add new item to appropriate position in priority queue
            """
            probe = self.front
            while item >= probe.data:
                trailer = probe
                probe = probe.next
                counter.increment()
            node = Node(item, probe)
            if probe == self.front:
                self.front = node
            else:
                trailer.next = node
        self.size += 1
        return counter


if __name__ == '__main__':
    print("Testing priority queue (expect a b c d e f): ")

    s = PriorityQueue()

    s.add('c')
    s.add('b')
    s.add('a')
    s.add('f')
    s.add('e')
    s.add('g')
    s.add('d')

    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
