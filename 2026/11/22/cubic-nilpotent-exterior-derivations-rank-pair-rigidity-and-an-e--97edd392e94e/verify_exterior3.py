#!/usr/bin/env python3
"""Check the exterior-derivation Jordan formula over the prime field of characteristic three.
Uses original Leibniz action on wedge monomials and independent modular elimination.
No external dependencies.
"""
from itertools import product
from collections import Counter
from math import comb

def mm(A,B,p=3):
    h=len(A); m=len(B); w=len(B[0]); C=[[0]*w for _ in range(h)]
    for i in range(h):
        for k in range(m):
            if A[i][k]:
                aik=A[i][k]
                for j in range(w):C[i][j]=(C[i][j]+aik*B[k][j])%p
    return C

def rank(A,p=3):
    A=[list(row) for row in A]; h=len(A); w=len(A[0]); r=0
    for j in range(w):
        z=next((i for i in range(r,h) if A[i][j]%p),None)
        if z is None:continue
        A[r],A[z]=A[z],A[r]
        inv=pow(A[r][j]%p,-1,p)
        A[r]=[(v*inv)%p for v in A[r]]
        for i in range(r+1,h):
            f=A[i][j]
            if f:A[i]=[(a-f*b)%p for a,b in zip(A[i],A[r])]
        r+=1
        if r==h: break
    return r

def identity_zero(A):return all(v%3==0 for row in A for v in row)

def wedge_matrix(M):
    n=len(M); N=1<<n; D=[[0]*N for _ in range(N)]
    for I in range(N):
        elems=[j for j in range(n) if I>>j&1]
        for pos,j in enumerate(elems):
            rest=I^(1<<j)
            for a in range(n):
                v=M[a][j]%3
                if v==0 or rest>>a&1:continue
                # a at original position pos, reorder tuple to ascending
                seq=elems.copy();seq[pos]=a
                inversions=sum(seq[x]>seq[y] for x in range(len(seq)) for y in range(x+1,len(seq)))
                target=rest|(1<<a)
                D[target][I]=(D[target][I]+(-1 if inversions%2 else 1)*v)%3
    return D

def parameters(M):
    n=len(M); r1=rank(M);r2=rank(mm(M,M))
    c=r2;b=r1-2*c;a=n-2*b-3*c
    return a,b,c

def predicted(n,a,b,c):
    u=2**(a+c)*(3**b+1)//2
    v=2**(a+c)*(3**b-1)//2
    assert a>=0 and b>=0 and c>=0 and a+2*b+3*c==n
    w=(2**n-u-2*v)//3
    assert w>=0 and u+2*v+3*w==2**n
    return u,v,w

def actual(M):
    D=wedge_matrix(M); D2=mm(D,D);D3=mm(D2,D)
    N=len(D);r1=rank(D);r2=rank(D2)
    assert identity_zero(D3), 'D^3 unexpectedly nonzero'
    return N-2*r1+r2,r1-2*r2,r2

def test(n, exhaustive=False):
    variants={}; checked=0; singular=0
    for entries in (product(range(3),repeat=n*n) if exhaustive else (None,)):
        if entries is None: continue
        M=[list(entries[i*n:(i+1)*n]) for i in range(n)]
        M2=mm(M,M);M3=mm(M2,M)
        D=wedge_matrix(M); D2=mm(D,D);D3=mm(D2,D)
        assert D3==wedge_matrix(M3), 'Frobenius-restricted identity failed'
        if not identity_zero(M3):continue
        a,b,c=parameters(M)
        got=actual(M);want=predicted(n,a,b,c)
        assert got==want,(n,a,b,c,got,want)
        variants[(a,b,c)]=variants.get((a,b,c),0)+1
        checked+=1
    return checked,variants

def jordan_matrix(parts):
    n=sum(parts);M=[[0]*n for _ in range(n)]; start=0
    for s in parts:
        for j in range(s-1):M[start+j][start+j+1]=1
        start+=s
    return M

def canonical_checks(maxn=8):
    checked=0
    for n in range(1,maxn+1):
        for c in range(n//3+1):
            for b in range((n-3*c)//2+1):
                a=n-2*b-3*c
                M=jordan_matrix([1]*a+[2]*b+[3]*c)
                assert actual(M)==predicted(n,a,b,c),('canonical',n,a,b,c)
                checked+=1
    return checked

if __name__=='__main__':
    print('canonical types tested:',canonical_checks(8))
    for n in (1,2,3):
        k,variants=test(n,exhaustive=True)
        print('all cubic-zero matrices n=',n,'count=',k,'types=',sorted(variants.items()))
    print('EXTERIOR_CUBIC_JORDAN_VERIFIED')
