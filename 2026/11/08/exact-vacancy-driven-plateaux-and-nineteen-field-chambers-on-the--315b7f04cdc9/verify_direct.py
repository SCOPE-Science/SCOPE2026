#!/usr/bin/env python3
"""Exact exhaustive certificate for the twelve-site spin-one icosahedral cluster.

Run with Python 3 standard library from the directory containing the CSV and JSON files.
"""
import csv
import itertools
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def table(filename):
    with (ROOT / filename).open(newline='', encoding='utf-8') as f:
        return [tuple(int(x) for x in row.values()) for row in csv.DictReader(f)]

edges = table('edges.csv')
assert len(edges) == 30 and len(set(tuple(sorted(e)) for e in edges)) == 30
assert all(0 <= u < v < 12 for u, v in edges)
assert all(sum(v in e for e in edges) == 5 for v in range(12))
triangles = sum(1 for a, b, c in itertools.combinations(range(12), 3)
                if all(tuple(sorted(e)) in edges for e in ((a,b),(a,c),(b,c))))
assert triangles == 20

counts = Counter()
for s in itertools.product((-1,0,1), repeat=12):
    K = sum(v != 0 for v in s)
    M = sum(s)
    B = sum(s[u]*s[v] for u,v in edges)
    counts[K, M, B] += 1
assert sum(counts.values()) == 3**12
sector = {}
for (K,M,B), multiplicity in counts.items():
    if M < 0: continue
    cur = sector.get((K,M))
    if cur is None or B < cur[0]:
        sector[K,M] = (B,multiplicity)
    elif B == cur[0]:
        sector[K,M] = (B,cur[1] + multiplicity)
assert len(sector) == 49
for (K,M), value in sector.items():
    if M > 0:
        assert all(counts[K,M,B] == counts[K,-M,B] for k,m,B in counts if k==K and m==M)
rows = table('sector_minima.csv')
assert len(rows)==49 and {(k,m):(b,n) for k,m,b,n in rows}==sector
chambers = table('open_chambers.csv')
assert len(chambers)==19 and len(set(chambers))==19
assert all(c in rows for c in chambers)
assert len({(k,m) for k,m,_,_ in chambers}) == 19

# Exhaustive rational lower-envelope proof: for any omitted sector its
# energy is at least a convex average of the chamber energies for all
# real delta and every nonnegative longitudinal field.
cert = json.loads((ROOT / 'domination_certificates.json').read_text('utf-8'))
omitted = {(k,m,b) for k,m,b,n in rows if (k,m,b,n) not in chambers}
assert len(cert)==len(omitted)==30
seen=set()
for item in cert:
    key=(item['K'],item['M'],item['Bmin'])
    assert key in omitted and key not in seen
    seen.add(key)
    coeffs={}
    for part in item['combination']:
        ix = part['chamber_index']
        coeffs[ix] = coeffs.get(ix,Fraction()) + Fraction(part['num'],part['den'])
    assert coeffs and all(0 <= ix < len(chambers) and w>=0 for ix,w in coeffs.items())
    assert sum(coeffs.values())==1
    k,m,b = key
    assert sum(w*chambers[ix][0] for ix,w in coeffs.items())==k
    assert sum(w*chambers[ix][1] for ix,w in coeffs.items())>=m
    assert sum(w*chambers[ix][2] for ix,w in coeffs.items())<=b
assert seen==omitted

# Exact rational field/crystal-field witnesses establish an open region
# for each of the nineteen branches; no reliance on floating point.
witnesses=json.loads((ROOT / 'open_chamber_witnesses.json').read_text('utf-8'))
assert len(witnesses)==19
assert {w['chamber_index'] for w in witnesses}==set(range(19))
for w in witnesses:
    idx=w['chamber_index']; k,m,b,_=chambers[idx]
    delta=Fraction(*w['delta']); field=Fraction(*w['field'])
    assert field>0
    low=b+k*delta-m*field
    gap=min(B+K*delta-M*field-low for K,M,B,_ in rows if (K,M)!=(k,m))
    assert gap>0 and gap==Fraction(*w['minimum_gap'])

# Complete zero-longitudinal-field degeneracies, including the
# otherwise nonexposed sectors appearing exactly at coexistence.
expected=[(Fraction(0),-10,72),
          (Fraction(1,2),-4,462),
          (Fraction(2,3),Fraction(-8,3),150),
          (Fraction(1),0,351),
          (Fraction(2),0,1)]
for delta,energy,deg in expected:
    v=[(b+K*delta,K,M,n) for K,M,b,n in rows]
    emin=min(z[0] for z in v)
    n0=sum(n*(1 if M==0 else 2) for e,K,M,n in v if e==emin)
    assert (emin,n0)==(energy,deg)
print('VERIFY_OK direct exhaustive, 49 sector minima, 19 chambers, 30 rational dominance certificates and coexistence counts')
