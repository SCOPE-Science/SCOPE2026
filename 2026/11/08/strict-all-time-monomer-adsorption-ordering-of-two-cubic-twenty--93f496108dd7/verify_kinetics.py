#!/usr/bin/env python3
"""Exact finite-time RSA comparison for two 20-vertex cubic graphs.

Run with Python 3; stdlib only. All arithmetic uses integers or Fraction.
"""
from fractions import Fraction
from math import factorial, comb
from functools import lru_cache
from pathlib import Path

N = 20
FULL = (1 << N) - 1
FAC = [factorial(k) for k in range(N + 1)]

def closed_neighborhoods(k):
    """Generalized Petersen graph GP(10,k), vertices u_i=i, v_i=10+i."""
    adj = [0] * N
    def edge(a, b):
        adj[a] |= 1 << b
        adj[b] |= 1 << a
    for i in range(10):
        edge(i, (i + 1) % 10)
        edge(i, i + 10)
        edge(i + 10, 10 + ((i + k) % 10))
    assert all(row.bit_count() == 3 for row in adj)
    return [(1 << i) | adj[i] for i in range(N)]

def exact_bernstein_means(k):
    closed = closed_neighborhoods(k)
    weighted = [0] * (1 << N)
    count = [0] * (N + 1)
    # weighted[S] = |S|! * E[number accepted among S]
    # next candidate is uniform among all vertices of S.
    for S in range(1, 1 << N):
        size = S.bit_count()
        total = FAC[size]
        bits = S
        while bits:
            bit = bits & -bits
            bits -= bit
            v = bit.bit_length() - 1
            rem = S & ~closed[v]
            total += (FAC[size - 1] // FAC[rem.bit_count()]) * weighted[rem]
        weighted[S] = total
        count[size] += total
    return [Fraction(count[j], FAC[j] * comb(N, j)) for j in range(N + 1)]

def allowed_terminal_distribution(k):
    """Terminal size generating function from the remaining-eligible-set recursion."""
    closed = closed_neighborhoods(k)
    @lru_cache(None)
    def F(S):
        if not S:
            return (Fraction(1),)
        total = [Fraction(0)] * (N + 1)
        r = S
        while r:
            bit = r & -r
            r -= bit
            v = bit.bit_length() - 1
            tail = F(S & ~closed[v])
            for i, coeff in enumerate(tail):
                total[i+1] += coeff
        return tuple(x / S.bit_count() for x in total[:-1])
    return [(i,c) for i,c in enumerate(F(FULL)) if c]

def main():
    means = {k: exact_bernstein_means(k) for k in (2,3)}
    delta = [means[3][j]-means[2][j] for j in range(N+1)]
    assert all(x == 0 for x in delta[:5])
    assert all(x > 0 for x in delta[5:])
    assert delta[5] == Fraction(1,3876)
    assert delta[20] == Fraction(2030003,3144960)
    assert comb(20,5) * delta[5] == 4
    lines = Path(__file__).with_name('bernstein_differences.tsv').read_text(encoding='utf-8').splitlines()
    assert lines[0] == 'k\tmu_Desargues_minus_mu_dodecahedron'
    assert len(lines) == N + 2
    for j, line in enumerate(lines[1:]):
       index, rational = line.split('\t')
       assert int(index) == j and Fraction(rational) == delta[j], (j, rational, delta[j])

    expected = {
       2: [(6,Fraction(1,90)), (7,Fraction(302009,336960)),(8,Fraction(31207,336960))],
       3: [(6,Fraction(1055,6912)), (7,Fraction(2152,7371)),
           (8,Fraction(81557,207360)),(10,Fraction(37763,232960))]
    }
    for k in (2,3):
       dist=allowed_terminal_distribution(k)
       assert dist == expected[k], (k, dist)
       assert sum(p for _, p in dist) == 1
       assert sum(i*p for i,p in dist) == means[k][-1]
       print('GP(10,%d) terminal distribution:' % k,[(i,str(p)) for i,p in dist])
       print('GP(10,%d) terminal mean:' % k, means[k][-1])
    p7_2 = sum(p for i,p in expected[2] if i>=7)
    p7_3 = sum(p for i,p in expected[3] if i>=7)
    p8_2 = sum(p for i,p in expected[2] if i>=8)
    p8_3 = sum(p for i,p in expected[3] if i>=8)
    assert p7_2 > p7_3 and p8_2 < p8_3
    for j, x in enumerate(delta):
       print('%2d %s' % (j, x))
    print('PASS: all 21 exact coefficients, full terminal laws, stochastic-order crossing')

if __name__ == '__main__': main()
