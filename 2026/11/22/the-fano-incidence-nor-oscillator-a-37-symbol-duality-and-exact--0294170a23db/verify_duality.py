"""Independent set-level and dual-closure verification of the Fano NOR census.
Run: python3 verify_duality.py
"""
from collections import Counter
from itertools import combinations
from math import comb
points=set(range(7)); lines=set(range(7))
inc={j:{(j+d)%7 for d in (0,1,3)} for j in lines}
A=lambda P:frozenset(j for j in lines if inc[j].isdisjoint(P))
B=lambda L:frozenset(p for p in points if all(p not in inc[j] for j in L))
subsets=[frozenset(c) for r in range(8) for c in combinations(range(7),r)]
cp=lambda P:B(A(P)); cl=lambda L:A(B(L))
w=Counter(cp(P) for P in subsets)
v=Counter(cl(L) for L in subsets)
assert len(w)==len(v)==37
assert Counter((len(P),cnt) for P,cnt in w.items())==Counter({(0,1):1,(1,1):7,(2,1):21,(4,5):7,(7,64):1})
assert sum(w.values())==sum(v.values())==128
assert all(A(B(A(P)))==A(P) for P in subsets)
assert all(B(A(B(L)))==B(L) for L in subsets)
fb=Counter(); ob=Counter()
closed=list(w)
for i,P in enumerate(closed):
    fb[w[P]*v[A(P)]]+=1
    for Q in closed[i+1:]:
        ob[w[P]*v[A(Q)]+w[Q]*v[A(P)]]+=1
assert fb==Counter({1:21,5:14,64:2})
assert ob==Counter({2:210,6:294,10:42,26:49,65:42,69:14,321:14,4097:1})
assert sum(s*c for s,c in fb.items())+sum(s*c for s,c in ob.items())==4**7
assert sum(ob.values())==666
print('closed_set_types 0:1x1 1:7x1 2:21x1 4:7x5 7:1x64')
print('fixed_orbits 37 primitive_two_orbits 666')
print('fixed_basins '+' '.join(f'{s}:{fb[s]}' for s in sorted(fb)))
print('two_basins '+' '.join(f'{s}:{ob[s]}' for s in sorted(ob)))
print('sum_basin_states 16384')
