#!/usr/bin/env python3
"""Independent constructive verification of bounded-gap geodesics."""
from itertools import combinations

def good(s,n,a,b):
    k=len(s)
    return all(a<= (s[(i+1)%k]-s[i])%n <=b for i in range(k))

def feasible_lift(x,n,a,b):
    k=len(x)
    return all(a<= (x[(i+1)%k]+(n if i==k-1 else 0)-x[i])<=b for i in range(k))

def lower(v,z,n,a,b):
    v=list(v);k=len(v);steps=0
    while v!=z:
        progressed=False
        for i in range(k):
            if v[i]<=z[i]: continue
            t=v.copy();t[i]-=1
            if feasible_lift(t,n,a,b):
                v=t;steps+=1;progressed=True;break
        if not progressed:raise AssertionError(('stalled',v,z,n,a,b))
    return steps

def test_pair(u,v,n,a,b):
    k=len(u)
    for j in range(k):
        for h in (-2,-1,0,1):
            Y=[v[(i+j)%k]+n*((i+j)//k+h) for i in range(k)]
            assert feasible_lift(Y,n,a,b)
            Z=[min(ui,yi) for ui,yi in zip(u,Y)]
            assert feasible_lift(Z,n,a,b)
            m=lower(u,Z,n,a,b)+lower(Y,Z,n,a,b)
            assert m==sum(abs(ui-yi) for ui,yi in zip(u,Y))

cases=0;pairs=0
for a,b in ((1,3),(2,3),(2,4),(2,5),(3,5)):
    for k in range(2,5):
        for n in range(a*k+1,min(b*k,13)):
            S=[s for s in combinations(range(n),k) if good(s,n,a,b)]
            if not S:continue
            cases+=1
            for i,u in enumerate(S):
                for v in S[i:]:
                    test_pair(u,v,n,a,b);pairs+=1
print('PASS', 'parameter_cases',cases,'unordered_pairs',pairs,'all_cyclic_lift_checks',sum([]) if False else '4k_per_pair')
