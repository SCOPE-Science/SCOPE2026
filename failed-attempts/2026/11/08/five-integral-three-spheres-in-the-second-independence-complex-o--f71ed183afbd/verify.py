"""Reproduce the integral homotopy type of the degree-one induced-subgraph complex of KG(6,2)."""
from collections import Counter, deque
from itertools import combinations

EDGES = list(combinations(range(6), 2))
N = len(EDGES)
assert N == 15
adj = [sum(1 << j for j, b in enumerate(EDGES)
           if i != j and set(a).isdisjoint(b)) for i, a in enumerate(EDGES)]

# Direct definition: induced graph has maximum degree <=1.
def valid_degree(mask):
    return all((adj[i] & mask).bit_count() <= 1
               for i in range(N) if mask & (1 << i))

FACES = {m for m in range(1, 1 << N) if valid_degree(m)}
assert len(FACES) == 746
assert Counter(m.bit_count() for m in FACES) == {1: 15, 2: 105, 3: 260,
                                                  4: 255, 5: 96, 6: 15}

# Independent definition: forbid any 3 vertices inducing at least two edges.
FORBIDDEN = []
for comb in combinations(range(N), 3):
    u, v, w = comb
    e = bool(adj[u] & (1 << v)) + bool(adj[v] & (1 << w)) + bool(adj[w] & (1 << u))
    if e >= 2:
        FORBIDDEN.append(sum(1 << i for i in comb))
assert all((m in FACES) == all(m & t != t for t in FORBIDDEN)
           for m in range(1, 1 << N))

# Sequential vertex-toggle discrete matching (only among not-yet-matched faces).
remaining = set(FACES)
matched = {}
for pivot in range(N):
    for low in sorted(remaining):
        high = low | (1 << pivot)
        if low != high and high in remaining:
            remaining.remove(low)
            remaining.remove(high)
            matched[low] = high
            matched[high] = low
assert len(matched) == 740 and len(remaining) == 6
assert Counter(m.bit_count()-1 for m in remaining) == {0: 1, 3: 5}
assert sorted(remaining) == [1, 5664, 10784, 19488, 28736, 29184]

# Exhaustive acyclicity test on the entire directed face Hasse diagram.
indeg = {m: 0 for m in FACES}
out = {m: [] for m in FACES}
covers = 0
for high in FACES:
    x = high
    while x:
        bit = x & -x
        low = high ^ bit
        if low:
            assert low in FACES
            if matched.get(low) == high:
                start, end = low, high
            else:
                start, end = high, low
            out[start].append(end)
            indeg[end] += 1
            covers += 1
        x ^= bit
q = deque(m for m in FACES if indeg[m] == 0)
seen = 0
while q:
    v = q.popleft()
    seen += 1
    for w in out[v]:
        indeg[w] -= 1
        if indeg[w] == 0:
            q.append(w)
assert seen == len(FACES), 'the matching had a directed cycle'

# Independent mod-two reduction of simplicial boundary operators.
def rank_F2(columns):
    pivots = {}
    for col in columns:
        while col:
            idx = col.bit_length()-1
            if idx not in pivots:
                pivots[idx] = col
                break
            col ^= pivots[idx]
    return len(pivots)

by_dim = [sorted(m for m in FACES if m.bit_count() == k) for k in range(1, 7)]
ranks = []
for k in range(1, 6):
    prev = {mask: ix for ix, mask in enumerate(by_dim[k-1])}
    columns = []
    for face in by_dim[k]:
        col = 0
        for i in range(N):
            if face >> i & 1:
                col ^= 1 << prev[face ^ (1 << i)]
        columns.append(col)
    ranks.append(rank_F2(columns))
assert ranks == [14, 91, 169, 81, 15], ranks
betti = [len(by_dim[k]) - (ranks[k-1] if k else 1) - (ranks[k] if k < 5 else 0)
         for k in range(6)]
assert betti == [0, 0, 0, 5, 0, 0], betti

print('Kneser pair vertices:', N)
print('Forbidden triples:', len(FORBIDDEN))
print('Face vector:', [len(v) for v in by_dim])
print('Matching pairs:', len(matched)//2)
print('Critical-cell count by dimension:', dict(sorted(Counter(m.bit_count()-1 for m in remaining).items())))
print('Poset covering relations:', covers)
print('Acyclicity topological-sort count:', seen)
print('Mod-two simplicial boundary ranks:', ranks)
print('Reduced mod-two Betti numbers:', betti)
print('ALL_KNESER_DISSOCIATION_CHECKS_PASS')
