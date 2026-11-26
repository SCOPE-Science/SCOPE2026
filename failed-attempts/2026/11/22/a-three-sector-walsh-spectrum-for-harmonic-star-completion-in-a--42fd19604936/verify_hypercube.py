#!/usr/bin/env python3
"""Exact-rational consistency checks for a Dirichlet extension on a binary cube."""
from fractions import Fraction as F
from math import comb

def solve(a, b):
    n=len(b)
    a=[[F(x) for x in row]+[F(b[i])] for i,row in enumerate(a)]
    for c in range(n):
        pivot=next((r for r in range(c,n) if a[r][c]), None)
        assert pivot is not None
        a[c],a[pivot]=a[pivot],a[c]
        x=a[c][c];a[c]=[v/x for v in a[c]]
        for r in range(c+1,n):
            y=a[r][c]
            if y:
                for k in range(c+1,n+1):a[r][k]-=y*a[c][k]
                a[r][c]=F(0)
    v=[F(0)]*n
    for c in range(n-1,-1,-1):
        v[c]=a[c][n]-sum(a[c][k]*v[k] for k in range(c+1,n))
    return v

def coefficients(d):
    if d==2:return [F(0),F(1)]
    a=[[F(0) for j in range(d-2)] for i in range(d-2)]
    b=[F(0)]*(d-2)
    for k in range(2,d):
        i=k-2;a[i][i]=F(d)
        if k==2:b[i]=F(1)
        else:a[i][i-1]=F(-(k-1))
        if k<d-1:a[i][i+1]=F(-(d-k-1))
    return [F(0),F(1)]+solve(a,b)

def direct(d):
    n=1<<d;bound=[0]+[1<<i for i in range(d)]
    inside=[x for x in range(n) if x not in bound]
    # Rational grounded Laplacian with sum-over-neighbours Dirichlet equations.
    pos={x:j for j,x in enumerate(inside)}
    m=len(inside)
    mat=[[F(d if i==j else -sum(1 for v in range(d) if (inside[i]^(1<<v))==inside[j])) for j in range(m)] for i in range(m)]
    e=[]
    for x in bound:
        rhs=[sum((z^(1<<v))==x for v in range(d)) for z in inside]
        interior=solve(mat,rhs) if m else []
        col=[F(int(y==x)) if y in bound else interior[pos[y]] for y in range(n)]
        e.append(col)
    return [[sum(e[i][x]*e[j][x] for x in range(n)) for j in range(d+1)] for i in range(d+1)]

def check(d):
    n=1<<d; c=coefficients(d)
    sig=sum(F(comb(d-2,k-1))*c[k]*c[k] for k in range(1,d))
    top=F(n-1,d)
    closed=F((1 << (d-2))*(d-1),(2**(d-1)-1)**2)*sum((F(comb(d-1,k),k) for k in range(1,d)),F(0))
    assert sig == closed, (d,sig,closed)
    exact=direct(d)
    assert exact[0][0]==1
    assert all(exact[0][i]==0 for i in range(1,d+1))
    assert all(sum(exact[i][j] for j in range(1,d+1))==top for i in range(1,d+1))
    diag=sig+(top-sig)/d
    off=(top-sig)/d
    for i in range(1,d+1):
        for j in range(1,d+1):assert exact[i][j]==(diag if i==j else off),(d,i,j,exact[i][j])
    assert (1<=sig<=top), (d,sig,top)
    if d>2: assert (1<sig<top)
    # Check each harmonic equation with explicit standard modes.
    for x in range(n):
        k=x.bit_count()
        if k in (0,1):continue
        for i in range(d-1):
            def u(z):
                zz=z.bit_count()
                return c[zz]*(int(bool(z & (1<<i)))-int(bool(z & (1<<(d-1))))) if zz<d else F(0)
            assert d*u(x)==sum(u(x^(1<<j)) for j in range(d)),(d,x,i)
    print(f'd={d}  Gram blocks exact, lambda_std={sig}, lambda_max={top}, c={c[1:]}')

if __name__=='__main__':
    for d in range(2,7):check(d)
    print('PASS: exact-rational grounded-Laplacian spectra in five cube dimensions')
