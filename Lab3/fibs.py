"""
Author: Lizzie Steilberg
File: fibs.py

Two versions of the functions to compute the nth Fibonacci number.
"""
from counter import Counter

def fib1(n, counter = None):
    """The standard recursive version."""
    if counter != None:
        counter.increment(amount=1)
    
    if n==1 or n==2:
        return 1
    else:
        return fib1(n-1, counter) + fib1(n-2, counter)

def fib2(n, counter = None):
    """The recursive version with a memoizing cache."""
    cache = dict()
    def fastFib(n, counter = None):
        if counter != None:
            counter.increment()
        if n<3:
            return 1
        elif n in cache:
            return cache[n]
        else:
            value = fastFib(n-1, counter) + fastFib(n-2, counter)
            cache[n] = value
            return value
    return fastFib(n, counter)


def test(fib):
    """Runs some tests on a fib function."""
    for n in range(1, 6):
        print("n:", n, "fib(n):", fib(n))

def testWithCounter(fib):
    """Runs some tests on a fib function."""
    counter = Counter()
    for n in range(1, 11):
        counter.reset()
        print("n:", n, "fib(n):", fib(n, counter),
              " Number of calls:", str(counter))

def main():
    """To test, pass the name of the fib function to test."""
    print("Fib1 Test:", end='\n')
    test(fib1)
    print()
    print("Fib2 Test:", end='\n')
    test(fib2)
    print()
    print("Fib1 Test with Counter:", end='\n')
    testWithCounter(fib1)
    print()
    print("Fib2 Test with Counter:", end='\n')
    testWithCounter(fib2)

if __name__ == "__main__":
    main()
