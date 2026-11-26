#!/usr/bin/env python3
"""Exact facet and graph-homotopy checks for doubles of cyclic 4-polytope boundaries.

No external packages required. Vertex parameters are integer points on the moment curve.
This finite checker is corroborative; the universal proof is combinatorial.
"""
from itertools import combinations
from collections import defaultdict


def facet_vandermonde(n):
    """A four-set is a moment-curve facet iff the defining polynomial is one-signed at the other vertices."""
    result = set()
    for s in combinations(range(n), 4):
        rem = (v for v in range(n) if v not in s)
        signs = set()
        for t in rem:
            p = 1
            for a in s:
                p *= t-a
            signs.add(p > 0)
            if len(signs) > 1:
                break
        if len(signs) == 1:
            result.add(s)
    return result


def facet_gale(n):
    result = set()
    for s in combinations(range(n),4):
        chosen = set(s)
        other = [i for i in range(n) if i not in chosen]
        if all(sum(a < k < b for k in chosen) % 2 == 0 for a,b in combinations(other,2)):
            result.add(s)
    return result


def facet_cycle(n):
    cyc = [frozenset((i, (i+1)%n)) for i in range(n)]
    fs=set()
    for a,b in combinations(cyc,2):
        if not a.intersection(b):
            fs.add(tuple(sorted(a|b)))
    return fs


def doubled_graph(n, facets):
    verts = list(combinations(range(n),2))
    vertex_index={e:i for i,e in enumerate(verts)}
    edgelist=[]
    for a,b,c,d in sorted(facets):
        for e,f in (((a,b),(c,d)),((a,c),(b,d)),((a,d),(b,c))):
            edgelist.append(tuple(sorted((vertex_index[e],vertex_index[f]))))
    assert len(set(edgelist)) == len(edgelist)
    parent=list(range(len(verts)))
    def root(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]]
            i=parent[i]
        return i
    def union(i,j):
        ri,rj=root(i),root(j)
        if ri != rj:
            parent[ri]=rj
    for i,j in edgelist:
        union(i,j)
    compV=defaultdict(list)
    compE=defaultdict(int)
    for i,pair in enumerate(verts):
        compV[root(i)].append(pair)
    for i,j in edgelist:
        assert root(i)==root(j)
        compE[root(i)]+=1
    return verts, edgelist, [(v,compE[r]) for r,v in compV.items()]


def run(n):
    f1=facet_vandermonde(n)
    f2=facet_gale(n)
    f3=facet_cycle(n)
    assert f1==f2==f3, (n, f1^f3)
    assert len(f1)==n*(n-3)//2
    vertices,edges,cc=doubled_graph(n, f1)
    assert len(vertices)==n*(n-1)//2
    assert len(edges)==3*n*(n-3)//2
    counts=sorted((len(v),e,e-len(v)+1) for v,e in cc)
    if n%2:
        assert counts==[(n*(n-1)//2,3*n*(n-3)//2,n*(n-4)+1)], (n,counts)
    else:
        m=n//2
        same=(m*(m-1),n*(n-3)//2,n*(n-4)//4+1)
        opposite=(m*m,n*(n-3),3*n*(n-4)//4+1)
        assert counts==sorted((same, opposite)),(n,counts)
        for vs,es in cc:
            typ={((a-b)&1) for a,b in vs}
            assert len(typ)==1
            k=typ.pop()
            expected=same if k==0 else opposite
            assert (len(vs),es,es-len(vs)+1)==expected
    return len(f1),len(vertices),len(edges),counts


if __name__ == '__main__':
    for n in list(range(5,25))+[28,29,30,31,32]:
        f,v,e,components=run(n)
        print(f"n={n:2d} facets={f:4d} vertices={v:4d} edges={e:5d} components={components}")
    print('ALL_VERIFY_OK')
