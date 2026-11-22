#!/usr/bin/env python3
"""Exact integer check of the three Specht-sector character identity.
The proof in the accompanying result applies to all n >= 4; these are finite checks.
"""
from itertools import permutations
from math import factorial

def cycles(p):
    n=len(p)
    seen=[False]*n
    c1=c2=0
    for i in range(n):
        if seen[i]:
            continue
        j=i;length=0
        while not seen[j]:
            seen[j]=True;length+=1;j=p[j]
        c1+=(length==1);c2+=(length==2)
    return c1,c2

def check(n):
    d=(n-1,n*(n-3)//2,(n-1)*(n-2)//2)
    rank=sum(a*a for a in d)
    h2=(((n-1)**2-1)*((n-1)**2+2))//2
    assert h2-rank == n**3-3*n*n+2*n-2
    assert rank <= factorial(n)
    norms=[0,0,0]
    total=[0,0,0]
    mixed=[[0]*3 for _ in range(3)]
    for p in permutations(range(n)):
        f,t=cycles(p)
        a=f-1
        b=f*(f-1)//2+t-f
        c=f*(f-1)//2-f+1-t
        assert a+b+c==f*(f-2)
        cs=(a,b,c)
        for i in range(3):
            total[i]+=cs[i]
            for j in range(3):mixed[i][j]+=cs[i]*cs[j]
    assert total==[0]*3
    assert mixed==[[factorial(n) if i==j else 0 for j in range(3)] for i in range(3)]
    assert [d[0],d[1],d[2]]==[n-1,n*(n-3)//2,(n-1)*(n-2)//2]
    print('n',n,'samples',factorial(n),'spherical-quadratic-dimension',h2,'rank',rank,'nullity',h2-rank,'character orthogonality PASS')

for n in range(4,9):check(n)
print('PASS')
