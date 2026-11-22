#!/usr/bin/env python3
"""Exact finite checker for the palette-three-to-five cube recolouring classification.
Requires Python 3 standard library only; all configurations regenerated from definitions.
"""
from itertools import permutations, product
from collections import Counter, deque
from math import comb

N = 8
EDGES = tuple((u, u ^ (1 << j)) for u in range(N) for j in range(3)
              if u < (u ^ (1 << j)))
assert len(EDGES) == 12
NEIGH = [tuple(v for u, v in EDGES if u == i) +
         tuple(u for u, v in EDGES if v == i) for i in range(N)]
assert all(len(ns) == 3 for ns in NEIGH)
AUTOS = tuple(tuple(sum(((((u >> axis[j]) & 1) ^ ((shift >> j) & 1)) << j)
                            for j in range(3)) for u in range(N))
              for axis in permutations(range(3)) for shift in range(8))
assert len(set(AUTOS)) == 48


def canon_palette(c):
    labels = {}
    return tuple(labels.setdefault(t, len(labels)) for t in c)


def orbit_key(c):
    # Pullback by all graph automorphisms, followed by canonical palette relabelling.
    # This exactly quotients Aut(Q_3) x S_k, even when some palette colours are unused.
    return min(canon_palette(tuple(c[p[i]] for i in range(N))) for p in AUTOS)


def graph(k):
    vertices = [x for x in product(range(k), repeat=N)
                if all(x[u] != x[v] for u, v in EDGES)]
    indices = {x: i for i, x in enumerate(vertices)}
    adj = [[] for _ in vertices]
    for i, x in enumerate(vertices):
        for v in range(N):
            for a in range(k):
                if a == x[v] or any(a == x[u] for u in NEIGH[v]):
                    continue
                y = x[:v] + (a,) + x[v + 1:]
                assert y in indices
                adj[i].append(indices[y])
        assert len(adj[i]) == len(set(adj[i]))
    for i, ns in enumerate(adj):
        for j in ns:
            assert i in adj[j]
    return vertices, adj


def bfs(root, adj):
    d = [-1] * len(adj)
    d[root] = 0
    todo = deque([root])
    while todo:
        u = todo.popleft()
        for v in adj[u]:
            if d[v] < 0:
                d[v] = d[u] + 1
                todo.append(v)
    return d


EXPECTED = {
    2: (2, 0, [1, 1], 1, 0, 0),
    3: (114, 240, [114], 4, 12, 279),
    4: (2652, 11808, [1]*24 + [2628], 13, 12, 15198),
    5: (29660, 217440, [29660], 23, 12, 85870),
}
# Nonzero distance pair histograms (ordered by distance 1..12).
EXPECTED_SHELLS = {
    3: [240,552,768,756,576,576,528,558,528,552,528,279],
    4: [11808,54432,159984,327600,491616,573336,558720,486936,
        385368,263040,123840,15198],
    5: [217440,1582320,7294800,23206920,52774080,86982840,104067840,
        89599740,53018760,18418440,2593920,85870],
}

def check(k):
    verts, adj = graph(k)
    size = len(verts)
    ecount = sum(len(ns) for ns in adj)//2
    classes = {}
    for i, x in enumerate(verts):
        key = orbit_key(x)
        if key not in classes:
            classes[key] = []
        classes[key].append(i)
    # Check quotient key really defines a group orbit: every member has same key,
    # all cube symmetries, and all palette permutations preserve legal moves.
    assert sum(len(members) for members in classes.values()) == size
    for a in AUTOS:
        for u, v in EDGES:
            assert a[u] in NEIGH[a[v]]
    assigned = [-1]*size
    comp_sizes=[]
    for v in range(size):
        if assigned[v] >= 0:
            continue
        todo = deque([v]);cid=len(comp_sizes);assigned[v]=cid; cnt=0
        while todo:
            u=todo.popleft();cnt+=1
            for w in adj[u]:
                if assigned[w] < 0:
                    assigned[w]=cid;todo.append(w)
        comp_sizes.append(cnt)
    weighted = Counter();rep_data=[];num_antipodes=0
    for key, members in sorted(classes.items()):
        root = members[0]
        distances = bfs(root, adj)
        reachable = sum(d >= 0 for d in distances)
        assert reachable == comp_sizes[assigned[root]]
        radius = max(distances)
        shell = Counter(d for d in distances if d >= 0)
        weighted.update({dist: len(members)*num for dist,num in shell.items()})
        if reachable > 1:
            num_antipodes += len(members)*shell[radius]
        rep_data.append((''.join(map(str,key)),len(members),reachable,radius,shell[radius]))
    assert num_antipodes % 2 == 0
    n_pairs = num_antipodes//2
    expected_n, expected_edges, expected_components, expected_orbits, expected_ecc, expected_pairs = EXPECTED[k]
    assert size == expected_n
    assert ecount == expected_edges
    assert sorted(comp_sizes) == sorted(expected_components)
    assert len(classes) == expected_orbits
    if k >= 3:
        assert all(x[3] == expected_ecc for x in rep_data if x[2] > 1)
        assert n_pairs == expected_pairs
        pairs = [weighted.get(d,0)//2 for d in range(1,13)]
        assert pairs == EXPECTED_SHELLS[k]
        assert sum(pairs) == sum(comb(c,2) for c in comp_sizes)
        assert pairs[0] == ecount
    if k == 4:
        frozen = [i for i in range(size) if not adj[i]]
        assert len(frozen) == 24
        # All frozen states are exactly the rainbow-on-each-face assignments.
        faces = [[x for x in range(N) if ((x>>bit)&1)==side]
                 for bit in range(3) for side in range(2)]
        rainbow = [i for i,x in enumerate(verts) if all(len({x[v] for v in f})==4 for f in faces)]
        assert frozen == rainbow
        assert len({orbit_key(verts[i]) for i in frozen}) == 1
        # Independent full-source BFS, with no orbit reduction, for the non-frozen component.
        for i in range(size):
            if adj[i]:
                distances=bfs(i,adj)
                assert sum(z>=0 for z in distances)==2628
                assert max(distances)==12
    if k == 3:
        for i in range(size):
            assert max(bfs(i,adj)) == 12
    print(f'K={k} STATES={size} EDGES={ecount} COMPONENTS={Counter(comp_sizes)} ORBITS={len(classes)}'+
          (f' DIAMETRAL_PAIRS={n_pairs}' if k>=3 else ''))
    if k>=3:print('SHELL_PAIRS',k,EXPECTED_SHELLS[k])
    return rep_data

if __name__ == '__main__':
    for k in range(2,6):
        check(k)
    print('VERIFY_OK')
