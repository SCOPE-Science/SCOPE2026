#!/usr/bin/env python3
"""Exhaustive three-outcome check of clone-free concurrent-game matrices.

Each nonempty subset of {0,...,n-1} is encoded by its bit mask.
A family is a tuple of distinct nonempty masks in increasing order.
The matrix entries are outcome bits; its rows and columns must have the exact given unions.
"""
from itertools import combinations, product
from functools import reduce
from operator import or_


def families(n):
    nonempty = range(1, 1 << n)
    return [subset for k in range(1, len(nonempty) + 1)
            for subset in combinations(nonempty, k)]


def permitted(a, b, n):
    full = (1 << n) - 1
    return (reduce(or_, a, 0) == full == reduce(or_, b, 0)
            and all(x & y for x in a for y in b)
            and all(x.bit_count() <= len(b) for x in a)
            and all(y.bit_count() <= len(a) for y in b))


def realizing_matrix(a, b, n):
    s, t = len(a), len(b)
    choice_lists = [tuple(i for i in range(n) if (a[r] & b[c]) & (1 << i))
                    for r in range(s) for c in range(t)]
    for flat in product(*choice_lists):
        if (all(sum((1 << flat[r*t+c] for c in range(t)), 0) >= 0 for r in range(s))
                and all(reduce(or_, ((1 << flat[r*t+c]) for c in range(t)), 0) == a[r]
                        for r in range(s))
                and all(reduce(or_, ((1 << flat[r*t+c]) for r in range(s)), 0) == b[c]
                        for c in range(t))):
            return flat
    return None


def classify(n):
    ff = families(n)
    good = [(a, b) for a in ff for b in ff if permitted(a, b, n)]
    bad = [(a, b) for a,b in good if realizing_matrix(a,b,n) is None]
    return good, bad


def main():
    expected = {1: (1, 0), 2: (4, 0), 3: (282, 54)}
    for n in (1, 2, 3):
        good, bad = classify(n)
        assert (len(good), len(bad)) == expected[n], (n,len(good),len(bad))
        print('outcomes', n, 'admissible', len(good), 'nonrealizable', len(bad))
    a,b=(3,5),(3,6)
    assert permitted(a,b,3)
    assert realizing_matrix(a,b,3) is None
    assert any((a,b) == x for x in classify(3)[1])
    print('CLONE_FREE_FIRST_OBSTRUCTION_OK')

if __name__ == '__main__':
    main()
