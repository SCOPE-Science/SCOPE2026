#!/usr/bin/env python3
"""Exact finite-field checks for conic self-Fourier restriction.

Calculations use only standard Python, modular arithmetic, and the
truncated coefficient ring F_p[t]/(t^L). They do not replace the proof.
"""
from math import comb
from itertools import permutations


def circle(p):
    return [(x,y) for x in range(p) for y in range(p)
            if (x*x + y*y) % p == 1]


def rank_mod_p(a,p):
    a=[list(row) for row in a]
    n=len(a); m=len(a[0]) if n else 0
    r=0
    for col in range(m):
        pivot=next((i for i in range(r,n) if a[i][col]%p),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=pow(a[r][col]%p,-1,p)
        a[r][col:]=[(v*inv)%p for v in a[r][col:]]
        for i in range(r+1,n):
            b=a[i][col]%p
            if b:
                for j in range(col,m):
                    a[i][j]=(a[i][j]-b*a[r][j])%p
        r+=1
        if r==n: break
    return r


def trunc_rank(p,L):
    H=circle(p); n=len(H)
    R=[[0]*(n*L) for _ in range(n*L)]
    for i,(x,y) in enumerate(H):
        for j,(u,v) in enumerate(H):
            e=(x*u+y*v)%p
            for degree in range(L):
                coefficient=comb(e,degree)%p if degree<=e else 0
                if not coefficient: continue
                for k in range(L-degree):
                    R[i*L+k+degree][j*L+k]=coefficient
    return rank_mod_p(R,p)


def trial(p):
    n=len(circle(p)); m=n//2
    pred=[0]+[j for j in range(1,m) for _ in range(2)]+[m]
    assert len(pred)==n
    # The integer matrix at t=0 consists entirely of ones.
    assert trunc_rank(p,1)==1
    for L in range(2,min(p-1,m+1)+1):
        got=trunc_rank(p,L)
        expected=sum(max(0,L-v) for v in pred)
        assert got==expected,(p,L,got,expected)
    print('PASS p=%d conic_size=%d max_smith_exp=%d smith_exponents=%s'
          %(p,n,m,','.join(map(str,pred))))


def determinant_p3():
    """Independent exact cyclotomic determinant using z*z+z+1=0."""
    h=circle(3)
    # A pair (a,b) represents a+b*z with z*z=-z-1.
    def mult(v,w):
        a,b=v; c,d=w
        return (a*c-b*d, a*d+b*c-b*d)
    def add(v,w): return (v[0]+w[0],v[1]+w[1])
    zs=((1,0),(0,1),(-1,-1))
    total=(0,0)
    for perm in permutations(range(len(h))):
        inv=sum(1 for i in range(4) for j in range(i+1,4)
                if perm[i]>perm[j])
        term=(1,0)
        for i,j in enumerate(perm):
            x,y=h[i]; u,v=h[j]
            term=mult(term,zs[(x*u+y*v)%3])
        if inv%2: term=(-term[0],-term[1])
        total=add(total,term)
    assert total==(9,0),total
    print('PASS p=3 exact_cyclotomic_determinant=9')


if __name__=='__main__':
    for prime in (3,5,7,11,13,17):
        trial(prime)
    determinant_p3()
    print('CONIC_TORUS_LOCAL_SMITH_PASS')
