"""Independent labelled-forest and Cayley coefficient checks for subdivided cliques."""
from collections import Counter
from itertools import combinations
from math import comb

def is_forest(n, selected):
    par=list(range(n))
    def root(v):
        while par[v]!=v:
            v=par[v]
        return v
    for i,j in selected:
        a,b=root(i),root(j)
        if a==b:return False
        par[a]=b
    return True

def enumerate_coefficients(n):
    edges=list(combinations(range(n),2))
    forests=Counter()
    for mask in range(1<<len(edges)):
        chosen=[edges[k] for k in range(len(edges)) if (mask>>k)&1]
        if is_forest(n,chosen):
            forests[len(chosen)]+=1
    return forests

def binomial_rows(n):
    out=Counter(); E=comb(n,2)
    for r in range(n+1):
        for edge_count,n_forests in enumerate_coefficients(r).items():
            # A contains n-r originals, extra selected subdivision edges incident to A.
            for extras in range(E-comb(r,2)+1):
                k=n-r+(comb(r,2)-edge_count)+extras
                out[k]+=comb(n,r)*n_forests*comb(E-comb(r,2),extras)
    return out

def cayley_minimals(n):
    poly=Counter()
    for r in range(2,n+1):
        poly[n-2+comb(r-2,2)]+=comb(n,r)*r**(r-2)
    return poly

known={3:{1:6,2:15,3:20,4:15,5:6,6:1},4:{2:18,3:104,4:206,5:252,6:210,7:120,8:45,9:10,10:1},5:{3:40,4:425,5:1746,6:4120,7:6060,8:6345,9:4995,10:3003,11:1365,12:455,13:105,14:15,15:1}}
min_known={3:{1:6},4:{2:18,3:16},5:{3:40,4:80,6:125}}
for n in range(3,6):
    assert dict(binomial_rows(n))==known[n]
    assert dict(cayley_minimals(n))==min_known[n]
    print('n=',n,'all=',sum(binomial_rows(n).values()),'minimal=',sum(cayley_minimals(n).values()))
print('POLYNOMIAL_OK')
