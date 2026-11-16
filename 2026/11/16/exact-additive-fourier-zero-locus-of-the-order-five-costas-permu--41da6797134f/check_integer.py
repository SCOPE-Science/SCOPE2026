#!/usr/bin/env python3
"""Exact cyclotomic-zero census for order-five Costas permutation vectors."""
from itertools import permutations, product
from collections import Counter
import json
from pathlib import Path

P = list(permutations(range(5)))

def costas(p):
    return all(len({p[i+d]-p[i] for i in range(5-d)}) == 5-d for d in range(1,5))

C = [p for p in P if costas(p)]
assert len(P) == 120 and len(C) == 40

def reduce_frequency(k):
    t = [(x-k[0]) % 5 for x in k]
    first = next((x for x in t if x), 0)
    return (0,0,0,0,0) if not first else tuple(x * pow(first, -1, 5) % 5 for x in t)

def profile(data, k):
    result = [0]*5
    for p in data:
        result[sum(a*b for a,b in zip(k,p))%5] += 1
    return tuple(result)

Q=sorted({reduce_frequency(k) for k in product(range(5), repeat=5)})
assert len(Q) == 157
certificate = json.loads((Path(__file__).resolve().parent / 'certificate.json').read_text(encoding='utf8'))
assert certificate['costas_count'] == len(C) and certificate['permutation_count'] == len(P)
assert len(certificate['complete_canonical_residue_table']) == len(Q)
for k, row in zip(Q,certificate['complete_canonical_residue_table']):
    assert tuple(row['canonical_frequency']) == k
    assert tuple(row['costas_residue_counts']) == profile(C,k)
    assert tuple(row['permutation_residue_counts']) == profile(P,k)
ZC={q for q in Q if len(set(profile(C,q)))==1}
ZP={q for q in Q if len(set(profile(P,q)))==1}
assert len(ZC) == 16 and len(ZP) == 125
assert len(ZC & ZP) == 12 and len(ZC-ZP) == 4
assert Q[0] == (0,0,0,0,0) and Q[0] not in ZC and Q[0] not in ZP
z_c_full = 0
z_p_full = 0
zero_by_weight=Counter()
for k in product(range(5), repeat=5):
    cc=profile(C,k); pp=profile(P,k)
    a=len(set(cc)) == 1
    b=len(set(pp)) == 1
    if a: z_c_full+=1;zero_by_weight[sum(t!=0 for t in k)]+=1
    if b: z_p_full+=1
    assert a == (reduce_frequency(k) in ZC)
    assert b == (reduce_frequency(k) in ZP)
assert z_c_full == 320 and z_p_full == 2500
assert zero_by_weight == {1:4, 2:4, 3:92, 4:108, 5:112}
assert 3125-z_c_full == 2805
assert 3125-z_p_full == 625
assert (3125-z_c_full)-(3125-z_p_full) == 2180
assert set(ZC-ZP) == {
    (0,1,0,3,1), (0,1,1,0,3), (0,1,2,0,2), (0,1,4,4,1)
}
for q in ZC:
    assert profile(C,q) == (8,)*5
for q in ZC-ZP:
    assert profile(P,q) == (40,20,20,20,20)
print('COSTAS5_PROJECTIVE_CYCLOTOMIC_PASS', len(C),len(Q),len(ZC),z_c_full,3125-z_c_full, z_p_full,3125-z_p_full)
print('COSTAS_ONLY_REPS', sorted(ZC-ZP))
print('WEIGHT_ZERO_COUNTS', sorted(zero_by_weight.items()))
