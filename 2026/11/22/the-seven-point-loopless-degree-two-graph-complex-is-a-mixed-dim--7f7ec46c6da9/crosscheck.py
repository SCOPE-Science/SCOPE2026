#!/usr/bin/env python3
"""Independent full 2^21-subset census, using Gray-code degree updates."""
from collections import Counter
n=7
edges=[(i,j) for i in range(n) for j in range(i+1,n)]
assert len(edges)==21
counts=Counter()
deg=[0]*n;bad=0;mask=0
for step in range(1<<len(edges)):
    if step:
        bit=step&-step
        i=bit.bit_length()-1
        a,b=edges[i]
        entering=not (mask>>i)&1
        update=1 if entering else -1
        for v in (a,b):
            before=deg[v]
            if before>2:bad-=1
            deg[v]+=update
            if deg[v]>2:bad+=1
        mask^=bit
    if bad==0:counts[mask.bit_count()-1]+=1
assert [counts[j] for j in range(-1,7)]==[1,21,210,1190,3780,6132,3997,465]
chi=sum((-1)**d*counts[d] for d in range(7))
assert chi==-179
print('LOOPLESS_7_INDEPENDENT_CENSUS_OK',dict(counts),'Euler',chi)
