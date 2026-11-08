#!/usr/bin/env python3
"""Independent prime-field enumeration of Clebsch line-incidence spectra."""
from itertools import combinations, product
from collections import Counter

def cubic(v,p):return (sum(x*x*x for x in v)-sum(v)**3)%p

def projective_points(p):
    for i in range(4):
        for tail in product(range(p),repeat=3-i):
            yield (0,)*i+(1,)+tail

def rref_lines(p):
    for i,j in combinations(range(4),2):
        cols=[k for k in range(4) if k not in (i,j)]
        free_a=[k for k in cols if k>i]
        free_b=[k for k in cols if k>j]
        for vv in product(range(p),repeat=len(free_a)+len(free_b)):
            a=[0]*4;b=[0]*4;a[i]=1;b[j]=1
            for k,x in zip(free_a,vv[:len(free_a)]):a[k]=x
            for k,x in zip(free_b,vv[len(free_a):]):b[k]=x
            yield i,j,tuple(a),tuple(b)

def lines_on_cubic(p):
    lines=[]
    for i,j,a,b in rref_lines(p):
        if cubic(a,p) or cubic(b,p):continue
        if cubic(tuple((a[k]+b[k])%p for k in range(4)),p):continue
        if cubic(tuple((a[k]-b[k])%p for k in range(4)),p):continue
        # Restriction of a homogeneous cubic to span(a,b) vanishes at
        # [1:0],[0:1],[1:1],[1:-1]; these are distinct when p>2.
        lines.append((i,j,a,b))
    return lines

def census(p):
    ll=lines_on_cubic(p)
    hist=Counter()
    for v in projective_points(p):
        if cubic(v,p):continue
        k=0
        for i,j,a,b in ll:
            c=v[i];d=(v[j]-c*a[j])%p
            if all((c*a[u]+d*b[u]-v[u])%p==0 for u in range(4)):k+=1
        hist[k]+=1
    return len(ll),hist

for p in (7,11,13,17,19,23):
    n,h=census(p)
    split=pow(5,(p-1)//2,p)==1
    expected=(27*p-213,105,10,p*p-20*p+99) if split else (15*p-45,15,10,p*p-10*p+21)
    actual=(h[1],h[2],h[3],h[0])
    assert n==(27 if split else 15),(p,n)
    assert actual==expected,(p,actual,expected)
    print('prime',p,'split',split,'lines',n,'N0_N1_N2_N3',h[0],h[1],h[2],h[3])
print('VERIFY_CLEBSCH_FINITE_OK fields=6')
