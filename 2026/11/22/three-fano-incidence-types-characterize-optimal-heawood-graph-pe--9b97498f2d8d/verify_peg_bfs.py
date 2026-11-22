#!/usr/bin/env python3
"""Independent forward-search certificate for the 4- and 5-peg Heawood classifications."""
from itertools import combinations
from collections import Counter

N=14
allmask=(1<<N)-1
edges=[]
for p in range(1,8):
    for l in range(1,8):
        # Dot product in F2, the Fano-plane incidence relation.
        dot=((p&1)*(l&1))^(((p>>1)&1)*((l>>1)&1))^(((p>>2)&1)*((l>>2)&1))
        if dot==0:edges.append((p-1,l+6))
adj=[0]*N
for u,v in edges:
    adj[u]|=1<<v
    adj[v]|=1<<u

def forward_reach(initial):
    todo=[initial]
    seen={initial}
    reached=0
    while todo:
        s=todo.pop()
        reached |= s
        for b in range(N):
            if not s>>b&1:continue
            sources=adj[b]&s
            targets=adj[b]&~s
            while sources:
                a=(sources&-sources).bit_length()-1
                sources &= sources-1
                t=targets
                while t:
                    c=(t&-t).bit_length()-1
                    t &= t-1
                    q=s^(1<<a)^(1<<b)^(1<<c)
                    if q not in seen:
                        seen.add(q)
                        todo.append(q)
    return reached

good4=set()
for t in combinations(range(N),4):
    m=sum(1<<v for v in t)
    if forward_reach(m)==allmask:good4.add(m)
assert len(good4)==336
mgood5=set()
for t in combinations(range(N),5):
    m=sum(1<<v for v in t)
    if forward_reach(m)!=allmask:continue
    if all(m^(1<<v) not in good4 for v in t):mgood5.add(m)
assert len(mgood5)==434
print('forward BFS four universal =',len(good4), 'five inclusion-minimal universal =',len(mgood5))
print('PASS')
