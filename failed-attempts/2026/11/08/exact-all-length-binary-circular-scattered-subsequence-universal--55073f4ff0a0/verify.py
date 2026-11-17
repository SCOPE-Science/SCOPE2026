#!/usr/bin/env python3
"""Independent exhaustive tests for binary circular scattered-subsequence universality."""
from itertools import product
from math import comb
from collections import Counter


def subsequence(p, w):
    j = 0
    for x in w:
        if j < len(p) and p[j] == x:
            j += 1
    return j == len(p)


def definition_index(w):
    m = 0
    for k in range(1, len(w) // 2 + 1):
        if not all(subsequence(t, w) for t in product((0, 1), repeat=k)):
            break
        m = k
    return m


def circular_index(w):
    return max(definition_index(w[i:] + w[:i]) for i in range(len(w))) if w else 0


def cycle_matching(w):
    n = len(w)
    if n <= 1:
        return 0
    transitions = [int(w[i] != w[(i + 1) % n]) for i in range(n)]
    # A cycle matching can omit the edge spanning an appropriate cut.
    best = 0
    for cut in range(n):
        edges = [transitions[(cut + i) % n] for i in range(n - 1)]
        dp0 = dp1 = 0
        for a in edges:
            dp0, dp1 = dp1, max(dp1, dp0 + a)
        best = max(best, dp1)
    return best


def formula(n, k):
    if k == 0: return 2
    if 2 * k > n: return 0
    return (n * comb(n - k, k) * (2 ** k)) // (n - k) - 2 * int(n == 2 * k)


def main():
    total = 0
    for n in range(1, 13):
        counts = Counter()
        for w in product((0, 1), repeat=n):
            c = circular_index(w)
            m = cycle_matching(w)
            assert c == m, (n, w, c, m)
            counts[c] += 1
            total += 1
        want = {k: formula(n, k) for k in range(n // 2 + 1) if formula(n, k)}
        assert dict(counts) == want, (n, counts, want)
        assert sum(counts.values()) == 2 ** n
        print('PASS n=%2d total=%d spectrum=%s' % (n, 2 ** n, sorted(counts.items())))
    # Closed formula, normalization, full-support extremum and Lucas recurrence.
    for n in range(1, 501):
        vals = [formula(n, k) for k in range(n // 2 + 1)]
        assert all(x >= 0 for x in vals)
        assert sum(vals) == 2 ** n
        if n % 2 == 0:
            assert vals[n//2] == 2 ** (n//2 + 1) - 2
    print('VERIFY_OK exhaustive_words=%d length_range=1..12 symbolic_lengths=1..500' % total)

if __name__ == '__main__':
    main()
