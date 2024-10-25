class Node:
    def __init__(self, data = None):
        self.value = None
        self.next = None
class Stack:
    def __init__(self):
        self.head = None

    def push(self, item):
        node = Node(item)
        if self.head is not None:
            node.next = self.head
        self.head = node
            
    def pop(self):
        item = self.head.item
        self.head = self.head.next
        return item

