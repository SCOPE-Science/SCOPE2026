#!/usr/bin/env python3
"""Independent verification of symmetry-orbit counts of exact zeros."""
from collections import Counter
from csv import reader
from itertools import permutations
from pathlib import Path
from verify_antichain import Q, transform, comparison_pairs, antichain_mask

ROOT=Path(__file__).resolve().parent

def main():
    f=[int(antichain_mask(m,comparison_pairs())) for m in range(Q)]
    w=transform(f)
    actions=[]
    for p in permutations(range(4)):
        for reverse in (False,True):
            actions.append(tuple((sum(((x>>i)&1)<<p[i] for i in range(4)) ^
                                (15 if reverse else 0)) for x in range(16)))
    assert len(set(actions))==48
    seen=bytearray(Q); all_orbits=Counter(); zero_orbits=Counter()
    for mask in range(Q):
        if seen[mask]:continue
        orbit=set()
        for a in actions:
            moved=0
            for i in range(16):
                if mask>>i&1:moved|=1<<a[i]
            orbit.add(moved)
        for k in orbit:
            assert not seen[k]
            seen[k]=1
            assert w[k]==w[mask]
        all_orbits[len(orbit)]+=1
        if w[mask]==0:zero_orbits[len(orbit)]+=1
    assert sum(all_orbits.values())==2104
    assert sum(zero_orbits.values())==199
    assert sum(k*v for k,v in zero_orbits.items())==6611
    with (ROOT/'orbit_census.csv').open(newline='',encoding='utf-8') as f:
        rows=list(reader(f))
    assert rows[0]==['orbit_size','all_orbits','zero_orbits']
    assert [[int(k),all_orbits[k],zero_orbits[k]] for k in sorted(all_orbits)]==[
        list(map(int,row)) for row in rows[1:]]
    print('ANTICHAIN_B4_ORBITS_PASS total_orbits=2104 zero_orbits=199 zero_frequencies=6611')

if __name__=='__main__':main()
