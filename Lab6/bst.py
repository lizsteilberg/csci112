"""
Filename: bst.py
Author: Lizzie Steilberg
"""

from math import (log2, ceil)


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def contains(target, node):
        if node is None:
            return False
        elif node.data == target:
            return True
        elif target < node.data:
            return node.contains(target, node.left)
        else:
            return node.contains(target, node.right)

    def __add__(self, newNode):
        # Helper function to search for item’s position
        def recurse(node):
            # New item is less; go left until spot is found
            if newNode.data < node.data:
                if node.left is None:
                    node.left = newNode
                else:
                    recurse(node.left)
            # New item is greater or equal; go right until spot is found
            elif node.right is None:
                node.right = newNode
            else:
                recurse(node.right)
            # End of recurse

        recurse(self)

    def level_count(self):
        s = []

        def recurse(node, level):
            if node is not None:
                level += 1
                s.append(level)
                recurse(node.right, level)
                recurse(node.left, level)
            return s

        return max(recurse(self, 0))

class BST:
    def __init__(self):
        self._root = None
        self.size = 0

    def add(self, item):
        newNode = BSTNode(item)
        if self._root is None:
            self._root = newNode
        else:
            BSTNode.__add__(self._root, newNode)
        self.size += 1

    def __contains__(self, target):
        def recurse(node):
            if node is None:
                return False
            elif target == node.data:
                return True
            elif target < node.data:
                return recurse(node.left)
            else:
                return recurse(node.right)

        return recurse(self._root)

    def height(self):
        if self._root is None:
            return 0
        else:
            return BSTNode.level_count(self._root)


    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise."""

        def recurse(node, level):
            s = ""
            if node is not None:
                s += recurse(node.right, level + 1)
                s += "| " * level
                s += str(node.data) + "\n"
                s += recurse(node.left, level + 1)
            return s

        return recurse(self._root, 0)

    def isBalanced(self):
        """
        doesn't have to be recursive; should be only one line
        a BST with height h and length l is balanced when h < ceil(log2(l))
        """
        pass


if __name__ == '__main__':
    print("Testing 1: ")
    binaryTree = BST()
    binaryTree.add('a')
    binaryTree.add('A')
    binaryTree.add('c')
    binaryTree.add('b')
    binaryTree.add('c')
    binaryTree.add('B')
    binaryTree.add('d')


    print(binaryTree)
    print("Testing height: ", binaryTree.height())
    print()

    print("Testing 2: ")
    binaryTree2 = BST()
    binaryTree2.add('b')
    binaryTree2.add('a')
    binaryTree2.add('c')
    binaryTree2.add('d')
    binaryTree2.add('A')
    binaryTree2.add('c')
    binaryTree2.add('c')
    binaryTree2.add('c')

    print(binaryTree2)
    print(binaryTree2.height())

