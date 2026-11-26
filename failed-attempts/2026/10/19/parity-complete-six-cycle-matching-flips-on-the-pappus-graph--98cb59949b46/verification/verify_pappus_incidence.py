#!/usr/bin/env python3
"""Independent Pappus point-line construction and direct permutation comparisons."""
from itertools import permutations,combinations
from collections import Counter,deque

# Pappus 9_3 incidence: two original triples, three collinear crosspoints.
lines=((0,1,2),(3,4,5),(6,7,8),(0,4,6),(3,1,6),(0,5,7),(3,2,7),(1,5,8),(4,2,8))
assert len(lines)==9
assert all(len(x)==3 for x in lines)
assert Counter(p for line in lines for p in line)=={i:3 for i in range(9)}
assert len(set(tuple(sorted(x)) for x in lines))==9
assert max(len(set(lines[i])&set(lines[j])) for i,j in combinations(range(9),2))<=1

# Enumerate all 9! permutations; acceptable matchings are those with every point incident with its image line.
matchings=[p for p in permutations(range(9)) if all(i in lines[p[i]] for i in range(9))]
assert len(matchings)==42

# Difference of exactly 3 positions between two permitted permutations
# automatically forms one alternating 6-cycle; verify cyclicity independently.
def legal(x,y):
    changed=[i for i in range(9) if x[i]!=y[i]]
    if len(changed)!=3:return False
    reverse={x[i]:i for i in changed}
    nxt={i:reverse[y[i]] for i in changed}
    a=changed[0]
    return nxt[a]!=a and nxt[nxt[a]]!=a and nxt[nxt[nxt[a]]]==a

adj=[set() for _ in matchings]
for a,b in combinations(range(42),2):
    if legal(matchings[a],matchings[b]):adj[a].add(b);adj[b].add(a)
assert sum(map(len,adj))//2==72
assert Counter(map(len,adj))=={3:36,6:6}

# Geometry from the incidences, independently of any LCF input.
E={tuple(sorted((p,9+j))) for j,line in enumerate(lines) for p in line}
assert len(E)==27
vertices=set(range(18)); neighbors=[set() for _ in vertices]
for x,y in E:neighbors[x].add(y);neighbors[y].add(x)
cycs=set()
def dfs(path):
    if len(path)==6:
        if path[-1] in neighbors[path[0]]:
            cycs.add(frozenset(tuple(sorted((path[i],path[(i+1)%6]))) for i in range(6)))
    else:
        for v in neighbors[path[-1]]:
            if v not in path:dfs(path+[v])
for v in vertices:dfs([v])
assert len(cycs)==18
idx={m:i for i,m in enumerate(matchings)}
for i,p in enumerate(matchings):
    mi=frozenset(tuple(sorted((x,9+p[x]))) for x in range(9))
    for j in adj[i]:
        mj=frozenset(tuple(sorted((x,9+matchings[j][x]))) for x in range(9))
        assert mi^mj in cycs

# Incidence-to-LCF graph isomorphism: explicit bijection, exhaustively check 27 edges.
iso=(0,2,8,10,6,12,4,16,14,1,11,15,5,3,17,9,13,7)
assert sorted(iso)==list(range(18))
shifts=(5,7,-7,7,-7,-5)*3
elcf={tuple(sorted((i,(i+1)%18))) for i in range(18)} | {tuple(sorted((i,(i+shifts[i])%18))) for i in range(18)}
assert {tuple(sorted((iso[a],iso[b]))) for a,b in E}==elcf

# All 42 matchings by an *independent* least-free-vertex DFS on the LCF representation.
adjl=[set() for _ in range(18)]
for i,j in elcf:adjl[i].add(j);adjl[j].add(i)
def rec(mask,edges):
    if not mask:
        yield frozenset(edges);return
    v=(mask&-mask).bit_length()-1
    for w in sorted(adjl[v]):
        if mask>>w&1:yield from rec(mask^(1<<v)^(1<<w),edges+[tuple(sorted((v,w)))])
ml=sorted(set(rec((1<<18)-1,[])), key=lambda m:tuple(sorted(m)))
assert len(ml)==42
lookup={m:i for i,m in enumerate(ml)}
perm=[]
for p in matchings:
    image=frozenset(tuple(sorted((iso[i],iso[9+p[i]]))) for i in range(9))
    perm.append(lookup[image])
assert sorted(perm)==list(range(42))
# Reconstruct LCF flips by six-cycle XOR and compare all 861 unordered pair decisions.
cyclesl={frozenset(tuple(sorted((iso[a],iso[b]))) for a,b in c) for c in cycs}
indexl={m:i for i,m in enumerate(ml)}
flipsl=[set() for _ in ml]
for i,m in enumerate(ml):
    for c in cyclesl:
        if len(c&m)==3:flipsl[i].add(indexl[m^c])
assert all({perm[j] for j in adj[i]}==flipsl[perm[i]] for i in range(42))

# A second exhaustive component and eccentricity certificate.
unseen=set(range(42));components=[]
while unseen:
    start=min(unseen);vis={start};dq=deque([start])
    while dq:
        u=dq.popleft()
        for v in adj[u]:
            if v not in vis:vis.add(v);dq.append(v)
    unseen.difference_update(vis);components.append(vis)
assert sorted(map(len,components))==[21,21]
for comp in components:
    diameter=0
    for x in comp:
        dist={x:0};dq=deque([x])
        while dq:
            v=dq.popleft()
            for w in adj[v]:
                if w not in dist:dist[w]=dist[v]+1;dq.append(w)
        assert set(dist)==comp and max(dist.values())<=4
        diameter=max(diameter,max(dist.values()))
    assert diameter==4

print('INCIDENCE_VERIFY_OK points=9 lines=9 incidence_edges=27 perfect_matchings=42')
print('INCIDENCE_VERIFY_OK six_cycles=18 flips=72 connected_components=21+21 diameter_each=4')
print('INDEPENDENT_CROSSCHECK_OK exact_all_42_adjacency_sets_match_under_verified_explicit_isomorphism=true')
