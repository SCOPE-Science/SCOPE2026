"""Standalone complete automorphism-orbit verification for Pappus semitotal minima.

Enumerates all 9! point permutations preserving the nine line triples,
then adjoining an explicit point-line duality.
"""
from itertools import combinations, permutations
from collections import Counter
import json

P='ABCabcXYZ'; L=('ABC','abc','XYZ','AbX','aBX','AcY','aCY','BcZ','bCZ')
N=18
V=tuple('P'+p for p in P)+tuple('L'+str(i) for i in range(9))
adj={v:set() for v in V}
for j,line in enumerate(L):
    for p in line:
        a,b='P'+p,'L'+str(j);adj[a].add(b);adj[b].add(a)
short2={v:set(adj[v]) | set().union(*(adj[w] for w in adj[v]))-{v} for v in V}

def eligible(S):
    return (all(v in S or adj[v]&S for v in V)
            and all((short2[v]&S)-{v} for v in S))
minima={frozenset(c) for c in combinations(V,6) if eligible(set(c))}
assert len(minima)==297
line_sets=[frozenset(P.index(p) for p in line) for line in L]
line_pos={b:j for j,b in enumerate(line_sets)}
side_preserving=[]
for perm in permutations(range(9)):
    images=[line_pos.get(frozenset(perm[p] for p in b)) for b in line_sets]
    if None in images:continue
    assert set(images)==set(range(9))
    a={V[i]:V[perm[i]] for i in range(9)}
    a.update({V[9+j]:V[9+images[j]] for j in range(9)})
    side_preserving.append(a)
assert len(side_preserving)==108
DUAL_IMAGES=('L3','L0','L5','L7','L2','L8','L4','L1','L6',
             'PA','PZ','Pa','PX','PB','Pb','Pc','PC','PY')
dual=dict(zip(V,DUAL_IMAGES))
assert set(dual.values())==set(V)
perms=side_preserving + [{v:dual[p[v]] for v in V} for p in side_preserving]
assert len(perms)==216
assert all({p[w] for w in adj[v]}==adj[p[v]] for p in perms for v in V)
def degrees(S):
    jump=slide=0
    for T in minima:
        lost=S-T
        if len(lost)==1 and len(T-S)==1:
            jump+=1
            if next(iter(T-S)) in adj[next(iter(lost))]:
                slide+=1
    return jump,slide

remaining=set(minima);sizes=[];orbit_reps=[];orbit_degree_pairs=[]
while remaining:
    rep=min(remaining,key=lambda s:tuple(sorted(s)))
    orbit={frozenset(p[v] for v in rep) for p in perms}
    assert orbit<=minima
    pair=degrees(rep)
    assert all(degrees(s)==pair for s in orbit)
    orbit_degree_pairs.append((len(orbit), *pair))
    sizes.append(len(orbit));orbit_reps.append((len(orbit),tuple(sorted(rep))))
    remaining-=orbit
assert sorted(sizes)==[9,18,54,108,108]
assert sorted(orbit_degree_pairs)==[(9,0,0),(18,6,6),(54,8,8),(108,6,2),(108,8,1)]

# The nine locked states form a cartesian 3 x 3 family.
T=(frozenset('P'+x for x in t) for t in ('AaZ','BbY','CcX'))
U=(frozenset('L'+str(x) for x in row) for row in ((0,1,2),(3,6,7),(4,5,8)))
T=list(T); U=list(U)
locked={t|u for t in T for u in U}
assert len(locked)==9
assert all(all(len(adj[v]&s)==1 for v in V) for s in locked)
assert locked<=minima
print(json.dumps({'graph':'Pappus nine-point configuration',
 'point_preserving_automorphisms':108,'all_automorphisms':216,
 'semitotal_minima':len(minima), 'orbits':sorted(sizes),
 'orbit_size_jump_degree_slide_degree': sorted(orbit_degree_pairs),
 'representatives':sorted(orbit_reps), 'grid_of_nine_total_domination_sets':True},
 sort_keys=True,indent=2))
print('VERIFY_OK')
