#!/usr/bin/env python3
"""Exact verification of the 72 sixers and 36 double-sixes on a six-point plane blow-up.
Only Python's standard library is required. All calculations are over the integers.
"""
from collections import Counter
from itertools import combinations, permutations

N = 6
LABELS = tuple(range(N))

# A divisor dH - sum m_i E_i is represented by (d,m_0,...,m_5).
E = [(0, *(-int(j == i) for j in LABELS)) for i in LABELS]
PAIR_LABELS = list(combinations(LABELS, 2))
L = [(1, *(int(j in pair) for j in LABELS)) for pair in PAIR_LABELS]
Q = [(2, *(int(j != i) for j in LABELS)) for i in LABELS]
LINES = tuple(E + L + Q)
assert len(LINES) == 27 and len(set(LINES)) == 27
LINE_IDS = {c: i for i, c in enumerate(LINES)}

def intersect(a, b):
    return a[0] * b[0] - sum(x * y for x, y in zip(a[1:], b[1:]))

assert all(intersect(x, x) == -1 for x in LINES)
assert all(intersect(LINES[i], LINES[j]) in (0, 1)
           for i, j in combinations(range(27), 2))

# Full independent enumeration, with no assumed group orbit decomposition.
SIXERS = frozenset(frozenset(s) for s in combinations(range(27), 6)
                  if all(intersect(LINES[i], LINES[j]) == 0
                         for i, j in combinations(s, 2)))
assert len(SIXERS) == 72

def structured_sixers():
    z = {frozenset(range(6)), frozenset(range(21, 27))}
    for i in LABELS:
        for j in LABELS:
            if i == j:
                continue
            star = [6 + PAIR_LABELS.index(tuple(sorted((j, k))))
                    for k in LABELS if k not in (i, j)]
            z.add(frozenset([i, 21+i, *star]))
    for subset in combinations(LABELS, 3):
        subset = set(subset)
        complement = set(LABELS) - subset
        edge_indices = [6 + PAIR_LABELS.index(pair)
                        for pair in combinations(sorted(complement), 2)]
        z.add(frozenset([*subset, *edge_indices]))
        z.add(frozenset([*(21+i for i in subset), *edge_indices]))
    return frozenset(z)

assert SIXERS == structured_sixers()

# This incidence-only definition of the complementary half is independent of
# the 1+30+20+20 representation.
COMPLEMENT = {}
for s in SIXERS:
    partners = [t for t in SIXERS if s.isdisjoint(t) and
                all(sum(intersect(LINES[a], LINES[b]) for b in t) == 5
                    for a in s)]
    assert len(partners) == 1
    COMPLEMENT[s] = partners[0]
assert all(COMPLEMENT[COMPLEMENT[s]] == s and COMPLEMENT[s] != s
           for s in SIXERS)
DOUBLES = frozenset(frozenset((s, COMPLEMENT[s])) for s in SIXERS)
assert len(DOUBLES) == 36

# Compare geometric complementary-six operation with the explicit S_6-orbit formulas.
assert COMPLEMENT[frozenset(range(6))] == frozenset(range(21, 27))
for i in LABELS:
    for j in LABELS:
        if i == j:continue
        def pair_sixer(a, b):
            return frozenset([a,21+a,*[6+PAIR_LABELS.index(tuple(sorted((b,k))))
                    for k in LABELS if k not in (a,b)]])
        assert COMPLEMENT[pair_sixer(i,j)] == pair_sixer(j,i)
for subset in combinations(LABELS, 3):
    A = set(subset)
    B = set(LABELS) - A
    LA = {6+PAIR_LABELS.index(pair) for pair in combinations(sorted(A), 2)}
    LB = {6+PAIR_LABELS.index(pair) for pair in combinations(sorted(B), 2)}
    UA = frozenset(A | LB)
    VB = frozenset({21+i for i in B} | LA)
    assert COMPLEMENT[UA] == VB

def relabel_line(j, p):
    x = LINES[j]
    m = [0] * N
    for i in LABELS:
        m[p[i]] = x[1+i]
    return LINE_IDS[(x[0], *m)]

