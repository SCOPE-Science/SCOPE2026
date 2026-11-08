#!/usr/bin/env python3
"""Exact, standard-library checks for a cyclic-triad fourth-cumulant identity.

Run: python3 VERIFY.py. Finite checks corroborate, but do not replace,
the incidence-spectrum and moment-count proof in RESULT.md.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb

checks = 0

def require(cond, message):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(message)

def build_signed_line_graph(n):
    edges = list(combinations(range(n), 2))
    inc = []
    for u, v in edges:
        col = [0] * n
        col[u] = 1
        col[v] = -1
        inc.append(col)
    m = len(edges)
    a = [[sum(inc[i][v] * inc[j][v] for v in range(n)) if i != j else 0
          for j in range(m)] for i in range(m)]
    return a

def matrix_and_cycle_checks(n):
    a = build_signed_line_graph(n)
    m = len(a)
    d = 2 * (n - 2)
    M = n * (n - 1) * (n - 2) // 2
    require(all(sum(x != 0 for x in row) == d for row in a), f'graph degree n={n}')
    require(sum(x != 0 for row in a for x in row) == 2 * M, f'edge count n={n}')
    a2 = [[sum(a[i][k] * a[k][j] for k in range(m)) for j in range(m)] for i in range(m)]
    trace4 = sum(a2[i][j] ** 2 for i in range(m) for j in range(m))
    predicted_trace = (n - 1) * (n - 2) ** 4 + 8 * (n - 1) * (n - 2)
    require(trace4 == predicted_trace, f'spectral trace n={n}')
    s = 0
    for i, j, k, ell in combinations(range(m), 4):
        for u, v, w, z in ((i,j,k,ell),(i,j,ell,k),(i,k,j,ell)):
            s += a[u][v] * a[v][w] * a[w][z] * a[z][u]
    predicted_s = n * (n - 1) * (n - 2) * (n - 3) * (n - 7) // 8
    require(s == predicted_s, f'signed four-cycle sum n={n}')
    require(trace4 == 8*s + 2*M + 2*m*d*(d-1), f'walk identity n={n}')
    k4_Q = -2*M + 24*s
    predicted_k4_Q = n*(n-1)*(n-2)*(3*n*n-30*n+62)
    require(k4_Q == predicted_k4_Q, f'fourth cumulant n={n}')

def enumeration_checks(n):
    e = list(combinations(range(n), 2))
    edge_pos = {ij: i for i, ij in enumerate(e)}
    t = [(edge_pos[(a,b)],edge_pos[(b,c)],edge_pos[(a,c)])
         for a,b,c in combinations(range(n), 3)]
    hist = Counter()
    for mask in range(1 << len(e)):
        cycles = 0
        for ab, bc, ac in t:
            x = (mask >> ab) & 1
            y = (mask >> bc) & 1
            z = (mask >> ac) & 1
            cycles += (x == y and x != z)
        hist[cycles] += 1
    samples = 1 << len(e)
    mean = Fraction(comb(n,3),4)
    variance = Fraction(3*comb(n,3),16)
    central = lambda power: sum(Fraction(count,samples)*(c-mean)**power
                                for c,count in hist.items())
    require(sum(hist.values()) == samples, f'enumeration count n={n}')
    require(central(1) == 0, f'centering n={n}')
    require(central(2) == variance, f'variance n={n}')
    k4 = central(4) - 3 * variance**2
    prediction = Fraction(n*(n-1)*(n-2)*(3*n*n-30*n+62),256)
    require(k4 == prediction, f'exact fourth cumulant n={n}')
    print(f'n={n}: enumerated {samples} tournaments, cumulant={k4}, PASS')

if __name__ == '__main__':
    for n in range(3,10):
        matrix_and_cycle_checks(n)
    for n in range(3,7):
        enumeration_checks(n)
    for n in range(3,101):
        polynomial = 3*n*n-30*n+62
        require((polynomial < 0) == (3 <= n <= 7), f'kurtosis threshold n={n}')
    print(f'PASS: {checks} independent exact assertions')
