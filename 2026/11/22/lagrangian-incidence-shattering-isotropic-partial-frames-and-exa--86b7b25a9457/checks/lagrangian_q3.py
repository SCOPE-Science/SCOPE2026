#!/usr/bin/env python3
# Independent odd-characteristic check of the symplectic Lagrangian trace criterion.
from itertools import combinations, product
from collections import Counter
Q=3; N=4
vs=list(product(range(Q),repeat=N)); zero=(0,)*N
add=lambda a,b:tuple((x+y)%Q for x,y in zip(a,b))
scale=lambda k,a:tuple(k*x%Q for x in a)
om=lambda a,b:sum(a[i]*b[2+i]-b[i]*a[2+i] for i in range(2))%Q
spaces=set()
for x,y in combinations(vs[1:],2):
    if om(x,y):continue
    s=frozenset(add(scale(a,x),scale(b,y)) for a in range(Q) for b in range(Q))
    if len(s)==Q*Q:spaces.add(s)
spaces=sorted(spaces,key=lambda z:sorted(z))
assert len(spaces)==40
for k in (1,2):
    total=0
    for S in combinations(vs[1:],k):
        dependent=k==2 and any(scale(a,S[0])==S[1] for a in range(1,Q))
        predicted=(not dependent) and all(om(a,b)==0 for a,b in combinations(S,2))
        traces={tuple(x in L for x in S) for L in spaces}
        actual=len(traces)==2**k
        assert actual==predicted, (S,predicted,traces)
        total+=actual
    assert total==({1:80,2:960}[k]),(k,total)
    print('q=3,n=2, k=',k,'shattered=',total)
print('ALL PASS')
