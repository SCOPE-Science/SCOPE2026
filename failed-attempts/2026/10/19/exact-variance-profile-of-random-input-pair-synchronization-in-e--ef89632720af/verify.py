#!/usr/bin/env python3
"""Exact reproducibility checks for the Cerny random-input pair-merging theorem."""
from fractions import Fraction as Q
from itertools import combinations


def first(n, d):
    return 4*d*n*(n-d-1)+2*d*d


def boundary_variance(n, d):
    A=4*n**5-10*n**4+8*n**3+n**2-7*n+2
    B=24*n**4-48*n**3+32*n**2-2*n-7
    num=4*d*A-2*d*d*B+8*d**3*(2*n-1)**3-8*d**4*(2*n-1)**2
    return Q(num,3)


def identity_grid():
    # Both residuals are polynomials in n,d. Their separate degrees are
    # <= 6, so zeros on this 8x8 Cartesian grid imply the identities.
    for n in range(3,11):
        for d in range(1,9):
            L=n-1-d
            assert first(n,d)==2*L+1+Q(first(n,L+1)+first(n,L),2)
            assert boundary_variance(n,d)==(
                2*L+Q(boundary_variance(n,L+1)+boundary_variance(n,L),2)
                +Q((first(n,L+1)-first(n,L))**2,4))
        assert first(n,0)==0
        assert boundary_variance(n,0)==0


def gauss(A,B):
    n=len(B)
    for k in range(n):
        r=next(i for i in range(k,n) if A[i][k])
        if k!=r:
            A[k],A[r]=A[r],A[k]
            B[k],B[r]=B[r],B[k]
        pivot=A[k][k]
        for j in range(k,n):A[k][j]/=pivot
        B[k]/=pivot
        for i in range(n):
            if i==k:continue
            mul=A[i][k]
            if not mul:continue
            for j in range(k,n):A[i][j]-=mul*A[k][j]
            B[i]-=mul*B[k]
    return B


def direct(n):
    states=list(combinations(range(n),2)); at={s:i for i,s in enumerate(states)}
    m=len(states)
    A=[[Q(int(i==j)) for j in range(m)] for i in range(m)]
    for s,i in at.items():
        for f in (lambda x:(x+1)%n, lambda x:0 if x==n-1 else x):
            t=tuple(sorted({f(s[0]),f(s[1])}))
            if len(t)==2:A[i][at[t]]-=Q(1,2)
    E=gauss([row[:] for row in A],[Q(1) for _ in states])
    M=gauss([row[:] for row in A],[2*e-1 for e in E])
    for s,i in at.items():
        lo,hi=s;d=hi-lo
        assert E[i]==first(n,d)-2*lo,('mean',n,s,E[i])
        assert M[i]-E[i]**2==boundary_variance(n,d)-2*lo,('variance',n,s)
    return m


def main():
    identity_grid()
    total=sum(direct(n) for n in range(3,9))
    print('VERIFY_OK polynomial_grid_8x8 exact_pair_markov_moments n=3..8 states='+str(total))

if __name__=='__main__':main()
