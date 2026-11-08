#!/usr/bin/env python3
"""Exact checks for the leaf-number law of weighted spanning trees on cactus graphs.

Requires networkx.  The finite checks are independent of the general proof.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
import networkx as nx


def simple_cycles_and_bridges(G):
    cycles = []
    bridges = []
    for block in nx.biconnected_components(G):
        H = G.subgraph(block)
        if len(block) == 2:
            bridges.extend(tuple(sorted(e)) for e in H.edges())
        else:
            assert H.number_of_edges() == len(block)
            assert all(d == 2 for _, d in H.degree())
            cycles.append(sorted(tuple(sorted(e)) for e in H.edges()))
    return cycles, sorted(bridges)


def convolution(A, B):
    D = Counter()
    for a, wa in A.items():
        for b, wb in B.items():
            D[a+b] += wa*wb
    return dict(D)


def predicted(G, weight):
    cycles, bridges = simple_cycles_and_bridges(G)
    leaf_count_fixed = sum(G.degree(v) == 1 for v in G)
    law = {leaf_count_fixed: Fraction(1)}
    for cycle in cycles:
        normalizer = sum(Fraction(1, weight[e]) for e in cycle)
        local = Counter()
        for e in cycle:
            contribution = sum(G.degree(v) == 2 for v in e)
            local[contribution] += Fraction(1, weight[e]) / normalizer
        law = convolution(law, local)
    return law, cycles, bridges


def brute(G, weight):
    cycles, bridges = simple_cycles_and_bridges(G)
    total = Fraction(0)
    raw = Counter()
    pairs = Counter()
    singles = Counter()
    for deletes in product(*cycles):
        removed = set(deletes)
        chosen = [e for e in sorted(tuple(sorted(e)) for e in G.edges()) if e not in removed]
        assert nx.is_tree(nx.Graph([(u, v) for u, v in chosen]).to_undirected())
        probweight = Fraction(1)
        for e in chosen:
            probweight *= weight[e]
        degrees = Counter()
        for u,v in chosen:
            degrees[u] += 1
            degrees[v] += 1
        leaves = {v for v in G.nodes() if degrees[v] == 1}
        raw[len(leaves)] += probweight
        for u in leaves:
            singles[u] += probweight
            for v in leaves:
                if u != v:
                    pairs[u,v] += probweight
        total += probweight
    return {k: v/total for k,v in raw.items()}, {k: v/total for k,v in singles.items()}, {k: v/total for k,v in pairs.items()}


def check_graph(G, weights):
    weight = {tuple(sorted(e)): Fraction(weights[tuple(sorted(e))]) for e in G.edges()}
    law, cycles, _ = predicted(G, weight)
    measured, singles, pairs = brute(G, weight)
    assert law == measured, (G.edges(),law,measured)
    for u in G.nodes():
        for v in G.nodes():
            if v <= u:
                continue
            cov = pairs.get((u,v), 0)-singles.get(u,0)*singles.get(v,0)
            assert cov == pairs.get((v,u),0)-singles.get(u,0)*singles.get(v,0)
            if G.degree(u) != 2 or G.degree(v) != 2:
                assert cov == 0
                continue
            Cu = next((i for i,C in enumerate(cycles) if any(u in e for e in C)), None)
            Cv = next((i for i,C in enumerate(cycles) if any(v in e for e in C)), None)
            if Cu != Cv or Cu is None:
                assert cov == 0
                continue
            C = cycles[Cu]
            z = sum(1/weight[e] for e in C)
            q = {e: (1/weight[e])/z for e in C}
            pu=sum(q[e] for e in C if u in e)
            pv=sum(q[e] for e in C if v in e)
            common=[e for e in C if u in e and v in e]
            predicted_cov=(q[common[0]] if common else 0)-pu*pv
            assert cov == predicted_cov
    return len(cycles)


def mask_counts(mask):
    # 1 marks an original-degree-two vertex of a cycle, 0 marks an attached pendant.
    m=len(mask)
    ac=[sum((mask[i],mask[(i+1)%m])) for i in range(m)]
    return ac.count(2),ac.count(1),ac.count(0)


def thresholds():
    first_nonreal=None
    first_nonlc=None
    for m in range(3,14):
        for mask in product((0,1),repeat=m):
            N=m+mask.count(0)
            a,b,c=mask_counts(mask)
            if b*b < 4*a*c:
                if first_nonreal is None or N < first_nonreal[0]:
                    first_nonreal=(N,m,mask,(c,b,a))
            if b*b < a*c:
                if first_nonlc is None or N < first_nonlc[0]:
                    first_nonlc=(N,m,mask,(c,b,a))
    assert first_nonreal[0] == 7, first_nonreal
    assert first_nonlc[0] == 10, first_nonlc
    print('minimum order for non-real roots:',first_nonreal)
    print('minimum order for non-log-concavity:',first_nonlc)


def main():
    graph_count=0
    cyclic_graph_count=0
    weighted_checks=0
    for G in nx.graph_atlas_g():
        if len(G)<3 or not nx.is_connected(G):
            continue
        try:
            cycles, _ = simple_cycles_and_bridges(G)
        except AssertionError:
            continue
        assert check_graph(G, {tuple(sorted(e)):1 for e in G.edges()}) == len(cycles)
        graph_count+=1
        cyclic_graph_count += bool(cycles)
        # independent reciprocal-conductance check with deterministic nonconstant weights
        weights={tuple(sorted(e)):1 + (5*min(e)+7*max(e))%11 for e in G.edges()}
        assert check_graph(G,weights) == len(cycles)
        weighted_checks += 1
    assert graph_count>100 and cyclic_graph_count>40
    print('all connected cactus graph isomorphism types, orders 3..7:',graph_count)
    print('of which cyclic:',cyclic_graph_count)
    print('nontrivial weighted repetitions:',weighted_checks)
    thresholds()
    for m, expected in [(5,(1,2,2)), (8,(1,2,5))]:
        G=nx.cycle_graph(m)
        for j in (0,1):
            G.add_edge(j,m+j)
        law,_cycles,_bridges=predicted(G,{tuple(sorted(e)):Fraction(1) for e in G.edges()})
        assert tuple(int(m*law.get(i+2,0)) for i in range(3)) == expected
        print('C_%d plus two adjacent pendant leaves has law'%m,law)
    print('PASS')

if __name__=='__main__':
    main()
