"""Structural and orbit verifier for ordinary bondage of the Pappus graph.
Requires Python 3 and networkx >= 2.8 for the automorphism orbit audit.
Run: python verify_structural.py
The core counts below use only the Python standard library.
"""
from itertools import combinations
from collections import Counter

P = [(x,y) for x in range(3) for y in range(3)]
L = [(d,c) for d in range(3) for c in range(3)]
def incident(pt, ln):
    x,y=pt; d,c=ln
    return (x if d==0 else y if d==1 else (x+y)%3)==c
edges=sorted((i,9+j) for i,p in enumerate(P) for j,l in enumerate(L) if incident(p,l))
assert len(edges)==27
N=[set() for _ in range(18)]
for u,v in edges:N[u].add(v);N[v].add(u)

def dominant(S, omit=frozenset()):
    return all(v in S or any(u in S and tuple(sorted((u,v))) not in omit for u in N[v]) for v in range(18))

# Minimum size follows also analytically: four closed neighborhoods cover at most 16 vertices.
minimum=[frozenset(s) for s in combinations(range(18),5) if dominant(set(s))]
assert len(minimum)==18
assert Counter((len(s&set(range(9))),len(s&set(range(9,18)))) for s in minimum)=={(3,2):9,(2,3):9}

# Read the 18 distinct optimum configurations as a complete obstruction system.
fail=[]
for a,b,c in combinations(edges,3):
    F=frozenset((a,b,c))
    # A minimum dominating set ceases to dominate iff some omitted vertex has
    # ALL of its edges to that set removed.
    if all(any(v not in S and all(tuple(sorted((v,u))) in F for u in S & N[v]) for v in range(18)) for S in minimum):
        fail.append(F)
assert len(fail)==171
stars=[];match=[]
for F in fail:
    deg=Counter(u for e in F for u in e)
    if max(deg.values())==3:stars.append(F)
    else:
        assert all(d==1 for d in deg.values())
        match.append(F)
assert (len(stars),len(match))==(18,153)
# Every two-edge deletion is safe: every such pair extends to a safe three-edge deletion
# OR check directly the 18 original optimizers.
for a,b in combinations(edges,2):
    F={a,b}
    assert any(dominant(S,F) for S in minimum)

# Full vertex automorphism group, independently checked against the standard
# 18-vertex Pappus graph implementation.
import networkx as nx
G=nx.Graph();G.add_nodes_from(range(18));G.add_edges_from(edges)
assert nx.is_isomorphic(G,nx.pappus_graph())
autos=list(nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter())
assert len(autos)==216
remaining=set(fail);orbit_records=[]
while remaining:
    F=min(remaining,key=lambda x:tuple(sorted(x)))
    orbit={frozenset(tuple(sorted((perm[u],perm[v]))) for (u,v) in F) for perm in autos}
    assert orbit<=set(fail)
    remaining-=orbit
    orbit_records.append((len(orbit),tuple(sorted(F))))
assert sorted(n for n,_ in orbit_records)==[9,18,36,108]
assert len(stars)==18
for n,r in sorted(orbit_records):print('orbit=',n,'representative_edges=',r)
print('vertices=18 edges=27 gamma=5 min_dom_sets=18')
print('bondage_1=0 bondage_2=0 bondage_3=171')
print('stars=18 matchings=153 automorphisms=216 orbit_sizes=9,18,36,108')
