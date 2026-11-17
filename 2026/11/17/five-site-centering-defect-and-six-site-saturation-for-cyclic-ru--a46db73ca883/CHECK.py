#!/usr/bin/env python3
"""Exact finite certificates and explicit-window diagnostics for cyclic three-point medians.

Run with Python 3 standard library only: python CHECK.py
The all-dimension bound and witnesses are proved in RESULT.md, not inferred from the finite diagnostics.
"""
from fractions import Fraction as F
from itertools import permutations


def transpose(a):
    return [list(c) for c in zip(*a)]


def matmul(a, b):
    return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]


def is_psd_exact(matrix):
    """Exact Schur complement test for a rational symmetric PSD matrix."""
    a = [[F(v) for v in row] for row in matrix]
    while a:
        n = len(a)
        assert all(a[i][j] == a[j][i] for i in range(n) for j in range(n))
        if any(a[i][i] < 0 for i in range(n)):
            return False
        pivot = next((i for i in range(n) if a[i][i] > 0), None)
        if pivot is None:
            return all(a[i][j] == 0 for i in range(n) for j in range(n))
        inds = [i for i in range(n) if i != pivot]
        v = a[pivot][pivot]
        a = [[a[i][j]-a[i][pivot]*a[pivot][j]/v for j in inds] for i in inds]
    return True


def selector(x):
    n=len(x)
    # An output row selects the middle *value* of the cyclic 3-point window.
    return tuple(sorted((x[(i+d)%n], (i+d)%n) for d in (-1,0,1))[1][1] for i in range(n))


def centered_square(x):
    n=len(x)
    return sum((F(z)-sum(x,F(0))/n)**2 for z in x)


def check_witness(x, a, b, expected):
    n=len(x)
    assert len(set(x))==n
    s=selector(x)
    h=[F(0)]*n
    h[a]=1;h[b]=-1
    out=[h[j] for j in s]
    assert centered_square(h)>0
    ratio=centered_square(out)/centered_square(h)
    assert ratio==expected, (n,ratio,expected,s)
    return s


def check_small():
    for n in (2,3,4,5):
        patterns=set()
        count=0
        for x in permutations(range(n)):
            count+=1
            s=selector(x)
            if s in patterns:
                continue
            patterns.add(s)
            S=[[int(s[i]==j) for j in range(n)] for i in range(n)]
            C=[[n*int(i==j)-1 for j in range(n)] for i in range(n)]
            # Q=C/n.  2Q-Q S^T Q S Q PSD iff
            # 2 n^2 C - C S^T C S C PSD, with integer entries.
            T=matmul(matmul(matmul(matmul(C,transpose(S)),C),S),C)
            B=[[2*n*n*C[i][j]-T[i][j] for j in range(n)] for i in range(n)]
            assert is_psd_exact(B),('failed exact upper bound',n,s)
        assert count=={2:2,3:6,4:24,5:120}[n]
        assert len(patterns)=={2:1,3:3,4:12,5:60}[n]
        print('EXHAUSTIVE_EXACT_PSD',n,count,len(patterns))
    assert check_witness([F(1),F(0),F(2),F(3)],0,2,F(2))==(0,0,2,2)
    assert check_witness([F(0),F(3),F(4),F(1),F(2)],1,4,F(2))==(4,1,1,4,3)
    assert selector([F(0),F(2),F(3),F(1),F(4)])==(1,1,1,2,3)
    print('EXACT_UNCENTERED_5_SITE_TRIPLE_REPLICATION_PASSED')
    print('EXACT_4_AND_5_SITE_WITNESS_RATIOS_2_PASSED')


def check_large():
    for n in range(6,101):
        x=[F(z) for z in (0,2,4,1,3,5)]
        if n>=7:
            x += [F(5,2)] + [F(2)+F(1,j+1) for j in range(7,n)]
        s=check_witness(x,1,4,F(3))
        assert s[:6]==(1,1,1,4,4,4)
        assert s.count(1)==3 and s.count(4)==3
    print('EXACT_EXPLICIT_WITNESS_DIAGNOSTICS_6_TO_100_PASSED')

if __name__=='__main__':
    check_small()
    check_large()
    print('ALL_CYCLIC_MEDIAN_CENTERED_HILBERT_CHECKS_PASSED')
