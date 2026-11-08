#!/usr/bin/env python3
"""Exact matching enumeration and two-edge reconfiguration for Q4.
Vertices are four-bit integers 0..15. Uses vertex-first recursive search.
"""
from collections import Counter, defaultdict, deque
import json

DIM=4
N=1<<DIM
EDGES={(min(u,u^(1<<j)),max(u,u^(1<<j))) for u in range(N) for j in range(DIM)}
EDGES=tuple(sorted(EDGES))
assert len(EDGES)==32
ADJ=[tuple(u^(1<<j) for j in range(DIM)) for u in range(N)]
solutions=defaultdict(list)

def enumerate_from_remaining(available,unmatched,edges):
    if available==0:
        if all(not((unmatched>>u)&1 and (unmatched>>v)&1) for u,v in EDGES):
            solutions[len(edges)].append(frozenset(edges))
        return
    u=(available&-available).bit_length()-1
    rest=available^(1<<u)
    enumerate_from_remaining(rest,unmatched|(1<<u),edges)
    for v in ADJ[u]:
        if (rest>>v)&1:
            enumerate_from_remaining(rest^(1<<v),unmatched,edges+((min(u,v),max(u,v)),))

enumerate_from_remaining((1<<N)-1,0,tuple())
counts={k:len(v) for k,v in solutions.items()}
assert counts=={6:192,7:1536,8:272},counts
M=solutions[6]
assert len(set(M))==192

# The exchange arity is |M\N|: replace at most t matching edges simultaneously.
neighbors={t:[set() for _ in M] for t in (1,2)}
for i in range(len(M)):
    for j in range(i+1,len(M)):
        replaced=len(M[i]-M[j])
        for t in (1,2):
            if replaced<=t:
                neighbors[t][i].add(j);neighbors[t][j].add(i)

assert sum(map(len,neighbors[1]))==0
assert sum(map(len,neighbors[2]))//2==528
assert Counter(map(len,neighbors[2]))=={5:96,6:96}

ecc=[]
for root in range(len(M)):
    dist={root:0};q=deque([root])
    while q:
        u=q.popleft()
        for v in neighbors[2][u]:
            if v not in dist:
                dist[v]=dist[u]+1;q.append(v)
    assert len(dist)==192
    ecc.append(max(dist.values()))
assert Counter(ecc)=={5:96,6:96}

print(json.dumps({
    "graph":"Q4", "edge_count":len(EDGES),
    "maximal_matching_spectrum":{str(k):counts[k] for k in sorted(counts)},
    "minimum_maximal_matching_size":6,
    "minimum_maximal_matching_count":len(M),
    "one_edge_exchange_edges":0,
    "two_edge_exchange_edges":528,
    "two_edge_exchange_components":1,
    "two_edge_degree_spectrum":dict(sorted(Counter(map(len,neighbors[2])).items())),
    "two_edge_radius":min(ecc),"two_edge_diameter":max(ecc),
    "two_edge_eccentricity_spectrum":dict(sorted(Counter(ecc).items()))
},sort_keys=True))
