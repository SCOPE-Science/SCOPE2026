#!/usr/bin/env python3
"""Exact algebraic certificate for the simplicial double of the 600-cell boundary.
Uses only Python's standard library and arithmetic in Z[phi], phi^2=phi+1.
The coordinates are twice the standard circumradius-one 600-cell coordinates.
"""
from itertools import combinations, permutations, product
from collections import Counter, deque
import json
from pathlib import Path

ZERO=(0,0)
ONE=(1,0)
PHI=(0,1)
INVPHI=(-1,1)  # phi-1

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def mul(x,y): return (x[0]*y[0]+x[1]*y[1],x[0]*y[1]+x[1]*y[0]+x[1]*y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def sgn(x):
    # x=(A+B*sqrt(5))/2. Integer-only sign test.
    a,b=x; A,B=2*a+b,b
    if B==0: return (A>0)-(A<0)
    if A==0: return (B>0)-(B<0)
    if A>0 and B>0: return 1
    if A<0 and B<0: return -1
    if A>0: return (A*A>5*B*B)-(A*A<5*B*B)
    return (5*B*B>A*A)-(5*B*B<A*A)

def dot(u,v):
    z=ZERO
    for x,y in zip(u,v):z=add(z,mul(x,y))
    return z

def vertices():
    vs=[]
    for k in range(4):
        for s in (-1,1):
            v=[ZERO]*4;v[k]=(2*s,0);vs.append(tuple(v))
    for signs in product((-1,1),repeat=4):
        vs.append(tuple((s,0) for s in signs))
    for p in permutations(range(4)):
        if sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2:continue
        for signs in product((-1,1),repeat=3):
            values=(ZERO,ONE,PHI,INVPHI)
            v=[ZERO]*4
            for i in range(4):
                x=values[i];s=1 if i==0 else signs[i-1]
                v[p[i]]=(s*x[0],s*x[1])
            vs.append(tuple(v))
    assert len(vs)==120 and len(set(vs))==120
    assert all(dot(v,v)==(4,0) for v in vs)
    return vs

def certify():
    vs=vertices()
    E=[];adj=[set() for _ in vs]
    target=(0,2)
    for i,j in combinations(range(120),2):
        d=dot(vs[i],vs[j]);assert d!=target or sgn(sub(d,target))==0
        assert sgn(sub(d,target)) <=0, (i,j,d)
        if d==target: E.append((i,j));adj[i].add(j);adj[j].add(i)
    assert len(E)==720
    assert Counter(map(len,adj))=={12:120}
    tetra=[]
    # All 4-cliques, enumerated once through sorted common-neighbor intersections
    for i,j in E:
        common=adj[i]&adj[j]
        for k in sorted(x for x in common if x>j):
            for l in sorted(x for x in common&adj[k] if x>k):
                tetra.append((i,j,k,l))
    assert len(tetra)==600 and len(set(tetra))==600
    tri=Counter(t for f in tetra for t in combinations(f,3))
    assert len(tri)==1200 and set(tri.values())=={2}
    # Every tetra is a *genuine supporting facet*, with only its four vertices touching.
    C=(4,6)  # the dot product of any facet vertex with its outward normal S
    for f in tetra:
        S=tuple(add(add(vs[f[0]][k],vs[f[1]][k]),add(vs[f[2]][k],vs[f[3]][k])) for k in range(4))
        equal=[]
        for i,v in enumerate(vs):
            diff=sub(C,dot(v,S))
            assert sgn(diff)>=0,(f,i,diff)
            if sgn(diff)==0:equal.append(i)
        assert tuple(equal)==f,(f,equal)
    # D^2 has one vertex for every original edge; a pair is joined iff opposite in a tetra.
    e_index={e:i for i,e in enumerate(E)}
    double_adj=[set() for _ in E]
    for f in tetra:
        a,b,c,d=f
        for e,g in (((a,b),(c,d)),((a,c),(b,d)),((a,d),(b,c))):
            i,j=e_index[e],e_index[g]
            assert j not in double_adj[i]
            double_adj[i].add(j);double_adj[j].add(i)
    assert len(double_adj)==720
    assert Counter(map(len,double_adj))=={5:720}
    assert sum(map(len,double_adj))==3600
    parent=[-2]*720;parent[0]=-1;q=deque([0]);order=[]
    while q:
        u=q.popleft();order.append(u)
        for v in sorted(double_adj[u]):
            if parent[v]==-2:parent[v]=u;q.append(v)
    assert len(order)==720
    # Independently verify the published spanning-tree parent certificate.
    tree_path=Path(__file__).with_name('spanning_tree.json')
    with tree_path.open(encoding='utf-8') as f:
        supplied=json.load(f)
    assert len(supplied)==720 and supplied[0]==-1
    for v in range(1,720):
        assert isinstance(supplied[v],int) and supplied[v] in double_adj[v]
        u=v;seen_chain=set()
        while u!=0:
            assert u not in seen_chain
            seen_chain.add(u)
            u=supplied[u]
    assert supplied==parent
    # A connected graph with V=720 and E=1800 retracts to wedge of 1800-720+1 circles.
    assert 1800-720+1==1081
    # Also calculate the precise graph girth (not needed for homotopy proof).
    g=1000
    for start in range(720):
        dis={start:0};par={start:-1};queue=deque([start])
        while queue:
            u=queue.popleft()
            for v in double_adj[u]:
                if v not in dis:dis[v]=dis[u]+1;par[v]=u;queue.append(v)
                elif par[u]!=v:g=min(g,dis[u]+dis[v]+1)
    assert g==6
    print('vertex_coords=120 original_edges=720 original_triangles=1200 tetrahedral_facets=600')
    print('all_600_facets_exactly_supporting=True; tetra_incidence=2_per_triangle')
    print('double_vertices=720 double_edges=1800 degree=5 components=1 girth=6')
    print('reduced_integral_homology=Z^1081 in degree 1; zero otherwise')
    print('exact_arithmetic_certificate=PASS')
    return parent

if __name__=='__main__': certify()
