"""
File: bribery.py
Author: Lizzie Steilberg
"""
from priorityqueue import PriorityQueue

queue = PriorityQueue()

while True:
    bribe = float(input('How much you got? '))

    if bribe > 0:
        position = queue.add(-abs(bribe))
        print('Thanks. You are now in position', position, 'in the queue. ')
    else:
        print('Yeah right, get lost!!')
