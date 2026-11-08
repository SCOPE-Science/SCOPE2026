#!/usr/bin/env python3
"""Exact graph-parameter, neighborhood, and excitation-profile checks."""
from pathlib import Path
from collections import Counter
from analyze_symmetries import neigh, step, POW

def canonical_cycle_profile(p):
    options=[tuple(p[i:]+p[:i]) for i in range(len(p))]
    return min(options)

EXPECTED={
    'shri': {(4,4,4,4):6},
    'rook': {(1,3,9,3):32,(2,2,6,6):48,(4,4,4,4):18},
}
for name in ('rook','shri'):
    N=neigh(name)
    assert all(len(set(ns))==6 for ns in N)
    assert all(set(N[i])=={j for j in range(16) if i in N[j]} for i in range(16))
    # A^2=4I+2J for strongly regular parameters (16,6,2,2).
    for i in range(16):
        for j in range(16):
            two_walks=sum(j in N[z] for z in N[i])
            assert two_walks==(6 if i==j else 2)
    root_neighbors=set(N[0]);root_nonnb=set(range(16)) - root_neighbors-{0}
    assert len(root_nonnb)==9
    assert len({frozenset(set(N[v])&root_neighbors) for v in root_nonnb})==9
    reps=[int(l.split()[1]) for l in Path(f'{name}_reps.txt').read_text().splitlines() if l.startswith('REP4 ')]
    stats=Counter()
    for r in reps:
        s=r;seq=[]
        for _ in range(4):
            seq.append(sum((s//w)%3==1 for w in POW))
            s=step(s,N)
        assert s==r
        stats[canonical_cycle_profile(seq)]+=1
    assert dict(stats)==EXPECTED[name],(name,stats)
    print(name,'all graph identities and four-step excitation profiles OK:',dict(stats))
print('GRAPH_INVARIANTS_OK')
