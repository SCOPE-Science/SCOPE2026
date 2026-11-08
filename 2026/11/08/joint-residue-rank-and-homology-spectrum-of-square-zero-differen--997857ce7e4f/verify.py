#!/usr/bin/env python3
"""Independent exhaustive checks of rank spectra of square-zero endomorphisms.
Only standard Python 3 required. The formula implementation and the direct enumeration
are deliberately separate functions. Run: python3 verify_squarezero_local.py
"""
from collections import Counter
from itertools import product
from math import prod

def rank(A,q):
    if not A: return 0
    z=[row[:] for row in A]
    h,w=len(z),len(z[0]); t=0
    for j in range(w):
        pivot=next((i for i in range(t,h) if z[i][j]%q),None)
        if pivot is None: continue
        z[t],z[pivot]=z[pivot],z[t]
        inv=pow(z[t][j],-1,q)
        z[t]=[(v*inv)%q for v in z[t]]
        for i in range(t+1,h):
            if z[i][j]:
                c=z[i][j]
                z[i]=[(z[i][k]-c*z[t][k])%q for k in range(w)]
        t+=1
        if t==h: break
    return t

def mult(A,B,q):
    n=len(A)
    return [[sum(A[i][h]*B[h][j] for h in range(n))%q for j in range(n)] for i in range(n)]

def is_square_zero(N, Ys,q):
    n=len(N)
    if any(any(row) for row in mult(N,N,q)): return False
    for Y in Ys:
        NY=mult(N,Y,q); YN=mult(Y,N,q)
        if any((NY[i][j]+YN[i][j])%q for i in range(n) for j in range(n)): return False
    return True

def full_k_matrix(N,Ys,q):
    n=len(N);d=len(Ys)
    W=[[0 for _ in range(n*(d+1))] for _ in range(n*(d+1))]
    for k in range(d+1):
        for i in range(n):
            for j in range(n): W[k*n+i][k*n+j]=N[i][j]
    for k,Y in enumerate(Ys):
        for i in range(n):
            for j in range(n): W[(k+1)*n+i][j]=Y[i][j]
    return W

def all_mats(n,q):
    for vals in product(range(q),repeat=n*n):
        yield [list(vals[i*n:(i+1)*n]) for i in range(n)]

def count_direct(n,d,q):
    matrices=list(all_mats(n,q))
    hist=Counter(); by_residue=Counter()
    for N in matrices:
        if any(any(row) for row in mult(N,N,q)): continue
        r=rank(N,q)
        for Ys in product(matrices,repeat=d):
            if is_square_zero(N,Ys,q):
                a=rank(full_k_matrix(N,Ys,q),q)
                hist[a]+=1
                by_residue[r,a]+=1
    return hist,by_residue

def GL(n,q):
    return prod(q**n-q**i for i in range(n))

def gauss(n,k,q):
    if k<0 or k>n: return 0
    if k==0: return 1
    a=prod(q**n-q**i for i in range(k))
    b=prod(q**k-q**i for i in range(k))
    assert a%b==0
    return a//b

def prediction(n,d,q):
    out=Counter(); by_residue=Counter()
    for r in range(n//2+1):
        s=n-2*r
        residue=gauss(n,r,q)*gauss(n-r,r,q)*GL(r,q)
        for t in range(s+1):
            K=gauss(s,t,q)*gauss(d*s,t,q)*GL(t,q)
            z=residue*q**(2*d*r*(n-r))*K
            out[(d+1)*r+t]+=z
            by_residue[r,(d+1)*r+t]+=z
    return out,by_residue

def main():
    cases=((1,3,2),(2,1,2),(2,1,3),(2,2,2),(2,3,2),(3,1,2))
    for n,d,q in cases:
        observed= count_direct(n,d,q)
        expected=prediction(n,d,q)
        assert observed==expected, (n,d,q,observed,expected)
        print(f'n={n},d={d},q={q}: {dict(sorted(observed[0].items()))}')
    for n in range(1,9):
        for d in range(1,5):
            for q in (2,3,4,5):
                p, pr=prediction(n,d,q)
                assert sum(p.values())==sum(pr.values())
                assert sum(pr[r,k] for k in range((d+1)*n+1) for r in range(n//2+1))==sum(p.values())
                assert max(p)==n+(d-1)*(n//2)
    print('VERIFY_OK')
if __name__=='__main__':main()
