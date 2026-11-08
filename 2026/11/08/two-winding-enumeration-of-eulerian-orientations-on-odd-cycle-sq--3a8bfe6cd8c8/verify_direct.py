#!/usr/bin/env python3
"""Independent direct enumeration of Eulerian orientations of squared cycles."""
from itertools import product
from collections import Counter
from math import comb

def edges(n):
    return [(i,(i+d)%n,d) for i in range(n) for d in (1,2)]

def direct(n):
    es=edges(n)
    assert len({tuple(sorted((u,v))) for u,v,_ in es}) == 2*n
    c=Counter()
    for mask in range(1<<(2*n)):
        out=[0]*n; sh=lo=0
        for k,(u,v,d) in enumerate(es):
            if mask>>k & 1:
                out[u]+=1
                if d==1:sh+=1
                else:lo+=1
            else:out[v]+=1
        if all(q==2 for q in out):
            c[(sh,lo)]+=1
    return c

def theoretical(n):
    c=Counter({(0,0):1, (n,n):1})
    for j in range(n//2+1):
        factor=n*comb(n-j,j)//(n-j)
        c[(n-2*j,j)]+=factor
        c[(2*j,n-j)]+=factor
    return +c

for n in range(5,10):
    a=direct(n);b=theoretical(n)
    assert a==b, (n,a,b)
    print(f"n={n} edges={2*n} count={sum(a.values())} profiles={len(a)} MATCH")
print("PASS direct Eulerian-orientation enumeration and exact bivariate count for n=5..9")
