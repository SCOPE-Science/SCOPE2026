"""Verify Gamma=C5 satisfies Nguyen-Tran Standing Assumptions and is non-CFS.
Standing Assumptions: connected, triangle-free, planar, >=5 vertices,
no separating vertex or edge. Non-CFS: no induced 4-cycles => square-graph empty.
"""
import itertools
import networkx as nx

G = nx.cycle_graph(5)
out = []
out.append(f"nodes={sorted(G.nodes())} n={G.number_of_nodes()} m={G.number_of_edges()}")
connected = nx.is_connected(G)
out.append(f"connected={connected}")
cliques = list(nx.enumerate_all_cliques(G))
maxclique = max(len(c) for c in cliques)
triangle_free = maxclique <= 2
out.append(f"max_clique_size={maxclique} triangle_free={triangle_free}")
planar, _ = nx.check_planarity(G)
out.append(f"planar={planar} n>=5={G.number_of_nodes() >= 5}")
sep_vertices = [v for v in G.nodes()
                if not nx.is_connected(G.subgraph([u for u in G.nodes() if u != v]))]
out.append(f"separating_vertices={sep_vertices}")
def sep_edges(G):
    res = []
    for e in list(G.edges()):
        H = G.copy()
        H.remove_edge(*e)
        if not nx.is_connected(H):
            res.append(e)
    return res
se = sep_edges(G)
out.append(f"separating_edges={se}")
squares = []
for quad in itertools.combinations(sorted(G.nodes()), 4):
    H = G.subgraph(quad)
    if H.number_of_edges() == 4 and all(d == 2 for _, d in H.degree()):
        squares.append(quad)
out.append(f"induced_C4_list={squares} count={len(squares)}")
out.append(f"square_free={len(squares) == 0}")
out.append("CFS check: square-graph Omega has 0 vertices (no induced C4); "
           "support=empty != V (5 vertices) => non-CFS by Dani-Thomas criterion")
standing = connected and triangle_free and planar and G.number_of_nodes() >= 5 \
    and len(sep_vertices) == 0 and len(se) == 0
out.append(f"STANDING_ASSUMPTIONS_HOLD={standing}")
out.append(f"NON_CFS={len(squares) == 0} (vacuous: no square support)")
text = "\n".join(out)
print(text)
with open("c5_check_output.txt", "w") as f:
    f.write(text + "\n")
