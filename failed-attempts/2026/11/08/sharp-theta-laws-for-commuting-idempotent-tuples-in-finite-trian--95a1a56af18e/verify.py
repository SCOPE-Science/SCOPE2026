#!/usr/bin/env python3
"""Direct finite checks of commuting idempotents in finite incidence algebras.
Run: python verify.py
Only standard-library Python is required. Prime fields are used for direct tests.
"""
from itertools import product
from math import comb, factorial


def matmul(a,b,n,p):
    return tuple(sum(a[i*n+k]*b[k*n+j] for k in range(n))%p
                 for i in range(n) for j in range(n))


def matrices(n,p,arcs):
    indexes=[(i,j) for i in range(n) for j in range(n) if i==j or (i,j) in arcs]
    for vals in product(range(p),repeat=len(indexes)):
        z=[0]*(n*n)
        for (i,j),v in zip(indexes,vals):z[i*n+j]=v
        yield tuple(z)


def polycount(n,q,t,arcs):
    total=0
    r=1<<t
    for colors in product(range(r),repeat=n):
        d=sum(colors[i]!=colors[j] for i,j in arcs)
        total+=q**d
    return total


def exhaustive(n,q,t,arcs):
    idem=[a for a in matrices(n,q,arcs) if matmul(a,a,n,q)==a]
    assert len(idem)==polycount(n,q,1,arcs), (n,q,'single',len(idem))
    result=0
    for tup in product(idem, repeat=t):
        if all(matmul(tup[i],tup[j],n,q)==matmul(tup[j],tup[i],n,q)
               for i in range(t) for j in range(i+1,t)):
            result+=1
    formula=polycount(n,q,t,arcs)
    assert result==formula,(n,q,t,result,formula)
    print('DIRECT_OK',n,q,t,len(idem),result)


def multi_count(n,q,r):
    # independent dynamic polynomial convolution over alphabet class sizes
    # sequence weighted by pairwise differences, all arithmetic integral
    dp={(0,0):1} # (used vertices, sum of within-class pair counts)
    for _ in range(r):
        nxt={}
        for (used,same),v in dp.items():
            for k in range(n-used+1):
                key=(used+k,same+comb(k,2))
                nxt[key]=nxt.get(key,0)+v*comb(used+k,k)
        dp=nxt
    return sum(v*q**(comb(n,2)-same) for (used,same),v in dp.items() if used==n)

for n,q,t in ((1,2,3),(2,2,3),(3,2,3),(4,2,2),(3,3,2)):
    exhaustive(n,q,t,[(i,j) for i in range(n) for j in range(i+1,n)])
for n,q,t,arcs in ((3,2,2,[(0,2),(1,2)]),(4,2,2,[(0,1),(0,2),(0,3),(1,3),(2,3)])):
    exhaustive(n,q,t,arcs)
for n in range(0,8):
    for q in (2,3):
        for t in (1,2,3):
            if n<=5 or t<=2:
                r=1<<t
                a=multi_count(n,q,r)
                b=polycount(n,q,t,[(i,j) for i in range(n) for j in range(i+1,n)]) if r**n<1_000_000 else None
                if b is not None:assert a==b,(n,q,t,a,b)
                if t==1 and n<=5: print('SINGLE_COUNT',n,q,a)
print('VERIFY_OK')
