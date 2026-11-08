#!/usr/bin/env python3
"""Independent occupancy-profile enumeration with exact binomial weights."""
from collections import Counter
from itertools import product
from math import comb, factorial

def theoretical(r,q):
    half=comb(q,q//2) if q%2==0 else 0
    F=2+half**r
    C={}
    for a in range(1,r//2+1):
        if r%2==1 and a==r//2:
            n=r*comb(r-1,a)*(2**q-2)
        else:
            n=factorial(r)//(factorial(a)*factorial(a)*factorial(r-2*a))*half**(r-2*a)
        if n:C[2*q*a]=n
    return F,C

def step(s,q):
    deg=q*(len(s)-1);total=sum(s)
    out=[]
    for occupied in s:
        twice=2*(total-occupied)
        out.append(q if twice>deg else 0 if twice<deg else occupied)
    return tuple(out)

cases=[]
for r in range(2,8):
    for q in range(2,8):
        if (q+1)**r>450000:continue
        fixed=0; activities=Counter()
        for s in product(range(q+1),repeat=r):
            y=step(s,q)
            if y!=s and step(y,q)!=s:continue
            ways=1
            for occupied in s: ways*=comb(q,occupied)
            if y==s:fixed+=ways
            else:
                changes=sum(abs(x-z) for x,z in zip(s,y))
                activities[changes]+=ways
        expected=theoretical(r,q)
        assert (fixed,dict(activities))==expected,(r,q,fixed,dict(activities),expected)
        cases.append((r,q,fixed,sum(activities.values()),dict(sorted(activities.items()))))
print('method=weighted_occupancy_profiles', 'case_count='+str(len(cases)))
for row in cases:print(*row)
print('PROFILE_ALL_PASS')
