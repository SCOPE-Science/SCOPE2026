"""Finite exhaustive certificate: maximal matchings of the Pappus incidence graph.
Requires only Python 3 standard library. All vertex and edge labels are constructed here.
"""
from collections import Counter, defaultdict, deque
from itertools import product

points = list(product(range(3), repeat=2))
point_index = {p: i for i, p in enumerate(points)}
lines = []
for direction in range(3):
    for intercept in range(3):
        lines.append(frozenset(i for i, (x, y) in enumerate(points)
                               if ((x if direction == 0 else y if direction == 1
                                    else (y-x) % 3) == intercept)))
edges = sorted((i, 9+j) for j, line in enumerate(lines) for i in line)
assert len(edges) == 27 and len(set(edges)) == 27
adj = [[] for _ in range(18)]
for j, (u, v) in enumerate(edges):
    adj[u].append((v, j))
    adj[v].append((u, j))
assert all(len(a) == 3 for a in adj)

maximal = []
def traverse(free, chosen, uncovered):
    if not free:
        assert all(not (uncovered & (1 << u) and uncovered & (1 << v))
                   for u, v in edges)
        maximal.append(chosen)
        return
    u = (free & -free).bit_length() - 1
    # Leave u unmatched only if it has no previously unmatched neighbour.
    if all(not (uncovered & (1 << v)) for v, _ in adj[u]):
        traverse(free ^ (1 << u), chosen, uncovered | (1 << u))
    for v, j in adj[u]:
        if free & (1 << v):
            traverse(free ^ (1 << u) ^ (1 << v), chosen | (1 << j), uncovered)
traverse((1 << 18)-1, 0, 0)
assert len(maximal) == len(set(maximal))
size_hist = dict(sorted(Counter(m.bit_count() for m in maximal).items()))
assert size_hist == {6: 36, 7: 567, 8: 648, 9: 42}, size_hist
opt = sorted(m for m in maximal if m.bit_count() == 6)
assert len(opt) == 36

classes = defaultdict(list)
for m in opt:
    covered = {w for j, uv in enumerate(edges) if m & (1 << j) for w in uv}
    uncovered = frozenset(set(range(18)) - covered)
    assert len(uncovered & set(range(9))) == 3
    assert len(uncovered & set(range(9,18))) == 3
    classes[uncovered].append(m)
assert len(classes) == 18 and all(len(ms) == 2 for ms in classes.values())
# Geometric classification by an axis-aligned corner and its slope-one diagonal.
triples = {
    frozenset([point_index[(x, y)], point_index[((x+a) % 3, y)],
               point_index[(x, (y-a) % 3)]])
    for x, y, a in product(range(3), range(3), [1, 2])
}
assert len(triples) == 18
assert {frozenset(t for t in k if t < 9) for k in classes} == triples
for k in classes:
    pts = frozenset(t for t in k if t < 9)
    omitted_lines = frozenset(9+j for j, L in enumerate(lines) if pts.isdisjoint(L))
    assert len(omitted_lines) == 3 and omitted_lines == frozenset(t for t in k if t >= 9)

def exchange_graph(t):
    graph = [set() for _ in opt]
    for i, a in enumerate(opt):
        for j in range(i):
            if ((a ^ opt[j]).bit_count() // 2) <= t:
                graph[i].add(j)
                graph[j].add(i)
    return graph

def distances(graph, source):
    depth = {source: 0}
    queue = deque([source])
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if v not in depth:
                depth[v] = depth[u] + 1
                queue.append(v)
    return depth

g1, g2, g3 = (exchange_graph(t) for t in (1, 2, 3))
assert sum(map(len, g1)) == sum(map(len, g2)) == 0
assert sum(map(len, g3)) == 252 and set(map(len, g3)) == {7}
shells = []
for i in range(len(opt)):
    depths = distances(g3, i)
    assert len(depths) == 36
    assert max(depths.values()) == 4
    shells.append(tuple(Counter(depths.values())[r] for r in range(5)))
assert set(shells) == {(1, 7, 12, 12, 4)}
triangles = sum(1 for i in range(36) for j in g3[i] if j > i
                for k in g3[i].intersection(g3[j]) if k > j)
assert triangles == 108

# Explicit affine collineations; the 108 that preserve the three line directions
# send any minimum matching to every other minimum matching.
line_lookup = {line: j for j, line in enumerate(lines)}
edge_lookup = {e: i for i, e in enumerate(edges)}
images = set()
number_collineations = 0
for a, b, c, d in product(range(3), repeat=4):
    if (a*d - b*c) % 3 == 0:
        continue
    for dx, dy in product(range(3), repeat=2):
        pmap = [point_index[((a*x+b*y+dx) % 3, (c*x+d*y+dy) % 3)]
                for x, y in points]
        lmap = [line_lookup.get(frozenset(pmap[p] for p in L), -1)
                for L in lines]
        if -1 in lmap:
            continue
        number_collineations += 1
        emap = [edge_lookup[(pmap[u], 9+lmap[v-9])] for u, v in edges]
        images.add(sum(1 << emap[j] for j in range(27) if opt[0] & (1 << j)))
assert number_collineations == 108
assert images == set(opt)
print('PAPPUS AFFINE CERTIFICATE PASS')
print('maximal matching polynomial:', size_hist)
print('minimum: 6; optimum count: 36; unmatched triples: 18, two matchings each')
print('exchange t=1,2: 36 isolates each; t=3: 126 edges, regular degree 7')
print('t=3: connected, diameter=radius=4, shells=(1,7,12,12,4), triangles=108')
print('affine automorphisms preserving line classes: 108; optimum orbit size: 36')
