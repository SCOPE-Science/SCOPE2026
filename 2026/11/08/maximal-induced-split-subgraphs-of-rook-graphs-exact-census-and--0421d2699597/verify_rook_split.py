#!/usr/bin/env python3
"""Independent forbidden-induced-subgraph enumeration for rook-graph split sets."""
from collections import Counter
from itertools import combinations
from math import factorial

def fall(n,k):
    return factorial(n)//factorial(n-k) if n>=k else 0

def predicted(m,n):
    if m>n:m,n=n,m
    if (m,n)==(2,2): return {3:4}
    if m==n: return {2*m-1:2*m*fall(m,m-1)}
    x=Counter()
    x[n+m-1]+=m*fall(n,m-1)
    x[2*m]+=n*fall(n-1,m)
    return dict(x)

def enumerated(m,n):
    sz=m*n
    adj=[0]*sz
    for u in range(sz):
        i,j=divmod(u,n)
        adj[u]=sum(1<<v for v in range(sz) if v!=u and (v//n==i or v%n==j))
    forbidden=[[] for _ in range(sz)]
    for k in (4,5):
        for vs in combinations(range(sz),k):
            bits=sum(1<<v for v in vs)
            deg=[(adj[v]&bits).bit_count() for v in vs]
            if (k==4 and (sorted(deg)==[1,1,1,1] or sorted(deg)==[2,2,2,2])) or (k==5 and sorted(deg)==[2]*5):
                forbidden[vs[0]].append(bits)
    ok=bytearray(1<<sz);ok[0]=1
    for s in range(1,1<<sz):
        v=(s&-s).bit_length()-1
        if ok[s & (s-1)] and not any((s&f)==f for f in forbidden[v]):ok[s]=1
    counts=Counter(); tot=0
    for s in range(1,1<<sz):
        if ok[s] and all(not ok[s|(1<<v)] for v in range(sz) if not (s>>v)&1):
            counts[s.bit_count()]+=1;tot+=1
    return dict(counts),tot

cases=[(2,n) for n in range(2,10)]+[(3,n) for n in range(3,7)]+[(4,4),(4,5)]
instances=0; subsets=0
for m,n in cases:
    if m*n>20:continue
    got,total=enumerated(m,n);want=predicted(m,n)
    assert got==want,(m,n,got,want)
    instances+=1;subsets+=1<<(m*n)
    print(f'{m}x{n}: {got} ({total} maximal subsets)')
print(f'VERIFY_OK instances={instances} candidate_subsets={subsets} forbidden_induced_tests=2K2_C4_C5')
