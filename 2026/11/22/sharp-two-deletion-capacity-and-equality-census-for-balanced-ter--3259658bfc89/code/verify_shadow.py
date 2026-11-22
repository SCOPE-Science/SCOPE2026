#!/usr/bin/env python3
"""Independent finite theorem checker: exact two-symbol deletion shadows.

Run: python3 verify_shadow.py
No external dependencies; all integer operations.
"""
from itertools import combinations, permutations
from collections import Counter

WORDS = sorted(set(permutations((0, 0, 1, 1, 2, 2))))
assert len(WORDS) == 90
shadows = [frozenset(tuple(w[i] for i in I) for I in combinations(range(6), 4)) for w in WORDS]
compatible = []
for i in range(90):
    mask = sum(1 << j for j in range(i+1,90) if not(shadows[i] & shadows[j]))
    compatible.append(mask)

histogram = [0]*6
foursets = []
def enumerate_cliques(prefix, possible):
    depth = len(prefix)
    histogram[depth] += 1
    if depth == 4:
        foursets.append(prefix)
    if depth == 5:
        raise AssertionError('a five-word code exists')
    while possible:
        bit = possible & -possible
        j = bit.bit_length() - 1
        possible ^= bit
        enumerate_cliques(prefix + (j,), possible & compatible[j])

enumerate_cliques((), (1 << 90)-1)
assert histogram == [1, 90, 1164, 1788, 144, 0], histogram
assert len(set(foursets)) == 144
s_index = {w:i for i,w in enumerate(WORDS)}
actions = []
for p in permutations((0,1,2)):
    for reflect in (False, True):
        actions.append(tuple(s_index[tuple(p[k] for k in (w[::-1] if reflect else w))] for w in WORDS))
assert len(set(actions)) == 12
remaining = set(foursets)
orbit_reps = []
while remaining:
    rep = min(remaining)
    orbit = {tuple(sorted(f[i] for i in rep)) for f in actions}
    assert orbit <= remaining
    remaining.difference_update(orbit)
    orbit_reps.append((rep, len(orbit)))
assert Counter(size for _,size in orbit_reps) == {6:4, 12:10}

# Construct and check a maximal code, including the decoder's uniqueness.
witness = ['012201','102102','200211','211200']
wi = [s_index[tuple(map(int,w))] for w in witness]
assert len(set(wi)) == 4
assert all(not(shadows[i]&shadows[j]) for i,j in combinations(wi,2))
assert tuple(sorted(wi)) in foursets

print('word_count=90')
print('compatible_k_set_histogram=' + str(histogram))
print('maximum_size=4')
print('maximal_codebook_count=144')
print('orbit_counts=' + str(dict(sorted(Counter(size for _,size in orbit_reps).items()))))
print('witness=' + ','.join(witness))
for code,size in orbit_reps:
    print('orbit', size, ','.join(''.join(map(str,WORDS[i])) for i in code))
