"""Reproducibility checks for the consecutive centered-triangular semigroups.

Finite checks supplement, but do not replace, the universal proof.
No third-party dependencies.
"""
from heapq import heappush, heappop
from math import gcd

def centered(n):
    return 1 + 3*n*(n-1)//2

def frobenius_and_genus(a, b, c):
    distances = [None]*a
    distances[0] = 0
    queue = [(0,0)]
    while queue:
        d,r=heappop(queue)
        if d != distances[r]:
            continue
        for g in (b,c):
            nd=d+g
            nr=nd%a
            if distances[nr] is None or nd<distances[nr]:
                distances[nr]=nd
                heappush(queue,(nd,nr))
    assert all(x is not None for x in distances)
    return max(distances)-a, sum(distances)//a-(a-1)//2

def in_pair(z,p,q):
    return any((z-j*q)%p==0 for j in range(z//q+1))

for n in range(2,121):
    a,b,c=(centered(k) for k in (n,n+1,n+2))
    assert gcd(gcd(a,b),c)==1
    assert gcd(a,b)==(2 if n%4==2 else 1)
    assert gcd(b,c)==(2 if n%4==1 else 1)
    assert gcd(a,c)==(17 if n%17==8 else 1)
    pair_gluing=False
    for x,y,z in ((a,b,c),(a,c,b),(b,c,a)):
        d=gcd(x,y)
        if d>1 and in_pair(z,x//d,y//d):
            pair_gluing=True
    assert pair_gluing == (n in (2,8)), ('pair-check',n)
    f,g=frobenius_and_genus(a,b,c)
    assert (2*g==f+1)==(n in (2,8)), ('Apéry-check',n,f,g)
    if n==2: assert (f,g)==(25,13)
    if n==8: assert (f,g)==(2203,1102)
print('PASS: 119 indices n=2..120; exact pair gcd and gluing classifications')
print('PASS: independent Apéry shortest paths; symmetric exactly n=2 and 8')
print('PASS: Frobenius/genus (25,13) and (2203,1102)')
print('NOTE: finite tests are not a proof for all n')
