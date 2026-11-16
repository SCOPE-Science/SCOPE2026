#!/usr/bin/env python3
"""Exact integer verification of Walsh data for binary 001-avoiding words.

Python 3, standard library only. The infinite theorem is proved separately;
these finite checks are reproducibility cross-checks, not an infinite proof.
"""
from math import gcd

def allowed(word, n):
    return all(((word >> (n-i-3)) & 7) != 1 for i in range(n-2))

def indicator(n):
    return [int(allowed(x,n)) for x in range(1<<n)]

def fwht(values):
    data=values[:]
    step=1
    while step<len(data):
        for base in range(0,len(data),2*step):
            for j in range(base,base+step):
                a,b=data[j],data[j+step]
                data[j],data[j+step]=a+b,a-b
        step*=2
    return data

def signed_dp(n, mask):
    a,b,c=1,0,0
    for i in range(n):
        sign=-1 if ((mask>>(n-1-i))&1) else 1
        a,b,c=sign*(a+b),a,b+c
    return a+b+c

def fib(m):
    a,b=0,1
    for _ in range(m):a,b=b,a+b
    return a

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

def matpow(M,n):
    p=[[int(i==j) for j in range(3)] for i in range(3)]
    for _ in range(n):p=matmul(p,M)
    return p

def rowprod(row,M):
    return [sum(row[k]*M[k][j] for k in range(3)) for j in range(3)]

A=[[1,1,0],[1,0,1],[0,0,1]]
C=[[-1,1,0],[-1,0,1],[0,0,1]]
J=[[1,0,0],[1,0,0],[0,0,0]]
I=[[int(i==j) for j in range(3)] for i in range(3)]
B=matmul(matmul(A,A),C)
assert matpow(C,3)==I
assert all(B[i][0]+B[i][1]+B[i][2]==1 for i in range(3))
assert all((matpow(A,3)[i][j]-I[i][j])%2==0 for i in range(3) for j in range(3))
for r in range(3):
    s=(1-r)%3
    row=rowprod([1,0,0],matpow(A,r))
    row=rowprod(row,J)
    row=rowprod(row,matpow(A,s))
    assert sum(row)%2==0
for length,expected in ((3,1),(4,2),(5,4)):
    row=[1,0,0]
    for j in range(length-1):row=rowprod(row,A)
    row=rowprod(row,C)
    assert sum(row)==expected,(length,row)

print('n count zeros min_nonzero gcd universal_bound')
for n in range(3,18):
    y=indicator(n)
    w=fwht(y)
    expected=(1,2,4)[n%3]
    positive=[abs(z) for z in w if z]
    gg=0
    for z in w:gg=gcd(gg,z)
    assert sum(y)==fib(n+3)-1,(n,sum(y))
    assert min(positive)==expected,(n,min(positive),expected)
    assert gg==expected,(n,gg,expected)
    assert ((w.count(0)==0) == (n%3==0)),n
    # Full independently formed signed-state sums for all short cases.
    if n<=10:
        for mask in range(1<<n):
            assert signed_dp(n,mask)==w[mask],(n,mask)
    else:
        masks=[0,(1<<n)-1,(1<<(n-1)),(1<<(n-2))]
        masks += [(i*7919+37)%(1<<n) for i in range(128)]
        for mask in masks:
            assert signed_dp(n,mask)==w[mask],(n,mask)
    assert w[(1<<n)-1]==(1 if n%3==0 else 0)
    # Explicit sharp witnesses are +^(n-1), -, followed by (+,+,-) blocks.
    base_n=3+n%3
    signs=[1]*(base_n-1)+[-1]+[1,1,-1]*((n-base_n)//3)
    mask=sum((1<<(n-1-i)) for i,t in enumerate(signs) if t==-1)
    assert w[mask]==expected,(n,mask,w[mask],expected)
    if n%3==2:
        assert all((z%4)==0 for z in w)
    print(n, sum(y), w.count(0), min(positive),gg,expected)
print('FORBIDDEN_001_SHARP_WALSH_PASS')
