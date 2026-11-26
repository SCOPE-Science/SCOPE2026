#!/usr/bin/env python3
"""Direct finite checks for the five-run minimal-absent-subsequence theorem.

Run: python verify.py
Only the Python standard library is needed.
"""
from collections import Counter
from itertools import product
from math import comb
from random import Random


def word(p):
    return '0' * p[0] + '1' * p[1] + '0' * p[2] + '1' * p[3] + '0' * p[4]


def proposed(p):
    a, b, c, d, e = p
    s = {
        '0' * (a + c + e + 1), '1' * (b + d + 1),
        '0' * (a + c + 1) + '1',
        '0' * (a + 1) + '1' * (d + 1),
        '1' + '0' * (c + e + 1),
        '1' * (b + 1) + '0' * (e + 1),
        '1' + '0' * (c + 1) + '1',
    }
    if b >= 2:
        s.add('10' + '1' * (d + 1))
    if d >= 2:
        s.add('1' * (b + 1) + '01')
    if c >= 2:
        s.add('0' * (a + 1) + '1' + '0' * (e + 1))
    if c >= 2 and d >= 2:
        s.add('0' * (a + 1) + '101')
    if b >= 2 and c >= 2:
        s.add('101' + '0' * (e + 1))
    if b >= 2 and c >= 2 and d >= 2:
        s.add('10101')
    return s


def all_subsequences(w):
    existing = {''}
    for c in w:
        existing.update(x + c for x in tuple(existing))
    return existing


def actual_mas(w):
    subs = all_subsequences(w)
    answer = set()
    for v in subs:
        for c in '01':
            u = v + c
            if u not in subs and all(u[:i] + u[i+1:] in subs for i in range(len(u))):
                answer.add(u)
    return answer


def expected_count(p):
    a, b, c, d, e = p
    B, C, D = int(b >= 2), int(c >= 2), int(d >= 2)
    return 7 + B + C + D + B*C + C*D + B*C*D


def expected_histogram(n):
    x = n-4
    def choose(k):
        return comb(x, k) if x >= k else 0
    return {7:choose(1), 8:3*choose(2), 9:choose(3),
            10:2*choose(3), 13:choose(4)}


def main():
    checked = 0
    for p in product(range(1, 6), repeat=5):
        expected = proposed(p)
        assert len(expected) == expected_count(p), ('duplicate templates', p)
        found = actual_mas(word(p))
        assert found == expected, (p, sorted(found - expected), sorted(expected - found))
        checked += 1

    rng = Random(20261023)
    extra = 0
    for _ in range(100):
        p = tuple(rng.randrange(1, 11) for i in range(5))
        if sum(p) > 32:
            continue
        expected = proposed(p)
        assert actual_mas(word(p)) == expected, ('random', p)
        extra += 1

    fixed = 0
    for n in range(5, 31):
        hist = Counter()
        for a in range(1, n - 3):
            for b in range(1, n - a - 2):
                for c in range(1, n - a - b - 1):
                    for d in range(1, n - a - b - c):
                        e = n - a - b - c - d
                        hist[expected_count((a,b,c,d,e))] += 1
        wanted = expected_histogram(n)
        assert all(hist[k] == wanted[k] for k in wanted), (n, hist, wanted)
        assert sum(hist.values()) == comb(n - 1, 4)
        fixed += 1
    print('VERIFY_OK complete_subsequence_frontiers=%d random_large=%d exact_length_histograms=%d' % (checked, extra, fixed))


if __name__ == '__main__':
    main()
