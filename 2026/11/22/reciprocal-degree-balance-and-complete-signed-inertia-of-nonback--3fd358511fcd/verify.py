#!/usr/bin/env python3
"""Finite diagnostics for signed self-commutators of nonbacktracking matrices.
Requires NumPy and NetworkX. The analytic proof is given separately.
"""
from fractions import Fraction
import numpy as np
import networkx as nx

checks = 0

def verify_graph(G):
    global checks
    assert nx.is_connected(G) and min(dict(G.degree()).values()) >= 3
    vertices = list(G.nodes())
    pos = {v: j for j, v in enumerate(vertices)}
    edges = [(a,b) for a,b in G.edges()] + [(b,a) for a,b in G.edges()]
    n, M = len(vertices), len(edges)
    B = np.array([[int(v == x and u != y) for x,y in edges]
                  for u,v in edges], dtype=np.int64)
    K = B.T @ B - B @ B.T
    X = np.array([[int(u == a) for a in vertices] for u,v in edges], dtype=np.int64)
    Y = np.array([[int(v == a) for a in vertices] for u,v in edges], dtype=np.int64)
    deg = np.array([G.degree(v) for v in vertices], dtype=np.int64)
    w = deg-2
    expected_K = (X*w) @ X.T - (Y*w) @ Y.T
    assert np.array_equal(K, expected_K)
    checks += 1

    reverse = {e:j for j,e in enumerate(edges)}
    flipped = np.array([reverse[(v,u)] for u,v in edges])
    assert np.array_equal(K[np.ix_(flipped, flipped)], -K)
    checks += 1

    ev = np.linalg.eigvalsh(K.astype(float))
    positive = int(np.count_nonzero(ev > 1.e-6))
    negative = int(np.count_nonzero(ev < -1.e-6))
    if nx.is_bipartite(G):
        l,r = nx.bipartite.sets(G)
        delta = sum((Fraction(1,G.degree(v)-2) for v in l), Fraction())
        delta -= sum((Fraction(1,G.degree(v)-2) for v in r), Fraction())
        expected_index = n-2 if delta == 0 else n-1
    else:
        expected_index = n-1
    assert positive == expected_index and negative == expected_index, (n, M, positive, negative, expected_index)
    checks += 1
    assert np.count_nonzero(abs(ev) < 1.e-6) == M-2*expected_index
    checks += 1

    hsf = 2*sum(int(deg[j]**2 * w[j]**2) for j in range(n))
    hsf -= 4*sum(int(w[pos[u]]*w[pos[v]]) for u,v in G.edges())
    assert int(np.sum(K*K)) == hsf
    checks += 1

    if np.all(deg == deg[0]):
        d = int(deg[0]); A = nx.to_numpy_array(G, nodelist=vertices)
        lam = np.linalg.eigvalsh(A)
        scale = d*(d-2)
        lv = np.sqrt(np.maximum(0,np.where(abs(abs(lam)-d)<1.e-10, 0,
                                             1-lam**2/d**2))) * scale
        expected = np.sort(np.concatenate([-lv,lv,np.zeros(M-2*n)]))
        assert np.max(abs(ev-expected)) < 1.e-6
        checks += 1

# Distinguished graphs: irregular nonbipartite; irregular balanced bipartite;
# irregular unbalanced bipartite; several regular examples.
examples = [nx.complete_graph(5), nx.complete_bipartite_graph(3,4),
            nx.complete_bipartite_graph(4,4), nx.petersen_graph(),
            nx.octahedral_graph()]
examples[0].remove_edge(0,1)
examples[2].remove_edge(0,4)
for G in examples: verify_graph(G)

for n,d in ((6,3),(8,3),(10,3),(7,4),(8,4),(10,4),(8,5),(9,6)):
    for seed in range(4):
        verify_graph(nx.random_regular_graph(d, n, seed=seed))
for n,p in ((6,.78),(7,.7),(8,.68),(9,.7)):
    found=0
    for seed in range(100):
        G=nx.gnp_random_graph(n,p,seed=seed)
        if nx.is_connected(G) and min(dict(G.degree()).values()) >= 3:
            verify_graph(G); found += 1
            if found == 12: break
    assert found >= 4

# Distinct parameter structures with an irregular bipartition.
for p,q in ((3,5),(4,5),(4,6)):
    verify_graph(nx.complete_bipartite_graph(p,q))
print('VERIFICATION_OK', checks)
