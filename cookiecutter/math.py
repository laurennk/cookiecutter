"""
A file for executing math functions.
"""

import numpy as np


def main():
    print("pi" + str(pi(100)))


def pi(n=100000):
    if n <= 0:
        raise ValueError("Only positive integers are allowed")

    count = 0

    for i in range(n):
        x = np.random.random()
        y = np.random.random()

        r = x * x + y * y

        if r < 1:
            count += 1

    return 4 * count / n


def euler(n=10):
    if n < 0:
        raise ValueError("Only positive integers are allowed")

    e = 1.0
    frac = 1.0

    for i in range(1, n + 1):
        frac *= i
        e += 1.0 / frac

    return e


if __name__ == '__main__':
    main()
