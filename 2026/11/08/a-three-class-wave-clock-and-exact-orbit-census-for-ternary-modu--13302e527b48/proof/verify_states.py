#!/usr/bin/env python3
"""State-level cross-check independent of matrix rank code. Run: python3 verify_states.py."""
from itertools import product
from collections import Counter
import random

def graph(m,d):
    vertices=list(product(range(m),repeat=d))
    return [[j for j,v in enumerate(vertices) if sum(x!=y for x,y in zip(u,v))==1] for u in vertices]

def update(pair,neighbors):
    u,v=pair; return (tuple((sum(u[j] for j in nei)-v[i])%3 for i,nei in enumerate(neighbors)),u)

def formula(m,d):
    n=m**d; a=((m-1)**d+(m-3)**d)//2
    b=((m-1)**d-(m-3)**d)//2;c=(n-a-2*b)//3
    k1=a+b+c;k2=a+2*b+2*c
    if d%3==0: return {1:1,4:3**(2*k1)-1,12:3**(2*n)-3**(2*k1)}
    if d%3==1: return {1:3**k1,3:3**(k1+k2)-3**k1,9:3**(2*n)-3**(k1+k2)}
    return {1:1,2:3**k1-1,6:3**(k1+k2)-3**k1,18:3**(2*n)-3**(k1+k2)}

def period(start,neighbors):
    initial=start; cur=start
    for t in range(1,19):
        cur=update(cur,neighbors)
        if cur==initial:return t
    raise AssertionError('no period divides 18')

for m,d in [(3,1)]:
    adj=graph(m,d); expected=formula(m,d)
    census=Counter()
    for a in product(range(3),repeat=2*len(adj)):
        pair=(a[:len(adj)],a[len(adj):]);census[period(pair,adj)]+=1
    assert dict(census)==expected,(census,expected)
    print('PASS exhaustive states',m,d,'states',sum(census.values()),'period census',dict(sorted(census.items())))

rng=random.Random(20261105)
for m,d,samples in [(3,2,1000),(3,3,500),(6,1,1000)]:
    adj=graph(m,d); allowed=set(formula(m,d)); observed=Counter()
    for _ in range(samples):
        state=(tuple(rng.randrange(3) for i in adj),tuple(rng.randrange(3) for i in adj))
        p=period(state,adj);assert p in allowed,(m,d,p)
        observed[p]+=1
    print('PASS sampled states',m,d,'samples',samples,'observed periods',dict(sorted(observed.items())))
print('ALL DIRECT STATE TESTS PASSED')
