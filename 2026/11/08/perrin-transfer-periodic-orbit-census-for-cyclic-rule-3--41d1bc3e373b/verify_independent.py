#!/usr/bin/env python3
"""Separate word-based checks of the recurrence, maximal independent sets,
and Moebius orbit enumeration. No code imported from the other checker.
"""
from math import gcd

def trace(M,n):
   s=len(M); T=[[int(i==j) for j in range(s)] for i in range(s)]
   for _ in range(n): T=[[sum(T[i][k]*M[k][j] for k in range(s)) for j in range(s)] for i in range(s)]
   return sum(T[i][i] for i in range(s))

def perrin(n):
    vals=[3,0,2]
    while len(vals)<=n:vals.append(vals[-2]+vals[-3])
    return vals[n]

U=[[1,1,0,0],[0,0,1,1],[1,0,0,0],[0,0,1,1]]
V=[[0,1,0,0],[0,0,1,0],[1,1,0,0],[0,0,0,0]]
for n in range(1,19):
    R=0;mis=0
    for x in range(1<<n):
        bits=[(x>>i)&1 for i in range(n)]
        if all((bits[i],bits[(i+1)%n],bits[(i+2)%n])!=(1,0,1) for i in range(n)):R+=1
        if all(bits[i] == (1-bits[(i-1)%n])*(1-bits[(i+1)%n]) for i in range(n)):mis+=1
    assert R==trace(U,n),(n,R,trace(U,n))
    assert mis==trace(V,n)==perrin(n),(n,mis,perrin(n))
    print(f'length {n:2d}: avoid101={R:6d}; maximal-independent-set={mis:4d}')

def mobius(k):
    d=2;p=0;v=1
    while d*d<=k:
        if k%d==0:
            k//=d;p+=1
            if k%d==0:return 0
            while k%d==0:k//=d
        d+=1
    return (-1)**(p+(k>1))
def phi(n,m):return trace(U,gcd(n,m//2)) if m%2==0 else perrin(gcd(n,m))
for n in range(3,20):
    total=0;orbits=[]
    for m in range(1,2*n+1):
        if 2*n%m:continue
        points=sum(mobius(m//d)*phi(n,d) for d in range(1,m+1) if m%d==0)
        assert points>=0 and points%m==0,(n,m,points)
        if points:orbits.append((m,points//m))
        total+=points
    assert total==trace(U,n),(n,total)
    print('ring',n,'orbit lengths & counts',orbits)
print('PASS: transfer recurrences (all words to length 18) and integral nonnegative complete orbit formula (rings 3..19).')
