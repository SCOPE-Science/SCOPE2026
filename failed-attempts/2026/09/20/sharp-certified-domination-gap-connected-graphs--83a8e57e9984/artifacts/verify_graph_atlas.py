"""Exhaustive Graph Atlas check for the certified-domination gap theorem.

Requires NetworkX.  The Graph Atlas contains every unlabeled graph through
seven vertices.  This script checks all connected atlas graphs of orders 2..7.
"""
import itertools
import collections
import networkx as nx

def is_dominating(G, S):
    S = set(S)
    return all(v in S or any(u in S for u in G.neighbors(v)) for v in G)

def is_certified(G, S):
    S = set(S)
    if not is_dominating(G, S):
        return False
    return all(sum(u not in S for u in G.neighbors(v)) != 1 for v in S)

def parameters(G):
    V = list(G.nodes())
    gamma = gamma_cer = None
    for k in range(1, len(V) + 1):
        if gamma is None:
            for C in itertools.combinations(V, k):
                if is_dominating(G, C):
                    gamma = k
                    break
        if gamma_cer is None:
            for C in itertools.combinations(V, k):
                if is_certified(G, C):
                    gamma_cer = k
                    break
        if gamma is not None and gamma_cer is not None:
            return gamma, gamma_cer
    raise AssertionError("parameters not found")

def corona(H):
    G = nx.Graph()
    for v in H:
        G.add_edge(("b", v), ("l", v))
    for u, v in H.edges():
        G.add_edge(("b", u), ("b", v))
    return G

def diadem(H, v):
    G = corona(H)
    G.add_edge(("b", v), ("x", v))
    return G

atlas = nx.graph_atlas_g()
connected_by_order = collections.defaultdict(list)
for G in atlas:
    if G.number_of_nodes() >= 1 and nx.is_connected(G):
        connected_by_order[G.number_of_nodes()].append(G)

for n in range(2, 8):
    graphs = connected_by_order[n]
    data = []
    for G in graphs:
        gamma, gamma_cer = parameters(G)
        data.append((gamma_cer - gamma, G))

    maximum = max(d for d, _ in data)
    extremals = [G for d, G in data if d == maximum]
    predicted = n // 2 if n % 2 == 0 else (n - 3) // 2
    assert maximum == predicted

    family = None
    if n % 2 == 0:
        m = n // 2
        family = [corona(H) for H in connected_by_order[m]]
    elif n >= 5:
        m = (n - 1) // 2
        family = []
        for H in connected_by_order[m]:
            for v in H:
                D = diadem(H, v)
                if not any(nx.is_isomorphic(D, F) for F in family):
                    family.append(D)

    if family is not None:
        assert len(extremals) == len(family)
        assert all(any(nx.is_isomorphic(G, F) for F in family)
                   for G in extremals)

    family_count = "-" if family is None else str(len(family))
    print(n, len(graphs), maximum, len(extremals), family_count)
