#!/usr/bin/env python3
"""Exact verification of chamber support counts for almost-collinear plane blow-ups.
Scientific inputs are the intersection numbers of explicit curve classes.
No numerical eigenvalue tests or external dependencies are used.
"""
from collections import Counter
from math import comb


def formula(n):
    # Polynomial stored as coefficients by degree, via binomial expansion.
    out = Counter()
    for k in range(n + 1):
        out[k] += comb(n, k) * 2**k
        out[k + 1] += comb(n, k)
    for k in range(n - 1):
        for j in range(n - k + 1):
            out[1 + k + j] += comb(n, k) * comb(n - k, j)
        out[k + 2] += comb(n, k)
    return tuple(out.get(j,0) for j in range(n+2))


def inter(n):
    # Order: E_1,..,E_n,E_*, L_1,..,L_n,R.
    m=2*n+2
    A=[[0]*m for _ in range(m)]
    for i in range(m): A[i][i]=-1
    A[m-1][m-1]=-(n-1)
    for i in range(n):
        A[i][n+1+i]=A[n+1+i][i]=1
        A[n][n+1+i]=A[n+1+i][n]=1
        A[i][m-1]=A[m-1][i]=1
    return A


def bareiss_det(a):
    """Exact fraction-free integer determinant, no floats."""
    n=len(a)
    if n==0:return 1
    M=[list(row) for row in a]
    sign=1; old=1
    for k in range(n-1):
        if M[k][k]==0:
            pivot=next((i for i in range(k+1,n) if M[i][k]!=0),None)
            if pivot is None:return 0
            M[k],M[pivot]=M[pivot],M[k];sign=-sign
        pivot=M[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=M[i][j]*pivot-M[i][k]*M[k][j]
                assert num%old==0
                M[i][j]=num//old
            M[i][k]=0
        old=pivot
    return sign*M[-1][-1]


def negative_definite(A,subset):
    # Sylvester criterion applied to -A in listed index order.
    for k in range(1,len(subset)+1):
        inds=subset[:k]
        minor=[[-A[i][j] for j in inds] for i in inds]
        if bareiss_det(minor)<=0:return False
    return True


def structural(n,S):
    E=set(range(n)); extra=n; L=set(range(n+1,2*n+1)); R=2*n+1
    chosen=set(S)
    if extra in chosen and chosen&L:return False
    for i in range(n):
        if i in chosen and n+1+i in chosen:return False
    if R in chosen and len(chosen&E)>=n-1:return False
    return True


def check_n(n):
    A=inter(n)
    count=Counter();struct=Counter()
    for mask in range(1<<(2*n+2)):
        inds=[i for i in range(2*n+2) if mask>>i&1]
        good=negative_definite(A,inds)
        valid=structural(n,inds)
        assert good==valid,(n,inds,good,valid)
        if good:count[len(inds)]+=1
        if valid:struct[len(inds)]+=1
    out=tuple(count.get(i,0) for i in range(n+2))
    assert out==formula(n),(n,out,formula(n))
    assert sum(out)==2*(3**n+2**n)-3*n-2
    assert out[-1]==2**n-n
    print(f"n={n}, total={sum(out)}, support_profile={out}, exact Sylvester + structural check PASS")


def main():
    for n in (3,4,5):check_n(n)
    # Formula checks for larger n, without claim that any large enumeration is exhaustive.
    for n in (6,7,8,9,10):
        P=formula(n)
        assert sum(P)==2*(3**n+2**n)-3*n-2
        assert P[-1]==2**n-n
        print(f"n={n}, formula_coefficient_check={sum(P)} PASS")
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':main()
