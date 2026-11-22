"""Independent direct enumeration for the radius-one Q4 covering-code concept family.
Run: python3 verify_python.py
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, product

VERTICES = range(16)
FULL = (1 << 16) - 1

def radius_one_mask(u):
    return (1 << u) | sum(1 << (u ^ (1 << k)) for k in range(4))

balls = [radius_one_mask(x) for x in VERTICES]

def dominates(code):
    covered = 0
    for v in VERTICES:
        if code & (1 << v):
            covered |= balls[v]
    return covered == FULL

# Search all 2^16 subsets, not merely size-four candidates.
min_size = 17
codes = []
for code in range(1 << 16):
    k = code.bit_count()
    if k > min_size:
        continue
    if dominates(code):
        if k < min_size:
            min_size = k
            codes = []
        codes.append(code)
assert min_size == 4 and len(codes) == 40

# The parity argument and two distinct types of dominating code.
parity = [[i for i in VERTICES if i.bit_count() % 2 == p] for p in (0, 1)]
distance = lambda x, y: (x ^ y).bit_count()
types = Counter()
for code in codes:
    selected = [v for v in VERTICES if code & (1 << v)]
    e = [v for v in selected if v in parity[0]]
    o = [v for v in selected if v in parity[1]]
    assert len(e) == len(o) == 2
    assert distance(*e) == distance(*o)
    assert distance(*e) in (2, 4)
    types[distance(*e)] += 1
assert types == {2: 24, 4: 16}

pairs = Counter()
for a, b in combinations(VERTICES, 2):
    counts = Counter(((code >> a) & 1, (code >> b) & 1) for code in codes)
    trace = tuple(counts[x] for x in product((0, 1), repeat=2))
    pairs[(distance(a,b),trace)] += 1
assert pairs == {
    (1,(21,9,9,1)): 32, (2,(21,9,9,1)): 48,
    (3,(24,6,6,4)): 32, (4,(24,6,6,4)): 8,
}

triples = Counter()
for tri in combinations(VERTICES, 3):
    profile = tuple(sorted(distance(a,b) for a,b in combinations(tri,2)))
    counts = Counter(tuple((code >> v) & 1 for v in tri) for code in codes)
    assert len(counts) == 7
    missing = tuple(p for p in product((0, 1), repeat=3) if p not in counts)
    assert len(missing) == 1
    triples[(profile,missing[0])] += 1
# Order-free geometric classification: 400 triples omit all-ones; 160 omit
# a pair-positive pattern, with precisely one zero in a designated coordinate.
missing_by_type = Counter()
for tri in combinations(VERTICES, 3):
    p = tuple(sorted(distance(a,b) for a,b in combinations(tri,2)))
    counts = {tuple((code >> v) & 1 for v in tri) for code in codes}
    absent = next(x for x in product((0, 1), repeat=3) if x not in counts)
    missing_by_type[(p, sum(absent))] += 1
assert missing_by_type == {
    ((1,1,2),3): 96, ((1,2,3),3): 192,
    ((1,3,4),2): 64, ((2,2,2),3): 64,
    ((2,2,4),3): 48, ((2,3,3),2): 96,
}

# Adaptive recursion on actual subfamilies of the forty concepts.
ALL = (1 << len(codes)) - 1
query_masks = [sum(1 << i for i,c in enumerate(codes) if c & (1 << v)) for v in VERTICES]
@lru_cache(None)
def online_dimension(family):
    best = 0
    for yes in query_masks:
        a, b = family & yes, family & (~yes) & ALL
        if a and b:
            best = max(best, 1 + min(online_dimension(a), online_dimension(b)))
    return best
assert online_dimension(ALL) == 3
assert online_dimension(query_masks[0]) == 2

# A depth-three complete adaptive witness with 8 nonempty leaves.
witness_branches = [
    [(0,1),(7,1),(8,1)], [(0,1),(7,1),(8,0)],
    [(0,1),(7,0),(1,1)], [(0,1),(7,0),(1,0)],
    [(0,0),(1,1),(2,1)], [(0,0),(1,1),(2,0)],
    [(0,0),(1,0),(2,1)], [(0,0),(1,0),(2,0)],
]
for br in witness_branches:
    assert any(all(((c >> q) & 1) == label for q,label in br) for c in codes)
print('gamma=4; minimum_codes=40; two_parity_orbits=(16,24)')
print('pair_trace_distributions=',sorted((str(k),v) for k,v in pairs.items()))
print('triple_missing_geometry=',sorted((str(k),v) for k,v in missing_by_type.items()))
print('shattering_polynomial=1+16*z+120*z^2')
print('every_one_of_560_triples_has_exactly_7_of_8_traces')
print('VCdim=2; Ldim=3; witness_leaves=8')
print('PASS')
