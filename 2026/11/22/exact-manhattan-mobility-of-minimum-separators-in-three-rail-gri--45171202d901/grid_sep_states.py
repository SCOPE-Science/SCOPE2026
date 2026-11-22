#!/usr/bin/env python3
"""Independent coordinate-system verification of three-rail minimum-separator geometry."""
from collections import deque

def report(n):
    states=[(i,j,k) for j in range(1,n-1) for i in (j-1,j,j+1) for k in (j-1,j,j+1)]
    lookup={state:idx for idx,state in enumerate(states)}
    assert len(lookup)==len(states)==9*(n-2)
    adj=[[] for _ in states]
    for idx,old in enumerate(states):
        for a in range(3):
            for step in (-1,1):
                nxt=list(old);nxt[a]+=step;key=tuple(nxt)
                if key in lookup:adj[idx].append(lookup[key])
    E=sum(map(len,adj))//2
    assert E==16*n-36,(n,E)
    # Independent graph metric check on all targets, all sources (n up to 24).
    ee=[]
    for src,u in enumerate(states):
        d={src:0};queue=deque([src])
        while queue:
            x=queue.popleft()
            for y in adj[x]:
                if y not in d:d[y]=d[x]+1;queue.append(y)
        assert len(d)==len(states)
        assert all(d[t]==sum(abs(x-y) for x,y in zip(u,v)) for t,v in enumerate(states))
        e=max(d.values()); ee.append(e)
        explicit=2+max(sum(abs(z-1) for z in u),sum(abs(z-(n-2)) for z in u))
        assert e==explicit
    assert min(ee)==2+(3*(n-3)+1)//2
    assert max(ee)==3*n-5
    return len(states),E,min(ee),max(ee)

if __name__=='__main__':
    for n in range(3,25):
        stats=report(n)
        if n<=10 or n in (12,16,20,24): print('n',n,'states edges radius diameter',*stats)
    print('COORDINATE_GRAPH_VERIFIED_3_TO_24')
