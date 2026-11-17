#!/usr/bin/env python3
"""Independent exact checks of shortest Frobenius edges of hollow symmetric Monge simplices."""
from fractions import Fraction
from itertools import combinations


def pairs(n):
    return [(a, b) for a in range(1, n) for b in range(1, n - a + 1)]


def norm_sq(p, q):
    a, b = p
    c, d = q
    return (Fraction(1, a*b) + Fraction(1, c*d) - Fraction(2, max(a,c)*max(b,d))) / 2


def direct_matrix(n, p):
    a, b = p
    z = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for i in range(a):
        for j in range(n-b, n):
            z[i][j] = z[j][i] = Fraction(1, 2*a*b)
    return z


def predicted(n):
    k, r = divmod(n, 3)
    if r == 0:
        m = 2*k*k*(2*k-1)
        axes = [k]
    elif r == 1:
        m = 2*k*k*(2*k+1)
        axes = [k]
    else:
        m = 2*k*(k+1)*(2*k+1)
        axes = [k, k+1]
    nearest = set()
    for a in axes:
        b = n-a-1
        nearest.add(frozenset(((a,b),(a,b+1))))
        nearest.add(frozenset(((b,a),(b+1,a))))
    if n == 3:
        nearest.add(frozenset(((1,2),(2,1))))
    return Fraction(1, 2*m), nearest


def verify():
    checked_pairs = 0
    direct_pairs = 0
    for n in range(3, 34):
        ps = pairs(n)
        pred_val, pred_pairs = predicted(n)
        best = None
        minima = set()
        mats = {p: direct_matrix(n,p) for p in ps} if n <= 9 else {}
        for p,q in combinations(ps,2):
            d2 = norm_sq(p,q)
            checked_pairs += 1
            if mats:
                direct = sum((mats[p][i][j]-mats[q][i][j])**2 for i in range(n) for j in range(n))
                assert d2 == direct,(n,p,q,d2,direct)
                direct_pairs += 1
            if best is None or d2 < best:
                best = d2
                minima = {frozenset((p,q))}
            elif d2 == best:
                minima.add(frozenset((p,q)))
        assert best == pred_val,(n,best,pred_val)
        assert minima == pred_pairs,(n,minima,pred_pairs)
    print('MONGE_MINIMUM_VERTEX_SEPARATION_CHECKS_PASSED n_range=3..33 all_pairs=%d direct_matrices_pairs=%d'%(checked_pairs,direct_pairs))

if __name__=='__main__':
    verify()
