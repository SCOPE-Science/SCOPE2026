"""Exact small-case verification of simplicial doubling for joins of cycles.

Requires Python 3.9 or later; no external libraries. This finite test
corroborates a separate symbolic proof for arbitrary cycle lengths.
"""
from itertools import combinations, product
from collections import deque

def canonical_edge(a,b):
    return tuple(sorted((a,b)))

def components(vertices,edges):
    adjacency={v:set() for v in vertices}
    for a,b in edges:
        assert a!=b
        adjacency[a].add(b)
        adjacency[b].add(a)
    left=set(vertices)
    sizes=[]
    while left:
        root=next(iter(left)); queue=[root]; left.remove(root)
        vs={root}
        while queue:
            v=queue.pop()
            for w in adjacency[v]:
                if w in left:
                    left.remove(w); vs.add(w); queue.append(w)
        ee=sum(1 for u,v in edges if u in vs and v in vs)
        sizes.append((len(vs),ee,ee-len(vs)+1))
    return sorted(sizes)

def check(m,n):
    L=[canonical_edge(i,(i+1)%m) for i in range(m)]
    R=[canonical_edge(m+j,m+(j+1)%n) for j in range(n)]
    facets=[set(e+f) for e,f in product(L,R)]
    # Vertices of the double are edges in the original join.
    vertices={e for F in facets for e in combinations(sorted(F),2)}
    doubled_edges=set()
    for F in facets:
        arr=sorted(F)
        # All three pair partitions of four vertices.
        for pairs in [((arr[0],arr[1]),(arr[2],arr[3])),
                      ((arr[0],arr[2]),(arr[1],arr[3])),
                      ((arr[0],arr[3]),(arr[1],arr[2]))]:
            u,v=(canonical_edge(*pair) for pair in pairs)
            doubled_edges.add(canonical_edge(u,v))
    A=set(L+R)
    B={canonical_edge(i,m+j) for i in range(m) for j in range(n)}
    expected=set()
    for e in L:
        for f in R:
            expected.add(canonical_edge(e,f))
    for i in range(m):
        for j in range(n):
            u=canonical_edge(i,m+j)
            for di,dj in ((1,1),(1,-1)):
                v=canonical_edge((i+di)%m,m+(j+dj)%n)
                expected.add(canonical_edge(u,v))
    assert vertices == A|B
    assert doubled_edges == expected
    assert not any((u in A and v in B) or (u in B and v in A) for u,v in doubled_edges)
    assert len(vertices)==m+n+m*n
    assert len(doubled_edges)==3*m*n
    all_components=components(vertices,doubled_edges)
    expected_components=[(m+n,m*n,(m-1)*(n-1))]
    if m%2==0 and n%2==0:
        expected_components.extend([(m*n//2,m*n,m*n//2+1)]*2)
    else:
        expected_components.append((m*n,2*m*n,m*n+1))
    assert all_components==sorted(expected_components),(m,n,all_components,expected_components)
    # The factor-preserving dihedral action has exactly two interval orbit
    # spaces, one for each canonical summand. Check all vertex/edge orbits,
    # including the edge inversion on the categorical-product summand.
    def act(v, a, s, b, t):
        def f(z):
            return (s*z+a)%m if z<m else m+(t*(z-m)+b)%n
        return canonical_edge(*(f(z) for z in v))
    group=[(a,s,b,t) for a in range(m) for s in (-1,1)
           for b in range(n) for t in (-1,1)]
    e_A={e for e in doubled_edges if e[0] in A}
    e_B=doubled_edges-e_A
    def orbit_vertex(v): return {act(v,*g) for g in group}
    def orbit_edge(e):
        return {canonical_edge(act(e[0],*g),act(e[1],*g)) for g in group}
    assert orbit_vertex(L[0]) == set(L)
    assert orbit_vertex(R[0]) == set(R)
    assert orbit_vertex(next(iter(B))) == B
    assert orbit_edge(next(iter(e_A))) == e_A
    u,v=next(iter(e_B))
    assert orbit_edge((u,v)) == e_B
    assert any(act(u,*g)==v and act(v,*g)==u for g in group)
    return len(vertices),len(doubled_edges),all_components

if __name__=='__main__':
    tested=0
    for m in range(3,10):
        for n in range(3,10):
            check(m,n); tested+=1
    for m,n in ((3,5),(4,4),(4,7),(6,8)):
        V,E,cc=check(m,n)
        print(f'{m}x{n}: vertices={V}, edges={E}, components={cc}')
    print(f'JOIN_CYCLES_DOUBLE_EXACT_PASS ({tested} ordered parameter pairs)')
