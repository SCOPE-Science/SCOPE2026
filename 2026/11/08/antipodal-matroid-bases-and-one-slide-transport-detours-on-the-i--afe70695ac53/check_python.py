#!/usr/bin/env python3
"""Independent, exhaustive metric-basis and token-move verification on the icosahedral graph."""
from collections import Counter, deque
from itertools import combinations, permutations

EDGES = [(0, 1), (0, 5), (0, 7), (0, 8), (0, 11), (1, 2), (1, 5), (1, 6), (1, 8), (2, 3), (2, 6), (2, 8), (2, 9), (3, 4), (3, 6), (3, 9), (3, 10), (4, 5), (4, 6), (4, 10), (4, 11), (5, 6), (5, 11), (7, 8), (7, 9), (7, 10), (7, 11), (8, 9), (9, 10), (10, 11)]
N = 12
adj = [set() for _ in range(N)]
for a, b in EDGES:
    assert a != b and b not in adj[a]
    adj[a].add(b); adj[b].add(a)
assert len(EDGES) == 30 and all(len(a) == 5 for a in adj)

distance = []
for origin in range(N):
    ds = [-1] * N
    ds[origin] = 0
    queue = deque([origin])
    while queue:
        a = queue.popleft()
        for b in adj[a]:
            if ds[b] < 0:
                ds[b] = ds[a] + 1
                queue.append(b)
    assert max(ds) == 3
    distance.append(ds)
antipode = [next(v for v in range(N) if distance[u][v] == 3) for u in range(N)]
assert all(antipode[antipode[u]] == u for u in range(N))
assert len({tuple(sorted((u, antipode[u]))) for u in range(N)}) == 6
for u, v in combinations(range(N), 2):
    equi = [w for w in range(N) if distance[w][u] == distance[w][v]]
    assert len(equi) == (0 if distance[u][v] == 3 else 4)
    assert all(antipode[w] in equi for w in equi)

def resolving(vs):
    return len({tuple(distance[x][v] for v in vs) for x in range(N)}) == N

assert not any(resolving(x) for k in (1,2) for x in combinations(range(N),k))
basis = [sum(1 << x for x in s) for s in combinations(range(N), 3) if resolving(s)]
basis_set = set(basis)
assert len(basis) == 160
for s in combinations(range(N),3):
    correct = all(distance[a][b] < 3 for a,b in combinations(s,2))
    assert resolving(s) == correct

def configurations(mask):
    return [u for u in range(N) if (mask >> u) & 1]
def neighbors(basis_list, slide):
    ids = {s: i for i, s in enumerate(basis_list)}
    graph = [set() for _ in basis_list]
    for i, mask in enumerate(basis_list):
        for a in configurations(mask):
            for b in (adj[a] if slide else range(N)):
                if mask & (1 << b):
                    continue
                nxt = mask ^ (1 << a) ^ (1 << b)
                if nxt in ids:
                    graph[i].add(ids[nxt])
    assert all(i in graph[j] for i, nbr in enumerate(graph) for j in nbr)
    return graph
slide = neighbors(basis,True)
jump = neighbors(basis,False)
assert all(len(x)==9 for x in slide)
assert all(len(x)==21 for x in jump)
assert sum(map(len, slide))//2 == 720
assert sum(map(len, jump))//2 == 1680
def bfs(graph, origin):
    ds=[-1]*len(graph);ds[origin]=0;queue=deque([origin])
    while queue:
        u=queue.popleft()
        for v in graph[u]:
            if ds[v]==-1:
                ds[v]=ds[u]+1;queue.append(v)
    assert -1 not in ds
    return ds
slide_dist=[bfs(slide,i) for i in range(len(basis))]
jump_dist=[bfs(jump,i) for i in range(len(basis))]
assert Counter(map(max,slide_dist)) == {4:20,5:120,6:20}
assert set(map(max,jump_dist)) == {3}
type_ecc = Counter()
for i,s in enumerate(basis):
    tup=configurations(s)
    pattern=tuple(sorted(distance[a][b] for a,b in combinations(tup,2)))
    type_ecc[(pattern, max(slide_dist[i]))]+=1
assert type_ecc=={
    ((1,1,1),6):20, ((1,1,2),5):60,
    ((1,2,2),5):60, ((2,2,2),4):20
}
hist=Counter();detours=Counter()
for i in range(len(basis)):
    a=configurations(basis[i])
    for j in range(i+1,len(basis)):
        b=configurations(basis[j])
        work=min(sum(distance[x][y] for x,y in zip(a,p)) for p in permutations(b))
        delta=slide_dist[i][j]
        hist[delta]+=1; detours[delta-work]+=1
        assert jump_dist[i][j]==3-len(set(a)&set(b))
assert hist == {1:720,2:2730,3:4960,4:3490,5:810,6:10}
assert detours == {0:12110,1:610}
# Independently obtain unrestricted token-graph distances to validate transport lower bounds.
allstates=[sum(1<<u for u in ss) for ss in combinations(range(N),3)]
token=neighbors(allstates,True)
fid={s:i for i,s in enumerate(allstates)}
free_dist=[bfs(token,fid[s]) for s in basis]
for i in range(len(basis)):
    a=configurations(basis[i])
    for j in range(i+1,len(basis)):
        b=configurations(basis[j])
        work=min(sum(distance[x][y] for x,y in zip(a,p)) for p in permutations(b))
        assert work==free_dist[i][fid[basis[j]]]
print("PASS Python: 12 vertices/30 edges; 6 antipodal pairs; 160 minimum metric bases;")
print("regular slide=9 (720 edges), jump=21 (1680 edges);")
print("slide eccentricities 4:20,5:120,6:20; jump diameter 3;")
print("slide pair distance histogram",dict(sorted(hist.items())),"; transport detours",dict(sorted(detours.items())))
