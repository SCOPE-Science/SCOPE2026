#!/usr/bin/env python3
"""Independent small-chain check of the stated Frobenius-adjoint axioms.

Usage: python3 verify_fgc_mv.py
Python standard library only. General theorems require the written proof.
"""
from itertools import product
from math import isqrt


def divisors(m):
    return [d for d in range(1, m + 1) if m % d == 0]


def admissible(m, f, g):
    a = range(m + 1)
    implication = lambda x, y: min(m, m - x + y)
    if any(f[x] > x for x in a):
        return False
    for x in a:
        for y in a:
            # Check all axioms as stated in the primary source, not
            # consequences of those axioms.
            if (g[x] <= y) != (x <= f[y]):
                return False
            if f[implication(g[x], y)] != implication(g[x], f[y]):
                return False
            if f[max(g[x], y)] != max(g[x], f[y]):
                return False
            if g[min(x, g[y])] != min(g[x], g[y]):
                return False
    return True


def candidate(m, d):
    return (tuple((j // d) * d for j in range(m + 1)),
            tuple(((j + d - 1) // d) * d for j in range(m + 1)))


def check(m):
    # Search all nondecreasing pointwise deflationary f. Adjunction forces
    # a UNIQUE g, the least y with x <= f(y). If no such y, reject f.
    count_f = 0
    survivors = set()
    def rec(prefix):
        nonlocal count_f
        j = len(prefix)
        if j == m + 1:
            count_f += 1
            f = tuple(prefix)
            if f[m] != m:
                return
            g = tuple(next((y for y in range(m + 1) if x <= f[y]), m + 1)
                      for x in range(m + 1))
            if any(y > m for y in g):
                return
            if admissible(m, f, g):
                survivors.add((f, g))
            return
        for v in range(prefix[-1] if prefix else 0, j + 1):
            rec(prefix + [v])
    rec([])
    expected = {candidate(m, d) for d in divisors(m)}
    assert survivors == expected, (m, sorted(survivors ^ expected))
    return m + 1, count_f, len(survivors), tuple(divisors(m))


def main():
    for m in range(1, 10):
        n, tried, found, ds = check(m)
        print(f"n={n:2d} candidates={tried:6d} expansions={found:2d} divisors={ds}")
    print('PASS: all independent direct-axiom tests through n=10.')

if __name__ == '__main__':
    main()
