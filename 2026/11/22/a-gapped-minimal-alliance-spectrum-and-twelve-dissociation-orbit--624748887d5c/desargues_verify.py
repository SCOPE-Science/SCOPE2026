#!/usr/bin/env python3
"""Exhaustive independent subset recursion for maximal dissociation sets of H(5,2).
Run: python3 desargues_verify.py
"""
import itertools
from collections import Counter
from itertools import combinations

pairs=list(combinations(range(5),2))
n=20
adj=[0]*n
for a,b in enumerate(pairs):
    for c,d in enumerate(pairs):
        if not set(b) & set(d):
            adj[a] |= 1 << (10+ c)
            adj[10+c] |= 1 << a
assert all(x.bit_count()==3 for x in adj)
N=1<<n
valid=bytearray(N)
valid[0]=1
hist=Counter()
for s in range(1,N):
    b = s&(-s)
    u = b.bit_length()-1
    t = s^b
    if valid[t]:
        touched = adj[u] & t
        if touched.bit_count() <= 1:
            if not touched or (adj[touched.bit_length()-1]&t)==0:
                valid[s]=1
    if valid[s]:hist[s.bit_count()]+=1
hist[0]=1
M=[]
for s in range(N):
    if not valid[s]:continue
    missing=(N-1)^s
    if all(not valid[s | (1<<i)] for i in range(n) if (missing>>i)&1): M.append(s)
counts=Counter(s.bit_count() for s in M)
permutation_maps=[]
pair_index={frozenset(p):i for i,p in enumerate(pairs)}
for sigma in itertools.permutations(range(5)):
    trans=[pair_index[frozenset((sigma[a],sigma[b]))] for a,b in pairs]
    for flip in [0,1]:
        permutation_maps.append([trans[i%10]+10*((i//10)^flip) for i in range(20)])
assert len(permutation_maps)==240
unseen=set(M)
reps=[]
while unseen:
    s=min(unseen)
    orbit=set()
    for pi in permutation_maps:
        t=0
        for i in range(n):
            if s>>i&1:t |= 1<<pi[i]
        orbit.add(t)
    assert orbit <= unseen
    unseen-=orbit
    reps.append((s.bit_count(),len(orbit),s))
reps.sort()
print('ALL_DISSOCIATION',sorted(hist.items()))
print('MAXIMAL_DISSOCIATION',sorted(counts.items()))
print('ORBITS',len(reps),reps)
assert sum(hist.values()) == 62049
assert dict(counts) == {8:65, 9:540, 10:234, 12:5}
assert len(reps) == 12
assert Counter((k,n) for k,n,s in reps) == Counter({(8,5):1,(8,60):1,(9,60):1,(9,120):2,(9,240):1,(10,2):1,(10,12):1,(10,40):1,(10,60):1,(10,120):1,(12,5):1})
# Structural identity: five extremal sets of size twelve are both shores of all pairs in one 4-label set.
extremal={s for s in M if s.bit_count()==12}
expected=set()
for missing in range(5):
    sh=sum(1<<i for i,p in enumerate(pairs) if missing not in p)
    expected.add(sh|(sh<<10))
assert extremal==expected
# Every eleven-vertex dissociation set has a unique twelve-vertex completion.
valid11=[s for s in range(N) if valid[s] and s.bit_count()==11]
assert len(valid11)==60
assert all(sum((s & x)==s for x in extremal)==1 for s in valid11)
print('UNIQUE_EXTENSION_11_TO_12',len(valid11))
print('PASS')
