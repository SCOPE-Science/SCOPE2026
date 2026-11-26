#!/usr/bin/env python3
"""Finite independent checks of degree-spectrum formulas for named ternary cycle colourings."""
from itertools import product
from collections import Counter
from math import comb


def formula(n):
    out = Counter()
    if n % 3 == 0:
        out[0] = 6
    for r in range(1, n // 2 + 1):
        s = sum(
            comb(a - 1, r - 1) * comb(n - a - 1, r - 1)
            for a in range(r, n-r+1)
            if (2*a-n) % 3 == 0
        )
        assert (3*n*s) % r == 0
        if s:
            out[2*r] = (3*n*s) // r
    return out


def independently_enumerate(n):
    counts = Counter()
    for colours in product(range(3), repeat=n):
        if any(colours[i] == colours[(i+1) % n] for i in range(n)):
            continue
        degree = 0
        for i in range(n):
            for replacement in range(3):
                if (replacement != colours[i]
                    and replacement != colours[(i-1) % n]
                    and replacement != colours[(i+1) % n]):
                    degree += 1
        counts[degree] += 1
    return counts


def main():
    for n in range(3, 13):
        expected = formula(n)
        observed = independently_enumerate(n)
        assert observed == expected, (n, observed, expected)
        assert sum(observed.values()) == 2**n + 2*(-1)**n
        assert sum(d*count for d, count in observed.items()) // 2 == n*(2**(n-2)+2*(-1)**n)
        top = n if n % 2 == 0 else n-3
        assert max(observed) == top
        assert observed[top] == (6 if n % 2 == 0 else n*(n*n-1)//4)
        assert min(observed) == (0 if n % 3 == 0 else 2)
        print(n, sorted(observed.items()))
    print('CHECKS PASS')


if __name__ == '__main__':
    main()
