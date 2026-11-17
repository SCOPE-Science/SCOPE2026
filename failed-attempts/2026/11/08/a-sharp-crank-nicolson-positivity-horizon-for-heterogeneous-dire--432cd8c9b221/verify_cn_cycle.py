#!/usr/bin/env python3
"""Exact-rational consistency checks for a cyclic-generator CN positivity theorem.

Tests are finite validation, not a substitute for the proof for arbitrary n/rates.
Python 3, standard library only.
"""
from fractions import Fraction as F
import random


def elementary(v):
    e = [F(1)] + [F(0)] * len(v)
    for t in v:
        for k in range(len(v), 0, -1):
            e[k] += t * e[k - 1]
    return e


def invert(A):
    n = len(A)
    M = [[F(A[i][j]) for j in range(n)] +
         [F(int(i == j)) for j in range(n)] for i in range(n)]
    for j in range(n):
        i0 = next(i for i in range(j, n) if M[i][j])
        M[i0], M[j] = M[j], M[i0]
        q = M[j][j]
        M[j] = [x/q for x in M[j]]
        for i in range(n):
            if i != j:
                q = M[i][j]
                M[i] = [x-q*y for x, y in zip(M[i], M[j])]
    return [row[n:] for row in M]


def entries(rate, s):
    n = len(rate)
    A = [[F(int(i == j)) + (s*rate[i] if j == i else F(0)) -
          (s*rate[i] if j == (i+1) % n else F(0))
          for j in range(n)] for i in range(n)]
    R = invert(A)
    C = [[2*R[i][j]-int(i == j) for j in range(n)] for i in range(n)]
    return R, C


def polynomial_H(rate, idx):
    a = rate[idx]
    others = rate[:idx] + rate[idx+1:]
    e = elementary(others)
    return [e[k] - (a*e[k-1] if k else F(0)) for k in range(len(rate))]


def evalpoly(coef, s):
    out = F(0)
    for c in reversed(coef):
        out = out*s+c
    return out


def run():
    rng = random.Random(202611020836)
    matrices = entries_checked = threshold_checks = 0
    for n in range(3, 9):
        for repetition in range(34):
            rates = [F(rng.randint(1, 13), rng.randint(1, 11)) for _ in range(n)]
            M = max(rates)
            argmax = rates.index(M)
            P_e = elementary(rates)
            for u in [F(1, 2), F(1), F(5, 4), F(2), F(3)]:
                s = u/M
                R, C = entries(rates, s)
                Q = sum((P_e[k]*s**k for k in range(n)), F(0))
                P = F(1)
                for r in rates:
                    P *= s*r/(1+s*r)
                for i, r in enumerate(rates):
                    diag = F(1, 1+s*r)/(1-P)
                    assert R[i][i] == diag
                    assert C[i][i] == 2*diag-1
                    H = evalpoly(polynomial_H(rates, i), s)
                    assert H/Q == C[i][i]
                    assert all(R[i][j] > 0 and C[i][j] > 0 for j in range(n) if i != j)
                    assert sum(C[i]) == 1
                    entries_checked += n
                # The largest exit rate has the smallest diagonal.
                assert C[argmax][argmax] == min(C[i][i] for i in range(n))
                assert (all(v >= 0 for row in C for v in row)) == (evalpoly(polynomial_H(rates, argmax), s) >= 0)
                threshold_checks += 1
                matrices += 1
            # Elementary-symmetric Newton quotient monotonicity (exact).
            e = elementary(rates[:argmax] + rates[argmax+1:])
            ratios = [e[k]/e[k-1] for k in range(1, n)]
            assert all(ratios[k] > ratios[k+1] for k in range(len(ratios)-1))
            assert ratios[-1] < M
            assert evalpoly(polynomial_H(rates,argmax),F(1,M)) > 0
    # Uniform-case threshold root: exactly n=3 -> golden ratio.
    assert polynomial_H([F(1)]*3, 0) == [F(1),F(1),F(-1)]
    # Single near-absorbing rate gives lower sharp infimum (signs bracket s=1/M).
    for n in range(3, 11):
        for k in range(2, 8):
            rates = [F(1)] + [F(1, 10**k)] + [F(1)]*(n-2)
            H=polynomial_H(rates,0)
            assert evalpoly(H,F(1))>0
            assert evalpoly(H,F(1, 1)+F(1,10**(k//2)))<0
    print('PASS: exact inverse matrices:', matrices)
    print('PASS: exact diagonal and stochastic identities:', entries_checked)
    print('PASS: threshold equivalences:', threshold_checks)
    print('PASS: coefficient-ratio monotonicity, boundary, uniform n=3, limit-rate brackets')


if __name__ == '__main__':
    run()
