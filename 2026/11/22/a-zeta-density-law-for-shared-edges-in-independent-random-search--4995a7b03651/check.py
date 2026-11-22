"""Exact finite verification for a two-search-tree edge-overlap theorem.

Requires Python 3 standard library only. Run: python check.py
The script checks finite statements, not the infinite ergodic limit.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import factorial, pi


def oriented_edges(order):
    """Parent-child pairs from increasing-priority Cartesian recursion."""
    rank = {v: t for t, v in enumerate(order)}
    n = len(order)
    output = []

    def recurse(lo, hi):
        if lo > hi:
            return
        root = min(range(lo, hi + 1), key=rank.__getitem__)
        for left, right in ((lo, root - 1), (root + 1, hi)):
            if left <= right:
                child = min(range(left, right + 1), key=rank.__getitem__)
                output.append((root, child))
                recurse(left, right)

    recurse(1, n)
    assert len(output) == n - 1
    return output


def parent_probability(n, i, j):
    assert 1 <= i < j <= n
    d = j - i
    left_parent = Fraction(1, 2 * d * (d + 1)) + Fraction(1, 2 * (n - i) * (n - i + 1))
    right_parent = Fraction(1, 2 * d * (d + 1)) + Fraction(1, 2 * (j - 1) * j)
    return left_parent, right_parent


def finite_mean(n):
    return sum((sum(parent_probability(n, i, j), Fraction(0))) ** 2
               for i in range(1, n) for j in range(i + 1, n + 1))


def main():
    checks = 0
    for n in range(2, 8):
        directed = Counter()
        total = factorial(n)
        for order in permutations(range(1, n + 1)):
            for parent, child in oriented_edges(order):
                directed[(parent, child)] += 1
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                lp, rp = parent_probability(n, i, j)
                assert Fraction(directed[(i, j)], total) == lp
                assert Fraction(directed[(j, i)], total) == rp
                checks += 2
        assert sum(directed.values()) == total * (n - 1)
        checks += 1
        expectation_from_counts = sum(
            Fraction((directed[(i, j)] + directed[(j, i)]) ** 2, total ** 2)
            for i in range(1, n) for j in range(i + 1, n + 1)
        )
        assert expectation_from_counts == finite_mean(n)
        checks += 1
        print(f'n={n}  permutations={total}  common-edge mean={finite_mean(n)}')

    # Check the finite decomposition independently (all rational).
    for n in (2, 3, 5, 10, 30, 75):
        a = lambda d: Fraction(1, d * (d + 1))
        b = lambda s: Fraction(1, s * (s + 1))
        baseline = sum((n - d) * a(d) ** 2 for d in range(1, n))
        cross = 2 * sum(Fraction(1, (s + 1) ** 2) for s in range(1, n))
        squares = Fraction(1, 2) * sum(s * b(s) ** 2 for s in range(1, n))
        border_cross = Fraction(1, 2) * sum(
            b(s) * b(t) for s in range(1, n) for t in range(1, n) if s + t >= n
        )
        assert finite_mean(n) == baseline + cross + squares + border_cross
        checks += 1
    c = pi * pi / 3 - 3
    C = 5 * pi * pi / 12 - 3
    for n in (100, 200, 400):
        approximate = float(finite_mean(n))
        assert abs(approximate - (n * c + C)) < 3.0 / n
        checks += 1
    print(f'PASS {checks} exact-or-controlled assertions; c={c:.12f}; C={C:.12f}')


if __name__ == '__main__':
    main()
