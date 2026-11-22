"""Exact unlabelled-tree census for leaf/vertex mean distance reversal.
Requires Python >=3.9 and NetworkX >=3.0; run python verify.py.
"""
from fractions import Fraction
from collections import Counter
import networkx as nx

EXPECTED = [1, 1, 2, 3, 6, 11, 23, 47, 106, 235, 551, 1301, 3159, 7741]
EXPECTED_MIN = {3: Fraction(2, 3),4:Fraction(1,2),5:Fraction(2,5),6:Fraction(1,3),7:Fraction(2,7),8:Fraction(1,4),9:Fraction(2,9),10:Fraction(1,5),11:Fraction(2,11),12:Fraction(1,6),13:Fraction(5,39),14:Fraction(1,52),15:Fraction(-1,10)}

def indices(tree):
    n = tree.number_of_nodes()
    leaves = {v for v in tree if tree.degree[v] == 1}
    l = len(leaves)
    W = WL = 0
    for u,v in list(tree.edges()):
        # Edge-cut identity: every pair separated by e contributes 1.
        tree.remove_edge(u,v)
        side = nx.node_connected_component(tree,u)
        tree.add_edge(u,v)
        a = len(side)
        ell = len(leaves.intersection(side))
        W += a*(n-a)
        WL += ell*(l-ell)
    delta = Fraction(2*WL,l*(l-1)) - Fraction(2*W,n*(n-1))
    return delta,W,WL,l

def broom(b,p):
    # One hub, b short leaf branches and one arm of length p.
    graph=nx.Graph()
    graph.add_nodes_from(range(b+p+1))
    graph.add_edges_from((0,j) for j in range(1,b+1))
    graph.add_edge(0,b+1)
    graph.add_edges_from((j,j+1) for j in range(b+1,b+p))
    return graph

records=[]
for n in range(3,16):
    total=0
    negative=[]
    minimum=None
    for T in nx.nonisomorphic_trees(n):
        total+=1
        vals=indices(T)
        if minimum is None or vals[0]<minimum: minimum=vals[0]
        if vals[0]<0: negative.append((T, vals))
    assert total==EXPECTED[n-2], (n,total)
    assert minimum==EXPECTED_MIN[n],(n,minimum)
    if n<15: assert not negative
    else:
        assert len(negative)==3
        brooms={(7,7): (Fraction(-1,10),378,98,8), (8,6): (Fraction(-4,45),336,112,9), (9,5): (Fraction(-2,105),296,126,10)}
        for (b,p),vals in brooms.items():
            graph=broom(b,p)
            assert indices(graph)==vals
            assert sum(nx.is_isomorphic(graph,T) for T,_ in negative)==1
            # A second, direct shortest-path computation verifies all witness sums.
            distance=dict(nx.all_pairs_shortest_path_length(graph))
            V=list(graph)
            L=[v for v in V if graph.degree[v]==1]
            W=sum(distance[u][v] for i,u in enumerate(V) for v in V[i+1:])
            WL=sum(distance[u][v] for i,u in enumerate(L) for v in L[i+1:])
            assert (W,WL)==vals[1:3]
    records.append((n,total,len(negative),str(minimum)))
for record in records:print(*record)
print('THREE_BROOM_ISOMORPHISM_CLASSES_AND_DIRECT_PAIRWISE_DISTANCE_CHECK_PASS')
print('EXHAUSTIVE_TREE_CENSUS_PASS')
