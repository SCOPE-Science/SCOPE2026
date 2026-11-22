#!/usr/bin/env python3
"""Independent verification of complement zero-forcing enumerator.
All graph generators and checks use only Python's standard library.
"""
from itertools import combinations, product
from math import comb

def make_graph(n, edges):
    a=[set() for _ in range(n)]
    for u,v in edges:
        if not 0<=u<n or not 0<=v<n or u==v: raise ValueError('edge')
        a[u].add(v);a[v].add(u)
    return a

def petersen():
    verts=list(combinations(range(5),2))
    return make_graph(10,[(i,j) for i in range(10) for j in range(i) if set(verts[i]).isdisjoint(verts[j])])

def heawood():
    v=list(range(1,8))
    return make_graph(14,[(i,7+j) for i,a in enumerate(v) for j,b in enumerate(v) if (a&b).bit_count()%2==0])

def dodecahedron():
    edges=[]
    for i in range(10):
        edges += [(i,(i+1)%10),(i,10+i),(10+i,10+(i+2)%10)]
    return make_graph(20,edges)

def desargues():
    v2=list(combinations(range(5),2));v3=list(combinations(range(5),3))
    return make_graph(20,[(i,10+j) for i,a in enumerate(v2) for j,b in enumerate(v3) if set(a)<set(b)])

def pg3():
    vecs=[]
    for v in product(range(3),repeat=3):
        if v==(0,0,0):continue
        if v not in vecs and tuple((2*x)%3 for x in v) not in vecs:vecs.append(v)
    assert len(vecs)==13
    return make_graph(26,[(i,13+j) for i,a in enumerate(vecs) for j,b in enumerate(vecs) if sum(x*y for x,y in zip(a,b))%3==0])

def hexagons(a):
    n=len(a); cycles=set()
    for v in range(n):
        def dfs(path):
            if len(path)==6:
                if path[-1] not in a[path[0]]:return
                c=tuple(path); reps=[]
                for p in (c,c[::-1]):
                    reps.extend(p[i:]+p[:i] for i in range(6))
                cycles.add(min(reps));return
            for w in a[path[-1]]:
                if w not in path:dfs(path+[w])
        dfs([v])
    return len(cycles)

def forcing(a, whites):
    n=len(a); white=set(whites)
    # deliberately sequential forcing, not synchronous
    while white:
        for u in range(n):
            if u in white:continue
            candidates=[v for v in white if v!=u and v not in a[u]]
            if len(candidates)==1:
                white.remove(candidates[0]);break
        else:return False
    return True

def check(a,name):
    n=len(a);degrees=[len(row) for row in a];assert min(degrees)>=2
    assert all(not (a[u]&a[v]) for u in range(n) for v in a[u]) # no triangles
    assert all(len(a[u]&a[v])<=1 for u in range(n) for v in range(u)) # no squares
    c6=hexagons(a)
    twopath=sum(comb(t,2) for t in degrees)
    degree2=[len(set().union(*(a[z] for z in a[u]))-{u}-a[u]) for u in range(n)]
    expected=(n-3)*twopath-sum(comb(t,2) for t in degree2)+2*c6
    got=0
    for S in combinations(range(n),3):
        rule=any(v not in S and sum(u in a[v] for u in S)==2 for v in range(n))
        brute=forcing(a,S)
        assert rule==brute,(name,S,rule,brute)
        got+=brute
    assert got==expected,(name,got,expected)
    assert all(forcing(a,S) for S in combinations(range(n),2))
    assert all(not forcing(a,S) for S in combinations(range(n),4))
    print(f'{name}: n={n}, degrees={min(degrees)}..{max(degrees)}, hexagons={c6}, minimum_white_triples={got}, formula={expected}, passed')

def c8_chord():
    return make_graph(8,[(i,(i+1)%8) for i in range(8)]+[(0,4)])

def joined_cycles():
    return make_graph(11,[(i,(i+1)%5) for i in range(5)]+[(i,5+(i-4)%6) for i in range(5,11)]+[(0,5)])

if __name__=='__main__':
    for name,a in [('Petersen',petersen()),('Heawood',heawood()),('Dodecahedron',dodecahedron()),('Desargues',desargues()),('PG(2,3) incidence',pg3()),('8-cycle plus antipodal chord',c8_chord()),('5-cycle bridged to 6-cycle',joined_cycles())]:check(a,name)

