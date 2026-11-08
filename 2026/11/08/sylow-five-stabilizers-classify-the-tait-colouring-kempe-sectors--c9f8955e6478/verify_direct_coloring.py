"""Independent exact verifier: edge-colour constraint search and Kempe chains.
Python 3 standard library; run: python verify_direct_coloring.py
"""
from collections import Counter, deque
from itertools import combinations, permutations

DUADS = list(combinations(range(6), 2))

def synthemes(points):
    if not points:
        yield ()
        return
    a = points[0]
    for b in points[1:]:
        for tail in synthemes(tuple(x for x in points[1:] if x != b)):
            yield (tuple(sorted((a, b))),) + tail

SYNTHEMES = sorted(tuple(sorted(s)) for s in synthemes(tuple(range(6))))
EDGES = tuple((d, s) for d, duad in enumerate(DUADS)
              for s, syn in enumerate(SYNTHEMES) if duad in syn)
assert len(DUADS) == len(SYNTHEMES) == 15 and len(EDGES) == 45
# Each incidence-edge is a different variable; each duad and syntheme needs all 3 colours.
endpoints = [(d, 15+s) for d,s in EDGES]
incident = [set() for _ in range(30)]
for k,(a,b) in enumerate(endpoints):
    incident[a].add(k)
    incident[b].add(k)
assert all(len(q) == 3 for q in incident)
assignment = [-1] * 45
mask = [0] * 30
states = []

def extend(filled):
    if filled == 45:
        states.append(tuple(assignment)); return
    best, possibilities = -1, None
    for k,(a,b) in enumerate(endpoints):
        if assignment[k] >= 0: continue
        available = tuple(c for c in range(3) if not ((mask[a] | mask[b]) >> c) & 1)
        if not available: return
        if possibilities is None or len(available) < len(possibilities):
            best, possibilities = k, available
            if len(available) == 1: break
    a,b=endpoints[best]
    for c in possibilities:
        bit=1<<c
        assignment[best]=c
        mask[a]|=bit; mask[b]|=bit
        extend(filled+1)
        mask[a]^=bit; mask[b]^=bit
        assignment[best]=-1

# Fix colours on the first degree-three duad; all other named colourings
# are the six images under the palette's permutation group.
start = sorted(incident[0])
for k,c in zip(start, range(3)):
    a,b=endpoints[k]
    assignment[k]=c
    mask[a]|=1<<c; mask[b]|=1<<c
extend(3)
assert len(states) == 144
full = {tuple(p[x] for x in c) for c in states for p in permutations(range(3))}
assert len(full) == 864
C = sorted(full)
index = {x:i for i,x in enumerate(C)}

adjacent = [set() for _ in C]
for i,c in enumerate(C):
    for color1,color2 in combinations(range(3),2):
        remaining = {v for v in range(30) if any(c[e] in (color1,color2) for e in incident[v])}
        while remaining:
            source = min(remaining)
            reached={source}; queue=[source]
            while queue:
                u=queue.pop()
                for e in incident[u]:
                    if c[e] not in (color1,color2): continue
                    a,b=endpoints[e];v=b if a==u else a
                    if v not in reached:
                        reached.add(v);queue.append(v)
            remaining -= reached
            change = list(c)
            for e,(a,b) in enumerate(endpoints):
                if a in reached and b in reached:
                    if c[e] == color1: change[e]=color2
                    if c[e] == color2: change[e]=color1
            j=index[tuple(change)]
            adjacent[i].add(j)
assert all(len(t) == 5 for t in adjacent)
assert all(i in adjacent[j] for j,t in enumerate(adjacent) for i in t)
components=[]; seen=set()
for i in range(864):
    if i in seen: continue
    component={i}; frontier=[i]
    while frontier:
        for v in adjacent[frontier.pop()]:
            if v not in component: component.add(v);frontier.append(v)
    seen |= component; components.append(component)
assert len(components) == 36 and Counter(map(len,components)) == {24:36}

def canon(c):
    return tuple(sorted(tuple(i for i,k in enumerate(c) if k==j) for j in range(3)))

quotient = {}
distance_profiles = Counter()
for component in components:
    part_ids={canon(C[i]) for i in component}
    assert len(part_ids) == 4
    for x in part_ids:
        rep=next(i for i in component if canon(C[i])==x)
        neighbors={canon(C[j]) for j in adjacent[rep] if canon(C[j]) != x}
        quotient[x] = neighbors
        assert len(neighbors) == 2
    # Four vertices all with degree two and connected: an induced four-cycle.
    for initial in component:
        distance={initial:0};queue=deque([initial])
        while queue:
            u=queue.popleft()
            for v in adjacent[u]:
                if v not in distance:
                    distance[v] = distance[u]+1;queue.append(v)
        assert set(distance) == component
        profile=tuple(Counter(distance.values())[j] for j in range(4))
        distance_profiles[profile] += 1
assert len(quotient) == 144
assert distance_profiles == {(1,5,13,5):864}
print('DIRECT_864_COLOURINGS_FROM_144_NORMALIZED_PASS')
print('36_COMPONENTS_OF_24_QUOTIENT_FOUR_CYCLES_PASS')
print('ALL_864_DISTANCE_SPHERES_1_5_13_5_PASS')
print('5_REGULAR_2160_EDGES_RADIUS_DIAMETER_3_PASS')
