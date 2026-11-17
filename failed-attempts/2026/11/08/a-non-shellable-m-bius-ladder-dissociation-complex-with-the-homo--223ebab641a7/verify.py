"""Reproduce the integral homotopy classification of the M14 dissociation complex.

Run: python3 verify.py
Requires only Python 3 standard library.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations

N = 14
ORDER = (7, 9, 0, 1, 5, 12, 3, 11, 2, 13, 8, 4, 10, 6)
CRITICAL_EXPECTED = (128, 3141, 4373, 9556)

neighbors = []
for v in range(N):
    neighbors.append(frozenset(((v - 1) % N, (v + 1) % N, (v + 7) % N)))
    assert len(neighbors[-1]) == 3
assert all(v in neighbors[u] for v in range(N) for u in neighbors[v])

forbidden = {sum(1 << x for x in (v, a, b))
             for v in range(N) for a, b in combinations(sorted(neighbors[v]), 2)}
assert len(forbidden) == 42

faces = []
for s in range(1, 1 << N):
    # Test 1: every selected vertex has induced degree at most one.
    degree_test = all(sum(bool(s & (1 << u)) for u in neighbors[v]) <= 1
                      for v in range(N) if s & (1 << v))
    # Test 2: no selected triple forms a (not necessarily induced) 3-vertex path.
    triple_test = not any((s & t) == t for t in forbidden)
    assert degree_test == triple_test, (s, degree_test, triple_test)
    if degree_test:
        faces.append(s)
F = set(faces)
fvector = Counter(s.bit_count() - 1 for s in F)
assert [fvector[i] for i in range(7)] == [14, 91, 322, 644, 658, 287, 30]
assert len(F) == 2046

facets = [s for s in faces if not any((s | (1 << v)) in F for v in range(N) if not (s & (1 << v)))]
facet_counts = Counter(s.bit_count() - 1 for s in facets)
assert facet_counts == {5: 119, 6: 30}

# Sequential vertex-toggle matching: each pair is removed permanently from the
# unmatched face poset before the next coordinate is considered.
live = set(F)
pairs = []
for v in ORDER:
    bit = 1 << v
    for a in sorted(live):
        if a & bit:
            continue
        b = a | bit
        if b in live:
            live.remove(a)
            live.remove(b)
            pairs.append((a, b))
critical = tuple(sorted(live))
assert critical == CRITICAL_EXPECTED, critical
assert Counter(s.bit_count() - 1 for s in critical) == {0: 1, 4: 2, 5: 1}
assert len(pairs) == 1021

upmatch = dict(pairs)
downmatch = {b: a for a, b in pairs}
assert len(upmatch) == len(downmatch) == 1021
assert not (set(upmatch) & set(downmatch))
assert set(upmatch) | set(downmatch) | set(critical) == F

# Hasse diagram: matched incidences point up; all others point down.
adj = defaultdict(list)
indegree = {s: 0 for s in F}
incidence_count = 0
for b in F:
    if b.bit_count() <= 1:
        continue
    for v in range(N):
        bit = 1 << v
        if not (b & bit):
            continue
        a = b ^ bit
        assert a in F
        incidence_count += 1
        if downmatch.get(b) == a:
            src, dst = a, b
        else:
            src, dst = b, a
        adj[src].append(dst)
        indegree[dst] += 1
assert incidence_count == 8946
queue = deque(s for s in faces if indegree[s] == 0)
processed = 0
while queue:
    s = queue.popleft()
    processed += 1
    for t in adj[s]:
        indegree[t] -= 1
        if indegree[t] == 0:
            queue.append(t)
assert processed == len(F), (processed, len(F))

# Orient each simplex by its increasing vertex labels.
def coefficient(b, a):
    bit = b ^ a
    assert bit.bit_count() == 1 and a == (b ^ bit)
    return -1 if ((b & (bit - 1)).bit_count() % 2) else 1

# Recursively project a k-face to its critical k-cells. An upward match
# substitutes the oriented boundary relation of its (k+1)-partner.
@lru_cache(None)
def flow(s):
    if s in live:
        return {s: 1}
    if s in downmatch:
        return {}
    b = upmatch[s]
    e = coefficient(b, s)
    out = defaultdict(int)
    for v in range(N):
        bit = 1 << v
        if (b & bit) and ((b ^ bit) != s):
            t = b ^ bit
            for c, val in flow(t).items():
                out[c] += -e * coefficient(b, t) * val
    return {c: v for c, v in out.items() if v != 0}

critical_five = next(s for s in critical if s.bit_count() == 6)
critical_fours = sorted(s for s in critical if s.bit_count() == 5)
result = defaultdict(int)
for v in range(N):
    bit = 1 << v
    if critical_five & bit:
        t = critical_five ^ bit
        for c, val in flow(t).items():
            result[c] += coefficient(critical_five, t) * val
morse_column = tuple(result[c] for c in critical_fours)
assert morse_column == (-1, -1), morse_column

# Independent homology calculation over F2 using original signed-simplex
# boundaries, without using the Morse matching or flow algorithm.
by_dim = [[s for s in faces if s.bit_count() == d + 1] for d in range(7)]
def gf2_rank(columns):
    basis = {}
    for vec in columns:
        while vec:
            lead = vec.bit_length() - 1
            if lead in basis:
                vec ^= basis[lead]
            else:
                basis[lead] = vec
                break
    return len(basis)

boundary_ranks = [0] * 8
for k in range(1, 7):
    index = {s: i for i, s in enumerate(by_dim[k - 1])}
    columns = []
    for b in by_dim[k]:
        col = 0
        for v in range(N):
            if b & (1 << v):
                col ^= 1 << index[b ^ (1 << v)]
        columns.append(col)
    boundary_ranks[k] = gf2_rank(columns)
betti = [len(by_dim[k]) - boundary_ranks[k] - boundary_ranks[k+1] for k in range(7)]
assert betti == [1, 0, 0, 0, 1, 0, 0], betti

# The Morse chain complex has one 0-cell, two 4-cells and one 5-cell.
# Its 5-cell attaches to the wedge of two 4-spheres with primitive
# degree vector (-1,-1). Since pi_4(S4 vee S4) = Z^2, a unimodular
# change of basis makes this a standard cancelling 4/5 cell pair.
print("GRAPH_VERTICES=14")
print("GRAPH_EDGES=21")
print("FORBIDDEN_3_PATHS=42")
print("FACE_VECTOR=" + str([fvector[i] for i in range(7)]))
print("TOTAL_NONEMPTY_FACES=" + str(len(F)))
print("FACET_DIMENSIONS=" + str(sorted(facet_counts.items())))
print("MATCHING_PAIRS=" + str(len(pairs)))
print("CRITICAL_MASKS=" + str(critical))
print("HASSE_INCIDENCES=" + str(incidence_count))
print("ACYCLES_TOPO_SORT=" + str(processed))
print("MORSE_D5_COLUMN=" + str(morse_column))
print("MOD2_BOUNDARY_RANKS=" + str(boundary_ranks[1:7]))
print("MOD2_BETTI=" + str(betti))
print("INTEGRAL_HOMOTOPY=S4")
print("NONPURE_SHELLABILITY=EXCLUDED_BY_NO_4_FACETS_AND_H4")
print("ALL_CHECKS_PASS")
