"""Exact small-support census and spanning tree test for two cubic graphs."""
from itertools import combinations
from collections import Counter
import networkx as nx

def canon_forest(edges):
    H=nx.Graph();H.add_edges_from(edges)
    return tuple(sorted((tuple(sorted(dict(H.subgraph(c).degree()).values())) for c in nx.connected_components(H))))

def census(G,k):
    E=list(G.edges())
    h=Counter()
    for selected in combinations(E,k):
        H=nx.Graph(); H.add_edges_from(selected)
        h[canon_forest(selected)]+=1
    return h

def bareiss_determinant(A):
    a=[list(map(int,row)) for row in A]
    n=len(a); sign=1; prev=1
    for k in range(n-1):
        if a[k][k]==0:
            pivot=next((i for i in range(k+1,n) if a[i][k]),None)
            if pivot is None:return 0
            a[k],a[pivot]=a[pivot],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=a[i][j]*pivot-a[i][k]*a[k][j]
                assert num%prev==0
                a[i][j]=num//prev
            a[i][k]=0
        prev=pivot
    return sign*a[n-1][n-1]

def tau(G):
    L=nx.laplacian_matrix(G).toarray()
    return bareiss_determinant(L[:-1,:-1])

def girth(G):
    # Independent all-source BFS shortest-cycle test, not a cycle-basis proxy.
    best = G.number_of_nodes() + 1
    for root in G.nodes:
        dist = {root: 0}
        parent = {root: None}
        queue = [root]
        for u in queue:
            for v in G[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    queue.append(v)
                elif parent[u] != v:
                    best = min(best, dist[u] + dist[v] + 1)
    return best

def check():
    A=nx.dodecahedral_graph(); B=nx.desargues_graph()
    assert A.number_of_nodes()==B.number_of_nodes()==20
    assert A.number_of_edges()==B.number_of_edges()==30
    assert all(d==3 for G in (A,B) for v,d in G.degree())
    assert girth(A)==5 and girth(B)==6
    print('degrees and girths',[(G.number_of_nodes(),G.number_of_edges(),girth(G)) for G in (A,B)])
    for k in range(1,5):
        ca,cb=census(A,k),census(B,k)
        assert ca==cb, (k,ca-cb,cb-ca)
        print('k',k,'histogram',sorted(ca.items(), key=lambda x:repr(x[0])))
    a,b=tau(A),tau(B)
    print('tau',a,b,'ratio',b/a)
    assert (a,b)==(5184000,6144000)
    print('HIGH_GIRTH_WIDTH_MOMENT_EXACT_PASS k=1..4')
if __name__=='__main__':check()
