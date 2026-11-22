#!/usr/bin/env python3
"""Direct finite tests for the unit-distance Katetov compatibility theorem.
Run with Python 3: python VERIFY.py.  No third-party libraries required.
These finite computations check examples; the all-n proof is in RESULT.md.
"""
from itertools import product

T = ((1,1,0),(1,1,1),(0,1,1))
TI = ((0,1,-1),(1,-1,1),(-1,1,0))


def integer_matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def valid(v):
    return all(abs(a-b)<=4<=a+b
               for i,a in enumerate(v) for b in v[i+1:])


def all_types(n):
    return [v for v in product(range(1,5),repeat=n) if valid(v)]


def metric_pair(u,v):
    return int(all(abs(a-b)<=1<=a+b for a,b in zip(u,v)))


def tensor(A,u,v):
    ans=1
    for x,y in zip(u,v):
        ans*=A[x][y]
    return ans


def rank_mod(A,p):
    B=[[int(v)%p for v in row] for row in A]
    rows=len(B); cols=len(B[0]); rank=0
    for j in range(cols):
        pivot=next((i for i in range(rank,rows) if B[i][j]),None)
        if pivot is None: continue
        B[rank],B[pivot]=B[pivot],B[rank]
        inv=pow(B[rank][j],-1,p)
        for i in range(rank+1,rows):
            if not B[i][j]: continue
            fac=B[i][j]*inv%p
            B[i][j:]=[(a-fac*b)%p for a,b in zip(B[i][j:],B[rank][j:])]
        rank+=1
        if rank==rows: break
    return rank


def test(n):
    vec=all_types(n)
    expected=3**n+n*2**(n-1)
    assert len(vec)==expected
    assert len(set(vec))==len(vec)
    C=[v for v in vec if 1 not in v]
    S=[v for v in vec if 1 in v]
    assert len(C)==3**n and len(S)==n*2**(n-1)
    assert all((1 not in v and all(x>=2 for x in v)) or
               (v.count(1)==1 and 2 not in v) for v in vec)
    ordered=C+S
    M=[[metric_pair(u,v) for v in ordered] for u in ordered]
    c=len(C); s=len(S)
    A=[row[:c] for row in M[:c]]
    B=[row[c:] for row in M[c:]]
    H=[row[:c] for row in M[c:]]
    assert A==[[tensor(T,tuple(x-2 for x in u),tuple(x-2 for x in v))
               for v in C] for u in C]
    assert B==[[int(u.index(1)==v.index(1)) for v in S] for u in S]
    assert integer_matmul(T,TI)==[[int(i==j) for j in range(3)] for i in range(3)]
    assert integer_matmul(TI,T)==[[int(i==j) for j in range(3)] for i in range(3)]
    # Canonical integer Schur elimination; no floating-point arithmetic.
    Ainv=[[tensor(TI,tuple(x-2 for x in u),tuple(x-2 for x in v))
           for v in C] for u in C]
    if n<=3:
        assert integer_matmul(A,Ainv)==[[int(i==j) for j in range(c)] for i in range(c)]
    W=integer_matmul(H,Ainv)
    K=integer_matmul(W,[list(row) for row in zip(*H)])
    assert all(x==0 for row in K for x in row), ('schur',n)
    # All signed integer row/column operations are unimodular.
    for p in (2,3,5):
        got=rank_mod(M,p)
        assert got==3**n+n,(n,p,got)
    print('n=%d types=%d core=%d special=%d rank=%d nullity=%d schur_zero=yes modular_ranks=pass' %
          (n,len(vec),c,s,3**n+n,s-n))

if __name__=='__main__':
    for n in range(1,5): test(n)
    print('VERIFY_OK')
