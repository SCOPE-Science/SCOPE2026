#!/usr/bin/env python3
"""Exhaustive finite certificate for all marker-refined 2-binomial fibers.

The 90 six-letter words with two occurrences of each of three colors
are split at k-1 cut positions. For each k, the full oriented pair
profile and the ordered segment contents are the complete observables.
The finite k=1..6 table proves the formulas for arbitrary marker count.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import comb, factorial

BASE = tuple(sorted(set(permutations((0, 0, 1, 1, 2, 2)))))
PAIRS = ((0, 1), (0, 2), (1, 2))
EXPECTED = {
    1: {1: 48, 2: 18, 6: 1},
    2: {1: 336, 2: 54, 6: 1},
    3: {1: 792, 2: 54},
    4: {1: 864, 2: 18},
    5: {1: 450},
    6: {1: 90},
}

def content(word):
    return tuple(word.count(a) for a in range(3))

def pair_profile(word):
    return tuple(sum(word[i] == a and word[j] == b
                     for i in range(6) for j in range(i + 1, 6))
                 for a, b in PAIRS)

def finite_certificate():
    results = {}
    for k in range(1, 7):
        classes = defaultdict(int)
        for word in BASE:
            p = pair_profile(word)
            for cuts in combinations(range(1, 6), k - 1):
                parts = tuple(word[i:j] for i, j in
                              zip((0,) + cuts, cuts + (6,)))
                classes[(tuple(content(part) for part in parts), p)] += 1
        sizes = dict(sorted(Counter(classes.values()).items()))
        assert sizes == EXPECTED[k], (k, sizes)
        assert sum(s * count for s, count in sizes.items()) == 90 * comb(5, k-1)
        results[k] = sizes
    return results

def full_formula(r, s):
    p = r + 1
    return factorial(r) * sum(EXPECTED[k].get(s, 0) * comb(p, k)
                              for k in range(1, min(6, p) + 1))

def closed_formula(r, s):
    f = factorial(r) * (r + 1) * (r + 2)
    if s == 1:
        return f * (r**4 + 18*r**3 + 107*r**2 + 258*r + 192) // 8
    if s == 2:
        return 3 * f * (r + 3) * (r + 4) // 4
    if s == 6:
        return f // 2
    raise ValueError(s)

if __name__ == '__main__':
    assert len(BASE) == 90
    table = finite_certificate()
    # Symbolic identity (using falling binomial polynomials): verify by
    # exact polynomial arithmetic rather than by sampling r values.
    import sympy as sp
    t = sp.symbols('t', integer=True, nonnegative=True)
    for s in (1, 2, 6):
        lhs = sum(EXPECTED[k].get(s, 0) * sp.prod(t+1-j for j in range(k))
                  / factorial(k) for k in range(1, 7))
        rhs = {1:(t+1)*(t+2)*(t**4+18*t**3+107*t**2+258*t+192)/8,
               2:3*(t+1)*(t+2)*(t+3)*(t+4)/4,
               6:(t+1)*(t+2)/2}[s]
        assert sp.expand(lhs-rhs) == 0, (s, sp.factor(lhs-rhs))
    for r in range(0, 12):
        assert all(full_formula(r,s) == closed_formula(r,s) for s in (1,2,6))
        assert sum(s * full_formula(r,s) for s in (1,2,6)) == factorial(r+6)//8
    print('CERTIFICATE PASS: 90 skeletons, 32 cut sets per skeleton')
    print('k, count of full decks by fiber size:')
    for k, spectrum in table.items():
        print(k, spectrum)
    print('Exact polynomial identities verified for every nonnegative marker count.')
