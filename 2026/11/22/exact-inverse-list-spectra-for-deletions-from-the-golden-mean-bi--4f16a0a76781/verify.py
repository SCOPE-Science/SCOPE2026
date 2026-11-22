#!/usr/bin/env python3
"""Reproduce finite checks for golden-mean deletion inverse fibers.

Uses independent brute-force enumeration and integer arithmetic only.
"""
from collections import defaultdict
from itertools import combinations, product
from math import comb


def legal(word):
    return all(not (a == 1 and b == 1) for a, b in zip(word, word[1:]))


def fib_words(n):
    return (w for w in product((0, 1), repeat=n) if legal(w))


def fib_coefficients(d):
    f = [1, 1]
    while len(f) <= d:
        f.append(f[-1] + f[-2])
    return f[:d + 1]


def formula(y, d):
    m = len(y)
    k = sum(y)
    r = sum(a == 1 and b == 1 for a, b in zip(y, y[1:]))
    a = m - 2 * k + r + 1
    assert a >= 0
    if d < r:
        return 0
    j = d - r
    poly = [comb(a, p) if p <= a else 0 for p in range(j + 1)]
    if k:
        poly = [sum(poly[p] * comb(k + s - p - 1, s - p)
                    for p in range(s + 1)) for s in range(j + 1)]
    fib = fib_coefficients(j)
    return sum(poly[p] * fib[j - p] for p in range(j + 1))


def direct_parent_counts(m, d):
    counts = defaultdict(set)
    n = m + d
    for parent in fib_words(n):
        for indices in combinations(range(n), m):
            y = tuple(parent[i] for i in indices)
            counts[y].add(parent)
    return counts


def parameter_count(m, k, r):
    if k == 0:
        return int(r == 0)
    if r < 0 or r >= k or m - k + 1 < k - r:
        return 0
    return comb(k - 1, r) * comb(m - k + 1, k - r)


def transfer_counts(m, max_r):
    if m == 0:
        return [1] + [0] * max_r
    counts = [[0] * (max_r + 1) for _ in range(2)]
    counts[0][0] = counts[1][0] = 1
    for _ in range(1, m):
        nxt = [[0] * (max_r + 1) for _ in range(2)]
        for prev in (0, 1):
            for bit in (0, 1):
                add = int(prev == 1 and bit == 1)
                for r in range(max_r + 1 - add):
                    nxt[bit][r + add] += counts[prev][r]
        counts = nxt
    return [counts[0][r] + counts[1][r] for r in range(max_r + 1)]


def main():
    checks = 0
    for m in range(9):
        words = list(product((0, 1), repeat=m))
        for d in range(6):
            observed = direct_parent_counts(m, d)
            for y in words:
                assert len(observed.get(y, ())) == formula(y, d), (m, d, y)
                r = sum(a == b == 1 for a, b in zip(y, y[1:]))
                assert (len(observed.get(y, ())) > 0) == (r <= d)
                assert (len(observed.get(y, ())) == 1) == (r == d)
                checks += 1
    # Independently check the numerator/denominator identity for G(z,u):
    # (1-z-z*z-u*z+u*z*z) G(z,u) = 1+z-u*z.
    prev2 = [1]
    prev1 = [2]
    for m in range(2, 13):
        curr = [0] * (m + 1)
        # H_m = (1+u) H_{m-1} + (1-u) H_{m-2}
        for j, value in enumerate(prev1):
            curr[j] += value
            curr[j + 1] += value
        for j, value in enumerate(prev2):
            curr[j] += value
            curr[j + 1] -= value
        assert curr == transfer_counts(m, m)
        prev2, prev1 = prev1, curr
    for m in range(13):
        observed = defaultdict(int)
        for y in product((0, 1), repeat=m):
            k = sum(y)
            r = sum(a == b == 1 for a, b in zip(y, y[1:]))
            observed[(k, r)] += 1
        assert sum(observed.values()) == (1 << m)
        for k in range(m + 1):
            for r in range(m + 1):
                assert observed[(k, r)] == parameter_count(m, k, r)
        expected = transfer_counts(m, m)
        for r in range(m + 1):
            assert sum(v for (k, rr), v in observed.items() if rr == r) == expected[r]
    print(f"CHECKS_OK parent_count_comparisons={checks}; type_histograms=13; transfer_histograms=13")


if __name__ == "__main__":
    main()
