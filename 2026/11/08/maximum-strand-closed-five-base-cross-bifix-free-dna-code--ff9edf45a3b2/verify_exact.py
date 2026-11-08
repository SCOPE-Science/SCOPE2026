#!/usr/bin/env python3
"""Exact proof-certificate validator: standard library only."""
import json
from itertools import product,combinations
from pathlib import Path

D=Path(__file__).resolve().parent
cert=json.loads((D/'certificate.json').read_text(encoding='utf-8'))
comp=str.maketrans('ACGT','TGCA')
def reverse_complement(w):
    return w.translate(comp)[::-1]
def bad(a,b):
    return any(a[:k]==b[-k:] for k in range(1,5))

# Every possible word whose first symbol lies in the canonical transversal.
possible=[''.join(v) for v in product('ACGT', repeat=5) if v[0] in 'AC' and v[-1] in 'GT']
assert len(possible)==256
seen=set()
vertices=[]
for word in possible:
    if word in seen:
        continue
    orbit=sorted({word,reverse_complement(word)})
    assert all(v in possible for v in orbit)
    seen.update(orbit)
    if any(bad(u,v) for u in orbit for v in orbit):
        continue
    vertices.append(orbit)
assert len(seen)==256
assert len(vertices)==56
assert all(len(orbit)==2 for orbit in vertices)
assert vertices==cert['orbit_table']
conflict=set()
for i,j in combinations(range(len(vertices)),2):
    if any(bad(a,b) or bad(b,a) for a in vertices[i] for b in vertices[j]):
        conflict.add((i,j))
assert len(conflict)==cert['edge_count']==412

partition=cert['clique_partition']
assert len(partition)==cert['upper_bound_orbits']==18
assert sorted(i for block in partition for i in block)==list(range(56))
assert all((i,j) in conflict for block in partition for i,j in combinations(sorted(block),2))
# Each block is a clique, so a compatible code selects <=1 orbit per block.
# In odd length every reverse-complement orbit has two members.
upper_bound=2*len(partition)
assert upper_bound==36

chosen=cert['selected_orbits']
assert len(chosen)==18 and len(set(chosen))==18
assert all(0<=i<len(vertices) for i in chosen)
assert all((i,j) not in conflict for i,j in combinations(sorted(chosen),2))
witness=sorted(word for i in chosen for word in vertices[i])
assert len(witness)==upper_bound==cert['achieved_words']==36
assert witness==(D/'witness.txt').read_text(encoding='ascii').splitlines()
assert {reverse_complement(w) for w in witness}==set(witness)
assert not any(bad(a,b) for a in witness for b in witness)
print('EXACT_CERTIFICATE_OK: 256 canonical words, 56 admissible orbits, 412 conflicts, 18-clique upper bound 36, witness 36')
