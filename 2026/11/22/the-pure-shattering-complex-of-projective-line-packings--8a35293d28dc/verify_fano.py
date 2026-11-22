"""Independent labelled-Fano realization of packing incidence and shattering.

Run: python3 verify_fano.py. Standard Python library only.
"""
from itertools import combinations, permutations
from collections import Counter

# Seven triples forming PG(2,2), with points encoded by nonzero F_2^3 vectors.
fano = sorted({tuple(sorted((a, b, a ^ b))) for a, b in combinations(range(1, 8), 2)})
assert len(fano) == 7
spread_labels = list(combinations(range(8), 3))
spread_index = {s: i for i, s in enumerate(spread_labels)}
packings = set()
for assignment in permutations(range(8), 7):
    p = tuple(sorted(spread_index[tuple(sorted(assignment[x-1] for x in triple))]
                     for triple in fano))
    packings.add(p)
assert len(packings) == 240
for p in packings:
    assert all(len(set(spread_labels[a]) & set(spread_labels[b])) == 1
               for a, b in combinations(p, 2))

mult = [Counter() for _ in range(6)]
for p in packings:
    for k in range(1, 6):
        mult[k].update(combinations(p, k))
assert [len(mult[i]) for i in range(1,6)] == [56,840,4200,7560,5040]
assert [Counter(mult[i].values()) for i in range(1,6)] == [
  Counter({30:56}),Counter({6:840}),Counter({2:4200}),
  Counter({1:6720,2:840}),Counter({1:5040})]

# Full Boolean-trace enumeration from independently generated hypotheses.
concepts = [sum(1 << v for v in p) for p in packings]
def has_all_patterns(s):
    return len({sum((1 << j) for j, x in enumerate(s) if c & (1 << x))
                for c in concepts}) == (1 << len(s))
for k in (2,3,4,5):
    assert sum(has_all_patterns(s) for s in mult[k]) == (840,4200,6720,0)[k-2]

# An even permutation of 8 labels acts on the 56 labelled spreads.
triples = list(spread_index)
baseops = []
for a in range(6):
    pm = list(range(8)); pm[a],pm[a+1],pm[a+2] = a+1,a+2,a
    baseops.append(tuple(spread_index[tuple(sorted(pm[i] for i in t))] for t in triples))
def orbit(seed):
    visited={seed};front=[seed]
    while front:
        t=front.pop()
        for op in baseops:
            u=tuple(sorted(op[i] for i in t))
            if u not in visited: visited.add(u); front.append(u)
    return visited
for m,expected in [(1,[3360,3360]),(2,[840])]:
    remaining={t for t,n in mult[4].items() if n==m};sizes=[]
    while remaining:
        orb=orbit(next(iter(remaining)))
        assert orb<=remaining
        sizes.append(len(orb));remaining-=orb
    assert sorted(sizes)==expected, (m,sizes)
print('FANO_PACKING_SHATTER_PASS 240 packings; facet orbits 3360+3360')
