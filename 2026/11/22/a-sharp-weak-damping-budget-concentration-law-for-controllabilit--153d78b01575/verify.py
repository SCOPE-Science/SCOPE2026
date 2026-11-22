"""Exact finite checks of the directed-cascade controllability-volume identity.

Uses only Python's standard library. Infinite-family conclusions require the
analytic arguments in RESULT.md; these checks are independent spot checks.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial


def determinant(matrix):
    a = [list(map(F, row)) for row in matrix]
    n = len(a)
    d = F(1)
    for i in range(n):
        pivot = next((j for j in range(i, n) if a[j][i]), None)
        if pivot is None:
            return F(0)
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            d = -d
        v = a[i][i]
        d *= v
        for j in range(i+1, n):
            t = a[j][i] / v
            for k in range(i+1, n):
                a[j][k] -= t * a[i][k]
            a[j][i] = F(0)
    return d


def gramian_recurrence(mu, weights):
    """Solve AW+WA^T+e_1 e_1^T=0 by the exact triangular recurrence."""
    n = len(weights)+1
    rates = [mu+w for w in weights]+[mu]
    W = [[F(0) for j in range(n)] for i in range(n)]
    for total in range(0, 2*n-1):
        for i in range(n):
            j = total-i
            if not (0<=j<n):
                continue
            val = F(int(i==0 and j==0))
            if i>0:
                val += weights[i-1]*W[i-1][j]
            if j>0:
                val += weights[j-1]*W[i][j-1]
            W[i][j] = val/(rates[i]+rates[j])
    assert all(W[i][j]==W[j][i] for i in range(n) for j in range(n))
    return W


def closed_formula(mu, weights):
    n=len(weights)+1
    rates = [mu+w for w in weights]+[mu]
    numerator=F(1)
    denominator=F(1)
    for i,w in enumerate(weights):
        numerator *= w**(2*(n-i-1))
    for a in rates:
        for b in rates:
            denominator *= a+b
    return numerator/denominator


def check():
    checks=0
    for n in range(2, 8):
        cases = [tuple(F(k) for k in range(1,n)),
                 tuple(F(n-k) for k in range(1,n)),
                 tuple(F(1) for _ in range(n-1)),
                 tuple(F(k*k+1, 3) for k in range(1,n)),
                 tuple(F(1, k+1) for k in range(1,n))]
        for mu in (F(1),F(1,7),F(7,4)):
            for w in cases:
                W = gramian_recurrence(mu,w)
                assert determinant(W) == closed_formula(mu,w), (n,mu,w)
                checks += 1
    # Swapping an earlier and later unequal conductance has the claimed effect.
    for n in range(3,8):
        w = tuple(F(k) for k in range(1,n))
        d0 = closed_formula(F(2,3),w)
        for i in range(n-1):
            for j in range(i+1,n-1):
                perm = list(w)
                perm[i],perm[j] = perm[j],perm[i]
                d1 = closed_formula(F(2,3),perm)
                # Original positions ascend: moving greater weight earlier raises det.
                assert d1>d0
                checks += 1
    print('Exact Gramian determinant identity and ordered-rate swap: PASS')
    print('Independent exact arithmetic test cases:', checks)
    print('Equal-rate (repeated-pole) cases included.')


if __name__=='__main__':
    check()
