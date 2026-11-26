#!/usr/bin/env python3
"""Independent exact checks for antipodal Johnson-orbit fifth-order cubature.

Uses only the Python standard library. The general theorem follows from
algebraic identities in RESULT.md, not from finite enumeration.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb


def falling(a, j):
    out = 1
    for v in range(j):
        out *= a-v
    return out


def c4_from_signs(n, k):
    z = lambda j: F(falling(k,j),falling(n,j))
    return 1-8*z(1)+24*z(2)-32*z(3)+16*z(4)


def formulas(n,k):
    c2 = F((n-2*k)**2-n,n*(n-1))
    c4 = c4_from_signs(n,k)
    a = 3-6*c2+3*c4
    b = -2+8*c2-6*c4
    expected_a = F(48*k*(k-1)*(n-k)*(n-k-1),n*(n-1)*(n-2)*(n-3))
    expected_b = F(16*k*(n-k)*(n*n+n-6*k*(n-k)),n*(n-1)*(n-2)*(n-3))
    assert a == expected_a, (n,k,'A')
    assert b == expected_b, (n,k,'B')
    return a,b


def fourth_exact(n,k,vector):
    assert len(vector)==n and sum(vector)==0
    denom=comb(n,k)
    total=0
    for ss in combinations(range(n),k):
        f=2*sum(vector[i] for i in ss)
        total+=f**4
    return F(total,denom)


def evaluate(n,k,v):
    a,b=formulas(n,k)
    p2=sum(x*x for x in v)
    p4=sum(x**4 for x in v)
    return a*p2*p2+b*p4


def pelldata(j):
    x,t=1,0
    for _ in range(j):
        x,t=2*x+3*t,x+2*t
    n=x+1
    assert (n-t)%2==0
    k=(n-t)//2
    assert x*x-3*t*t==1
    assert n*(n+1)==6*k*(n-k)
    return n,k


def main():
    checks=0
    for n in range(4,20):
        for k in range(1,n):
            formulas(n,k)
            checks+=2
    for n in range(4,11):
        for k in range(1,n//2+1):
            vectors=[(1,-1)+(0,)*(n-2), (1,1,-1,-1)+(0,)*(n-4),
                     (1,2,3,-6)+(0,)*(n-4)]
            for v in vectors:
                assert fourth_exact(n,k,v)==evaluate(n,k,v),(n,k,v)
                checks+=1
    known=((3,1),(8,2),(27,6),(98,21),(363,77))
    assert tuple(pelldata(j) for j in range(1,6))==known
    checks+=5
    for n,k in known[1:]:
        v=(1,-1)+(0,)*(n-2)
        w=(1,1,-1,-1)+(0,)*(n-4)
        for a in (v,w):
            p2=sum(x*x for x in a)
            norm_4=F(n*n,16*k*k*(n-k)*(n-k))*evaluate(n,k,a)
            spherical=F(3*p2*p2,(n-1)*(n+1))
            assert norm_4==spherical,(n,k,norm_4,spherical)
            checks+=1
    # Equivalence to Pell, checked exhaustively over a finite range
    for n in range(4,220):
        for k in range(1,n):
            if n*(n+1)==6*k*(n-k):
                x,t=n-1,n-2*k
                assert x*x-3*t*t==1
                checks+=1
    # Explicit anisotropy example at (9,2): p4 changes, so two nonidentical fourth moments.
    v=(1,-1)+(0,)*7
    w=(1,1,-1,-1)+(0,)*5
    assert F(evaluate(9,2,v),sum(x*x for x in v)**2) != F(evaluate(9,2,w),sum(x*x for x in w)**2)
    checks+=1
    print(f'PASS: {checks} exact rational identities, combinatorial moment checks and Pell tests')


if __name__=='__main__':
    main()
