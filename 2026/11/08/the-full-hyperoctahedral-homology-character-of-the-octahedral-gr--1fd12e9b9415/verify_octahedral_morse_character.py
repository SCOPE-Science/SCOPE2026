#!/usr/bin/env python3
"""Exact finite verification of the octahedral rooted-forest Morse-complex character.

Requires only Python 3.9+ standard library. Run: python3 verify_octahedral_morse_character.py
"""
from itertools import combinations, permutations, product
from collections import Counter, defaultdict, deque

PAIRS = ((0, 1), (2, 3), (4, 5))
VERTICES = tuple(range(6))
EDGES = tuple((u, v) for u in VERTICES for v in range(u + 1, 6)
              if u // 2 != v // 2)
ARCS = tuple((u, v) for a, b in EDGES for u, v in ((a, b), (b, a)))
ARC_ID = {a: i for i, a in enumerate(ARCS)}
assert len(EDGES) == 12 and len(ARCS) == 24


def valid_arc_indices(indices):
    out = {}
    used_edges = set()
    for i in indices:
        u, v = ARCS[i]
        e = (min(u, v), max(u, v))
        if u in out or e in used_edges:
            return False
        used_edges.add(e)
        out[u] = v
    for u in out:
        seen = set()
        v = u
        while v in out:
            if v in seen:
                return False
            seen.add(v)
            v = out[v]
    return True


def enumerate_by_subsets():
    out = {0}
    for k in range(1, 6):
        for c in combinations(range(24), k):
            if valid_arc_indices(c):
                out.add(sum(1 << i for i in c))
    return out


def enumerate_by_tails():
    neighbors = tuple(tuple(v for v in VERTICES if u // 2 != v // 2)
                      for u in VERTICES)
    out = set()
    for assignment in product(*( (None,) + n for n in neighbors)):
        arcs = tuple(ARC_ID[(u, v)] for u, v in enumerate(assignment)
                     if v is not None)
        if valid_arc_indices(arcs):
            out.add(sum(1 << i for i in arcs))
    return out


FACES = enumerate_by_subsets()
assert FACES == enumerate_by_tails()
assert Counter(m.bit_count() for m in FACES) == {
    0: 1, 1: 24, 2: 228, 3: 1072, 4: 2496, 5: 2304
}

# Independent one-vertex-at-a-time greedy matching on the complete Hasse poset.
remaining = FACES - {0}
MATCHED_UP = set()
PAIRS_MATCHED = set()
for i in range(24):
    bit = 1 << i
    for lo in sorted(remaining):
        hi = lo | bit
        if not lo & bit and hi in remaining:
            PAIRS_MATCHED.add((lo, hi))
            remaining.remove(lo)
            remaining.remove(hi)
            MATCHED_UP.add((lo, hi))
assert len(PAIRS_MATCHED) == 2724
assert Counter(f.bit_count() - 1 for f in remaining) == {0: 1, 4: 675}

# Exhaustive acyclicity test: all incidences, reverse exactly the matched ones.
faces_nonempty = FACES - {0}
indegree = {f: 0 for f in faces_nonempty}
adjacency = defaultdict(list)
covers = 0
for upper in faces_nonempty:
    bits = upper
    while bits:
        bit = bits & -bits
        bits -= bit
        lower = upper ^ bit
        if lower == 0:
            continue
        if (lower, upper) in PAIRS_MATCHED:
            src, dst = lower, upper
        else:
            src, dst = upper, lower
        adjacency[src].append(dst)
        indegree[dst] += 1
        covers += 1
q = deque(f for f in faces_nonempty if indegree[f] == 0)
visited = 0
while q:
    v = q.popleft()
    visited += 1
    for w in adjacency[v]:
        indegree[w] -= 1
        if indegree[w] == 0:
            q.append(w)
assert visited == len(faces_nonempty)

# The complement of the octahedral graph is a perfect matching, so this is
# exactly the full automorphism group (the signed permutation group B_3).
GROUP = []
for p in permutations(range(3)):
    for flips in product((0, 1), repeat=3):
        g = tuple(2 * p[u // 2] + ((u % 2) ^ flips[u // 2])
                  for u in VERTICES)
        amap = tuple(ARC_ID[(g[u], g[v])] for u, v in ARCS)
        assert set(amap) == set(range(24))
        GROUP.append((p, flips, g, amap))
assert len(GROUP) == 48 and len({x[2] for x in GROUP}) == 48

FACE_LIST = tuple(sorted(f for f in FACES if f))

def signed_chain_trace(amap):
    t = [1, 0, 0, 0, 0, 0]  # 1 from the augmented empty simplex
    for f in FACE_LIST:
        x = tuple(i for i in range(24) if f >> i & 1)
        y = tuple(amap[i] for i in x)
        if sum(1 << j for j in y) != f:
            continue
        inv = sum(y[i] > y[j] for i in range(len(y))
                  for j in range(i + 1, len(y)))
        t[len(x)] += -1 if inv % 2 else 1
    return t


def signed_cycle_type(p, flips):
    seen = set()
    pos, neg = [], []
    for x in range(3):
        if x in seen:
            continue
        cycle = []
        y = x
        while y not in seen:
            seen.add(y)
            cycle.append(y)
            y = p[y]
        (neg if sum(flips[i] for i in cycle) % 2 else pos).append(len(cycle))
    return (tuple(sorted(pos, reverse=True)), tuple(sorted(neg, reverse=True)))

CLASS = defaultdict(list)
CHAR = {}
for p, flips, g, amap in GROUP:
    # A simplicial automorphism of the ordinary Morse complex preserves its
    # chain differential, with orientation signs induced by vertex order.
    for f in FACES:
        out = sum(1 << amap[i] for i in range(24) if f >> i & 1)
        assert out in FACES
    t = signed_chain_trace(amap)
    chi = -1 + sum((-1) ** (k - 1) * t[k] for k in range(1, 6))
    CLASS[signed_cycle_type(p, flips)].append(chi)
    CHAR[p, flips] = chi
assert len(CLASS) == 10 and all(len(set(v)) == 1 for v in CLASS.values())

EXPECTED = {
    ((), (1, 1, 1)): (1, -25),
    ((), (2, 1)): (6, 1),
    ((), (3,)): (8, -1),
    ((1,), (1, 1)): (3, -5),
    ((1,), (2,)): (6, 1),
    ((1, 1), (1,)): (3, -9),
    ((1, 1, 1), ()): (1, 675),
    ((2,), (1,)): (6, -15),
    ((2, 1), ()): (6, -3),
    ((3,), ()): (8, 3),
}
assert {typ: (len(a), a[0]) for typ, a in CLASS.items()} == EXPECTED
assert sum(len(a)*a[0] for a in CLASS.values()) == 48*11

# Build all irreducible characters via the bipartition induction formula for
# B_3 = C_2 wr S_3. No computer algebra or pre-tabulated character table.
PARTITIONS = {0: ((),), 1: ((1,),),
              2: ((2,), (1, 1)),
              3: ((3,), (2, 1), (1, 1, 1))}

def cycle_lengths(p, subset):
    seen = set()
    out = []
    for i in subset:
        if i in seen:
            continue
        x, length = i, 0
        while x not in seen:
            seen.add(x)
            x, length = p[x], length + 1
        out.append(length)
    return tuple(sorted(out, reverse=True))

def specht_character(part, cycle):
    n = sum(part)
    if n < 2 or part == (n,):
        return 1
    if part == (1,) * n:
        return (-1) ** (n - len(cycle))
    if part == (2, 1):
        return cycle.count(1) - 1
    raise AssertionError((part, cycle))

def irreducible_character(p, flips, plus, minus):
    total = 0
    for aa in combinations(range(3), sum(plus)):
        a = set(aa)
        b = set(range(3)) - a
        if {p[i] for i in a} != a:
            continue
        total += ((-1) ** sum(flips[i] for i in b)
                  * specht_character(plus, cycle_lengths(p, a))
                  * specht_character(minus, cycle_lengths(p, b)))
    return total

MULTIPLICITIES = {}
for a in range(4):
    for plus in PARTITIONS[a]:
        for minus in PARTITIONS[3-a]:
            scalar = sum(CHAR[p, flips] * irreducible_character(p, flips, plus, minus)
                         for p, flips, g, amap in GROUP)
            assert scalar % 48 == 0
            m = scalar // 48
            dim = irreducible_character((0, 1, 2), (0, 0, 0), plus, minus)
            assert m >= 0
            MULTIPLICITIES[(plus, minus)] = (dim, m)
assert sum(d*m for d, m in MULTIPLICITIES.values()) == 675
assert MULTIPLICITIES[((3,), ())] == (1, 11)

print('OCTAHEDRAL_MORSE_FULL_CHARACTER_PASS')
print('faces (augmented):', {k: v for k,v in sorted(Counter(f.bit_count() for f in FACES).items())})
print('Hasse covers:', covers, 'acyclic matching pairs:', len(PAIRS_MATCHED),
      'critical:', dict(sorted(Counter(f.bit_count()-1 for f in remaining).items())))
print('full automorphism group order:', len(GROUP))
for typ in sorted(CLASS):
    print('signed cycle type', typ, 'class size', len(CLASS[typ]),
          'H4 character', CLASS[typ][0])
for (plus, minus), (dim, m) in sorted(MULTIPLICITIES.items()):
    print('bipartition', (plus, minus), 'irreducible dimension', dim,
          'multiplicity', m)
print('central involution H4 trace:', CLASS[((),(1,1,1))][0])
print('central involution dimensions +,-:', 325, 350)
print('full group fixed H4 dimension:', 11)
