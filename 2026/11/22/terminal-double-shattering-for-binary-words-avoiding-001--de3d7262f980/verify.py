#!/usr/bin/env python3
"""Independent exhaustive oracle for coordinate shattering by 001-avoiding words."""
from itertools import product,combinations
from math import comb

def words(n):
    return tuple(w for w in product((0,1),repeat=n)
                 if not any(w[i:i+3]==(0,0,1) for i in range(n-2)))

def pred(S):
    return not any(i+1 in S and any(j>i+1 for j in S) for i in S)

def independent_poly(m):
    if m<=0:return [1]
    if m==1:return [1,1]
    a=[1];b=[1,1]
    for x in range(2,m+1):
        c=[0]*(max(len(b),len(a)+1))
        for j,v in enumerate(b):c[j]+=v
        for j,v in enumerate(a):c[j+1]+=v
        a,b=b,c
    return b

def formula(n):
    c=independent_poly(n)+[0]*(n+1-len(independent_poly(n)))
    for t in range(2,n+1):
        for k,v in enumerate(independent_poly(t-3)):c[k+2]+=v
    return c

ct=0
for n in range(1,13):
    W=words(n);count=[0]*(n+1)
    for k in range(n+1):
        for S in combinations(range(n),k):
            actual=len({tuple(w[j] for j in S) for w in W})==1<<k
            expect=pred(S)
            assert actual==expect,(n,S,actual,expect)
            ct+=1;count[k]+=actual
    assert count==formula(n),(n,count,formula(n))
    assert max(i for i,c in enumerate(count) if c)==n//2+1
    print(n,len(W),count,flush=True)
print('ALL_001_CHECKS_PASS',ct)
