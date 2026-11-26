#!/usr/bin/env python3
"""Exact integer checks for a fixed lower-index binomial coefficient theorem."""
from math import comb
from collections import Counter


def value(n, r):
    return comb(n, r) if n >= r else 0


def predicted(s, k, y):
    total = int(y % 2 == 1)
    for j in range(1, s + 1):
        t = min(j, k)
        if y % (1 << t) == 0:
            total += 1 << (j + t - 2)
    return total


def v2(x):
    assert x
    return (abs(x) & -abs(x)).bit_length() - 1


def main():
    comparisons = 0
    for s in range(1, 7):
        r = (1 << s) - 1
        for k in range(1, 9):
            m = 1 << k
            period = 1 << (s + k - 1)
            hist = Counter(value(n, r) % m for n in range(period))
            for y in range(m):
                expected = predicted(s, k, y)
                assert hist[y] == expected, (s, k, y, hist[y], expected)
                comparisons += 1
            if k == 1:
                assert value(r, r) % 2 == 1
                assert value(r - (1 << (s - 1)), r) % 2 == 0
            else:
                # The exhibited half-period fails at n=r.
                assert (value(r + period // 2, r) - value(r, r)) % m
    # On a few cosets and small parameters verify exact isometry valuations.
    isometry_checks = 0
    for s in range(1, 6):
        r = (1 << s) - 1
        step = 1 << s
        for a in range(r + 1):
            c = 1 if a == r else s - v2(a + 1)
            for t in range(12):
                for u in range(t + 1, 12):
                    x = value(a + step * t, r)
                    y = value(a + step * u, r)
                    assert v2(x - y) == c + v2(t - u), (s, a, t, u)
                    isometry_checks += 1
    print(f'PASS: {comparisons} residue-fiber checks; {isometry_checks} isometry checks; all tested half-period obstructions.')


if __name__ == '__main__':
    main()
