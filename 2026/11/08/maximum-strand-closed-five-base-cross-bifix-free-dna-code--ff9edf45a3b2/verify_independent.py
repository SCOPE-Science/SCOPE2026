#!/usr/bin/env python3
"""Independent bitwise reconstruction of exact graph and witness; stdlib only."""
import json
from itertools import combinations
from pathlib import Path

base=Path(__file__).resolve().parent
record=json.loads((base/'certificate.json').read_text(encoding='utf-8'))
DNA='ACGT'
# Integers 0,1,2,3 correspond to A,C,G,T; complement is 3-x.
def digits(x):
    out=[0]*5
    for i in range(4,-1,-1):
        out[i]=x&3
        x>>=2
    return out
def pack(a):
    z=0
    for x in a:
        z=(z<<2)|x
    return z
def revcomp(x):
    return pack([3-y for y in digits(x)[::-1]])
def collide(x,y):
    ax=digits(x);by=digits(y)
    return any(ax[:t]==by[5-t:] for t in (1,2,3,4))

canonical=[x for x in range(4**5) if (x>>8) in (0,1) and (x&3) in (2,3)]
assert len(canonical)==256
used=set();pairs=[]
for x in canonical:
    if x in used:continue
    y=revcomp(x);orbit=tuple(sorted({x,y}));used.update(orbit)
    if any(collide(a,b) for a in orbit for b in orbit):continue
    pairs.append(orbit)
assert len(pairs)==56 and all(len(p)==2 for p in pairs)
assert [[ ''.join(DNA[i] for i in digits(x)) for x in o] for o in pairs]==record['orbit_table']
blocked=set()
for i,j in combinations(range(56),2):
    if any(collide(x,y) or collide(y,x) for x in pairs[i] for y in pairs[j]):
        blocked.add((i,j))
assert len(blocked)==412
for B in record['clique_partition']:
    assert all((min(i,j),max(i,j)) in blocked for i,j in combinations(B,2))
assert sorted(v for B in record['clique_partition'] for v in B)==list(range(56))
chosen=record['selected_orbits']
assert all((i,j) not in blocked for i,j in combinations(chosen,2))
selected={x for i in chosen for x in pairs[i]}
assert len(selected)==36 and all(revcomp(x) in selected for x in selected)
assert not any(collide(x,y) for x in selected for y in selected)
listed=(base/'witness.txt').read_text(encoding='ascii').splitlines()
assert sorted(''.join(DNA[d] for d in digits(x)) for x in selected)==listed
print('INDEPENDENT_INTEGER_REPLAY_OK: optimum exactly 36 by clique cover and witness')
