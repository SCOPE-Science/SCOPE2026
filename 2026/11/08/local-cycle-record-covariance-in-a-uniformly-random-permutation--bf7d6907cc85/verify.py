#!/usr/bin/env python3
"""Exact finite checks for cycle-count and record-position covariances.

Run: python3 verify.py
Only Python's standard library is required. All computed moments use integers
and fractions; the infinite-parameter statement is proved in RESULT.md.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import permutations
from math import comb, factorial


def cycles(p):
    n = len(p)
    used = [False] * n
    c = 0
    for a in range(n):
        if used[a]:
            continue
        c += 1
        k = a
        while not used[k]:
            used[k] = True
            k = p[k] - 1
    return c


def local_records(p):
    peak = 0
    out = []
    for x in p:
        rec = int(x > peak)
        out.append(rec)
        peak = max(peak, x)
    return out


def harmonic(m):
    return sum((Fraction(1, k) for k in range(1, m + 1)), Fraction(0))


def exact_local(n, i):
    return Fraction(i - 1, i * i * comb(n, i))


def verify():
    checks = 0
    for n in range(1, 10):
        all_p = list(permutations(range(1, n + 1)))
        total = len(all_p)
        cycle_sum = sum(cycles(p) for p in all_p)
        assert Fraction(cycle_sum, total) == harmonic(n)
        checks += 1
        mixed = [0] * n
        record_counts = [0] * n
        global_mix = 0
        for p in all_p:
            c = cycles(p)
            flags = local_records(p)
            for j, flag in enumerate(flags):
                mixed[j] += c * flag
                record_counts[j] += flag
            global_mix += c * sum(flags)
        for j in range(n):
            i = j + 1
            assert Fraction(record_counts[j], total) == Fraction(1, i)
            checks += 1
            observed = Fraction(mixed[j], total) - harmonic(n) / i
            assert observed == exact_local(n, i), (n, i, observed)
            checks += 1
        observed_global = Fraction(global_mix, total) - harmonic(n) ** 2
        assert observed_global == sum((exact_local(n, i) for i in range(1, n + 1)), Fraction(0))
        checks += 1

    # Independent confirmation of conditional completion identity, using all
    # permutations and grouping by the exposed image injection.
    for n in range(2, 7):
        for i in range(1, n + 1):
            buckets = defaultdict(lambda: [0, 0])
            for p in permutations(range(1, n + 1)):
                s, c = buckets[p[:i]]
                buckets[p[:i]] = [s + cycles(p), c + 1]
            for exposed, (sumc, count) in buckets.items():
                seen = set()
                finished = 0
                for k in range(1, i + 1):
                    if k in seen:
                        continue
                    j = k
                    chain = set()
                    while j <= i and j not in chain and j not in seen:
                        chain.add(j)
                        j = exposed[j - 1]
                    if j in chain:
                        finished += 1
                    seen |= chain
                assert Fraction(sumc, count) == finished + harmonic(n - i), (n, i, exposed)
                checks += 1
    print(f'PASS {checks} exact assertions; full permutation enumeration through n=9;')
    print('conditional extension identity checked for all prefix injections through n=6.')


if __name__ == '__main__':
    verify()
