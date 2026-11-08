#!/usr/bin/env python3
"""Exact finite corroboration of a Pell-offset semigroup identity.
No finite test is asserted to establish the theorem for all indices.
"""
from math import gcd
from heapq import heappush, heappop

P=[0,1]
for n in range(2,55):
    P.append(2*P[-1]+P[-2])

def apery(a,b,c):
    d=[None]*a
    d[0]=0
    pq=[(0,0)]
    while pq:
        x,r=heappop(pq)
        if x!=d[r]:
            continue
        for s in (b,c):
            z=x+s
            rr=z%a
            if d[rr] is None or z<d[rr]:
                d[rr]=z
                heappush(pq,(z,rr))
    assert all(x is not None for x in d)
    F=max(d)-a
    g=(2*sum(d)-a*(a-1))//(2*a)
    assert (2*sum(d)-a*(a-1))%(2*a)==0
    return F,g

def in2(z,x,y):
    for j in range(z//y+1):
        if (z-j*y)%x==0:
            return ((z-j*y)//x,j)
    return None

for n in range(3,13):
    a,b,c=P[n],P[n+3],P[n+5]
    assert gcd(gcd(a,b),c)==1
    assert 5*c==2*a+29*b
    assert b==14*a+(P[n-3] if n>=3 else -1)
    if n>=5: assert c==82*a+P[n-5]
    assert gcd(a,b)==(5 if n%3==0 else 1)
    assert gcd(a,c)==(29 if n%5==0 else 1)
    assert gcd(b,c)==(2 if n%2 else 1)
    sy=(n%3==0 or n in (4,5))
    F,g=apery(a,b,c)
    assert (2*g==F+1)==sy,(n,F,g,sy)
    if n%3==0:
        assert F==a*b//5-a-b+4*c
    if n in (4,5):
        assert F==a*b-a-b
    print(f'n={n} a={a} b={b} c={c} F={F} genus={g} symmetric={sy}')
print('PELL35_EXACT_APERY_CHECK_OK tested_n=3..12')
