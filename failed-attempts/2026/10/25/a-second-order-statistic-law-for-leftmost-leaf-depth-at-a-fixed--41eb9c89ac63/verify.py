"""Exact checks for the conditioned leftmost-leaf depth in ordered trees.

Standard library only. Run: python3 verify.py
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import comb

checks = 0

def check(condition, note):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(note)

def binomial(n, k):
    return comb(n, k) if 0 <= k <= n and n >= 0 else 0

def dyck_paths(n):
    def rec(up, down, path):
        if up == down == n:
            yield path
            return
        if up < n:
            yield from rec(up + 1, down, path + 'U')
        if down < up:
            yield from rec(up, down + 1, path + 'D')
    yield from rec(0, 0, '')

def theoretical_count(n, k, h):
    if k == 1:
        return int(h == n)
    if 1 <= h <= n - k + 1:
        return h * binomial(n - h - 1, k - 2) * binomial(n - 1, k - 2) // (k - 1)
    return 0

# Entire uniform Dyck populations, independently enumerated to size ten.
for n in range(1, 11):
    d = Counter()
    for word in dyck_paths(n):
        peaks = word.count('UD')
        first_height = word.index('D')
        d[peaks, first_height] += 1
    for k in range(1, n + 1):
        nk = binomial(n, k) * binomial(n, k - 1) // n
        check(sum(d[k, h] for h in range(1, n + 1)) == nk,
              ('Narayana', n, k))
        for h in range(1, n + 1):
            check(d[k, h] == theoretical_count(n, k, h),
                  ('exact joint count', n, k, h))
            if k >= 2 and h <= n - k + 1:
                check(Fraction(d[k, h], nk) ==
                      Fraction(h * binomial(n - h - 1, k - 2), binomial(n, k)),
                      ('subset law', n, k, h))
        mean = sum(Fraction(h * d[k, h], nk) for h in range(1, n + 1))
        variance = sum(Fraction((h - mean) ** 2 * d[k, h], nk)
                       for h in range(1, n + 1))
        check(mean == Fraction(2 * n - k + 1, k + 1), ('mean', n, k))
        check(variance == Fraction(2 * (k - 1) * (n + 1) * (n - k),
                                   (k + 1) ** 2 * (k + 2)), ('variance', n, k))
        for h in range(1, n + 1):
            observed = Fraction(sum(d[k, j] for j in range(h, n + 1)), nk)
            predicted = Fraction(binomial(n - h, k) + h * binomial(n - h, k - 1),
                                 binomial(n, k))
            check(observed == predicted, ('tail', n, k, h))
    for k in range(1, n):
        for h in range(1, n + 1):
            old_tail = sum(d[k, j] for j in range(h, n + 1))
            new_tail = sum(d[k + 1, j] for j in range(h, n + 1))
            old_denom = binomial(n, k) * binomial(n, k - 1) // n
            new_denom = binomial(n, k + 1) * binomial(n, k) // n
            check(new_tail * old_denom <= old_tail * new_denom,
                  ('stochastic order', n, k, h))

# Independent finite-set construction, checked over a full population of k-subsets.
from itertools import combinations
for n in range(2, 11):
    for k in range(2, n + 1):
        d = Counter(subset[1] - 1 for subset in combinations(range(1, n + 1), k))
        for h in range(1, n + 1):
            check(d[h] == h * binomial(n - h - 1, k - 2),
                  ('order statistic', n, k, h))

# Exact monotone coupling: any order of revealing one additional chosen position.
for n in range(2, 8):
    for order in permutations(range(1, n + 1)):
        hs = []
        for k in range(1, n + 1):
            chosen = sorted(order[:k])
            hs.append(chosen[1] - 1 if k >= 2 else n)
        check(all(a >= b for a, b in zip(hs, hs[1:])), ('coupling', n, order))

print(f'PASS: {checks} exact assertions, no random sampling')
