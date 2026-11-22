"""Exact finite verification of geodetic and edge-geodetic sets in the Fano incidence graph."""
from collections import Counter, deque
from itertools import combinations

N = 14
LINE = [frozenset(((j + d) % 7 for d in (0, 1, 3))) for j in range(7)]
adj = [set() for _ in range(N)]
for j, points in enumerate(LINE):
    for p in points:
        adj[p].add(j + 7)
        adj[j + 7].add(p)
assert all(len(a) == 3 for a in adj)

def distance(root):
    dist = [-1] * N
    dist[root] = 0
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)
    return dist

D = [distance(i) for i in range(N)]
assert max(map(max, D)) == 3
EDGES = tuple((u, v) for u in range(N) for v in sorted(adj[u]) if u < v)
assert len(EDGES) == 21
EID = {e: i for i, e in enumerate(EDGES)}
PAIR_VERT, PAIR_EDGE = {}, {}
for a, b in combinations(range(N), 2):
    path_masks = []
    def traverse(u, verts, edges):
        if u == b:
            path_masks.append((verts, edges))
            return
        for v in sorted(adj[u]):
            if D[a][v] == D[a][u] + 1 and D[a][v] + D[v][b] == D[a][b]:
                e = tuple(sorted((u, v)))
                traverse(v, verts | (1 << v), edges | (1 << EID[e]))
    traverse(a, 1 << a, 0)
    assert path_masks
    vbits = ebits = 0
    for vb, eb in path_masks:
        vbits |= vb
        ebits |= eb
    PAIR_VERT[a, b] = vbits
    PAIR_EDGE[a, b] = ebits

GEODETIC, EDGE_GEODETIC = set(), set()
for mask in range(1 << N):
    vertices = [x for x in range(N) if (mask >> x) & 1]
    vbits = ebits = 0
    for a, b in combinations(vertices, 2):
        vbits |= PAIR_VERT[a, b]
        ebits |= PAIR_EDGE[a, b]
    if vbits == (1 << N) - 1:
        GEODETIC.add(mask)
    if ebits == (1 << len(EDGES)) - 1:
        EDGE_GEODETIC.add(mask)
assert GEODETIC == EDGE_GEODETIC

MINIMAL = {m for m in EDGE_GEODETIC if all(m ^ (1 << v) not in EDGE_GEODETIC for v in range(N) if (m >> v) & 1)}

# Four explicit projective families of inclusion-minimal sets.
FAMILY = {}
def ins(mask, label):
    assert mask not in FAMILY, (mask, label, FAMILY.get(mask))
    FAMILY[mask] = label

def bitmask(vs):
    return sum(1 << v for v in vs)
for j, line in enumerate(LINE):
    for p in line:
        ins(bitmask([x for x in line if x != p] + [7 + k for k in range(7) if p in LINE[k] and k != j]), 'flag')
for j, line in enumerate(LINE):
    ins(bitmask([p for p in range(7) if p not in line] + [7 + j]), 'off_line')
for p in range(7):
    ins(bitmask([p] + [7 + j for j in range(7) if p not in LINE[j]]), 'off_point')
for j, line in enumerate(LINE):
    for p in range(7):
        if p not in line:
            ins(bitmask(list(line) + [7 + k for k in range(7) if p in LINE[k]]), 'nonflag')
ins(bitmask(range(7)), 'all_points')
ins(bitmask(range(7, 14)), 'all_lines')
assert MINIMAL == set(FAMILY), (len(MINIMAL - set(FAMILY)), len(set(FAMILY) - MINIMAL))
counts = Counter(m.bit_count() for m in GEODETIC)
mincounts = Counter(m.bit_count() for m in MINIMAL)
familycounts = Counter(FAMILY.values())
assert dict(sorted(counts.items())) == {4:21,5:224,6:931,7:1962,8:2394,9:1862,10:987,11:364,12:91,13:14,14:1}
assert dict(sorted(mincounts.items())) == {4:21,5:14,6:28,7:2}
assert familycounts == {'flag':21, 'off_line':7,'off_point':7,'nonflag':28,'all_points':1,'all_lines':1}
print('PASS geodetic=edge-geodetic on 16384 subsets; size counts:', dict(sorted(counts.items())))
print('PASS minimal projective families:', dict(sorted(familycounts.items())))
