"""Independent check via the wheel-and-spokes 10-vertex Petersen graph.
Requires networkx. Uses BFS/DFS instead of the first checker's union-find.
"""
import itertools
from collections import Counter
import networkx as nx

G = nx.petersen_graph()
U = set(G.nodes)


def acyclic_after_deletion(S):
    return nx.is_forest(G.subgraph(U.difference(S)))

sets = [frozenset(c) for k in range(3, 6) for c in itertools.combinations(range(10), k) if acyclic_after_deletion(c)]
assert Counter(map(len, sets)) == Counter({3: 20, 4: 140, 5: 240})
assert not any(acyclic_after_deletion(c) for k in range(3) for c in itertools.combinations(range(10), k))


def tar(cap):
    states = [s for s in sets if len(s) <= cap]
    H = nx.Graph()
    H.add_nodes_from(states)
    for s in states:
        for x in U - s:
            t = s | {x}
            if t in H:
                H.add_edge(s, t)
    return H

h4 = tar(4)
h5 = tar(5)
assert len(h4) == 160 and h4.number_of_edges() == 140
assert Counter(map(len, nx.connected_components(h4))) == Counter({29: 5, 1: 15})
assert len(h5) == 400 and h5.number_of_edges() == 980 and nx.is_connected(h5)
E = dict(nx.all_pairs_shortest_path_length(h5))
assert Counter((len(s), max(d.values())) for s, d in E.items()) == Counter({(3, 8): 20, (4, 9): 140, (5, 10): 240})
mins = [s for s in sets if len(s) == 3]
lengths = Counter()
for a, b in itertools.combinations(mins, 2):
    assert E[a][b] == len(a ^ b)
    lengths[E[a][b]] += 1
assert lengths == Counter({2: 30, 4: 90, 6: 70})
assert sum(E[a][b] == 10 for a, b in itertools.combinations(sets, 2)) == 120
print('PASS independent wheel/spoke Petersen construction; TAR cap=4 and cap=5; all 400x400 distances')
