"""Independent directed-graph replay of the exceptional 7-cycle bound."""
import json
from itertools import combinations
from pathlib import Path
D=json.loads((Path(__file__).parent/'witnesses.json').read_text())
V=32
arcs=[((2*v)%V,(2*v+1)%V) for v in range(V)]
cycles=[]
for start in range(V):
    def search(u,path,seen):
        if len(path)==7:
            if start in arcs[u]:
                cycles.append(tuple(path))
            return
        for v in arcs[u]:
            if v>start and v not in seen:
                search(v,path+[v],seen|{v})
    search(start,[start],{start})
assert len(cycles)==12
sets=[set(c) for c in cycles]
assert len(set(frozenset(c) for c in sets))==12
assert not any(not(sets[a]&sets[b] or sets[a]&sets[c] or sets[a]&sets[d] or sets[b]&sets[c] or sets[b]&sets[d] or sets[c]&sets[d]) for a,b,c,d in combinations(range(12),4))
assert any(all(not(sets[a]&sets[b]) for a,b in combinations(comb,2)) for comb in combinations(range(12),3))

# Convert every binary circle listed in the certificate independently
# into its five-window vertex set, checking all claimed capacity witnesses.
for ns,ws in D['witnesses_by_ring_length'].items():
    k=int(ns); visited=set()
    for word in ws:
        vertices=[]
        for j in range(k):
            z=''.join(word[(j+i)%k] for i in range(5))
            vertices.append(int(z,2))
        assert len(set(vertices))==k
        assert not visited.intersection(vertices)
        visited.update(vertices)
    assert len(ws)==(3 if k==7 else V//k)
print('INDEPENDENT_DIGRAPH_OK: 12 seven-cycles; no disjoint quadruple; all constructive packs checked')
