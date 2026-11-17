#!/usr/bin/env python3
"""Exact three-step orbit transfer for Brian's Brain on a two-row torus.

States: -1 is silent through three times, 0/1/2 is the firing time.
Each of the eight Moore offsets is counted, including coincidences.
Requires networkx and sympy; all adjacency entries are integers.
"""
from itertools import product
from collections import defaultdict
import networkx as nx

COLUMNS = list(product((-1, 0, 1, 2), repeat=2))

def allows(left, mid, right):
    for row in (0, 1):
        other = 1-row
        ns = (left[row], left[other], left[other], right[row], right[other], right[other], mid[other], mid[other])
        counts = [sum(phase == t for phase in ns) for t in range(3)]
        if mid[row] == -1:
            if 2 in counts: return False
        elif counts[(mid[row]-1) % 3] != 2:
            return False
    return True

def graph():
    graph = nx.DiGraph()
    for a, b, c in product(range(16), repeat=3):
        if allows(COLUMNS[a], COLUMNS[b], COLUMNS[c]):
            graph.add_edge((a,b), (b,c))
    return graph

def core_components(graph):
    components = [comp for comp in nx.strongly_connected_components(graph)
                  if len(comp)>1 or graph.has_edge(next(iter(comp)), next(iter(comp)))]
    return sorted(components, key=lambda comp: (-len(comp), sorted(comp)))

def trace_walks(graph, n):
    out=0
    for start in graph.nodes():
        masses = {start: 1}
        for _ in range(n):
            next_masses = defaultdict(int)
            for vertex, count in masses.items():
                for target in graph.successors(vertex):
                    next_masses[target] += count
            masses = next_masses
        out += masses.get(start, 0)
    return out

def main():
    g=graph()
    assert (len(COLUMNS),g.number_of_nodes(),g.number_of_edges())==(16,199,346)
    components=core_components(g)
    assert [len(c) for c in components]==[12,12,1]
    for comp in components:
        edges=sum(1 for a in comp for b in g.successors(a) if b in comp)
        assert edges==len(comp)
        for vertex in comp:
            assert sum(1 for b in g.successors(vertex) if b in comp)==1
            assert sum(1 for b in g.predecessors(vertex) if b in comp)==1
    for n in range(3,25):
        expected=1+(24 if n%12==0 else 0)
        assert trace_walks(g,n)==expected
    print('column alphabet:',len(COLUMNS))
    print('pair transfer: vertices=%d edges=%d' %(g.number_of_nodes(),g.number_of_edges()))
    print('all cyclic SCC sizes:',[len(c) for c in components])
    print('each cyclic SCC has one internal in-edge and one out-edge per vertex')
    for index,comp in enumerate(components):
        start=min(comp)
        seq=[start]
        vertex=start
        while True:
            successors=[b for b in g.successors(vertex) if b in comp]
            vertex=successors[0]
            if vertex==start:break
            seq.append(vertex)
        assert len(seq)==len(comp)
        print('cycle %d column phases:' %index, [COLUMNS[a] for a,b in seq])
    print('trace(F^3) for n=3..24:',[trace_walks(g,n) for n in range(3,25)])
    print('ALL EXACT TRANSFER CHECKS PASSED')

if __name__=='__main__': main()