def cycle_type(p):
    unseen = set(LABELS)
    parts = []
    while unseen:
        i = min(unseen)
        j = i
        size = 0
        while j in unseen:
            unseen.remove(j)
            size += 1
            j = p[j]
        parts.append(size)
    return tuple(sorted(parts, reverse=True))

def orbit_profile(objects, action):
    remaining = set(objects)
    cnt = Counter()
    while remaining:
        start = next(iter(remaining))
        x = start
        steps = 0
        while x in remaining:
            remaining.remove(x)
            steps += 1
            x = action[x]
        assert x == start
        cnt[steps] += 1
    return dict(sorted(cnt.items()))

def formula_fixed(p):
    fixed_labels = sum(p[i] == i for i in LABELS)
    # A subset is invariant iff it is a union of whole permutation cycles.
    cycles = []
    seen = set()
    for i in LABELS:
        if i in seen:continue
        v = i
        cc = []
        while v not in seen:
            seen.add(v)
            cc.append(v)
            v = p[v]
        cycles.append(cc)
    u2 = sum(sum(map(len, xs)) == 2
             for k in range(len(cycles)+1)
             for xs in combinations(cycles, k))
    u3 = sum(sum(map(len, xs)) == 3
             for k in range(len(cycles)+1)
             for xs in combinations(cycles, k))
    return (2+2*u3+fixed_labels*(fixed_labels-1), 1+u2+u3,
            sum(len(c) == 2 for c in cycles))

RESULTS = {}
for p in permutations(LABELS):
    perm = tuple(relabel_line(j, p) for j in range(27))
    sixer_action = {s:frozenset(perm[j] for j in s) for s in SIXERS}
    assert set(sixer_action.values()) == set(SIXERS)
    double_action = {d:frozenset(sixer_action[s] for s in d) for d in DOUBLES}
    assert set(double_action.values()) == set(DOUBLES)
    six_prof = orbit_profile(SIXERS, sixer_action)
    double_prof = orbit_profile(DOUBLES, double_action)
    fixed_six = six_prof.get(1, 0)
    fixed_double = double_prof.get(1, 0)
    swapped_halves = sum(1 for d in DOUBLES if double_action[d] == d
                         and all(sixer_action[s] != s for s in d))
    assert (fixed_six, fixed_double, swapped_halves) == formula_fixed(p)
    assert fixed_six + 2*swapped_halves == 2*fixed_double
    assert sum(k*v for k, v in six_prof.items()) == 72
    assert sum(k*v for k, v in double_prof.items()) == 36
    key = cycle_type(p)
    outcome = (six_prof, double_prof, fixed_six, fixed_double, swapped_halves)
    if key in RESULTS:assert RESULTS[key] == outcome
    else:RESULTS[key] = outcome

EXPECTED = {
    (1,1,1,1,1,1):({1:72},72,36,0),
    (2,1,1,1,1):({1:30,2:21},30,16,1),
    (2,2,1,1):({1:12,2:30},12,8,2),
    (2,2,2):({1:2,2:35},2,4,3),
    (3,1,1,1):({1:12,3:20},12,6,0),
    (3,2,1):({1:6,2:3,3:8,6:6},6,4,1),
    (3,3):({1:6,3:22},6,3,0),
    (4,1,1):({1:4,2:4,4:15},4,2,0),
    (4,2):({1:2,2:5,4:15},2,2,1),
    (5,1):({1:2,5:14},2,1,0),
    (6,):({1:2,2:2,6:11},2,1,0),
}
assert len(RESULTS) == len(EXPECTED) == 11
for partition, (prof, _, n_s, n_d, swapped) in RESULTS.items():
    assert (prof, n_s, n_d, swapped) == EXPECTED[partition]
for k in sorted(RESULTS, reverse=True):
    prof, _, s, d, flipped = RESULTS[k]
    print(f'{k}: {prof}, rational_sixers={s}, rational_double_sixes={d}, exchanged_halves={flipped}')
print('CUBIC_SIXER_S6_FROBENIUS_EXHAUSTIVE_OK')
