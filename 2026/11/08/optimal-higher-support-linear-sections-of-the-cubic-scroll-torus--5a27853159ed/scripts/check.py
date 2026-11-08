#!/usr/bin/env python3
"""Finite-field exhaustive rank-subspace check for scroll torus evaluation code."""
from itertools import combinations, product
from math import prod

def run(q):
    assert q in (5,7)
    t=q-1
    mon=[(x**a*y**b)%q for x in range(1,q) for y in range(1,q) for a,b in ((0,0),(1,0),(2,0),(0,1),(1,1))]
    cols=[mon[i:i+5] for i in range(0,len(mon),5)]
    maxima=[]; counts=[]
    for r in range(1,6):
        best=-1; nsub=0; achievers=0
        for piv in combinations(range(5),r):
            positions=[(i,j) for i in range(r) for j in range(piv[i]+1,5) if j not in piv]
            for values in product(range(q), repeat=len(positions)):
                rows=[[0]*5 for _ in range(r)]
                for i,p in enumerate(piv): rows[i][p]=1
                for (i,j),v in zip(positions,values): rows[i][j]=v
                z=0
                for c in cols:
                    if all(sum(a*b for a,b in zip(row,c))%q==0 for row in rows):z+=1
                if z>best:best=z; achievers=1
                elif z==best: achievers+=1
                nsub+=1
        maxima.append(best);counts.append((nsub,achievers))
    print('q',q,'max_common_zeros',maxima,'weights',[t*t-v for v in maxima],'subspaces',counts)
    expected=[2*t,t+1,t,1,0]
    assert maxima==expected,(maxima,expected)
    counts_expected=[t*(t-1)//2,t*t*(t-1),t,t*t,1]
    assert [v for n,v in counts]==counts_expected, (counts,counts_expected)
    print('ALL_CHECKS_PASSED')
if __name__=='__main__':
    run(5);run(7)
