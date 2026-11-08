#!/usr/bin/env python3
"""Finite, independent replay for the square-idempotent fiber theorem."""
from collections import Counter
from itertools import combinations
from math import comb, prod


def motzkin(n):
    states = {0: 1}
    for _ in range(n):
        new = Counter()
        for level, count in states.items():
            new[level] += count
            new[level + 1] += count
            if level:
                new[level - 1] += count
        states = new
    return states.get(0, 0)


def expected_fiber(n, fixed):
    boundaries = (-1,) + tuple(fixed) + (n,)
    return prod(motzkin(boundaries[i + 1] - boundaries[i] - 1)
                for i in range(len(boundaries) - 1))


def transformations(n):
    for r in range(n + 1):
        for dom in combinations(range(n), r):
            for image in combinations(range(n), r):
                if all(x <= y for x, y in zip(dom, image)):
                    yield dict(zip(dom, image))


def convolution(a, b, degree):
    return sum(a[j] * b[degree - j] for j in range(degree + 1))


def main():
    nmax = 9
    mot = [motzkin(n) for n in range(30)]
    assert mot[:9] == [1, 1, 2, 4, 9, 21, 51, 127, 323]
    total = [0] * 30
    total[0] = 1
    refined = [[0] * (n + 1) for n in range(30)]
    refined[0][0] = 1
    for n in range(1, 30):
        # M(z) / (1 - u z M(z)), expanded by the number of fixed points.
        for k in range(n + 1):
            if k == 0:
                refined[n][k] = mot[n]
            else:
                refined[n][k] = sum(mot[j] * refined[n - 1 - j][k - 1]
                                    for j in range(n) if k - 1 <= n - 1 - j)
        total[n] = sum(refined[n])
    assert total[:10] == [1, 2, 5, 13, 35, 96, 267, 750, 2123, 6046]
    examined = 0
    fiber_cases = 0
    for n in range(nmax + 1):
        counts = Counter()
        whole = 0
        for f in transformations(n):
            whole += 1
            f2 = {x: f[y] for x, y in f.items() if y in f}
            if all(x == y for x, y in f2.items()):
                fixed = tuple(sorted(f2))
                counts[fixed] += 1
        expected_whole = comb(2 * n + 2, n + 1) // (n + 2)
        assert whole == expected_whole, (n, whole, expected_whole)
        assert sum(counts.values()) == total[n], (n, total[n])
        for r in range(n + 1):
            observed = sum(v for s, v in counts.items() if len(s) == r)
            assert observed == refined[n][r], (n, r, observed, refined[n][r])
            for subset in combinations(range(n), r):
                assert counts[subset] == expected_fiber(n, subset), (n, subset)
                fiber_cases += 1
        examined += whole
    # Direct differential identity: dF/du at u=1 = z F(z)^2.
    for n in range(1, 30):
        left = sum(k * refined[n][k] for k in range(n + 1))
        right = convolution(total, total, n - 1)
        assert left == right, (n, left, right)
    print(f'VERIFY_OK n=0..{nmax}; mappings={examined}; square-root fibers={fiber_cases}; coefficients=0..29')


if __name__ == '__main__':
    main()
