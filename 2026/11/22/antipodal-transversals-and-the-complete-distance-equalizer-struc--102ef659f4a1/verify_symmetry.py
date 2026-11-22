"""Independent orbit/reconfiguration verification for the dodecahedral graph.

Only the Python standard library is used. Automorphisms are constructed from
rooted distance signatures, not from a graph isomorphism package.
"""
from collections import Counter, deque
from itertools import combinations

N = 20
adj = [set() for _ in range(N)]
for i in range(10):
    for x, y in ((i, (i+1) % 10), (i, 10+i), (10+i, 10+(i+2)%10)):
        adj[x].add(y)
        adj[y].add(x)

def bfs(root):
    d = [-1]*N
    d[root] = 0
    todo = deque([root])
    while todo:
        v = todo.popleft()
        for w in adj[v]:
            if d[w] == -1:
                d[w] = d[v] + 1
                todo.append(w)
    return d

d = [bfs(i) for i in range(N)]
base = (9, 0, 1)
assert 9 in adj[0] and 1 in adj[0]

def signatures(path):
    return {tuple(d[x][y] for y in path): x for x in range(N)}

original = signatures(base)
assert len(original) == N  # A 2-arc fixes each vertex in this graph.
autos = set()
for center in range(N):
    for left in adj[center]:
        for right in adj[center] - {left}:
            target = signatures((left, center, right))
            if len(target) != N:
                continue
            m = tuple(target[tuple(d[x][v] for v in base)] for x in range(N))
            if all({m[w] for w in adj[v]} == adj[m[v]] for v in range(N)):
                autos.add(m)
assert len(autos) == 120, len(autos)
# The vertex stabilizer acts transitively on each distance sphere, allowing
# one representative equalizer calculation per distance 1,...,5.
stabilizer = [m for m in autos if m[0] == 0]
assert len(stabilizer) == 6
for radius in range(1, 6):
    sphere = {v for v in range(1,N) if d[0][v] == radius}
    rep = min(sphere)
    assert {m[rep] for m in stabilizer} == sphere
    witnesses = {w for w in range(N) if d[0][w] == d[rep][w]}
    assert len(witnesses) == (0 if radius == 5 else 4)
    assert all((w+5)%10 in witnesses for w in witnesses if w < 10)
    assert all(10+(w-10+5)%10 in witnesses for w in witnesses if w >= 10)

pairs = [(i,i+5) for i in range(5)] + [(i+10,i+15) for i in range(5)]
assert all(d[a][b] == 5 for a,b in pairs)
choices = []
for bits in range(1<<10):
    choices.append(frozenset(pair[(bits>>j)&1] for j,pair in enumerate(pairs)))
assert len(set(choices)) == 1024
seen = set()
orbits = []
for S in choices:
    if S in seen:
        continue
    orbit = {frozenset(m[x] for x in S) for m in autos}
    assert all(T in choices for T in orbit)
    orbits.append(orbit)
    seen.update(orbit)
assert len(seen) == 1024
assert len(orbits) == 20
sizes = Counter(map(len,orbits))
assert sizes == Counter({12:2,20:4,40:2,60:10,120:2}), sizes

# Every single replacement necessarily changes the chosen endpoint of exactly
# one antipodal pair. These pairs have graph distance five, so slides are absent.
for i,S in enumerate(choices):
    neighbors = 0
    for T in choices:
        if len(S-T)==1:
            assert all(d[x][y] == 5 for x in S-T for y in T-S)
            neighbors+=1
    assert neighbors==10

# The induced subgraph-size profile refines the orbit distribution.
edge_hist = Counter(sum(1 for u,v in combinations(S,2) if v in adj[u]) for S in choices)
assert edge_hist == Counter({3:20,4:60,5:72,6:120,7:240,8:240,9:120,10:72,11:60,12:20}),edge_hist
print('AUTOMORPHISMS',len(autos))
print('OPTIMUM_SETS',len(choices))
print('AUTOMORPHISM_ORBITS',len(orbits),' '.join(f'{size}:{count}' for size,count in sorted(sizes.items())))
print('INDUCED_EDGE_HIST', ' '.join(f'{e}:{k}' for e,k in sorted(edge_hist.items())))
print('TOKEN_JUMP_DEGREE',10,'TOKEN_SLIDE_EDGES',0)
print('PASS')
