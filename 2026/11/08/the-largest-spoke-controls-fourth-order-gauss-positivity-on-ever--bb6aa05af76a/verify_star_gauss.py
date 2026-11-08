#!/usr/bin/env python3
"""Exact-rational spot checks of the weighted-star Gauss endpoint identities.

The general all-size theorem is proved algebraically in RESULT.md; these finite
checks test the two independent formula representations, not logical infinity.
Requires Python 3 and sympy.
"""
from fractions import Fraction as F
from itertools import product
from math import prod
import sympy as S


def star_matrix(weights):
    n = len(weights) + 1
    lap = S.zeros(n)
    for j, w in enumerate(weights, 1):
        lap[0, 0] += w
        lap[0, j] = lap[j, 0] = -w
        lap[j, j] = w
    return lap


def expected_entries(weights, step):
    z = [step * w for w in weights]
    den = [v*v + 6*v + 12 for v in z]
    U = 1 + sum((v*v/d for v, d in zip(z, den)), S.Rational(0))
    V = sum((v/d for v, d in zip(z, den)), S.Rational(0))
    ans = {}
    for i in range(len(z)):
        zi = z[i]
        bi = U - zi*V
        ai = (zi+3)*(U+3*V)+3*V
        ans[(0, i+1)] = 12*zi*bi/(ai*ai+3*bi*bi)
    for i in range(len(z)):
        for j in range(i+1, len(z)):
            zi,zj = z[i],z[j]
            bi = (zi+zj+6)*U+(12-zi*zj)*V
            a = (zi+3)*(zj+3)-3
            ai = a*(U+3*V)+3*(zi+zj+6)*V
            ans[(i+1,j+1)] = 12*zi*zj*bi/(ai*ai+3*bi*bi)
    return ans, U, V


def check():
    count = 0
    ensembles = [
        (F(1),F(1)), (F(1),F(2)), (F(1),F(3)),
        (F(1),F(2),F(3)), (F(2),F(3),F(4)),
        (F(1),F(1),F(1)), (F(1),F(1),F(2)),
        (F(1),F(2),F(2),F(2)), (F(2),F(3),F(3),F(4)),
        (F(3),F(3),F(3),F(3)), (F(1),F(2),F(3),F(4),F(5)),
        (F(2),F(2),F(2),F(2),F(2)),
        (F(1),F(1),F(1),F(1),F(1),F(2)),
    ]
    steps = [F(1,10),F(1,2),F(1),F(2),F(7),F(35),F(300)]
    for weights in ensembles:
        weights = tuple(map(S.Rational, weights))
        lap = star_matrix(weights)
        n = lap.rows
        eye = S.eye(n)
        wmax = max(weights)
        criterion = (n >= wmax * sum((1/w for w in weights), S.Rational(0)))
        for step in steps:
            h = S.Rational(step)
            H = h*lap
            direct = (H*H - 6*H + 12*eye)*(H*H + 6*H + 12*eye).inv()
            expected,U,V = expected_entries(weights,h)
            for (i,j), val in expected.items():
                assert direct[i,j] == val, (weights,step,i,j,direct[i,j],val)
                count += 1
            assert all(direct[i,i]>0 for i in range(n))
            assert direct * S.ones(n,1) == S.ones(n,1)
            count += n+1
            if criterion:
                assert all(direct[i,j]>0 for i in range(n) for j in range(i+1,n))
                count += 1
            # Formula: the only possible negative offdiagonal entries are
            # hub/leaf entries. If one is negative, a maximum spoke is negative.
            if any(direct[i,j]<0 for i in range(n) for j in range(i+1,n)):
                assert direct[0,1+weights.index(wmax)]<0
                count += 1
    # Independent exact check of the one-outlier boundary for all degrees.
    for m in range(2,31):
        for t in [S.Rational(1,3),S.Rational(1,2),S.Rational(3,4),
                  S.Rational(1),S.Rational(m,m-1),S.Rational(m+1,m-1)]:
            w=(S.Rational(1),)*(m-1)+(t,)
            general = max(w)*sum(1/x for x in w) <= m+1
            reduced = S.Rational(1,2)<=t<=S.Rational(m,m-1)
            assert general == reduced
            count += 1
    print('VERIFY_OK', count)

if __name__ == '__main__':
    check()
