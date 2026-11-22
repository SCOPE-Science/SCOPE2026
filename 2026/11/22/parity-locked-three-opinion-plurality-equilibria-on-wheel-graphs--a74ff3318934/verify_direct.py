#!/usr/bin/env python3
"""Independent full-state fixed-point check for three-color wheel plurality."""
from itertools import product
from math import comb


def fixed(hub, rim):
    n = len(rim)
    # This code uses neighbor frequency directly rather than a run characterization.
    for i in range(n):
        counts = [0, 0, 0]
        for v in (hub, rim[(i-1) % n], rim[(i+1) % n]):
            counts[v] += 1
        top = max(counts)
        leaders = [c for c in range(3) if counts[c] == top]
        if len(leaders) == 1 and leaders[0] != rim[i]:
            return False
    counts = [rim.count(c) for c in range(3)]
    top = max(counts)
    leaders = [c for c in range(3) if counts[c] == top]
    return len(leaders) != 1 or leaders[0] == hub


def predicted(n):
    if n % 2:
        return 3
    m = n//2
    b = sum((n * comb(m-r-1, r-1)**2)//r for r in range(1,m//2+1))
    return 3*(1+b)


def main():
    for n in range(3,12):
        actual = sum(fixed(hub,list(w)) for hub in range(3)
                     for w in product(range(3), repeat=n))
        expected = predicted(n)
        assert actual == expected, (n, actual, expected)
        print(f'rim_length={n} fixed={actual} exhaustive=yes')

if __name__ == '__main__':
    main()
