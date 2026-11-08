#!/usr/bin/env python3
"""Independent tests for the zero-gap border-correlation theorem.

Run: python3 verify_gap_border.py
No external packages are required.
"""
from itertools import combinations
from math import comb
from fractions import Fraction


def unbordered_naive(s):
    return all(s[:j] != s[-j:] for j in range(1, len(s)))


def unbordered_kmp(s):
    pi = [0] * len(s)
    for i in range(1, len(s)):
        j = pi[i - 1]
        while j and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi[-1] == 0


def predicted_cuts(g):
    pos = []
    p = 0
    for z in g:
        pos.append(p)
        p += z + 1
    cuts = set()
    for i, z in enumerate(g):
        prev = g[(i-1) % 3]
        if z < prev:
            cuts.add(pos[i])
        elif z > prev:
            cuts.add(pos[i] + 1)
    return cuts


def count_classes(n):
    k = (n - 1) // 2
    div3 = int(n % 3 == 0)
    return {0: n // 3 if div3 else 0,
            2: n * (k - div3),
            3: comb(n, 3) - n * (k - div3) - (n // 3 if div3 else 0)}


def test(max_length=29):
    total = 0
    for n in range(3, max_length+1):
        histogram = {0: 0, 2: 0, 3: 0}
        for positions in combinations(range(n), 3):
            bits = ['0'] * n
            for i in positions:
                bits[i] = '1'
            w = ''.join(bits)
            p0, p1, p2 = positions
            gaps = (p1-p0-1, p2-p1-1, n-1-p2+p0)
            predicted = {(p0+i) % n for i in predicted_cuts(gaps)}
            via_prefix = set()
            for j in range(n):
                rotation = w[j:]+w[:j]
                fast = unbordered_kmp(rotation)
                # Deliberately independently test shorter prefixes for small words.
                if n <= 17:
                    assert fast == unbordered_naive(rotation), (w, j)
                if fast:
                    via_prefix.add(j)
            assert predicted == via_prefix, (w, gaps, predicted, via_prefix)
            histogram[len(via_prefix)] += 1
            total += 1
        assert histogram == count_classes(n), (n, histogram, count_classes(n))
        denom = comb(n, 3)
        mean = Fraction(sum(k * v for k, v in histogram.items()), denom)
        second = Fraction(sum(k * k * v for k, v in histogram.items()), denom)
        k = (n - 1) // 2
        div3 = int(n % 3 == 0)
        predicted_mean = Fraction(3) - Fraction(n * k, denom)
        predicted_var = Fraction(n * (k + 2 * div3), denom) - Fraction(n * k, denom)**2
        assert mean == predicted_mean, (n, mean, predicted_mean)
        assert second - mean**2 == predicted_var, (n, second - mean**2, predicted_var)
        if n in (3, 4, 5, 6, 12, 20, max_length):
            print('n =', n, 'distribution =', histogram)
    print('DIRECT_KMP_BORDER_AND_FULL_POPULATION_OK', total)
    print('EXACT_MOMENT_FORMULAS_OK 3..' + str(max_length))


if __name__ == '__main__':
    test()
