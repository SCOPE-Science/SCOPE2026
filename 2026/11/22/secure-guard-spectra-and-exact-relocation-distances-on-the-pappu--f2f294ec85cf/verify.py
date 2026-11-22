#!/usr/bin/env python3
"""Exact secure-domination and optimal-reconfiguration certificate for Pappus incidence graph.
Only Python standard library is needed. All 2^18 initial subsets are tested.
"""
from collections import Counter, deque
N = 18
ALL = (1 << N) - 1

def point_id(x, y):
    return 3 * x + y

def line_id(m, b):
    return 9 + 3 * m + b

adj = [0] * N
for x in range(3):
    for y in range(3):
        i = point_id(x, y)
        for m in range(3):
            j = line_id(m, (y - m * x) % 3)
            adj[i] |= 1 << j
            adj[j] |= 1 << i
assert all(a.bit_count() == 3 for a in adj)
closed = [adj[v] | (1 << v) for v in range(N)]
cover = [0] * (1 << N)
for mask in range(1, 1 << N):
    b = mask & -mask
    cover[mask] = cover[mask ^ b] | closed[b.bit_length() - 1]

def is_secure(mask):
    if cover[mask] != ALL:
        return False
    outside = ALL ^ mask
    while outside:
        b = outside & -outside
        outside ^= b
        u = b.bit_length() - 1
        guards = adj[u] & mask
        found = False
        while guards:
            g = guards & -guards
            guards ^= g
            if cover[(mask ^ g) | b] == ALL:
                found = True
                break
        if not found:
            return False
    return True

secure = {mask for mask in range(1 << N) if is_secure(mask)}
frequency = Counter(mask.bit_count() for mask in secure)
expected_frequency = {8:1755,9:13088,10:24624,11:24948,12:16899,13:8316,14:3042,
                      15:816,16:153,17:18,18:1}
assert dict(frequency) == expected_frequency, (frequency, expected_frequency)
minimal = {mask for mask in secure if not any((mask & (1 << v)) and
                                            ((mask ^ (1 << v)) in secure)
                                            for v in range(N))}
assert dict(Counter(s.bit_count() for s in minimal)) == {8:1755, 9:3224}
optima = sorted(mask for mask in secure if mask.bit_count() == 8)
assert len(optima) == 1755
index = {s:i for i,s in enumerate(optima)}

def make_moves(slide):
    graph = [[] for _ in optima]
    for i, mask in enumerate(optima):
        chosen = mask
        while chosen:
            bu = chosen & -chosen
            chosen ^= bu
            u = bu.bit_length() - 1
            candidates = (adj[u] if slide else ALL) & ~mask
            while candidates:
                bv = candidates & -candidates
                candidates ^= bv
                j = index.get(mask ^ bu ^ bv)
                if j is not None:
                    graph[i].append(j)
        assert len(graph[i]) == len(set(graph[i]))
    for i, nbrs in enumerate(graph):
        assert all(i in graph[j] for j in nbrs)
    return graph

def distances(graph):
    ecc = Counter()
    histogram = Counter()
    for source in range(len(graph)):
        distances = [-1] * len(graph)
        distances[source] = 0
        q = deque([source])
        while q:
            u = q.popleft()
            for v in graph[u]:
                if distances[v] == -1:
                    distances[v] = distances[u] + 1
                    q.append(v)
        assert min(distances) >= 0
        ecc[max(distances)] += 1
        histogram.update(distances)
    return ecc, histogram

jump = make_moves(False)
slide = make_moves(True)
assert sum(map(len, jump)) // 2 == 12798
assert sum(map(len, slide)) // 2 == 4320
assert Counter(map(len, jump)) == {8:108,10:216,11:108,12:108,13:216,16:432,17:108,18:432,28:27}
assert Counter(map(len, slide)) == {2:216,3:324,4:216,5:756,10:108,11:108,12:27}
assert distances(jump)[0] == {8:1755}
assert distances(slide)[0] == {9:1539,10:216}

def make_maps():
    maps = []
    for a in (1,2):
      inva = a
      for d in (1,2):
       for b in range(3):
        for c in range(3):
         for e in range(3):
          perm = [None] * N
          for x in range(3):
           for y in range(3):
            perm[point_id(x,y)] = point_id((a*x+b)%3,(c*x+d*y+e)%3)
          for m in range(3):
           for q in range(3):
            mt = ((c+d*m)*inva)%3
            qt = (d*q+e-mt*b)%3
            perm[line_id(m,q)] = line_id(mt,qt)
          maps.append(tuple(perm))
    dual = [None] * N
    for x in range(3):
     for y in range(3):
      dual[point_id(x,y)] = line_id(x,(-y)%3)
    for m in range(3):
     for b in range(3):
      dual[line_id(m,b)] = point_id(m,(-b)%3)
    maps += [tuple(dual[p[v]] for v in range(N)) for p in list(maps)]
    assert len(set(maps)) == 216
    for p in maps:
        for u in range(N):
            assert sum(1<<p[v] for v in range(N) if (adj[u]>>v)&1) == adj[p[u]]
    return maps

automorphisms = make_maps()
unseen = set(optima)
orbits = []
while unseen:
    s = min(unseen)
    orbit = {sum(1 << p[v] for v in range(N) if s & (1<<v)) for p in automorphisms}
    assert orbit <= unseen
    orbits.append(len(orbit))
    unseen -= orbit
assert Counter(orbits) == {27:1,108:8,216:4}
print('PAPPUS_SECURE_VERIFY_OK')
print('secure polynomial:', sorted(frequency.items()))
print('minimal polynomial:', [(8,1755),(9,3224)])
print('minimum slide:', len(optima), 4320, 'radius=9 diameter=10')
print('minimum jump:', len(optima), 12798, 'radius=8 diameter=8')
print('automorphisms=216; optimum orbit sizes:', sorted(orbits))
