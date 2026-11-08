#!/usr/bin/env python3
"""Exact finite arithmetic checks for positive-diagonal triangular shift block powers."""
from fractions import Fraction

def mul(A,B):
    z=len(A);return [[sum(A[i][k]*B[k][j] for k in range(z)) for j in range(z)] for i in range(z)]

def finite_case(N, coefficients, maxn):
    Z=Fraction(0);U=Fraction(1);T=[[Z]*(2*N) for _ in range(2*N)]
    for j in range(N-1):T[j+1][j]=U;T[N+j][N+j+1]=U
    for j,c in enumerate(coefficients):T[j][N+j]=Fraction(c)
    P=[[U if i==j else Z for j in range(2*N)] for i in range(2*N)]
    count=0
    for n in range(1,maxn+1):
        P=mul(P,T)
        H=[[Z]*N for _ in range(N)]
        for j in range(n):
            for k in range(N):
                # input column k+j, output row k+n-1-j
                m=k+j;i=k+n-1-j
                if m<N and i<N:H[i][m]+=Fraction(coefficients[k])
        b=max(sum(coefficients[m:min(N,m+n)]) for m in range(N))
        for i in range(N):
            assert P[i][N:]==H[i]
            assert sum(H[i])<=b
            count+=2
        for j in range(N):
            assert sum(H[i][j] for i in range(N))<=b
            count+=1
    for i in range(1,N):
        b_i=max(sum(coefficients[m:min(N,m+i)]) for m in range(N))
        for j in range(1,N-i):
            b_j=max(sum(coefficients[m:min(N,m+j)]) for m in range(N))
            b_ij=max(sum(coefficients[m:min(N,m+i+j)]) for m in range(N))
            assert b_ij<=b_i+b_j
            count+=1
    return count

if __name__=='__main__':
    count=0
    for N in (9,12,16):
        for kind in (0,1,2,3):
            c=[Fraction(1,1) if kind==0 else Fraction(j+1, N) if kind==1 else Fraction((j%4)+1,3) if kind==2 else Fraction(1,j+1) for j in range(N)]
            count+=finite_case(N,c,min(5,N-2))
    print('EXACT_POSITIVE_BLOCK_CHECK_OK',count)
