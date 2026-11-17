#!/usr/bin/env python3
"""Independent edge-list verifier and exact automorphism/orbit enumeration.
Uses NetworkX >=2.8 for only graph automorphism computation. All state transitions
are coded independently of the other checker. Run python3 check_symmetry.py.
"""
from collections import Counter
from networkx import Graph, icosahedral_graph
from networkx.algorithms.isomorphism import GraphMatcher
EDGE_LIST=[(0,1),(0,5),(0,7),(0,8),(0,11),(1,2),(1,5),(1,6),(1,8),
(2,3),(2,6),(2,8),(2,9),(3,4),(3,6),(3,9),(3,10),(4,5),(4,6),
(4,10),(4,11),(5,6),(5,11),(7,8),(7,9),(7,10),(7,11),(8,9),
(9,10),(10,11)]
G=Graph();G.add_nodes_from(range(12));G.add_edges_from(EDGE_LIST)
assert G.number_of_edges()==30 and set(dict(G.degree()).values())=={5}
assert GraphMatcher(G,icosahedral_graph()).is_isomorphic()  # independent standard graph recognition
# Compute each neighborhood vote by an explicit loop over neighbor bits.
def update(s):
    result=0
    for v in range(12):
        ones=sum((s>>u)&1 for u in G.neighbors(v))
        if 2*ones>5: result|=1<<v
    return result
states=range(4096)
next_state=[update(x) for x in states]
fixed=[x for x in states if next_state[x]==x]
periodic=[x for x in states if next_state[next_state[x]]==x]
twocycles={frozenset((x,next_state[x])) for x in periodic if x!=next_state[x]}
assert (len(fixed),len(twocycles))==(14,156)
perms=list(GraphMatcher(G,G).isomorphisms_iter())
assert len(perms)==120
assert len({tuple(p[i] for i in range(12)) for p in perms})==120
assert all(set(p.keys())==set(range(12)) for p in perms)
def act(s,p):
    value=0
    for i in range(12):
        if (s>>i)&1:value|=1<<p[i]
    return value
for p in perms:
    for x in states:
        assert next_state[act(x,p)]==act(next_state[x],p)
# A cycle is considered as an unordered pair of states (temporal phases identified).
seen=set();orbit_sizes=[];descriptors=[]
for cyc in twocycles:
    if cyc in seen: continue
    orbit={frozenset(act(x,p) for x in cyc) for p in perms}
    assert orbit<=twocycles
    seen.update(orbit)
    representative=min(tuple(sorted(cyc)) for cyc in orbit)
    orbit_sizes.append(len(orbit))
    descriptors.append((len(orbit),tuple(sorted((representative[0].bit_count(),representative[1].bit_count())))))
assert seen==twocycles
assert sorted(orbit_sizes)==[6,10,20,30,30,30,30]

# Independently trace every basin by repeatedly applying the explicit vertex-level update.
periodic_set=set(periodic)
first_entry=Counter(); basin=Counter()
for initial in states:
    current=initial
    t=0
    while current not in periodic_set:
        current=next_state[current]
        t+=1
        assert t<=5
    first_entry[t]+=1
    key=(current,) if current==next_state[current] else tuple(sorted((current,next_state[current])))
    basin[key]+=1
assert dict(first_entry)=={0:326,1:986,2:984,3:1080,4:480,5:240}
assert Counter(basin.values())=={1:12,2:16,4:60,6:60,14:20,1586:2}
# Compute the full 82-row orbit quotient certificate.
rep={}
for s in states:
    if s in rep:continue
    orb={act(s,p) for p in perms}
    r=min(orb)
    for z in orb:rep[z]=r
assert len(set(rep.values()))==82
rows=[]
for r in sorted(set(rep.values())):
    orbit_size=sum(1 for s in states if rep[s]==r)
    y=r;t=0
    while y not in periodic_set:
        y=next_state[y];t+=1
    cyc=(y,) if y==next_state[y] else tuple(sorted((y,next_state[y])))
    rows.append((r,orbit_size,rep[next_state[r]],t,len(cyc),basin[cyc],r.bit_count()))
import csv
with open('state_orbits.csv','w',newline='',encoding='utf-8') as out:
    w=csv.writer(out);w.writerow(['representative','orbit_size','update_rep','first_entry_time','attractor_period','attractor_basin_size','ones']);w.writerows(rows)
assert sum(q[1] for q in rows)==4096
print('MODEL fixed_edge_list=30 vertices=12 two_cycles=156 fixed=14')
print('AUTOMORPHISMS',len(perms),'GEOMETRIC_TWO_CYCLE_CLASSES',len(orbit_sizes))
print('GEOMETRIC_TWO_CYCLE_CLASS_SIZES',sorted(orbit_sizes))
print('GEOMETRIC_STATE_CLASSES',len(rows),'STATE_CERTIFICATE','state_orbits.csv')
print('BASIN_HISTOGRAM',sorted(Counter(basin.values()).items()))
print('ENTRY_HISTOGRAM',sorted(first_entry.items()))
print('GEOMETRIC_TWO_CYCLE_DESCRIPTORS',sorted(descriptors))
print('ALL_AUTOMORPHISMS_COMMUTE_WITH_UPDATE PASS')
