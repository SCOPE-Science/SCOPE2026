#!/usr/bin/env python3
"""Exact rational finite diagnostics for the two-dimensional twisted baker map.

The mathematical conclusion for all periods follows from the symbolic product
identity, not from a finite search. No external packages required.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb

def matmul(A,B):
    return ((A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]),
            (A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]))
def matvec(A,x):
    return (A[0][0]*x[0]+A[0][1]*x[1], A[1][0]*x[0]+A[1][1]*x[1])
I=((1,0),(0,1))
PL=((2,0),(0,1))
PR=((0,-2),(1,0))
q=(1,0)

def branch_step(x,s):
    P=PR if s else PL
    t=matvec(P,x)
    return (t[0]+1,t[1])

def point_and_matrix(w):
    A=I
    b=(0,0)
    for s in w:
        P=PR if s else PL
        A=matmul(P,A)
        v=matvec(P,b)
        b=(v[0]+1,v[1])
    U=Q(1-A[0][0]); V=Q(-A[0][1]); W=Q(-A[1][0]); Z=Q(1-A[1][1]); det=U*Z-V*W
    assert det!=0
    x=((Z*b[0]-V*b[1])/det,(-W*b[0]+U*b[1])/det)
    return x,A

def signsum(w):
    parity=0
    total=0
    for s in reversed(w):
        total+=1 if parity==0 else -1
        parity ^= s
    return total

def audit(N=11):
    for n in range(1,N+1):
        hist={}
        real=complex_=0
        extreme=False
        for w in product((0,1),repeat=n):
            if not any(w):continue
            x,A=point_and_matrix(w)
            xx=x
            for s in w:
                assert Q(-1)<=xx[0]<=Q(1) and Q(0)<=xx[1]<=Q(1)
                assert (xx[0]>=0)==bool(s)
                xx=branch_step(xx,s)
            assert xx==x
            t=sum(w)
            S=signsum(w)
            if t%2==0:
                real+=1
                assert A[0][1]==0 and A[1][0]==0
                assert abs(A[0][0])==2**((n+S)//2)
                assert abs(A[1][1])==2**((n-S)//2)
                assert S%2==n%2
                hist[S]=hist.get(S,0)+1
                if n>=2 and abs(S)==n-2: extreme=True
            else:
                complex_+=1
                assert A[0][0]==0 and A[1][1]==0
                assert A[0][1]*A[1][0]==-2**n
        assert real==2**(n-1)-1
        assert complex_==2**(n-1)
        for k in range(n):
            S=n-2*k
            assert hist.get(S,0)==comb(n-1,k)-(k==0)
        if n>=2:assert extreme
        print('n=%2d: real=%5d complex=%5d histogram=%s'%(n,real,complex_,sorted(hist.items())))
    print('TWISTED_BAKER_BINOMIAL_ANISOTROPY_CHECK_OK')

if __name__=='__main__':audit()
