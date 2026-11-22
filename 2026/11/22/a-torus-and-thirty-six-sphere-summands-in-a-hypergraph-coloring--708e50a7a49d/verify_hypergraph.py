"""Finite, dependency-free certificate for the nine-edge coloring-complex splitting.

Run: python3 verify_hypergraph.py
The topological inputs are Lemma 17 and Proposition 19 in Breuer--Dall--Kubitzke,
Hypergraph Coloring Complexes, Section 5; the script checks their finite poset data.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations

EDGE_STRINGS = (
    '12347', '12358', '12369', '14567', '24568', '34569',
    '14789', '25789', '36789'
)
EDGES = tuple(tuple(map(int, s)) for s in EDGE_STRINGS)
COLLAPSES = (
    ((1, 6, 7), (0, 1, 6, 7)),
    ((0, 1, 4), (0, 1, 3, 4)),
    ((0, 3, 5), (0, 2, 3, 5)),
    ((1, 2, 7), (1, 2, 7, 8)),
    ((4, 6, 7), (3, 4, 6, 7)),
    ((4, 5, 8), (4, 5, 7, 8)),
    ((3, 6, 8), (3, 5, 6, 8)),
    ((2, 6, 8), (0, 2, 6, 8)),
    ((1, 2, 4), (1, 2, 4, 5)),
    ((3, 8), (3, 5, 8)),
    ((4, 6), (3, 4, 6)),
    ((2, 6), (0, 2, 6)),
    ((0, 5), (0, 2, 5)),
    ((1, 6), (0, 1, 6)),
    ((4, 8), (4, 7, 8)),
    ((2, 7), (2, 7, 8)),
    ((2, 4), (2, 4, 5)),
    ((0, 4), (0, 3, 4)),
)

def components(subset):
    parent = list(range(10))
    def find(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v
    for k in subset:
        edge = EDGES[k]
        for v in edge[1:]:
            parent[find(v)] = find(edge[0])
    blocks = defaultdict(list)
    for vertex in range(1, 10):
        blocks[find(vertex)].append(vertex)
    return tuple(sorted(tuple(x) for x in blocks.values()))

def finer(a, b):
    bset = [set(block) for block in b]
    return all(any(set(block) <= target for target in bset) for block in a)

def connected(vertices, edges):
    if not vertices:
        return False
    neighbor = {v: set() for v in vertices}
    for u,v in edges:
        neighbor[u].add(v)
        neighbor[v].add(u)
    stack=[next(iter(vertices))]
    seen = set(stack)
    while stack:
        for v in neighbor[stack.pop()]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen)==len(vertices)

def check():
    all_subsets = [frozenset(i for i in range(9) if m & (1 << i))
                   for m in range(1, 1 << 9)]
    partitions = {s: components(s) for s in all_subsets}
    P = {p for p in partitions.values() if len(p)>=2}
    assert Counter(map(len,P)) == {5:9,3:18,2:9}, Counter(map(len,P))
    assert sum(len(p) == 1 for p in partitions.values()) == 421
    for p in P:
        assert len(p) in (2,3,5)
    for p in (p for p in P if len(p)==3):
        lo=[q for q in P if q != p and finer(q,p)]
        assert len(lo)==2 and all(len(q)==5 for q in lo)
    for p in (p for p in P if len(p)==2):
        lo=[q for q in P if q != p and finer(q,p)]
        pairs=[(i,j) for i in range(len(lo)) for j in range(i+1,len(lo))
               if finer(lo[i],lo[j]) or finer(lo[j],lo[i])]
        degree=Counter(u for pair in pairs for u in pair)
        assert len(lo)==8 and len(pairs)==8
        assert sum(len(q)==5 for q in lo)==4
        assert sum(len(q)==3 for q in lo)==4
        assert set(degree.values())=={2}
        assert connected(set(range(len(lo))),pairs)
    nerve={s for s,p in partitions.items() if len(p)>=2}
    assert Counter(map(len,nerve)) == {1:9,2:36,3:36,4:9}
    for s in nerve:
        assert all(frozenset(t) in nerve for k in range(1,len(s))
                   for t in combinations(s,k))
    remaining = set(nerve)
    for face, coface in COLLAPSES:
        face,coface=map(frozenset,(face,coface))
        assert face in remaining and coface in remaining
        assert face < coface and len(coface)==len(face)+1
        assert [s for s in remaining if face<s] == [coface]
        remaining.remove(face)
        remaining.remove(coface)
    assert Counter(map(len,remaining)) == {1:9,2:27,3:18}
    triangles=sorted(tuple(sorted(t)) for t in remaining if len(t)==3)
    edges=sorted(tuple(sorted(t)) for t in remaining if len(t)==2)
    vertices=set(next(iter(t)) for t in remaining if len(t)==1)
    assert connected(vertices,edges)
    incidence=defaultdict(list)
    for index,tri in enumerate(triangles):
        for e in combinations(tri,2):
            incidence[e].append(index)
    assert set(incidence)==set(edges)
    assert all(len(v)==2 for v in incidence.values())
    for vertex in vertices:
        link_edges=[]
        for t in triangles:
            if vertex in t:
                link_edges.append(tuple(x for x in t if x!=vertex))
        link_vertices={v for edge in link_edges for v in edge}
        assert link_vertices and connected(link_vertices,link_edges)
        assert len(link_edges)==len(link_vertices)
        degree=Counter(v for edge in link_edges for v in edge)
        assert set(degree.values())=={2}
    # Propagate coherent orientations of all triangles across shared edges.
    adjacent=defaultdict(list)
    def induced_boundary_sign(tri, e):
        # Oriented boundary of sorted triple: (b,c)-(a,c)+(a,b).
        a,b,c=tri
        if e==(b,c): return +1
        if e==(a,c): return -1
        if e==(a,b): return +1
        raise AssertionError((tri,e))
    for edge,ts in incidence.items():
        i,j=ts
        # If orientation variables eps_i and eps_j are coherent,
        # eps_j = -eps_i * boundary_sign_i * boundary_sign_j.
        factor=-induced_boundary_sign(triangles[i],edge)*induced_boundary_sign(triangles[j],edge)
        adjacent[i].append((j,factor))
        adjacent[j].append((i,factor))
    sign={0:1}; queue=deque([0])
    while queue:
        i=queue.popleft()
        for j,factor in adjacent[i]:
            value=sign[i]*factor
            if j in sign:
                assert sign[j]==value
            else:
                sign[j]=value
                queue.append(j)
    assert len(sign)==len(triangles)
    assert len(vertices)-len(edges)+len(triangles)==0
    print('HYPERGRAPH_COLORING_TORUS_WEDGE_VERIFIED')
    print('intersection_poset: 9 S3, 18 S1, 9 S0; empty index-subsets 421')
    print('nerve: 9 vertices,36 edges,36 triangles,9 tetrahedra')
    print('collapse: 18 elementary pairs; remaining closed connected orientable')
    print('surface: V=9 E=27 F=18 genus=1')
    print('wedge_lemma: T2 plus (18+9) S2 and 9 S3')

if __name__=='__main__':
    check()
