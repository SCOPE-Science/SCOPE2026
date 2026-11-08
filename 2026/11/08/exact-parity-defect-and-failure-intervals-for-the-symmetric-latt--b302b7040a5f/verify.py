#!/usr/bin/env python3
"""Exact small-case checks for parity-lattice box formulas.

The general mathematical arguments are in RESULT.md. Exhaustive checks here
are supplementary and not a replacement for the all-dimension proof.
"""
from fractions import Fraction as Q
from itertools import product, combinations_with_replacement
from math import prod, ceil

def rank(rows):
    if not rows: return 0
    a = [[Q(x) for x in row] for row in rows]
    nrows, ncols = len(a), len(a[0]); j = i = 0
    while i < nrows and j < ncols:
        pivot = next((k for k in range(i, nrows) if a[k][j]), None)
        if pivot is None: j += 1; continue
        a[i], a[pivot] = a[pivot], a[i]
        fac = a[i][j]
        for col in range(j, ncols): a[i][col] /= fac
        for k in range(i + 1, nrows):
            fac = a[k][j]
            if fac:
                for col in range(j, ncols): a[k][col] -= fac * a[i][col]
        i += 1; j += 1
    return i

def minima(r):
    r=sorted(r,reverse=True)
    return [min(Q(2)/r[0],Q(1)/r[1])]+[Q(1)/v for v in r[1:]]

def ell(r):
    return ceil(r)-1

def formula_count(r):
    a = [ell(x) for x in r]
    return (prod(2*x+1 for x in a) + (-1)**sum(a))//2

def count_brute(r):
    a=[ell(x) for x in r]
    return sum(sum(z)%2 ==0 for z in product(*[range(-v,v+1) for v in a]))

def bound(r):
    return prod(2*x for x in r)*prod((1-L/2 for L in minima(r)),start=Q(1))/2

def rank_minima(r):
    r=list(r);n=len(r)
    vectors=[v for v in product(range(-2,3),repeat=n) if any(v) and sum(v)%2==0]
    values=sorted({max(Q(abs(v[i]))/r[i] for i in range(n)) for v in vectors})
    out=[]; d=0
    for t in values:
        rows=[v for v in vectors if max(Q(abs(v[i]))/r[i] for i in range(n))<=t]
        k=rank(rows)
        out.extend([t]*(k-d));d=k
        if d==n:return out
    raise AssertionError('missing rank')

def check_int(m):
    r=[Q(v) for v in m];n=len(r);a=sorted(m,reverse=True)
    P=prod(2*x-1 for x in a[1:]);eta=(-1)**sum(x-1 for x in a)
    defect=(min(Q(a[0],a[1]),Q(2))-1)*P/2+Q(eta,2)
    gap=Q(formula_count(r))-bound(r)
    assert gap==defect
    assert gap<0 if a[0]==a[1] and eta==-1 else gap>=0
    assert (gap==0)==(a[0]>a[1] and a[1]==1 and a[0]%2==0)

checks=0
for n in (2,3,4):
    for m in combinations_with_replacement(range(1,5),n):
        r=[Q(v) for v in sorted(m,reverse=True)]
        assert formula_count(r)==count_brute(r)
        assert minima(r)==rank_minima(r)
        check_int(m)
        checks+=1
for n in (2,3,4):
    for r in combinations_with_replacement([Q(3,4),Q(5,4),Q(7,4),Q(9,4)],n):
        assert formula_count(r)==count_brute(r)
        assert minima(r)==rank_minima(r)
        checks+=1
for n in (2,3,4,5,6,7):
    for k in range(1,9):
        for r in (Q(k)+Q(1,2),Q(k)+Q(99,100),Q(k+1)):
            lhs=Q(formula_count([r]*n));rhs=(2*r-1)**n/2
            assert lhs==((2*k+1)**n+(-1)**(n*k))/2
            assert bound([r]*n)==rhs
            if n%2==0 or k%2==0:
                assert lhs>=rhs
            checks+=1
print('PASS',checks,'independent exact check cases for minima, parity counts, and bounds')
