"""Verification for independent domination of iterated central graphs.

Requires Python 3 and NetworkX.  The checks are finite sanity tests; the
general theorem is proved in RESULT.md.
"""

import math
import networkx as nx


def central_graph(G):
    H = nx.Graph()
    for u in G.nodes:
        H.add_node(("v", u))
    for u, v in G.edges:
        e = ("e", min(u, v), max(u, v))
        H.add_edge(("v", u), e)
        H.add_edge(("v", v), e)
    nodes = list(G.nodes)
    for i, u in enumerate(nodes):
        for v in nodes[i + 1 :]:
            if not G.has_edge(u, v):
                H.add_edge(("v", u), ("v", v))
    return H


def iterate_central(G, k):
    H = G.copy()
    for _ in range(k):
        H = central_graph(H)
    return H


def alpha(G):
    return max(len(Q) for Q in nx.find_cliques(nx.complement(G)))


def independent_domination(G):
    # Independent dominating sets are exactly maximal independent sets.
    return min(len(Q) for Q in nx.find_cliques(nx.complement(G)))


def c2_formula(G):
    n = G.number_of_nodes()
    m = G.number_of_edges()
    a = alpha(G)
    return (
        math.comb(n, 2)
        + m
        - a * (n - 2)
        + math.comb(a, 2)
    )


def check():
    atlas = nx.graph_atlas_g()
    connected = [
        G
        for G in atlas
        if 3 <= G.number_of_nodes() <= 7 and nx.is_connected(G)
    ]

    alpha_checked = 0
    reduction_checked = 0
    direct_c2_checked = 0
    direct_c3_checked = 0

    for G in connected:
        C1 = central_graph(G)
        assert alpha(C1) == G.number_of_edges()
        alpha_checked += 1

        # Applying the source C^2 formula to C(G) should collapse to
        # twice the number of edges of C(G), which is the k=3 identity.
        assert c2_formula(C1) == 2 * C1.number_of_edges()
        reduction_checked += 1

        if G.number_of_nodes() <= 5:
            C2 = central_graph(C1)
            assert independent_domination(C2) == c2_formula(G)
            direct_c2_checked += 1

            C3 = central_graph(C2)
            assert independent_domination(C3) == 2 * C1.number_of_edges()
            direct_c3_checked += 1

    print(f"NetworkX {nx.__version__}")
    print(f"alpha(C(G)) checks: {alpha_checked}")
    print(f"higher-iterate formula reductions: {reduction_checked}")
    print(f"direct i(C^2(G)) checks: {direct_c2_checked}")
    print(f"direct i(C^3(G)) checks: {direct_c3_checked}")
    print("all checks passed")


if __name__ == "__main__":
    check()
