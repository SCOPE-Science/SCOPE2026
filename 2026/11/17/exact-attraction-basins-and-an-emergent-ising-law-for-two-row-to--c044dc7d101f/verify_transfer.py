#!/usr/bin/env python3
"""Independent transfer sum and Ising correlation check using integer matrices."""
from itertools import product
from fractions import Fraction
from math import comb

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def power(A,n):
    R=[[1,0],[0,1]]
    while n:
        if n&1: R=matmul(R,A)
        A=matmul(A,A); n//=2
    return R

def trace(A): return A[0][0]+A[1][1]
T=[[3,1],[1,3]]
Z=[[1,0],[0,-1]]
for n in range(3,22):
    base=trace(power(T,n))
    assert base==4**n+2**n
    norm=base-2**(n+1)
    assert norm==4**n-2**n
    for d in range(1,n):
        numer=trace(matmul(matmul(matmul(power(T,d),Z),power(T,n-d)),Z))-2**(n+1)
        exact=2**d*4**(n-d)+4**d*2**(n-d)-2**(n+1)
        assert numer==exact
    if n<=9:
        norm2=0; corr2=[0]*n
        for word in product((0,1),repeat=n):
            k=sum(word[i]!=word[(i+1)%n] for i in range(n))
            b=3**(n-k) if k else 3**n-2**n
            norm2+=b
            for d in range(n):
                corr2[d]+=b*(1-2*word[0])*(1-2*word[d])
        assert norm2==norm
        for d in range(1,n):
            assert corr2[d]==2**d*4**(n-d)+4**d*2**(n-d)-2**(n+1)
    print('n=',n,'Z=',norm,'corr1=',str(Fraction(2*4**(n-1)+4*2**(n-1)-2**(n+1),norm)))
print('ALL_TRANSFER_CHECKS_PASS')
