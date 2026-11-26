#!/usr/bin/env python3
"""Direct finite enumeration of induced-matching exchange graphs of the Pappus graph.

Run: python3 check_lcf.py
Uses only the Python standard library. The graph is specified by LCF notation.
"""
from itertools import combinations
from collections import Counter, deque
import json

N = 18
shifts = [5, 7, -7, 7, -7, -5]
def edge(u,v): return tuple(sorted((u,v)))
E = sorted({edge(i,(i+1)%N) for i in range(N)} |
           {edge(i,(i+shifts[i%len(shifts)])%N) for i in range(N)})
assert len(E) == 27
Eset = set(E)

def induced(combo):
    for i,j in combinations(combo,2):
        u,v = E[i]; x,y = E[j]
        if len({u,v,x,y}) != 4 or any(edge(a,b) in Eset for a in (u,v) for b in (x,y)):
            return False
    return True

F = {k: [tuple(c) for c in combinations(range(len(E)),k) if induced(c)] for k in (4,5,6)}
assert (len(F[4]), len(F[5]), len(F[6])) == (135,27,0)

def jump_graph(states):
    nbr = [set() for _ in states]
    for i,j in combinations(range(len(states)),2):
        if len(set(states[i]) & set(states[j])) == len(states[i])-1:
            nbr[i].add(j);nbr[j].add(i)
    return nbr

J5,J4 = jump_graph(F[5]),jump_graph(F[4])
assert sum(map(len,J5))==0
assert sum(map(len,J4))//2==486
parents=[]
for q in F[4]:
    p=[i for i,m in enumerate(F[5]) if set(q).issubset(m)]
    assert len(p)==1
    parents.append(p[0])

Q={}
for a in range(len(F[5])):
    for b in range(a+1,len(F[5])):
        Q[(a,b)] = 0
for i in range(len(F[4])):
    for j in J4[i]:
        if i<j and parents[i]!=parents[j]:
            Q[tuple(sorted((parents[i],parents[j])))] +=1
Q={k:v for k,v in Q.items() if v}
assert len(Q)==54 and set(Q.values())=={4}
# An explicit isomorphism: quotient-vertex index -> source-edge index.
MAP=(0,1,2,3,4,21,22,20,23,6,13,14,12,15,11,18,26,25,16,17,9,5,8,7,10,19,24)
assert sorted(MAP)==list(range(27))
assert all(((i,j) in Q) == (bool(set(E[MAP[i]])&set(E[MAP[j]])))
           for i,j in combinations(range(27),2))
assert Counter(len(set(x)&set(y)) for x,y in combinations(F[5],2))=={0:189,1:108,3:54}

# An optimal-matching quotient adjacency corresponds precisely to three shared edges.
assert {q for q in Q} == {(a,b) for a,b in combinations(range(27),2)
                           if len(set(F[5][a])&set(F[5][b]))==3}

def bfs(start,nbr):
    dist={start:0}; q=deque([start])
    while q:
        a=q.popleft()
        for b in nbr[a]:
            if b not in dist:dist[b]=dist[a]+1;q.append(b)
    return dist
D=[bfs(i,J4) for i in range(len(F[4]))]
assert all(len(d)==135 for d in D)
ex=[max(d.values()) for d in D]
assert (min(ex),max(ex))==(8,9)
assert Counter(map(len,J4))=={4:27,8:108}
# Count degree-4 vertex for each optimal matching and verify parent cliques.
for a in range(27):
    block=[i for i,p in enumerate(parents) if p==a]
    assert len(block)==5 and all(j in J4[i] for i,j in combinations(block,2))
    assert sum(len(J4[i])==4 for i in block)==1

distances=Counter(D[i][j] for i,j in combinations(range(135),2))
res={
 'graph': 'Pappus graph LCF [5,7,-7,7,-7,-5]^3',
 'vertices':18,'edges':len(E),'induced_matching_sizes':{'4':135,'5':27,'6':0},
 'top_exchange_edges':sum(map(len,J5))//2,
 'near_top_exchange_edges':sum(map(len,J4))//2,
 'near_top_degrees':dict(sorted(Counter(map(len,J4)).items())),
 'near_top_radius':min(ex),'near_top_diameter':max(ex),
 'near_top_eccentricities':dict(sorted(Counter(ex).items())),
 'near_top_distance_histogram':dict(sorted(distances.items())),
 'parent_multiplicities':dict(Counter(sum(set(x).issubset(y) for y in F[5]) for x in F[4])),
 'quotient':{'vertices':27,'edges':len(Q),'degree':4,'interblock_edges_each':4,
             'max_parent_intersections':dict(Counter(len(set(x)&set(y)) for x,y in combinations(F[5],2)))},
 'verified':True
}
print(json.dumps(res,sort_keys=True,indent=2))
