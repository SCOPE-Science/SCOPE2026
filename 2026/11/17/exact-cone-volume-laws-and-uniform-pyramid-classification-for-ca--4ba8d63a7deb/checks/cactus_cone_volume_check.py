"""Standalone finite checks for cone-volume weights of cactus graphical zonotopes.
Requires Python 3, networkx, sympy, numpy, scipy. The theorem is proved analytically;
these small exact tests verify normalization, all bonds and factorization.
"""
import itertools
from fractions import Fraction
import networkx as nx
import sympy as sp
import numpy as np
from scipy.linalg import null_space
from scipy.spatial import ConvexHull


def make_cactus(blocks):
    # Each block = ('cycle', attachment_vertex, length) or ('bridge', attachment_vertex).
    G=nx.Graph();G.add_node(0); next_vertex=1
    for block in blocks:
        kind,root=block[:2]
        if kind=='bridge':
            G.add_edge(root,next_vertex);next_vertex+=1
        else:
            m=block[2];nodes=[root]+list(range(next_vertex,next_vertex+m-1));next_vertex+=m-1
            G.add_edges_from((nodes[i],nodes[(i+1)%m]) for i in range(m))
    return G


def trees(G):
    n=len(G)
    if n<=1:return 1
    A=nx.to_numpy_array(G,nodelist=sorted(G),dtype=int)
    L=sp.diag(*[int(v) for v in A.sum(axis=1)])-sp.Matrix(A.astype(int).tolist())
    return int(L[:n-1,:n-1].det())


def actual_facets(G):
    N=G.number_of_nodes();V=set(G.nodes)
    assert sorted(V)==list(range(N))
    tau=trees(G)
    cycles=nx.cycle_basis(G);lengths=[len(c) for c in cycles]
    bridges={frozenset(e) for e in nx.bridges(G)}
    assert tau==sp.prod(lengths)
    d=N-1
    facets=[]
    for r in range(1,N):
      for S_t in itertools.combinations(range(1,N),r):
        S=set(S_t);T=V-S
        if not nx.is_connected(G.subgraph(S)) or not nx.is_connected(G.subgraph(T)):continue
        crossing={frozenset((a,b)) for a,b in nx.edge_boundary(G,S)}
        base=trees(G.subgraph(S))*trees(G.subgraph(T))
        # Actual exact cone volume from subgraph determinant and cut norm.
        w=Fraction(len(crossing)*base,2*d*tau)
        if len(crossing)==1:
            assert crossing <= bridges
            expected=Fraction(1,2*d);klass=('bridge',None)
        else:
            assert len(crossing)==2
            matching=[len(cyc) for cyc in cycles if all(edge.issubset(cyc) for edge in crossing)]
            assert len(matching)==1,(G.edges(),S,crossing,matching)
            ell=matching[0];expected=Fraction(1,d*ell);klass=('cycle',ell)
        assert w==expected,(S,w,expected)
        facets.append((klass,w))
    b=len(bridges)
    assert len(facets)*2==2*b+sum(ell*(ell-1) for ell in lengths)
    assert 2*sum(w for _,w in facets)==1
    weights=[w for _,w in facets]
    uniform=len(set(weights))==1
    equal_cycles=(len(set(lengths))==1)
    expected_uniform=(len(cycles)==0 or (b==0 and equal_cycles))
    assert uniform==expected_uniform,(G.edges(),weights)
    return {'N':N,'bridges':b,'cycle_lengths':lengths,'facets':2*len(facets),'uniform':uniform}


def hull_facet_count(G):
    # All acyclic edge orientations yield vertices of the centred zonotope.
    E=list(G.edges());N=len(G); V=[]
    for bits in itertools.product((-1,1),repeat=len(E)):
        D=nx.DiGraph();D.add_nodes_from(G.nodes)
        D.add_edges_from((a,b) if s==1 else (b,a) for (a,b),s in zip(E,bits))
        if not nx.is_directed_acyclic_graph(D):continue
        v=np.zeros(N)
        for (a,b),s in zip(E,bits):v[a]+=s/2;v[b]-=s/2
        V.append(v)
    P=np.array(V)@null_space(np.ones((1,N)))
    H=ConvexHull(P,qhull_options='Qx')
    planes={tuple(np.round(eq/np.linalg.norm(eq[:-1]),6)) for eq in H.equations}
    result=actual_facets(G)
    assert len(planes)==result['facets'],(len(planes),result)
    return len(V),len(planes)


if __name__=='__main__':
    tests={
        'tree': [('bridge',0),('bridge',1),('bridge',2),('bridge',1)],
        'one-cycle-with-bridge':[('cycle',0,4),('bridge',1)],
        'two-triangles-bouquet':[('cycle',0,3),('cycle',0,3)],
        'two-cycles-chain':[('cycle',0,3),('cycle',1,3)],
        'unequal-cycle-bouquet':[('cycle',0,3),('cycle',0,4)],
        'equal-cycles-with-bridge':[('cycle',0,3),('cycle',1,3),('bridge',4)],
        'three-triangles-chain':[('cycle',0,3),('cycle',1,3),('cycle',4,3)],
        'two-four-cycles-chain':[('cycle',0,4),('cycle',2,4)],
    }
    for name,blocks in tests.items():
        G=make_cactus(blocks)
        print(name,actual_facets(G))
    for name in ['tree','one-cycle-with-bridge','two-triangles-bouquet','two-cycles-chain','unequal-cycle-bouquet']:
        G=make_cactus(tests[name]);print('independent_hull',name,hull_facet_count(G))
    print('CACTUS_CONE_VOLUME_PASS')
