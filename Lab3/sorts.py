"""
Author: Lizzie Steilberg
File: sorts.py

Defines the selection sort and the quick sort.
"""
from counter import Counter
from tools import getRandomList

def selectionSort(lyst, comps = None, swaps = None):
    """Sorts lyst with a selection sort."""
    lystLen = len(lyst)
    for i in range(lystLen):
        minIndex = minInRange(lyst, i, lystLen, comps)
        if minIndex != i:
            swap(lyst, i, minIndex, swaps)
        if comps: comps.increment() #I'm also counting the equality check in lines 15-16 as a comp haha
    
def minInRange(lyst, i, n, comps = None):
    minValue = lyst[i]
    minIndex = i
    for j in range(i, n):
        if lyst[j] < minValue:
            minValue = lyst[j]
            minIndex = j
        if comps: comps.increment()
    return minIndex
    
def quickSort(lyst, comps = None, swaps = None):
    """Sorts lyst with a quick sort."""
    def recurse(left, right):
        if left<right:
            if comps: comps.increment()
            pivotPosition = partition(lyst, left, right, comps, swaps)
            recurse(left, pivotPosition - 1)
            recurse(pivotPosition + 1, right)

    def partition(lyst, left, right, comps = None, swaps = None):
        middle = (left + right) // 2
        pivot = lyst[middle]
        lyst[middle] = lyst[right]
        lyst[right] = pivot
        boundary = left
        for index in range(left, right):
            if comps: comps.increment()
            if lyst[index] < pivot:
                swap(lyst, index, boundary, swaps)
                boundary+=1
        swap(lyst, right, boundary, swaps)
        return boundary
    recurse(0, len(lyst)-1)

def swap(lyst, i, j, counter = None):
    """Exchanges the items at i and j in lyst and increments
    the counter if it exists."""
    if counter: counter.increment()
    lyst[i], lyst[j] = lyst[j], lyst[i]       

def test(sort, n = 15):
    """Runs some tests on a sort function."""
    lyst = list(range(1, n + 1))
    print("Sorting", lyst)
    sort(lyst)
    print("Result", lyst)
    lyst = getRandomList(n)
    print("Sorting", lyst)
    sort(lyst)
    print("Result", lyst)

def testWithCounters(sort, n = 15):
    """Runs some tests on a sort function."""
    comps = Counter()
    swaps = Counter()
    lyst = list(range(1, n + 1))
    print("Sorting", lyst)
    sort(lyst, comps, swaps)
    print("Result", lyst, "Comps:", str(comps), "Swaps:", str(swaps))
    comps.reset()
    swaps.reset()
    lyst = getRandomList(n)
    print("Sorting", lyst)
    sort(lyst, comps, swaps)
    print("Result", lyst, "Comps:", str(comps), "Swaps:", str(swaps))


def main():
    """To test, pass the name of the sort function to test."""
    print("Selection Sort:")
    test(selectionSort)
    print()

    print("Selection Sort w Counters:")
    testWithCounters(selectionSort)
    print()
    print("Quick Sort:")
    test(quickSort)
    print()

    print("Quick Sort w Counters:")
    testWithCounters(quickSort)

if __name__ == "__main__":
    main()
