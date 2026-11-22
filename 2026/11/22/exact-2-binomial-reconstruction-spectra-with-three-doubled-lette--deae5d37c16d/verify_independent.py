#!/usr/bin/env python3
"""Independent all-pair deck verification by actual marker-word enumeration.

Directly enumerate multiset words with three duplicated symbols and r
DISTINCT singleton symbols in a fixed relative marker order. No cut-table
or inversion-skeleton shortcut is used; all pair counts are measured.
"""
from collections import Counter
from itertools import combinations, permutations
from math import factorial

BASE = sorted(set(permutations((0, 0, 1, 1, 2, 2))))

def observed_deck(word, alphabet):
    single = [0] * alphabet
    ordered_pair = [[0] * alphabet for _ in range(alphabet)]
    for current in word:
        for previous in range(alphabet):
            ordered_pair[previous][current] += single[previous]
        single[current] += 1
    return tuple(single) + tuple(x for row in ordered_pair for x in row)

def direct_spectrum(r):
    length = r + 6
    markers = list(range(3, r+3))
    fibers = Counter()
    for w in BASE:
        for positions in combinations(range(length), 6):
            array = [-1] * length
            for i, a in zip(positions, w):
                array[i] = a
            itr = iter(markers)
            for i in range(length):
                if array[i] < 0:
                    array[i] = next(itr)
            fibers[observed_deck(array, r + 3)] += 1
    return dict(sorted(Counter(fibers.values()).items())), sum(fibers.values())

def formulas_fixed_marker_order(r):
    f = (r + 1) * (r + 2)
    return {1: f * (r**4 + 18*r**3 + 107*r**2 + 258*r + 192)//8,
            2: 3 * f * (r+3) * (r+4)//4,
            6: f//2}

if __name__ == '__main__':
    for r in range(6):
        got, n = direct_spectrum(r)
        expected = formulas_fixed_marker_order(r)
        assert got == expected, (r,got,expected)
        assert n == factorial(r+6) // (8*factorial(r))
        print('r=',r,'spectrum=',got,'source words=',n)
    print('INDEPENDENT ALL-PAIR DECK CHECK PASS for r=0,...,5')
