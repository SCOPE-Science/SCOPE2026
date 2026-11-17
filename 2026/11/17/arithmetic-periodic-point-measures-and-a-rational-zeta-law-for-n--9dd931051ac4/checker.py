#!/usr/bin/env python3
"""Finite cross-checks for the periodic census of binary frequency shifts.

This verifies finite instances only; the accompanying mathematical proof covers
all positive integers. The generator and admissibility test use independent
representations.
"""
from itertools import product
from fractions import Fraction
from math import gcd


def allowed_circular_word(word, k):
    n = len(word)
    if word.count('1') in (0, n):
        return True
    cut = [i for i in range(n) if word[(i - 1) % n] == '1' and word[i] == '0']
    assert cut
    for a, b in zip(cut, cut[1:] + [cut[0] + n]):
        seg = ''.join(word[i % n] for i in range(a, b))
        zeros = len(seg) - len(seg.lstrip('0'))
        if zeros == 0 or seg != ('0' * zeros + '1' * (k * zeros)):
            return False
    return True


def encoded_words(k, m):
    L = k + 1
    n = L * m
    ans = set()
    for bits in product((0, 1), repeat=m):
        cuts = [i for i, v in enumerate(bits) if v]
        if not cuts:
            continue
        for phase in range(L):
            arr = ['?'] * n
            for j, a in enumerate(cuts):
                b = cuts[(j + 1) % len(cuts)] + (m if j + 1 == len(cuts) else 0)
                g = b - a
                for t in range(g):
                    arr[(phase + L * a + t) % n] = '0'
                for t in range(k * g):
                    arr[(phase + L * a + g + t) % n] = '1'
            word = ''.join(arr)
            assert '?' not in word
            assert word not in ans, (k, m, word)
            ans.add(word)
    assert len(ans) == L * (2 ** m - 1)
    return ans


def run_tests():
    tested = 0
    for k in range(1, 5):
        L = k + 1
        for n in range(1, 15):
            brute = {''.join(w) for w in product('01', repeat=n)
                     if allowed_circular_word(''.join(w), k)}
            expected = 2 + (L * (2 ** (n // L) - 1) if n % L == 0 else 0)
            assert len(brute) == expected, (k, n, len(brute), expected)
            tested += 1
        for m in range(1, 4):
            if L * m > 14:
                continue
            n = L * m
            words = encoded_words(k, m)
            brute = {''.join(w) for w in product('01', repeat=n)
                     if allowed_circular_word(''.join(w), k)}
            assert words | {'0' * n, '1' * n} == brute
            # Each invariant ensemble is translation-invariant; check [01] mass.
            p = len(brute)
            num01 = sum(w.startswith('01') for w in brute)
            assert Fraction(num01, p) == Fraction(2 ** (m - 1), p)
            tested += 1
    print('PASS', tested, 'finite parameter/length census and marker checks')

if __name__ == '__main__':
    run_tests()
