#!/usr/bin/env python3
"""Exhaustive direct census of comma-free permutation 4-mer codes.
Runs using Python 3 standard library only. All loops have fixed finite ranges.
"""
from itertools import permutations, product
from collections import Counter
from pathlib import Path

alphabet = '0123'
words = tuple(''.join(t) for t in permutations(alphabet))
seen = set()
rotation_classes = []
for word in words:
    if word in seen:
        continue
    orbit = tuple(word[k:] + word[:k] for k in range(4))
    assert len(set(orbit)) == 4
    rotation_classes.append(orbit)
    seen.update(orbit)
assert len(rotation_classes) == 6 and seen == set(words)

def comma_free(code):
    return all((u[k:] + v[:k]) not in code
               for u in code for v in code for k in (1,2,3))

def non_overlapping(code):
    return all(u[:k] != v[-k:] for u in code for v in code for k in (1,2,3))

maximum = set()
for choice in product(*rotation_classes):
    code = frozenset(choice)
    if comma_free(code):
        maximum.add(code)
assert len(maximum) == 2872
assert sum(non_overlapping(code) for code in maximum) == 32
symmetries = []
for labeling in permutations(alphabet):
    mapping = dict(zip(alphabet, labeling))
    for reflected in (False, True):
        def transform(code, mapping=mapping, reflected=reflected):
            return frozenset(''.join(mapping[c] for c in (w[::-1] if reflected else w)) for w in code)
        symmetries.append(transform)
assert len(symmetries) == 48
remaining = set(maximum)
orbits = []
while remaining:
    representative = min(remaining, key=lambda c:tuple(sorted(c)))
    orbit = {g(representative) for g in symmetries}
    assert orbit <= maximum
    orbits.append((tuple(sorted(representative)), orbit))
    remaining.difference_update(orbit)
assert len(orbits) == 73
assert Counter(len(o) for rep,o in orbits) == {8:4,16:2,24:17,48:50}
# A machine-readable canonical list for every isomorphism class.
reps = sorted((len(o), rep) for rep,o in orbits)
content = 'orbit_size\t' + '\t'.join('word'+str(j) for j in range(1,7)) + '\n'
content += ''.join(str(sz)+'\t'+'\t'.join(rep)+'\n' for sz,rep in reps)
path = Path(__file__).with_name('ORBIT_REPRESENTATIVES.tsv')
if path.exists():
    assert path.read_text(encoding='utf-8') == content
else:
    path.write_text(content, encoding='utf-8')
print('DIRECT_OK candidate_combinations=4096 optimum=6 labeled_optima=2872 orbits=73 orbit_sizes=8:4,16:2,24:17,48:50 nonoverlap=32')
