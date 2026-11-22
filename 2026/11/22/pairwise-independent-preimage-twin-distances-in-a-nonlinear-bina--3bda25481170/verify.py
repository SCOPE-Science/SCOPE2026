#!/usr/bin/env python3
"""Exact finite checks for the preimage-twin distance theorem; standard library only."""
import itertools
from collections import Counter


def trigger(bits, i):
    n = len(bits)
    return bits[(i-1)%n] & (1 ^ bits[(i+1)%n]) & bits[(i+2)%n]


def K(bits):
    return tuple(bits[i] ^ trigger(bits, i) for i in range(len(bits)))


def local_F(a,b,c,d,e):
    return b ^ c ^ (a & (1 ^ c) & d) ^ (b & (1 ^ d) & e)


def F(bits):
    return tuple(local_F(*(bits[(i+j)%len(bits)] for j in range(5))) for i in range(len(bits)))


def twin(bits):
    return K(tuple(1 ^ b for b in K(bits)))


def w(a,b,c):
    return 1 ^ (a & (1 ^ b) & c) ^ ((1 ^ a) & b & (1 ^ c))


def H_from_u(u):
    return sum(w(u[(i-1)%len(u)], u[(i+1)%len(u)],u[(i+2)%len(u)]) for i in range(len(u)))


def mat_mul(A,B):
    n=len(A)
    C=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if A[i][j]:
                for k in range(n):
                    C[i][k]+=A[i][j]*B[j][k]
    return C


def mat_at_z(z):
    T=[[0]*8 for _ in range(8)]
    for s in range(8):
        a=(s>>2)&1; b=(s>>1)&1; c=s&1
        for d in (0,1):
            t=(b<<2)|(c<<1)|d
            T[s][t]+=z**w(a,c,d)
    return T


def mat_trace_power(M,n):
    A=[[int(i==j) for j in range(8)] for i in range(8)]
    for _ in range(n):
        A=mat_mul(A,M)
    return sum(A[i][i] for i in range(8))


def charpoly_eval(z,t):
    p=t**4-t**2*z**2+t**2*z+t*z**3-t*z+z**4-2*z**3+z**2
    q=t**4-2*t**3*z+t**2*z**2-t**2*z-t*z**3+2*t*z**2-t*z+z**4-2*z**3+z**2
    return p*q


def det(A):
    # Fraction-free Bareiss integer determinant.
    A=[list(x) for x in A]
    n=len(A); den=1; sign=1
    for k in range(n-1):
        if A[k][k]==0:
            i=next((i for i in range(k+1,n) if A[i][k]),None)
            if i is None:return 0
            A[i],A[k]=A[k],A[i]; sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=A[i][j]*pivot-A[i][k]*A[k][j]
                assert num%den==0
                A[i][j]=num//den
            A[i][k]=0
        den=pivot
    return sign*A[n-1][n-1]


def main():
    checks=0
    for n in range(1,12):
        hist=Counter(); mean=0; second=0; joint=0
        for u in itertools.product((0,1),repeat=n):
            x=K(u); y=twin(x)
            assert K(x)==u
            assert F(x)==F(y) and x!=y
            h=sum(a!=b for a,b in zip(x,y))
            assert h==H_from_u(u)
            hist[h]+=1
            mean+=h
            second+=h*h
            if n>=7:
                d=[w(u[(i-1)%n],u[(i+1)%n],u[(i+2)%n]) for i in range(n)]
                joint+=d[0]*d[1]*d[2]
            checks+=1
        assert sum(hist.values())==2**n
        if n>=7:
            assert mean*4==3*n*2**n
            assert (16*second-9*n*n*2**n)==3*n*2**n
            assert joint*16==7*2**n
        # Matrix weighted closed-walk trace == full exact distance histogram.
        for z in (0,1,2,3):
            lhs=sum(count*z**h for h,count in hist.items())
            assert lhs==mat_trace_power(mat_at_z(z),n)
            checks+=1
    # Exact polynomial identity: both sides have z-degree and t-degree <=8,
    # so agreement on a 9 by 9 integer grid proves the identity globally.
    for z,t in itertools.product(range(9), repeat=2):
        T=mat_at_z(z)
        assert det([[(t if i==j else 0)-T[i][j] for j in range(8)] for i in range(8)])==charpoly_eval(z,t)
        checks+=1
    # Independent finite local tests certify the universal Boolean premises.
    for a,b,c in itertools.product((0,1),repeat=3):
        for i in range(3):
            totals=[0,0]
            for x in itertools.product((0,1),repeat=3):
                if x[i]==(a,b,c)[i]:totals[w(*x)]+=1
            assert totals==[1,3]
            checks+=1
    for bits in itertools.product((0,1),repeat=7):
        assert K(K(bits))==bits
        checks+=1
    for bits in itertools.product((0,1),repeat=5):
        u=K(bits)
        assert F(bits)==tuple(u[(i+1)%5]^u[(i+2)%5] for i in range(5))
        checks+=1
    print('VERIFY_OK checks=',checks,'distance_hist_n11=',dict(sorted(hist.items())))


if __name__=='__main__':
    main()
