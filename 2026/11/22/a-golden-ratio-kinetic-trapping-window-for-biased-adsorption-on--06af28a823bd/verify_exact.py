#!/usr/bin/env python3
"""Independent exact finite-state race verification for biased Kneser adsorption."""
from functools import lru_cache
from fractions import Fraction
from itertools import combinations


def formula(n, w):
    w = Fraction(w)
    s = 2*w/(n-2+2*w)
    return (s*(w/((w+1)*(1+(n-3)*w)) + w/((w+1)*(w+n-3)))
            + (1-s)*(w*w+n-3)/(w+n-3)**2)


def independent_exact(n, w):
    w = Fraction(w)
    edges = list(combinations(range(n), 2))
    rates = [w if 0 in e else Fraction(1) for e in edges]
    compat = []
    for i, e in enumerate(edges):
        compat.append(sum((1 << j) for j, f in enumerate(edges)
                          if i != j and (e[0] in f or e[1] in f)))
    @lru_cache(None)
    def recurse(occupied_mask, available_mask):
        if not available_mask:
            chosen = [edges[j] for j in range(len(edges)) if occupied_mask & (1 << j)]
            triangle = len(chosen) == 3 and len({v for edge in chosen for v in edge}) == 3
            return Fraction(int(triangle))
        candidates = [j for j in range(len(edges)) if available_mask & (1 << j)]
        total = sum((rates[j] for j in candidates), Fraction(0))
        return sum((rates[j]/total * recurse(occupied_mask | (1 << j), available_mask & compat[j])
                    for j in candidates), Fraction(0))
    return recurse(0, (1 << len(edges))-1)


def main():
    tests = 0
    for n in (5, 6, 7):
        for w in (Fraction(1,2), Fraction(1), Fraction(2), Fraction(5), Fraction(20)):
            result = independent_exact(n, w)
            assert result == formula(n, w), (n,w,result,formula(n,w))
            if w == 1:
                assert result == Fraction(1,n-2)
            tests += 1
    print(f"PASS: {tests} independently enumerated exact parameter cases")

if __name__ == '__main__':
    main()
