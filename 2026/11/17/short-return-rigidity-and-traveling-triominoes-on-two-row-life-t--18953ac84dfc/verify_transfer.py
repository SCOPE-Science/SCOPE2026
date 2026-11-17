"""Finite, exhaustive de Bruijn certificate for two-row periodic B3/S23 Life.

Run: python verify_transfer.py
No external Python packages are needed.
"""

def local(a, b, c):
    out = 0
    for row in (0, 1):
        other = 1 - row
        neighbor_count = ((a >> row) & 1) + ((c >> row) & 1)
        neighbor_count += 2 * (((a >> other) & 1) +
                               ((b >> other) & 1) + ((c >> other) & 1))
        alive = (b >> row) & 1
        if neighbor_count == 3 or (alive and neighbor_count == 2):
            out |= 1 << row
    return out


def transfer_edges(steps):
    if steps == 1:
        vertices = range(16)
        edges = []
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    if local(a, b, c) == b:
                        edges.append((4*a + b, 4*b + c))
    else:
        vertices = range(256)
        edges = []
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    for d in range(4):
                        for e in range(4):
                            if local(local(a,b,c),local(b,c,d),local(c,d,e)) == c:
                                edges.append((64*a+16*b+4*c+d,64*b+16*c+4*d+e))
    return vertices, edges


def tarjan(vertices, edges):
    graph = {u: [] for u in vertices}
    for u,v in edges:
        graph[u].append(v)
    indices={}; low={};stack=[];on=set();components=[]
    def visit(u):
        indices[u] = low[u] = len(indices)
        stack.append(u);on.add(u)
        for v in graph[u]:
            if v not in indices:
                visit(v);low[u]=min(low[u],low[v])
            elif v in on:
                low[u]=min(low[u],indices[v])
        if low[u] == indices[u]:
            comp=[]
            while True:
                v=stack.pop();on.remove(v);comp.append(v)
                if v==u:break
            components.append(frozenset(comp))
    for u in vertices:
        if u not in indices:visit(u)
    return {c for c in components if len(c)>1 or any((v,v) in edges for v in c)}

def reachability_components(vertices,edges):
    """Independent SCC finder: repeated ordinary graph reachability."""
    adj={u:set() for u in vertices}
    for u,v in edges:adj[u].add(v)
    reaches={}
    for source in vertices:
        seen={source};front=[source]
        while front:
            u=front.pop()
            for v in adj[u]:
                if v not in seen:
                    seen.add(v);front.append(v)
        reaches[source]=seen
    remaining=set(vertices);components=[]
    while remaining:
        u=min(remaining)
        comp={v for v in remaining if v in reaches[u] and u in reaches[v]}
        remaining-=comp
        if len(comp)>1 or (u,u) in edges:
            components.append(frozenset(comp))
    return set(components)

v1,edges1=transfer_edges(1)
v2,edges2=transfer_edges(2)
assert len(edges1)==23 and len(edges2)==223
expected1 = {frozenset(x) for x in ([0],[3,12],[5,6,9,10])}
expected2 = {frozenset(x) for x in (
    [0],[51,204],
    [85,86,90,105,106,149,150,165,169,170],
    [15,60,195,240],[30,120,135,225],[45,75,180,210])}
assert tarjan(v1,edges1)==expected1
assert tarjan(v2,edges2)==expected2
assert reachability_components(v1,edges1)==expected1
assert reachability_components(v2,edges2)==expected2
# Three 4-cycles are the only genuinely two-periodic column words.
for group in ([15,60,195,240],[30,120,135,225],[45,75,180,210]):
    assert all(sum(v in group for a,v in edges2 if a==u)==1 for u in group)
    assert any(local((u>>4)&3,(u>>2)&3,u&3) != ((u>>2)&3) for u in group)
# Every two-step closed walk in the other three components is already fixed.
for group in ([0],[51,204],[85,86,90,105,106,149,150,165,169,170]):
    assert all(local((u>>4)&3,(u>>2)&3,u&3) == ((u>>2)&3) for u in group)
# Explicit four-state fixed-point adjacency and its characteristic polynomial.
core = [5,6,9,10]
B = [[int((u,v) in edges1) for v in core] for u in core]
assert B == [[1,1,0,0],[0,0,0,1],[1,0,0,0],[0,0,1,1]]
# The polynomial is (z^2-z-1)(z^2-z+1) = z^4-2z^3+z^2-1.
def multiply(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]
I = [[int(i==j) for j in range(4)] for i in range(4)]
B2=multiply(B,B); B3=multiply(B2,B); B4=multiply(B3,B)
assert all(B4[i][j]-2*B3[i][j]+B2[i][j]-I[i][j]==0
           for i in range(4) for j in range(4))
# Independent characteristic determinant verification at 5 integer arguments.
from itertools import permutations
for z in (-3,-1,0,2,4):
    M=[[z*I[i][j]-B[i][j] for j in range(4)] for i in range(4)]
    det=0
    for p in permutations(range(4)):
        inversions=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        term=(-1)**inversions
        for i in range(4):term*=M[i][p[i]]
        det+=term
    assert det == z**4-2*z**3+z*z-1
print('PASS: local transfer edges: 23 (one step), 223 (two steps)')
print('PASS: exhaustive SCC list: 3 and 6 cyclic components respectively')
print('PASS: only new two-step components: three forced spatial four-cycles')
print('PASS: fixed-point core characteristic z^4-2z^3+z^2-1')
