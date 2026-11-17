"""Independent reference implementation of the finite graph via NetworkX SCCs.
Run with Python 3 and networkx 3.x.
"""
from itertools import product
import networkx as nx

def local(a,b,c,highlife):
    result = 0
    for row in range(3):
        near = sum((a>>k)&1 for k in range(3)) + sum((c>>k)&1 for k in range(3))
        near += sum((b>>k)&1 for k in range(3) if k != row)
        alive = (b>>row)&1
        if ((near in (2,3) if alive else near in ((3,6) if highlife else (3,)))):
            result |= 1<<row
    return result

def build(highlife):
    table = [[[[] for target in range(8)] for b in range(8)] for a in range(8)]
    for a,b,c in product(range(8),repeat=3):
        table[a][b][local(a,b,c,highlife)].append(c)
    graph = nx.DiGraph()
    for a,b in product(range(512),repeat=2):
        valid = []
        for t in range(3):
            col_a=(a>>(3*t))&7
            col_b=(b>>(3*t))&7
            next_b=(b>>(3*((t+1)%3)))&7
            valid.append(table[col_a][col_b][next_b])
        if not all(valid):continue
        for c0,c1,c2 in product(*valid):
            c = c0|(c1<<3)|(c2<<6)
            graph.add_edge((a,b),(b,c))
    return graph

for highlife in [False,True]:
    graph=build(highlife)
    cycles=[s for s in nx.strongly_connected_components(graph)
            if len(s)>1 or any(graph.has_edge(v,v) for v in s)]
    cyclic=set().union(*cycles)
    varying=sum(not all(((z>>(3*t))&7)==(z&7) for t in range(3) for z in pair)
                for pair in cyclic)
    sizes=sorted((len(s) for s in cycles),reverse=True)
    print(('HighLife' if highlife else 'Life'),
          'edges',graph.number_of_edges(),
          'nontrivial SCC sizes',sizes,'cyclic vertices',len(cyclic),'varying',varying)
    assert sizes==[30,27] and len(cyclic)==57 and varying==0
    if not highlife:baseline=cyclic
    else:assert baseline==cyclic
