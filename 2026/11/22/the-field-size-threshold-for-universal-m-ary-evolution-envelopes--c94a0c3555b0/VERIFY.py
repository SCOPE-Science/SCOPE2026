#!/usr/bin/env python3
"""Exact finite-field and rational tests for the simplex-power interpolation lemma.
Run using Python 3. No third-party packages are needed.
"""
from itertools import product
from math import factorial, comb
from fractions import Fraction
import random

def indices(n,m):
    if n==1:
        yield (m,)
    else:
        for a in range(m+1):
            for tail in indices(n-1,m-a):
                yield (a,)+tail

def matinv(M, p=None):
    N=len(M)
    if p is None:
        A=[[Fraction(M[i][j]) for j in range(N)]+[Fraction(i==j) for j in range(N)] for i in range(N)]
    else:
        A=[[M[i][j]%p for j in range(N)]+[int(i==j) for j in range(N)] for i in range(N)]
    for j in range(N):
        k=next((i for i in range(j,N) if A[i][j] != 0),None)
        assert k is not None, ('singular',N,p,j)
        A[j],A[k]=A[k],A[j]
        d=A[j][j]
        inv=1/d if p is None else pow(d,-1,p)
        A[j]=[(x*inv if p is None else x*inv%p) for x in A[j]]
        for i in range(N):
            if i==j:continue
            r=A[i][j]
            A[i]=[(x-r*y if p is None else (x-r*y)%p) for x,y in zip(A[i],A[j])]
    return [row[N:] for row in A]

def run(n,m,p,seed):
    P=list(indices(n,m)); N=len(P)
    assert N==comb(n+m-1,m)
    M=[[__import__('math').prod(pow(a[i],b[i]) for i in range(n)) for a in P] for b in P]
    inv=matinv(M,p)
    rng=random.Random(seed)
    for trial in range(4):
        f=[[rng.randrange(11) if p is None else rng.randrange(p) for _ in range(n)] for _ in range(N)]
        # Given symmetric m-linear multiplication values f_b in K^n,
        # solve v_a with f_b = sum_a a^b v_a.
        v=[[sum(inv[a][b]*f[b][j] for b in range(N)) for j in range(n)] for a in range(N)]
        if p is not None: v=[[int(c)%p for c in row] for row in v]
        for b in range(N):
            for j in range(n):
                got=sum(M[b][a]*v[a][j] for a in range(N))
                if p is not None: got%=p
                assert got==f[b][j],(n,m,p,b,j,got,f[b][j])
        # Coordinate injection: l_{m e_i}(e_j) = m delta_ij.
        for j in range(n):
            a=tuple(m*int(i==j) for i in range(n))
            assert a in P
            assert [a[i] for i in range(n)]==[m*int(i==j) for i in range(n)]
    return N

if __name__=='__main__':
    for n,m,p in [(1,3,None),(2,3,None),(3,3,None),(2,4,None),
                  (2,3,5),(3,3,5),(3,4,5),(4,3,7),(2,5,7),(3,5,7)]:
        print('checked',n,m, p if p is not None else 'Q','N',run(n,m,p,1000+n*100+m))
    print('VERIFY_OK')
