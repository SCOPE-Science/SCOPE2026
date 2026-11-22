#!/usr/bin/env python3
"""Independent Coxeter realization through Fano lines over GF(2)^3.
Uses set-based propagation and tuple-state BFS, without external packages.
"""
from itertools import combinations
from collections import Counter, deque
import json
lines = {frozenset((a,b,a^b)) for a,b in combinations(range(1,8),2)}
assert len(lines)==7
verts = [tuple(T) for T in combinations(range(1,8),3) if frozenset(T) not in lines]
assert len(verts)==28
adj = [set() for _ in verts]
for i,j in combinations(range(len(verts)),2):
    if set(verts[i]).isdisjoint(verts[j]):
        adj[i].add(j); adj[j].add(i)
assert Counter(map(len,adj)) == {3:28}

def works(seed):
    observed = set(seed)
    for x in seed:
        observed.update(adj[x])
    # Different from first checker: one vertex forced at a time.
    while True:
        added = False
        for v in sorted(observed):
            options = adj[v] - observed
            if len(options)==1:
                observed.add(options.pop()); added=True;break
        if not added:
            return len(observed)==28

counts = {}
for k in (0,1,2,3):
    counts[k] = [T for T in combinations(range(28),k) if works(T)]
assert len(counts[0])==len(counts[1])==len(counts[2])==0
states = counts[3];assert len(states)==336
index = {T:i for i,T in enumerate(states)}
J=[set() for _ in states]; L=[set() for _ in states]
for i,S in enumerate(states):
    for x in S:
        for y in range(28):
            if y in S:continue
            T = tuple(sorted((set(S)-{x}) | {y}))
            j = index.get(T)
            if j is not None:
                J[i].add(j)
                if y in adj[x]:L[i].add(j)

def inspect(A):
    shell=Counter();ecc=Counter()
    for a in range(len(A)):
        q=deque([a]);dist={a:0}
        while q:
            x=q.popleft()
            for y in A[x]:
                if y not in dist:
                    dist[y]=dist[x]+1;q.append(y)
        ecc[max(dist.values())]+=1
        for b in range(a+1,len(A)):
            if b in dist:shell[dist[b]]+=1
    return shell,ecc
jdist,jecc=inspect(J)
assert dict(jdist)=={1:1764,2:7392,3:19740,4:22428,5:4844,6:112}
assert dict(jecc)=={5:112,6:224}
assert Counter(map(len,J))=={9:168,12:168}
assert Counter(map(len,L))=={0:168,2:168}
unseen=set(range(len(states)));components=[]
while unseen:
    x=unseen.pop();component={x};q=[x]
    while q:
        for y in L[q.pop()]:
            if y in unseen:
                unseen.remove(y);component.add(y);q.append(y)
    components.append(component)
assert Counter(map(len,components))=={1:168,6:28}
assert all(len(L[x])==2 for c in components if len(c)==6 for x in c)
matching_supports = set()
for c in components:
    if len(c)!=6: continue
    union = set().union(*(set(states[i]) for i in c))
    assert len(union)==6
    pairs = tuple((u,v) for u,v in combinations(sorted(union),2) if v in adj[u])
    assert len(pairs)==3 and set().union(*(set(e) for e in pairs))==union
    assert all(all(len(set(states[i]) & set(e))==1 for e in pairs) for i in c)
    corners = {frozenset((a,b,d)) for a in pairs[0] for b in pairs[1] for d in pairs[2]}
    missing = corners - {frozenset(states[i]) for i in c}
    assert len(missing)==2 and not set.intersection(*(set(x) for x in missing))
    matching_supports.add(pairs)
assert len(matching_supports)==28

def lengths(source):
    distances={source:0};q=deque([source])
    while q:
        x=q.popleft()
        for y in adj[x]:
            if y not in distances:
                distances[y]=distances[x]+1;q.append(y)
    return distances
D=[lengths(i) for i in range(28)]
sigs=Counter()
for i,S in enumerate(states):
    sig=tuple(sorted(D[u][v] for u,v in combinations(S,2)))
    sigs[(sig,len(L[i]))]+=1
assert sigs=={((3,3,3),0):168,((3,3,4),2):168}
result=dict(vertices=28,edges=sum(map(len,adj))//2,minimum_size=3,optimal_sets=len(states),jump_edges=sum(map(len,J))//2,
    jump_degrees={str(k):v for k,v in sorted(Counter(map(len,J)).items())},
    jump_distance_pairs={str(k):v for k,v in sorted(jdist.items())},
    jump_eccentricities={str(k):v for k,v in sorted(jecc.items())},
    slide_edges=sum(map(len,L))//2,
    slide_degrees={str(k):v for k,v in sorted(Counter(map(len,L)).items())},
    slide_components={str(k):v for k,v in sorted(Counter(map(len,components)).items())},
    slide_signature_counts={','.join(map(str,k[0]))+':'+str(k[1]):v for k,v in sorted(sigs.items())})
print('VERIFY_OK',json.dumps(result,sort_keys=True))
