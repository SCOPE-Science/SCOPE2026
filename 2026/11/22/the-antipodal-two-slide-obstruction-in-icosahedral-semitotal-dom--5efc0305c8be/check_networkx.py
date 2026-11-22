"""Independent exhaustive cross-check using NetworkX's icosahedral graph and BFS.

Execute: python check_networkx.py (requires NetworkX 3.x).
"""
from collections import Counter
from itertools import combinations
import networkx as nx

G=nx.icosahedral_graph()
assert G.number_of_nodes()==12 and G.number_of_edges()==30
verts=tuple(sorted(G))
paths=dict(nx.all_pairs_shortest_path_length(G))

def admissible(vs):
    s=set(vs)
    if any(not s.intersection(nx.ego_graph(G,u,radius=1)) for u in verts):
        return False
    return all(any(paths[u][w]<=2 for w in s if w!=u) for u in s)
assert all(not admissible(c) for k in range(3) for c in combinations(verts,k))
Q={tuple(c) for c in combinations(verts,3) if admissible(c)}
assert len(Q)==80

def signature(T):
    return tuple(sorted(paths[a][b] for a,b in combinations(T,2)))
assert Counter(signature(T) for T in Q)==Counter({(1,2,3):60,(2,2,2):20})
J=nx.Graph();J.add_nodes_from(Q)
H=nx.Graph();H.add_nodes_from(Q)
for u,v in combinations(sorted(Q),2):
    lost=set(u)-set(v); gained=set(v)-set(u)
    if len(lost)!=1 or len(gained)!=1:continue
    J.add_edge(u,v)
    if G.has_edge(next(iter(lost)),next(iter(gained))):H.add_edge(u,v)
assert (J.number_of_edges(),H.number_of_edges())==(480,300)
assert nx.is_connected(J) and nx.is_connected(H)
assert Counter(d for _,d in J.degree())==Counter({13:60,9:20})
assert Counter(d for _,d in H.degree())==Counter({7:60,9:20})
D1={u:dict(nx.single_source_shortest_path_length(J,u)) for u in Q}
D2={u:dict(nx.single_source_shortest_path_length(H,u)) for u in Q}
assert Counter(max(D1[u].values()) for u in Q)==Counter({3:80})
assert Counter(max(D2[u].values()) for u in Q)==Counter({4:60,3:20})
assert Counter(D1[u][v] for u,v in combinations(sorted(Q),2))==Counter({1:480,2:1200,3:1480})
assert Counter(D2[u][v] for u,v in combinations(sorted(Q),2))==Counter({1:300,2:1050,3:1570,4:240})
assert Counter(D2[u][v]-D1[u][v] for u,v in combinations(sorted(Q),2))==Counter({0:2440,1:690,2:30})

def has_opposite_pair(s):
    return any(paths[a][b]==3 for a,b in combinations(s,2))
def exceptional(u,v):
    both=set(u)&set(v)
    if len(both)!=2 or not has_opposite_pair(tuple(both)): return False
    return paths[next(iter(set(u)-both))][next(iter(set(v)-both))]==3
for u,v in combinations(sorted(Q),2):
    assert (D2[u][v]-D1[u][v]==2)==exceptional(u,v)

# A group-theoretic check independent of the bit-mask implementation.
auts=list(nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter())
assert len(auts)==120
remaining=set(Q);orbits=[]
while remaining:
    seed=next(iter(remaining))
    orbit={tuple(sorted(a[v] for v in seed)) for a in auts}
    assert orbit<=Q
    remaining-=orbit
    orbits.append(len(orbit))
assert sorted(orbits)==[20,60]
print('PASS independent NetworkX graph, exhaustive 3-subsets, all-pairs BFS, and automorphism orbit check')
print('80 minimum states; 120 symmetries; orbit sizes 20,60; jumps 480; slides 300')
print('eccentricities jump all 3; slide 20 at 3, 60 at 4; detours 2440/690/30')
