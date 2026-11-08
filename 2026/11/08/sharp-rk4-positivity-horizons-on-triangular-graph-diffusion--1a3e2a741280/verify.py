"""Exact regression checks for RK4 graph-diffusion thresholds on triangular graphs.

Run: python3 verify.py. Python standard library only.
The general all-order conclusion follows from the accompanying algebraic proof,
not from this finite regression suite.
"""
from fractions import Fraction as Q
from itertools import combinations
import math


def matmul(a, b):
    n = len(a)
    out = [[Q(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if a[i][k]:
                c = a[i][k]
                for j in range(n):
                    out[i][j] += c * b[k][j]
    return out


def triangular(n):
    verts = list(combinations(range(n), 2))
    v = len(verts)
    adjacency = [[Q(int(bool(set(verts[i]) & set(verts[j])))) if i != j else Q(0)
                  for j in range(v)] for i in range(v)]
    degree = 2 * (n-2)
    lap = [[Q(degree if i == j else -adjacency[i][j]) for j in range(v)] for i in range(v)]
    return verts, adjacency, lap


def rk4_matrix(lap, h):
    v = len(lap)
    power = [[Q(int(i == j)) for j in range(v)] for i in range(v)]
    ans = [[Q(int(i == j)) for j in range(v)] for i in range(v)]
    for k in range(1, 5):
        power = matmul(power, lap)
        factor = (-h)**k / math.factorial(k)
        for i in range(v):
            for j in range(v):
                ans[i][j] += factor * power[i][j]
    return ans


def f(n, h):
    return (Q(24) - (36*n-72)*h + (28*n*n-88*n+48)*h*h
            - (15*n**3-62*n*n+68*n-24)*h**3)


def nonedge(n, h):
    return h*h * (12 + (8-12*n)*h + (7*n*n-10*n+4)*h*h) / 6


def bisect(n):
    lo, hi = 0., 1.
    while f(n, Q.from_float(hi)) > 0:
        hi *= 2
    for _ in range(70):
        mid = (lo+hi)/2
        if f(n, Q.from_float(mid)) > 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def test():
    tested_entries = 0
    for n in range(4, 9):
        vertices, a, lap = triangular(n)
        v = len(vertices)
        for i in range(v):
            assert sum(a[i]) == 2*(n-2)
            for j in range(v):
                common = sum(a[i][k]*a[k][j] for k in range(v))
                expected = 2*(n-2) if i == j else (n-2 if a[i][j] else 4)
                assert common == expected, (n,i,j,'common')
        for h in [Q(1, 9), Q(1, 4), Q(2, 5), Q(3, 5)]:
            r = rk4_matrix(lap, h)
            for i in range(v):
                assert sum(r[i]) == 1
                for j in range(v):
                    if i != j:
                        expected = h*f(n,h)/24 if a[i][j] else nonedge(n,h)
                        assert r[i][j] == expected, (n,h,i,j)
                        tested_entries += 1
                    else:
                        assert r[i][j] > 0
        root = bisect(n)
        assert f(n,Q.from_float(root-1e-7)) > 0
        assert f(n,Q.from_float(root+1e-7)) < 0
    for n in range(4,101):
        a = 15*n**3-62*n*n+68*n-24
        b = 28*n*n-88*n+48
        c = 36*n-72
        q = 209*n**4-1252*n**3+2576*n*n-2208*n+720
        assert a>0 and b>0 and c>0 and q>0
        assert 4*b*b-12*a*c == -16*q
        assert (12*n-8)**2-48*(7*n*n-10*n+4)<0
    print('VERIFY_OK', 'offdiagonal_entries',tested_entries,
          'graph_sizes',list(range(4,9)),'symbolic_coefficient_checks',97)
    for n in [4,5,6,8,10,20,100]:
        print('threshold',n,'%.12f'%bisect(n))


if __name__=='__main__':
    test()
