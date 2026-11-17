#!/usr/bin/env python3
"""Exact-rational checks for half-lazy wheel Gini operator coefficients.

Python 3 standard library only. Exhaustive finite checks corroborate the
proof; unrestricted assertions rely on the accompanying analytic argument.
"""
from fractions import Fraction as F


def gini(values):
    d = {}
    for a in values:d[a] = d.get(a,0)+1
    v = list(d.items())
    return sum(abs(a-b)*ca*cb for i,(a,ca) in enumerate(v) for b,cb in v[i+1:])


def ratio(m, mask):
    """Binary rim input, hub zero, exact output/input Gini ratio."""
    x = [(mask >> i) & 1 for i in range(m)]
    k = sum(x)
    if k == 0:
        return F(0)
    t = [3*x[i] + x[(i - 1) % m] + x[(i + 1) % m] for i in range(m)]
    t.append(F(3*k, m))
    return F(gini(t), 6*k*(m + 1 - k))


def interval_ratio(m, k):
    return ratio(m, (1 << k) - 1)


def interior_formula(m, k):
    assert 3 <= k <= m - 2
    num = F(5*k*(m-k) + 8*k - 8) - F(6*k*(k+2), m)
    if 3*k > m:
        num = F(5*k*(m-k) + 8*k - 12) - F(6*k*k, m)
    return num / (6*k*(m+1-k))


def exact_stochastic_matrix(m):
    n = m+1
    P = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(m):
        P[i][i] += F(1, 2)
        P[i][(i-1)%m] += F(1, 6)
        P[i][(i+1)%m] += F(1, 6)
        P[i][m] += F(1, 6)
    P[m][m] = F(1, 2)
    for i in range(m):P[m][i] = F(1,2*m)
    colsum = [sum(P[i][j] for i in range(n)) for j in range(n)]
    v = [(1 - z)/n for z in colsum]
    Q = [[P[i][j]+v[j] for j in range(n)] for i in range(n)]
    assert all(sum(row) == 1 for row in Q)
    assert all(sum(Q[i][j] for i in range(n)) == 1 for j in range(n))
    assert all(z > 0 for row in Q for z in row)
    return P, Q


def main():
    checked = 0
    for m in range(3, 12):
        b = max(interval_ratio(m, k) for k in range(1, m+1))
        for mask in range(1, 1<<m):
            assert ratio(m, mask) <= b, (m, mask)
            checked += 1
    print('EXACT_ALL_BINARY_CUTS_MATCH_CYCLIC_INTERVAL_MAXIMA', checked)
    interior = 0
    for m in range(5, 301):
        for k in range(3, m-1):
            assert interval_ratio(m, k) == interior_formula(m, k), (m,k)
            interior += 1
    print('EXACT_INTERIOR_BLOCK_FORMULAS_PASSED', interior)
    for m in range(3, 29):
        assert max(interval_ratio(m,k) for k in range(1,m+1)) <= F(5,6), m
    assert interval_ratio(29,6) == F(10441,12528)
    assert interval_ratio(29,6) > F(5,6)
    for m in range(29, 301):
        assert interval_ratio(m,6)> F(5,6)
    print('EXACT_SHARP_FIRST_DOBRUSHIN_BENCHMARK_CROSSING_AT_29_PASSED')
    for m in range(3, 51):
        _, Q = exact_stochastic_matrix(m)
    print('EXACT_POSITIVE_BISTOCHASTIC_GAUGE_CHECKS_PASSED_3_TO_50')
    for m in range(6, 201):
        L = max(interval_ratio(m,k) for k in range(1,m+1))
        assert L < 1
        assert L <= F(5,6)+F(1,2*m)
        assert L >= F(5,6)-F(1,2*m)-F(3,m*m)
    print('EXACT_DIMENSION_ENVELOPE_AND_ASYMPTOTIC_BRACKETS_PASSED_6_TO_200')
    print('ALL_WHEEL_HALF_LAZY_GINI_EXACT_CHECKS_PASSED')

if __name__=='__main__':main()
