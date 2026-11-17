"""Independent all five-node simple graph enumeration for matching-polytope distances."""
from itertools import combinations
from fractions import Fraction as F
import networkx as nx
from verify import checks, cycles, disjoint_packs

n=5
all_edges=list(combinations(range(n),2))
total_packs=total_v=0
for mask in range(1<<len(all_edges)):
    G=nx.Graph();G.add_nodes_from(range(n))
    G.add_edges_from([e for i,e in enumerate(all_edges) if mask>>i&1])
    p,v,q,d=checks(G)
    total_packs+=p
    total_v+=v
    assert d==max([sum((F(1,4*len(c)) for c in pack),F(0)) for pack in disjoint_packs(cycles(G))] or [F(0)])
print(f'FIVE_NODE_GRAPH_EXHAUSTIVE_PASS graphs={1<<len(all_edges)} vertices={total_v} packs={total_packs}')
