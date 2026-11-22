#!/usr/bin/env python3
"""Independent exhaustive graph-state decomposition; no signature reduction."""
from collections import Counter,deque
from signature_certificate import closed_formula,DEFECTS

def classify_all(n,name):
    missing={frozenset(v) for v in DEFECTS[name]}
    powers=[3**i for i in range(n)]
    N=3**n
    nxt=[0]*N
    for x in range(N):
        digits=[x//p%3 for p in powers]
        excited=[i for i,v in enumerate(digits) if v==1]
        y=0
        for i,v in enumerate(digits):
            if v==1:out=2
            elif v==2:out=0
            else:out=int(any(j!=i and frozenset((i,j)) not in missing for j in excited))
            y+=powers[i]*out
        nxt[x]=y
    indeg=[0]*N
    for y in nxt: indeg[y]+=1
    q=deque(x for x in range(N) if not indeg[x]);order=[]
    while q:
        x=q.popleft();order.append(x);y=nxt[x];indeg[y]-=1
        if indeg[y]==0:q.append(y)
    depth=[0]*N; period=[0]*N;seen=set()
    for x in range(N):
        if indeg[x] and x not in seen:
            orbit=[];z=x
            while z not in seen:
                seen.add(z);orbit.append(z);z=nxt[z]
            for v in orbit:period[v]=len(orbit)
    for x in reversed(order):period[x]=period[nxt[x]];depth[x]=depth[nxt[x]]+1
    return Counter(zip(depth,period))

def main():
    total=0
    for name in ('adjacent','disjoint'):
        for n in range(5,10):
            got=classify_all(n,name)
            expected=closed_formula(name,n)
            assert dict(got)==expected,(name,n,got,expected)
            total+=3**n
            print(name,n,'states',3**n,'max first entry',max(a for a,b in got))
    print('independently classified',total,'state and graph pairs')
    print('DIRECT_ENUMERATION_OK')
if __name__=='__main__':main()
