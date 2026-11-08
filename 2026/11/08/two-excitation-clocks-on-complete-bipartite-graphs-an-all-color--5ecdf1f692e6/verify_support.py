#!/usr/bin/env python3
"""Independent exhaustive support dynamics, with direct expected cyclic supports."""
from collections import defaultdict

def expected(k):
    full=(1<<k)-1
    fullstate=full+(full<<k)
    A=sum(1<<j for j in range(1,k,2)) + (1 if k%2 else 0)
    B=sum(1<<j for j in range(2,k,2)) + 1
    both=A+(B<<k)
    swapped=B+(A<<k)
    return fullstate,{both,swapped}


def next_mask(z,k):
    lim=(1<<k)-1
    A=z&lim;B=z>>k
    def sub(M,other):
        v=0
        for col in range(k):
            if M & (1<<col):
                nxt=(col+1)%k if col else (1 if (other&2) else 0)
                v|=1<<nxt
        return v
    return sub(A,B)+(sub(B,A)<<k)

all_cases=0
for k in range(3,10):
    Q=1<<(2*k)
    step=[next_mask(z,k) for z in range(Q)]
    indeg=[0]*Q
    for y in step: indeg[y]+=1
    todo=[z for z,v in enumerate(indeg) if v==0]
    while todo:
        z=todo.pop();w=step[z];indeg[w]-=1
        if not indeg[w]:todo.append(w)
    zeros=0;other=set()
    for z in range(Q):
        if not indeg[z]:continue
        if z==0:zeros+=1
        else:other.add(z)
    full,alt=expected(k)
    assert other=={full}|alt|{1,1<<k,1+(1<<k)},(k,other,full,alt)
    assert next_mask(full,k)==full
    assert next_mask(next(iter(alt)),k) in alt
    print('k',k,'mask states',Q,'periodic supports',len(other)+1)
    all_cases+=Q
print('PASS independent support-graph comparisons',all_cases,'states')
