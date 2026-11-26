#!/usr/bin/env python3
"""Independent finite checks for ternary adjacent-distinct subsequence-universality law.
Uses only the Python standard library; no data files are required.
"""
from collections import Counter, defaultdict
from itertools import product
from math import comb

def bound(n, k):
    if k == 0:
        return 1 if n == 0 else 3 * 2 ** (n - 1)
    if n < 3 * k:
        return 0
    return 3 * 2 ** (2 * k - 1) * sum(comb(n - 2 * k, j)
                                         for j in range(k, n - 2 * k + 1))

def closed_distribution(n):
    if n == 0:
        return {0: 1}
    return {k: bound(n, k) - bound(n, k + 1)
            for k in range(n // 3 + 1)}

def dynamic_distribution(nmax):
    d = {(a, 1 << a, 0): 1 for a in range(3)}
    for n in range(1, nmax + 1):
        c = Counter()
        for (_, _, k), weight in d.items():
            c[k] += weight
        assert dict(c) == {k: v for k, v in closed_distribution(n).items() if v}
        assert sum(c.values()) == 3 * 2 ** (n - 1)
        if n == nmax: break
        nd = defaultdict(int)
        for (a, mask, k), weight in d.items():
            for b in range(3):
                if b == a: continue
                m = mask | (1 << b)
                if m == 7:
                    nd[(b, 0, k + 1)] += weight
                else:
                    nd[(b, m, k)] += weight
        d = nd

def direct_universality(w):
    def subsequence(x):
        j = 0
        for c in w:
            if c == x[j]:
                j += 1
                if j == len(x): return True
        return False
    best = 0
    for k in range(1, len(w) // 3 + 1):
        if all(subsequence(x) for x in product(range(3), repeat=k)):
            best = k
        else: break
    return best

def direct_enumeration(nmax):
    for n in range(1, nmax + 1):
        obs = Counter()
        for first in range(3):
            for choices in product((0, 1), repeat=n - 1):
                w = [first]
                for x in choices:
                    w.append([v for v in range(3) if v != w[-1]][x])
                obs[direct_universality(w)] += 1
        assert dict(obs) == {k: v for k, v in closed_distribution(n).items() if v}, (n, obs)

if __name__ == '__main__':
    dynamic_distribution(80)
    direct_enumeration(11)
    assert closed_distribution(8) == {0: 6, 1: 114, 2: 264}
    print('TERNARY_NO_REPEAT_UNIVERSALITY_PASS dynamic_n=1..80 direct_spectra_n=1..11')
