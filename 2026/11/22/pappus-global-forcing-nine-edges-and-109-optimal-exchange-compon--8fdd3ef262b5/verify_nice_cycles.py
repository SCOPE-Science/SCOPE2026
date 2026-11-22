"""Reconstruct the Pappus perfect-matching alternating-cycle hypergraph.
Run: python3 verify_nice_cycles.py
No external libraries required.
"""
from itertools import permutations
from collections import Counter

points = [(x,y) for x in range(3) for y in range(3)]
lines = [(direction,c) for direction in range(3) for c in range(3)]
def incident(p,L):
    x,y=p;direction,c=L
    return (x if direction==0 else (y if direction==1 else (y-x)%3))==c
edges=[(i,9+j) for i,p in enumerate(points) for j,L in enumerate(lines) if incident(p,L)]
assert len(edges)==27
edge_id={e:i for i,e in enumerate(edges)}
matchings=[]
for sigma in permutations(range(9)):
    if all((i,9+sigma[i]) in edge_id for i in range(9)):
        matchings.append(sum(1<<edge_id[(i,9+sigma[i])] for i in range(9)))
assert len(matchings)==42
cycles=set()
for ia,a in enumerate(matchings):
    for b in matchings[ia+1:]:
        difference=a^b
        adj={v:[] for v in range(18)}
        for eid,(u,v) in enumerate(edges):
            if difference>>eid&1:
                adj[u].append((v,eid));adj[v].append((u,eid))
        seen=set()
        for v in range(18):
            if v in seen or not adj[v]:continue
            todo=[v];seen.add(v);cycle_bits=0
            for x in todo:
                assert len(adj[x])==2
                for y,eid in adj[x]:
                    cycle_bits|=1<<eid
                    if y not in seen:seen.add(y);todo.append(y)
            assert cycle_bits.bit_count()>=6 and cycle_bits.bit_count()%2==0
            cycles.add(cycle_bits)
hist=Counter(c.bit_count() for c in cycles)
assert hist=={6:18,8:54,10:54,12:225,14:108,16:108,18:36}
assert len(cycles)==603
# The universal equivalence: every two perfect matchings disagree on an
# alternating cycle; conversely each nice cycle can be flipped.
for mask in range(10000):
    all_signatures_distinct=len({m&mask for m in matchings})==42
    hits_all_cycles=all(mask&c for c in cycles)
    assert all_signatures_distinct==hits_all_cycles
print('Pappus perfect matchings: 42')
print('nice even cycles: 603')
print('length multiplicities:', ' '.join(f'{k}:{hist[k]}' for k in sorted(hist)))
print('pairwise-signature criterion equals nice-cycle transversal criterion on 10000 test masks')
