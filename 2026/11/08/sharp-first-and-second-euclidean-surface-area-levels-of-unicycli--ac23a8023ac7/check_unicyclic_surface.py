"""Exact graph enumeration and numerical geometric consistency checks.
Unicyclic graphical zonotopes in canonical Euclidean coordinates.
Only standard libraries and networkx/scipy/numpy are needed.
"""
from itertools import combinations, product
from math import sqrt
import networkx as nx
import numpy as np
from scipy.spatial import ConvexHull

def bond_area(G):
    n=G.number_of_nodes(); nodes=list(G)
    ans=0.
    for bits in range(1,1<<(n-1)):
        # choose one representative of each unordered cut by requiring last vertex outside
        S={nodes[i] for i in range(n-1) if bits>>i&1};R=set(nodes)-S
        if not nx.is_connected(G.subgraph(S)) or not nx.is_connected(G.subgraph(R)):continue
        tau1=round(nx.number_of_spanning_trees(G.subgraph(S))) if len(S)>1 else 1
        tau2=round(nx.number_of_spanning_trees(G.subgraph(R))) if len(R)>1 else 1
        ans+=2*tau1*tau2*sqrt(len(S)*len(R))
    return ans

def unicyclic_area_formula(G):
    n=len(G); C=nx.cycle_basis(G);assert len(C)==1
    cyc=C[0];ell=len(cyc)
    total=0.
    for a,b in nx.bridges(G):
        H=G.copy();H.remove_edge(a,b)
        c=len(nx.node_connected_component(H,a));total+=2*ell*sqrt(c*(n-c))
    for e,f in combinations([(cyc[i],cyc[(i+1)%ell]) for i in range(ell)],2):
        H=G.copy();H.remove_edges_from([e,f]);comp=list(nx.connected_components(H))
        assert len(comp)==2
        c=len(comp[0]);total+=2*sqrt(c*(n-c))
    return total

def geometric_area(G):
    n=len(G);edges=list(G.edges())
    pts=[]
    Q=np.linalg.qr((np.eye(n) -np.ones((n,n))/n)[:,:-1])[0]
    for mask in range(1<<len(edges)):
        x=np.zeros(n)
        for i,(a,b) in enumerate(edges):
            if mask>>i&1:x[a]+=1;x[b]-=1
        pts.append(x@Q)
    return ConvexHull(np.asarray(pts),qhull_options='Qx').area

def classes(n):
    out=[]
    for T in nx.generators.nonisomorphic_trees(n):
        for u,v in combinations(range(n),2):
            if T.has_edge(u,v):continue
            G=T.copy();G.add_edge(u,v)
            if not any(nx.is_isomorphic(G,H) for H in out):out.append(G)
    return out

def expected(n):
    f=lambda k:sqrt(k*(n-k))
    m=(6*n-14)*f(1)+2*f(2)
    if n==4: return m, 8+8*sqrt(3)
    second=(6*n-16)*f(1)+2*f(2)+2*f(3)
    return m,second

if __name__=='__main__':
    totals=[]
    for n in range(4,10):
        arr=[]
        gs=classes(n)
        for G in gs:
            a=unicyclic_area_formula(G);b=bond_area(G)
            assert abs(a-b)<1e-8,(n,a,b,G.edges())
            arr.append((a,G))
        arr.sort(key=lambda z:z[0]); minval,second=expected(n)
        assert abs(arr[0][0]-minval)<1e-8,(n,minval,arr[:3])
        assert abs(arr[1][0]-second)<1e-8,(n,second,arr[:3])
        assert arr[0][0]+1e-8<arr[1][0]
        if len(arr)>2: assert arr[1][0]+1e-8<arr[2][0]
        if n<=6:
            for v,g in arr[:min(4,len(arr))]:
                geom=geometric_area(g)
                assert abs(v-geom)<1e-7,(n,v,geom)
        totals.append((n,len(arr),round(arr[0][0],7),round(arr[1][0],7)))
    print('UNICYCLIC_GRAPHICAL_ZONOTOPE_FIRST_TWO_SURFACE_LEVELS_PASSED',totals)
