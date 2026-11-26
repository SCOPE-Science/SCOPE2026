"""Exact finite certificate for the two-independence complex of the Heawood graph.

Run: python3 VERIFY.py. Uses only the Python standard library.
"""
import collections

N = 14
NEIGH = [0] * N
# Seven points 0,...,6 and seven Fano lines 7,...,13.
for j in range(7):
    for d in (0, 1, 3):
        i = (j + d) % 7
        NEIGH[i] |= 1 << (j + 7)
        NEIGH[j + 7] |= 1 << i
assert all(mask.bit_count() == 3 for mask in NEIGH)
assert sum(mask.bit_count() for mask in NEIGH) == 42
FACES = {
    s for s in range(1 << N)
    if all(not (s >> i & 1) or (s & NEIGH[i]).bit_count() <= 1
           for i in range(N))
}
for s in FACES:
    for i in range(N):
        if s & (1 << i):
            assert s ^ (1 << i) in FACES
assert 0 in FACES
counts = collections.Counter(s.bit_count() - 1 for s in FACES if s)
assert [counts[d] for d in range(7)] == [14, 91, 322, 651, 728, 392, 58]
print('f-vector:', [counts[d] for d in range(7)])
print('total faces including empty:', len(FACES))

# Sequential toggle matching; every chosen pair differs by the current vertex.
unmatched = set(FACES - {0})
pairs = {}
for i in range(N):
    bit = 1 << i
    for low in sorted(unmatched):
        high = low | bit
        if low in unmatched and not (low & bit) and high in unmatched:
            unmatched.remove(low)
            unmatched.remove(high)
            pairs[low] = high
assert all(low in FACES and high in FACES and
           high.bit_count() == low.bit_count()+1 for low, high in pairs.items())
assert len(pairs) * 2 + len(unmatched) == len(FACES) - 1
crit = collections.Counter(s.bit_count() - 1 for s in unmatched)
assert crit == {0: 1, 5: 13}
print('matched pairs:', len(pairs), 'critical cells:', sorted(crit.items()))

# Direct acyclicity certificate: orient every nonempty cover upper->lower,
# except matched covers lower->upper; topological sorting must remove every face.
indegree = {s: 0 for s in FACES if s}
arcs = collections.defaultdict(list)
for upper in indegree:
    for i in range(N):
        if not upper & (1 << i):
            continue
        lower = upper ^ (1 << i)
        if not lower:
            continue
        u, v = (lower, upper) if pairs.get(lower) == upper else (upper, lower)
        arcs[u].append(v)
        indegree[v] += 1
queue = collections.deque(s for s in indegree if indegree[s] == 0)
seen = 0
while queue:
    x = queue.popleft()
    seen += 1
    for y in arcs[x]:
        indegree[y] -= 1
        if indegree[y] == 0:
            queue.append(y)
assert seen == len(FACES) - 1
print('directed Hasse diagram acyclic:', seen, 'nonempty faces')

# Independent simplicial boundary ranks over F_2, using bit-packed exact elimination.
by_dim = {d: sorted(s for s in FACES if s.bit_count() == d + 1)
          for d in range(7)}
ranks = {}
for d in range(1, 7):
    ids = {face: k for k, face in enumerate(by_dim[d-1])}
    pivots = {}
    for face in by_dim[d]:
        col = 0
        for i in range(N):
            if face & (1 << i):
                col ^= 1 << ids[face ^ (1 << i)]
        while col:
            top = col.bit_length() - 1
            if top in pivots:
                col ^= pivots[top]
            else:
                pivots[top] = col
                break
    ranks[d] = len(pivots)
assert [ranks[d] for d in range(1,7)] == [13, 78, 244, 407, 321, 58]
betti = {d: len(by_dim[d]) - (ranks[d] if d else 1) - ranks.get(d+1, 0)
         for d in range(7)}
assert betti == {d: (13 if d == 5 else 0) for d in range(7)}
print('mod-2 ranks:', [ranks[d] for d in range(1,7)])
print('reduced mod-2 Betti numbers:', [betti[d] for d in range(7)])
print('ALL_CHECKS_PASS')
