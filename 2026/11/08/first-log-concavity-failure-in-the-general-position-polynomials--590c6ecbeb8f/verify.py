#!/usr/bin/env python3
"""Exact independent checks for triangular-graph GP log-concavity cutoff.
Run: python3 verify.py. No third-party packages, internet, or input files.
"""
from math import comb, factorial
from fractions import Fraction
from itertools import combinations

LIMIT = 30

def via_components(limit):
    # Distinguish the component containing original vertex 0.
    A = [[1]]
    for n in range(1, limit + 1):
        p = [0] * (max(n, comb(n, 2)) + 1)
        def add(a, shift, factor):
            for k, v in enumerate(a):
                p[k + shift] += factor * v
        add(A[n - 1], 0, 1)  # isolated original vertex
        if n >= 2:
            add(A[n - 2], 1, n - 1)  # isolated edge
        for s in range(3, n + 1):
            add(A[n - s], s - 1, comb(n - 1, s - 1) * s)  # star of order s
        if n >= 3:
            add(A[n - 3], 3, comb(n - 1, 2))  # triangle
        A.append(p)
    return A

def via_exponential_formula(limit):
    # Independent power-series computation of
    # n!*[t^n] exp(t^3/6) B(t)^d/d!, B(t)=t exp(t)-t^2/2.
    B = [Fraction(0) for _ in range(limit + 1)]
    B[1] = Fraction(1)
    B[2] = Fraction(1, 2)
    for k in range(3, limit + 1):
        B[k] = Fraction(1, factorial(k - 1))
    E = [Fraction(0) for _ in range(limit + 1)]
    for k in range(limit // 3 + 1):
        E[3*k] = Fraction(1, 6**k * factorial(k))
    P = [Fraction(0) for _ in range(limit + 1)]
    P[0] = Fraction(1)
    rows = [[0] * (max(n, comb(n, 2)) + 1) for n in range(limit + 1)]
    for d in range(limit + 1):
        conv = [Fraction(0) for _ in range(limit + 1)]
        for i, p in enumerate(P):
            if p:
                for j in range(limit - i + 1):
                    if E[j]: conv[i+j] += p * E[j]
        for n in range(d, limit + 1):
            value = factorial(n) * conv[n] / factorial(d)
            assert value.denominator == 1, (n, d, value)
            rows[n][n-d] = int(value)
        if d < limit:
            nextP = [Fraction(0) for _ in range(limit + 1)]
            for i, p in enumerate(P):
                if p:
                    for j in range(1, limit-i+1):
                        if B[j]: nextP[i+j] += p*B[j]
            P = nextP
    return rows

def brute_force_gp(n):
    edges = list(combinations(range(n), 2))
    N = len(edges)
    adjacent = [[bool(set(edges[i]) & set(edges[j])) for j in range(N)] for i in range(N)]
    forbidden = []
    for a,b,c in combinations(range(N), 3):
        pair_count = adjacent[a][b]+adjacent[a][c]+adjacent[b][c]
        if pair_count == 2:
            forbidden.append((1<<a)|(1<<b)|(1<<c))
    count = [0]*(N+1)
    for mask in range(1<<N):
        if not any(mask & tri == tri for tri in forbidden):
            count[mask.bit_count()] += 1
    return count

def run():
    a = via_components(LIMIT)
    b = via_exponential_formula(LIMIT)
    for n in range(LIMIT + 1):
        assert a[n] == b[n], ('independent recurrence/EGF mismatch',n)
    subsets = 0
    for n in range(3, 7):
        assert a[n] == brute_force_gp(n), ('direct subsets disagree',n)
        subsets += 1 << comb(n,2)
    for n in range(3, 30):
        p = a[n]
        assert all(p[k]*p[k] >= p[k-1]*p[k+1] for k in range(1,len(p)-1)), ('early failure',n)
    p = a[30]
    bad = [k for k in range(1,len(p)-1) if p[k]*p[k] < p[k-1]*p[k+1]]
    assert bad == [29], ('unexpected failure list',bad)
    assert p[28] == 4575989857607826108600
    assert p[29] == 73770312933671827650
    assert p[30] == 1208883745669600000
    deficit = p[28]*p[30]-p[29]*p[29]
    assert deficit == 89780688879179441682809722027255477500
    print('VERIFY_OK n=3..30 two_independent_exact_algorithms=PASS '
          f'bruteforce_n3..6=PASS subsets={subsets} earliest_failure_n=30 '
          'only_bad_index=29 log_concavity_witness=PASS')
    print('a28=',p[28], 'a29=',p[29], 'a30=',p[30], 'deficit=',deficit)
if __name__ == '__main__': run()
