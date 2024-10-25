""""
File: LinkedList.py
Author: Lizzie Steilberg/MIT
"""


class Node:
    def __init__(self, datum):

        self.datum = datum
        self.next = None


class List:

    def __init__(self):

        self.head = None
        self.tail = None

    def add(self, datum):

        newnode = Node(datum)

        # Empty list: new node is head
        if self.head is None:
            self.head = newnode

        # Non-empty: point from current tail to new node
        else:
            self.tail.next = newnode

        # New node always becomes current tail
        self.tail = newnode

    def __iter__(self):

        node = self.head

        while node is not None:
            yield node
            node = node.next

    def __str__(self):

        return '[' + ', '.join([node.datum for node in self]) + ']'

    def __contains__(self, datum):

        # Loop over list until we find the datum or reach the end
        for node in self:
            if node.datum == datum:
                return True

        # Didn't find it!
        return False


def main():

    lyst = List()

    print(lyst)

    lyst.add('alpha')
    lyst.add('beta')
    lyst.add('gamma')

    print(lyst)

    print('beta' in lyst)
    print('delta' in lyst)

if __name__ == '__main__':
    main()