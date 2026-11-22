"""Independent cube-edge linear-forest and Hamiltonian-path certification."""
from collections import Counter
from itertools import permutations

E = sorted((a, a ^ (1 << k)) for a in range(8) for k in range(3)
           if a < (a ^ (1 << k)))
edge_id = {e:i for i,e in enumerate(E)}
N = len(E)
assert N == 12

def linear_forest(mask):
    parents = list(range(8))
    degree = [0]*8
    def root(x):
        while parents[x] != x:
            x = parents[x]
        return x
    for i,(u,v) in enumerate(E):
        if not (mask & (1 << i)):
            continue
        degree[u] += 1
        degree[v] += 1
        if degree[u] > 2 or degree[v] > 2:
            return False
        ru,rv = root(u),root(v)
        if ru == rv:
            return False
        parents[ru] = rv
    return True

forest_count = Counter()
optimal = set()
for m in range(1 << N):
    if linear_forest(m):
        forest_count[N-m.bit_count()] += 1
        if m.bit_count() == 7:
            optimal.add(m)
expected = {5:72,6:300,7:492,8:417,9:212,10:66,11:12,12:1}
assert dict(forest_count) == expected
assert len(optimal) == 72

cube_adj = {v:[v ^ (1 << bit) for bit in range(3)] for v in range(8)}
paths = set()
def visit(path):
    if len(path) == 8:
        mask = 0
        for u,v in zip(path, path[1:]):
            mask |= 1 << edge_id[tuple(sorted((u,v)))]
        paths.add(mask)
        return
    for nxt in cube_adj[path[-1]]:
        if nxt not in path:
            visit(path+[nxt])
for origin in range(8):
    visit([origin])
assert len(paths) == 72
assert paths == optimal

def transformed_vertex(v,flip,perm):
    w = 0
    for old_bit in range(3):
        if (v >> old_bit) & 1:
            w |= 1 << perm[old_bit]
    return w ^ flip

automorphisms = []
for perm in permutations(range(3)):
    for flip in range(8):
        mapped = tuple(edge_id[tuple(sorted((transformed_vertex(u,flip,perm),
                                           transformed_vertex(v,flip,perm))))]
                       for u,v in E)
        automorphisms.append(mapped)
assert len(set(automorphisms)) == 48

def orbit(m):
    return {sum(1 << perm[i] for i in range(N) if m & (1 << i))
            for perm in automorphisms}

remaining = set(optimal)
reps = []
while remaining:
    representative = min(remaining)
    o = orbit(representative)
    assert o <= remaining
    reps.append((representative,len(o)))
    remaining -= o
assert sorted(sz for _,sz in reps) == [24,24,24]
print('linear-forest census: PASS', sorted(forest_count.items()))
print('Hamiltonian paths:', len(paths), 'orbits:', reps)
print('representative cube-edge ID sets:',
      [[i for i in range(N) if m & (1<<i)] for m,_ in reps])
print('edge ID dictionary:',E)
