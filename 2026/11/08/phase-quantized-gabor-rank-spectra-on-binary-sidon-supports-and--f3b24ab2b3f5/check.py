#!/usr/bin/env python3
"""Self-contained finite checks of phase-resolved binary-Sidon Gabor lifting ranks."""
from collections import Counter
from cmath import exp, pi
from itertools import combinations
from math import comb, cos, sin, sqrt

IRRED = {1: 0b11, 2: 0b111, 3: 0b1011, 4: 0b10011}


def gf_mult(x, y, m):
    q = 1 << m
    polynomial = IRRED[m]
    out = 0
    while y:
        if y & 1:
            out ^= x
        y >>= 1
        x <<= 1
        if x & q:
            x ^= polynomial
    return out


def gf_trace(x, m):
    a = x
    t = 0
    for _ in range(m):
        t ^= a
        a = gf_mult(a, a, m)
    assert t in (0, 1)
    return t


def circle(m):
    q = 1 << m
    alpha = next(a for a in range(q) if gf_trace(a, m) == 1)
    def norm(x, y):
        return gf_mult(x, x, m) ^ gf_mult(x, y, m) ^ gf_mult(alpha, gf_mult(y, y, m), m)
    out = [x | (y << m) for x in range(q) for y in range(q) if norm(x, y) == 1]
    assert len(out) == q + 1
    differences = [x ^ y for x, y in combinations(out, 2)]
    assert 0 not in differences and len(set(differences)) == len(differences)
    return out


def direct_ambiguity_ranks(S, N, L, labels):
    """Independent summation over the entire time-frequency plane."""
    assert len(S) == len(labels)
    g = {x: exp(2j*pi*a/L) for x, a in zip(S, labels)}
    rank = 0
    zeros_by_shift = Counter()
    for shift in range(N):
        overlaps = [x for x in S if (x ^ shift) in g]
        for freq in range(N):
            val = sum(g[x].conjugate() * g[x ^ shift]
                      * (-1 if ((freq & x).bit_count() % 2) else 1) for x in overlaps)
            if abs(val) > 1e-8:
                rank += 1
            else:
                zeros_by_shift[shift] += 1
    return rank, zeros_by_shift


def predicted_rank(S, N, L, labels):
    d = __import__('math').gcd(L, 4)
    r = L // d
    populations = Counter(a % r for a in labels)
    c = sum(comb(v, 2) for v in populations.values() if v >= 2)
    C = comb(len(S), 2)
    return (N * (2 + 2*C - c) // 2, c)


def main():
    for m in range(1, 5):
        S = circle(m)
        q = 1 << m
        N = q*q
        for L, labels in ((4, [j % 4 for j in range(len(S))]),
                          (6, [j % 6 for j in range(len(S))]),
                          (101, list(range(len(S))))):
            actual, zero_counts = direct_ambiguity_ranks(S, N, L, labels)
            expected, c = predicted_rank(S, N, L, labels)
            assert actual == expected, (m,L,actual,expected,c)
            for a in range(1,N):
                if a not in {x ^ y for x, y in combinations(S,2)}:
                    assert zero_counts[a] == N
            print('q',q,'N',N,'alphabet',L,'rank',actual,'resonant_pairs',c,'OK')
        assert predicted_rank(S, N, 4, [0] * len(S))[0] == N * (4 + q*(q+1)) // 4
        assert predicted_rank(S, N, 101, list(range(len(S))))[0] == N * (2 + q*(q+1)) // 2
    print('BINARY_SIDON_PHASE_RANK_SPECTRUM_PASS')


if __name__ == '__main__':
    main()
