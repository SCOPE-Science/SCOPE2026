#!/usr/bin/env python3
"""Independent edge-distance census for complete graph prisms."""
from itertools import combinations
from math import comb

def census(n):
    vertices=[(layer,c) for layer in range(2) for c in range(n)]
    edges=[(i,j) for i in range(2*n) for j in range(i+1,2*n)
           if vertices[i][0]==vertices[j][0] or vertices[i][1]==vertices[j][1]]
    edge_dists=[]
    for e in edges:
        v,w=e
        edge_dists.append([min((z[0]!=vertices[v][0])+(z[1]!=vertices[v][1]),
                                   (z[0]!=vertices[w][0])+(z[1]!=vertices[w][1]))
                           for z in vertices])
    size=n if n<=6 else n-1
    observed=[]
    for S in combinations(range(2*n),size):
        seen=set()
        for row in edge_dists:
            signature=tuple(row[i] for i in S)
            if signature in seen:break
            seen.add(signature)
        else:
            observed.append(S)
    if n<=6:
        assert observed, ('no n-element basis',n)
        if n>=2:
            assert all(not self_resolves(edge_dists,S) for S in combinations(range(2*n),n-1))
        print(f'n={n} dimension={n} number_of_n_bases={len(observed)}')
    else:
        expected=n*sum(comb(n-1,k) for k in range(3,n-3))
        assert len(observed)==expected,(n,len(observed),expected)
        for S in observed:
            cols=[vertices[i][1] for i in S]
            a=sum(vertices[i][0]==0 for i in S)
            assert len(set(cols))==n-1 and 3<=a<=n-4
        print(f'n={n} dimension={n-1} minimum_bases={len(observed)} classified=yes')
    return len(observed)

def self_resolves(edge_dists,S):
    sigs=[tuple(d[i] for i in S) for d in edge_dists]
    return len(sigs)==len(set(sigs))

if __name__=='__main__':
    for n in range(2,10):census(n)
    print('PASS direct exhaustive edge-distance census')
