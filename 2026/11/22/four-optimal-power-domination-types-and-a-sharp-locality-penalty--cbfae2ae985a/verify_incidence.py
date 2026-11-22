"""Independent incidence-set and graph-distance certificate for the Folkman graph."""
from itertools import combinations, product, permutations
from collections import Counter, deque
import json

base = tuple(range(5))
E = tuple(combinations(base, 2))
U = tuple(('u', i, bit) for i in base for bit in (0, 1))
W = tuple(('e', i, j) for i, j in E)
V = U + W
neighbors = {v: set() for v in V}
for i, j in E:
    e = ('e', i, j)
    for x in (i, j):
        for bit in (0, 1):
            a = ('u', x, bit)
            neighbors[e].add(a)
            neighbors[a].add(e)
assert len(V) == 20 and all(len(neighbors[v]) == 4 for v in V)

def observe(S):
    marked = set(S)
    for v in S:
        marked.update(neighbors[v])
    while True:
        additions = {next(iter(unknown)) for v in marked
                     if len(unknown := neighbors[v] - marked) == 1}
        if not additions - marked:
            return len(marked) == 20
        marked.update(additions)

by_size = {}
for k in range(5):
    by_size[k] = {frozenset(t) for t in combinations(V, k) if observe(t)}
assert {k: len(v) for k, v in by_size.items()} == {0:0,1:0,2:0,3:0,4:560}

# Four explicit, disjoint placement types, built without a graph automorphism search.
classes = [set() for _ in range(4)]
def choices(originals):
    for bits in product((0,1), repeat=len(originals)):
        yield frozenset(('u', i, t) for i, t in zip(originals, bits))

# Type I: one selected edge of K5 and one selected twin at each outside vertex.
for i, j in E:
    outside = tuple(x for x in base if x not in (i, j))
    for choice in choices(outside):
        classes[0].add(choice | {('e', i, j)})

# Type II: two selected adjacent K5 edges, and both outside vertex groups.
for center in base:
    for i, j in combinations((x for x in base if x != center), 2):
        outside = tuple(x for x in base if x not in (center, i, j))
        for choice in choices(outside):
            classes[1].add(choice | {('e', *sorted((center, i))), ('e', *sorted((center, j)))})

# Type III: two disjoint selected K5 edges; choose one of their endpoints and the fifth vertex.
for e1, e2 in combinations(E, 2):
    covered = set(e1) | set(e2)
    if len(covered) != 4:
        continue
    left = next(x for x in base if x not in covered)
    for other in covered:
        for choice in choices((left, other)):
            classes[2].add(choice | {('e', *e1), ('e', *e2)})

# Type IV: selected K5 edges make a path of length three, twin at the unused fifth vertex.
for p in permutations(base, 4):
    if p > tuple(reversed(p)):
        continue
    outside = next(x for x in base if x not in p)
    epath = {('e', *sorted((p[t], p[t + 1]))) for t in range(3)}
    for bit in (0, 1):
        classes[3].add(frozenset(epath | {('u', outside, bit)}))
assert [len(C) for C in classes] == [80,120,240,120]
assert all(classes[i].isdisjoint(classes[j]) for i in range(4) for j in range(i+1,4))
assert set().union(*classes) == by_size[4]

states = sorted(by_size[4], key=lambda x: tuple(V.index(v) for v in sorted(x, key=V.index)))
assert len(set(states)) == 560
n = len(states)
a_jump = [[] for _ in range(n)]
a_slide = [[] for _ in range(n)]
for i, A in enumerate(states):
    for j in range(i + 1, n):
        B = states[j]
        if len(A.intersection(B)) != 3:
            continue
        a_jump[i].append(j); a_jump[j].append(i)
        outgoing = next(iter(A - B))
        incoming = next(iter(B - A))
        if incoming in neighbors[outgoing]:
            a_slide[i].append(j); a_slide[j].append(i)
assert sum(map(len,a_jump))//2 == 4680
assert sum(map(len,a_slide))//2 == 1920
assert Counter(map(len,a_jump)) == {15:80,16:120,17:240,18:120}
assert Counter(map(len,a_slide)) == {4:240,8:240,12:80}

def bfs(G, start):
    distance = {start:0}
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for nxt in G[v]:
            if nxt not in distance:
                distance[nxt] = distance[v] + 1
                queue.append(nxt)
    assert len(distance) == n
    return distance
jump_dist = [bfs(a_jump,i) for i in range(n)]
slide_dist = [bfs(a_slide,i) for i in range(n)]
J = Counter();S = Counter();extra = Counter();extra_types = Counter()
for i in range(n):
    for j in range(i+1,n):
        x = jump_dist[i][j];y = slide_dist[i][j]
        J[x] += 1;S[y] += 1;extra[y-x] += 1
        if y-x == 4:
            extra_types[(x,y)] += 1
assert J == {1:4680, 2:22440, 3:64960, 4:64440}
assert S == {1:1920, 2:9000, 3:23760, 4:50280, 5:42240, 6:24700, 7:4080, 8:540}
assert extra == {0:38400, 1:65940, 2:41400, 3:9460, 4:1320}
assert extra_types == {(2,6):780,(4,8):540}
assert Counter(max(x.values()) for x in jump_dist) == {4:560}
assert Counter(max(x.values()) for x in slide_dist) == {7:80,8:480}
assert {states[i] for i in range(n) if max(slide_dist[i].values()) == 7} == classes[0]
print(json.dumps({'vertex_count':len(V),'edge_count':sum(map(len,neighbors.values()))//2,
    'optimum_size':4,'minimum_placements':n,'four_family_sizes':[len(c) for c in classes],
    'jump_edges':sum(map(len,a_jump))//2,'slide_edges':sum(map(len,a_slide))//2,
    'jump_distances':dict(sorted(J.items())),'slide_distances':dict(sorted(S.items())),
    'penalty':dict(sorted(extra.items())),'extremal_penalty_types':{str(k):v for k,v in sorted(extra_types.items())},
    'slide_centers':len(classes[0])},sort_keys=True))
