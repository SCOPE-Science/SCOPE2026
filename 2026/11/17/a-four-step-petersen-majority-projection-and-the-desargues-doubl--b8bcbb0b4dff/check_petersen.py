#!/usr/bin/env python3
"""Exhaustive incidence and symmetry certificate for 10 Petersen coordinates."""
from itertools import combinations, permutations
from collections import Counter
V=list(combinations(range(5),2))
N=[tuple(j for j,v in enumerate(V) if set(v).isdisjoint(e)) for e in V]
assert all(len(row)==3 for row in N)
# Explicit isomorphism from the bipartite double of KG(5,2) to GP(10,3).
image_a=[0,19,13,2,8,17,11,6,15,4]
image_b=[5,14,18,7,3,12,16,1,10,9]
assert sorted(image_a+image_b)==list(range(20))
gp_edges=set()
for i in range(10):
    for u,v in ((i,(i+1)%10),(10+i,10+(i+3)%10),(i,10+i)):
        gp_edges.add(tuple(sorted((u,v))))
iso_edges={tuple(sorted((image_a[i],image_b[j]))) for i in range(10) for j in N[i]}
assert iso_edges==gp_edges and len(iso_edges)==30

def T(mask):
    result=0
    for i,nb in enumerate(N):
        result|=(sum((mask>>j)&1 for j in nb)>=2)<<i
    return result

tab=[list(range(1024))]
for d in range(1,7):tab.append([T(v) for v in tab[-1]])
assert tab[6]==tab[4] and tab[3]!=tab[5]
R=set(tab[4]); weights=Counter(tab[4]); assert len(R)==124
assert all(tab[2][r]==r for r in R)
assert all(weights[T(r)]==weights[r] for r in R)
assert Counter(weights.values())==Counter({1:72,10:50,226:2})
assert sum(T(r)==r for r in R)==14
assert sum(T(r)!=r for r in R)==110
assert len(set(tab[3]))==144
assert len(set(tab[4]))==124

perms=[]
for p in permutations(range(5)):
    perms.append(tuple(V.index(tuple(sorted((p[a],p[b])))) for a,b in V))
def act(x,p):return sum(((x>>i)&1)<<p[i] for i in range(10))
reps=[];covered=set()
for s in range(1024):
    if s in covered:continue
    orb={act(s,p) for p in perms}
    assert s==min(orb)
    covered.update(orb)
    reps.append((s,len(orb),tab[4][s],weights[tab[4][s]]))
assert len(reps)==34 and len(covered)==1024
assert sum(o for _,o,_,_ in reps)==1024
print('petersen_vertices='+repr(V))
print('orbits_of_five_vertex_graphs=34; symmetry_group_order=120')
print('representative_hex,orbit_size,periodic_target_hex,target_fiber:')
for rep,size,target,w in reps:
    print(f'{rep:03x},{size},{target:03x},{w}')
print('recurrent_symbols=124 fixed_symbols=14 paired_symbols=110')
print('recurrent_by_cardinality_and_fiber='+repr(sorted(Counter((s.bit_count(),weights[s]) for s in R).items())))
print('fiber_multiplicity='+repr(sorted(Counter(weights.values()).items())))
print('distinct_shore_images='+repr([len(set(x)) for x in tab[1:7]]))
print('T6_equals_T4=True T5_not_equal_T3=True')
print('all_checks_passed')
