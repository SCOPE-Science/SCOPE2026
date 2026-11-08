#!/usr/bin/env python3
"""Exact local cut checks for finite-range cycle graphs; no asymptotic claim from enumeration."""
import itertools
from math import comb
checks=0
for m in (2,3,4):
    B=m*(m+1)
    for k in range(m,m+4):
        L=min(m*(k-1),22)
        # Enumerate all local configurations within a fixed linear span.
        minimum=None; minimizers=[]
        for tail in itertools.combinations(range(1,L+1),k-1):
            a=(0,)+tail
            edges=sum(a[j]-a[i]<=m for i in range(k) for j in range(i+1,k))
            boundary=2*m*k-2*edges
            if minimum is None or boundary<minimum:
                minimum=boundary;minimizers=[a]
            elif boundary==minimum:
                minimizers.append(a)
            checks+=1
        assert minimum==B,(m,k,minimum,B)
        if k==m:
            expected={tuple((0,)+t) for t in itertools.combinations(range(1,m+1),m-1)}
        else:
            expected={tuple(range(k))}
        assert set(minimizers)==expected,(m,k,minimizers[:5],expected)
        checks+=2
    # Count cliques of order m on a sufficiently large cycle by checking all m-subsets.
    n=4*m+9
    def edge(x,y):return min((x-y)%n,(y-x)%n)<=m
    clique=sum(all(edge(x,y) for x,y in itertools.combinations(S,2)) for S in itertools.combinations(range(n),m))
    assert clique==m*n,(m,clique,n*m)
    checks+=1
print('LOCAL_CHECKS_PASS',checks)
