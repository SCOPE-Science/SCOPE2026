"""Independent symmetry-reduced enumeration of Petersen vertex recolorings.

Usage: python3 verify_orbits.py
Vertices are indexed lexicographically by two-subsets of {0,1,2,3,4}.
Colours are the individually named integers 0,1,2,3.
"""
from collections import Counter, deque
from itertools import combinations, permutations

V = list(combinations(range(5), 2))
Vindex = {v: i for i, v in enumerate(V)}
neighbors = [set() for _ in V]
for i, v in enumerate(V):
    for j, w in enumerate(V):
        if i < j and set(v).isdisjoint(w):
            neighbors[i].add(j)
            neighbors[j].add(i)
assert len(V) == 10 and sum(map(len, neighbors)) == 30


def generate(k):
    result, current = [], [-1] * 10
    def rec(pos):
        if pos == len(V):
            result.append(tuple(current))
            return
        for color in range(k):
            if all(current[j] != color for j in neighbors[pos] if j < pos):
                current[pos] = color
                rec(pos + 1)
        current[pos] = -1
    rec(0)
    return result


def graph(states, k):
    lookup = {s: i for i, s in enumerate(states)}
    edges = [[] for _ in states]
    for q, coloring in enumerate(states):
        for v in range(10):
            forbidden = {coloring[j] for j in neighbors[v]}
            for c in range(k):
                if c != coloring[v] and c not in forbidden:
                    other = coloring[:v] + (c,) + coloring[v+1:]
                    edges[q].append(lookup[other])
    return edges


def distances(adj, src):
    ds = [-1] * len(adj)
    ds[src] = 0
    todo = deque([src])
    while todo:
        u = todo.popleft()
        for v in adj[u]:
            if ds[v] < 0:
                ds[v] = ds[u] + 1
                todo.append(v)
    return ds


def canonical_colors(coloring):
    table, result = {}, []
    for c in coloring:
        if c not in table:
            table[c] = len(table)
        result.append(table[c])
    return tuple(result)

s3 = generate(3)
a3 = graph(s3, 3)
assert len(s3) == 120 and sum(map(len, a3)) == 120
assert all(len(adj) == 1 for adj in a3)
assert all(a3[a3[i][0]][0] == i for i in range(len(s3)))
print('THREE_COLOURS states=120 edges=60 components=60 each_size=2')

s4 = generate(4)
a4 = graph(s4, 4)
index = {s:i for i,s in enumerate(s4)}
assert len(s4) == 12960 and sum(map(len,a4)) == 106560
relabels = []
for p in permutations(range(5)):
    relabels.append(tuple(Vindex[tuple(sorted((p[u], p[v])))] for u,v in V))
assert len(relabels) == 120
canon_states = {canonical_colors(c) for c in s4}
unseen = set(canon_states)
orbits = []
while unseen:
    representative = min(unseen)
    orbit = {
        canonical_colors(tuple(representative[p[i]] for i in range(10)))
        for p in relabels
    }
    assert orbit <= canon_states
    unseen -= orbit
    # Every canonical colouring admits 24 injections of its used colours
    # into four named colours: all have at least three used colours.
    assert len(set(representative)) in (3, 4)
    orbit_size = len(orbit) * 24
    ds = distances(a4, index[representative])
    assert min(ds) == 0 and -1 not in ds
    shells = Counter(ds)
    hist = [shells[r] for r in range(max(ds)+1)]
    orbits.append((representative, orbit_size, max(ds), hist))

orbits.sort(key=lambda item: item[0])
assert len(canon_states) == 540 and len(orbits) == 11
assert sum(row[1] for row in orbits) == 12960
pair_distance = Counter()
ecc = Counter()
for representative, size, e, hist in orbits:
    ecc[e] += size
    for d in range(1,len(hist)):
        pair_distance[d] += size * hist[d] # oriented pairs (divide later)
    print('ORBIT', ''.join(map(str,representative)), 'states',size,'ecc',e,'last_shell',hist[-1], 'shells',','.join(map(str,hist)))
assert all(count%2==0 for count in pair_distance.values())
pair_distance = {d:count//2 for d,count in sorted(pair_distance.items())}
assert len(pair_distance) == 14 and sum(pair_distance.values()) == 12960*12959//2
assert ecc == Counter({13:3360,14:9600})
assert pair_distance[14] == 44400
print('FOUR_COLOURS states=12960 edges=53280 components=1 radius=13 diameter=14')
print('ECCENTRICITIES',dict(sorted(ecc.items())))
print('UNORDERED_PAIRS',pair_distance)

# A reproducible pair attaining the diameter. Its integer packing is deliberately
# different from the base-four lexicographic state ordering used above.
def unpack(x):
    return tuple((x>>(2*i))&3 for i in range(10))
start, target = unpack(5547), unpack(518224)
a, b = index[start], index[target]
assert distances(a4,a)[b] == 14
parent = [-1]*len(s4)
parent[a] = a
queue = deque([a])
while queue and parent[b] == -1:
    u = queue.popleft()
    for v in a4[u]:
        if parent[v] == -1:
            parent[v] = u
            queue.append(v)
path = [b]
while path[-1] != a:
    path.append(parent[path[-1]])
path.reverse()
assert len(path) == 15
assert all(sum(x != y for x,y in zip(s4[u],s4[v])) == 1 for u,v in zip(path,path[1:]))
print('DIAMETRAL_PATH', ' -> '.join(''.join(map(str,s4[i])) for i in path))
print('ALL_SYMMETRY_CHECKS_PASSED')
