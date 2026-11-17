#!/usr/bin/env python3
"""Finite independent numerical checks for a sharp circumradius union bound.

The general theorem has a separate analytic proof; finite tests are not a proof.
Standard-library Python only.
"""
from itertools import combinations
from math import sqrt, isclose
import random


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def difference(a,b):
    return tuple(x-y for x,y in zip(a,b))


def solve(A,b):
    """Solve nonsingular square linear system; None for dependent rows."""
    n=len(b)
    M=[list(map(float,row))+[float(z)] for row,z in zip(A,b)]
    for j in range(n):
        i=max(range(j,n),key=lambda h:abs(M[h][j]))
        if abs(M[i][j])<1e-10:return None
        M[i],M[j]=M[j],M[i]
        s=M[j][j]
        for l in range(j,n+1):M[j][l]/=s
        for k in range(n):
            if k!=j:
                z=M[k][j]
                for l in range(j,n+1):M[k][l]-=z*M[j][l]
    return tuple(M[i][-1] for i in range(n))


def radius(points):
    """Find smallest enclosing ball via all affine-independent support sets."""
    if not points:return 0.0
    d=len(points[0]); best=float('inf')
    for k in range(1,min(len(points),d+1)+1):
        for subset in combinations(points,k):
            base=subset[0]
            edges=[difference(x,base) for x in subset[1:]]
            if edges:
                G=[[dot(e,f) for f in edges] for e in edges]
                t=solve(G,[dot(e,e)/2 for e in edges])
                if t is None:continue
                c=tuple(base[j]+sum(t[i]*edges[i][j] for i in range(k-1)) for j in range(d))
            else:c=base
            R=sqrt(dot(difference(c,base),difference(c,base)))
            if R>=best:continue
            if all(dot(difference(x,c),difference(x,c))<=R*R+1e-8 for x in points):best=R
    if best==float('inf'):raise AssertionError('No support ball found')
    return best


def check(A,B):
    C=list(set(A).intersection(B))
    assert C
    ra,rb,rc,ru=radius(A),radius(B),radius(C),radius(list(set(A).union(B)))
    s=(ra+rb)/2
    upper=s+sqrt(max(0.0,s*s-rc*rc))
    factor=(1+sqrt(2))/2
    assert ru<=upper+1e-7,(ra,rb,rc,ru,upper)
    assert ru+rc<=factor*(ra+rb)+1e-7,(ra,rb,rc,ru)
    return ra,rb,rc,ru


def main():
    b=1+sqrt(2)
    C=[(-1.,0.),(1.,0.)]
    A=C+[(0.,b)]
    B=C+[(0.,-b)]
    ra,rb,rc,ru=check(A,B)
    assert isclose(ra,sqrt(2),abs_tol=1e-10)
    assert isclose(rb,sqrt(2),abs_tol=1e-10)
    assert isclose(rc,1.,abs_tol=1e-10)
    assert isclose(ru,b,abs_tol=1e-10)
    assert isclose((ru+rc)/(ra+rb),(1+sqrt(2))/2,abs_tol=1e-10)
    # The example from Bryant--Tupper, 2026, Example 15, is below the optimum.
    C=[(-1.,0.),(1.,0.)]
    ra,rb,rc,ru=check(C+[(0.,2.)],C+[(0.,-2.)])
    assert isclose((ru+rc)/(ra+rb),1.2,abs_tol=1e-10)
    rng=random.Random(20261110)
    count=0
    for d in (2,3,4):
        for rep in range(35):
            n=5 if d==4 else 6
            points=[tuple(rng.uniform(-3,3) for _ in range(d)) for _ in range(n)]
            for trial in range(20):
                a=rng.randrange(1,1<<n)
                b=rng.randrange(1,1<<n)
                if a&b==0:continue
                A=[points[i] for i in range(n) if (a>>i)&1]
                B=[points[i] for i in range(n) if (b>>i)&1]
                check(A,B)
                count+=1
    print('PASS: numerical equality witness and published-example comparison;')
    print('PASS:',count,'random finite-set comparisons in dimensions 2, 3, 4.')
    print('Scope: numerical tests support but cannot certify the universal inequality.')


if __name__=='__main__':main()
