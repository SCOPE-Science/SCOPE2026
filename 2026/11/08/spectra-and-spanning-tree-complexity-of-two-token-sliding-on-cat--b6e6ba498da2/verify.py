#!/usr/bin/env python3
"""Direct literal graph and spectral checks for two-token independence reconfiguration."""
from itertools import combinations,product
from math import comb, log
import numpy as np
import networkx as nx
import sympy as sp


def direct_adjacency(a,b):
    return a[0]!=b[0] and a[1]!=b[1]

def independent(I):
    return all(not direct_adjacency(a,b) for a,b in combinations(I,2))

def ts_graph(m,n,k):
    cells=list(product(range(m),range(n)))
    states=[frozenset(I) for I in combinations(cells,k) if independent(I)]
    G=nx.Graph(); G.add_nodes_from(states)
    for i,a in enumerate(states):
        for b in states[i+1:]:
            x=a-b;y=b-a
            if len(x)==1 and len(y)==1 and direct_adjacency(next(iter(x)),next(iter(y))):G.add_edge(a,b)
    return G

def expected_spectrum(m,n):
    out=[]
    combos=[(2*np.sqrt((m-1)*(n-1)),1),
            (np.sqrt(2*(m-1)*(n-2)),n-1),
            (np.sqrt(2*(n-1)*(m-2)),m-1),
            (np.sqrt((m-2)*(n-2)),(m-1)*(n-1))]
    for a,mult in combos: out.extend([a]*mult+[-a]*mult)
    out += [0.0]*(m*n*(m+n-6)//2)
    return np.array(sorted(out))

def trees(m,n):
    assert m>=3 and n>=3
    dH=2*(m-1);dV=2*(n-1)
    a=m*n*(n-3)//2;b=m*n*(m-3)//2
    return (4*pow(dH,a)*pow(dV,b)*pow(2*n*(m-1),n-1)*pow(2*m*(n-1),m-1)*pow(3*m*n-2*m-2*n,(m-1)*(n-1)))//(m*n)

def main():
    total=0;checks=0
    for m in range(3,6):
        for n in range(m,7):
            G=ts_graph(m,n,2)
            H=m*comb(n,2);V=n*comb(m,2)
            assert G.number_of_nodes()==H+V
            assert G.number_of_edges()==m*n*(m-1)*(n-1)
            assert nx.is_connected(G) and nx.is_bipartite(G)
            expected=expected_spectrum(m,n)
            eig=np.linalg.eigvalsh(nx.to_numpy_array(G))
            assert len(eig)==len(expected)
            assert np.max(np.abs(eig-expected))<1e-7,(m,n,'eigen')
            # Literal graph-based Laplacian eigenvalue tree check, rounded integer.
            lap=np.linalg.eigvalsh(nx.laplacian_matrix(G).toarray().astype(float))
            if len(lap)<=50:
                logtree=float(np.log(lap[1:]).sum()-np.log(len(lap)))
                assert abs(logtree-log(trees(m,n)))<1e-9,(m,n,'tree log')
            total+=G.number_of_nodes();checks+=1
    exact_tree_checks=0
    for m,n in [(3,3),(3,4)]:
        G=ts_graph(m,n,2)
        mat=nx.laplacian_matrix(G).toarray()
        cof=sp.Matrix(mat[:-1,:-1]).det(method="domain-ge")
        assert int(cof)==trees(m,n)
        exact_tree_checks+=1
    frozen=0
    for m in range(3,5):
        for n in range(m,6):
            for k in range(3,max(m,n)+1):
                G=ts_graph(m,n,k)
                assert G.number_of_nodes()==m*(comb(n,k) if k<=n else 0)+n*(comb(m,k) if k<=m else 0)
                assert G.number_of_edges()==0
                frozen+=1
    print('VERIFY_OK two_token_profiles=',checks,'total_two_token_states=',total,
          'direct_rule=PASS','full_adjacency_spectrum=PASS',
          'tree_formula=PASS','exact_tree_checks=',exact_tree_checks,'connected_bipartite=PASS',
          'frozen_profiles=',frozen)
if __name__=='__main__':main()
