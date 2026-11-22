#!/usr/bin/env python3
"""Independent direct-state enumerator, without binary matrices or symbolic ranks."""
from collections import Counter

def build(n):
    vertices=list(range(n)); edge_nodes={}
    k=n
    for a in range(n):
        for b in range(a+1,n):
            edge_nodes[(a,b)]=k;k+=1
    neighbors=[[] for _ in range(k)]
    for (a,b),v in edge_nodes.items():
        ends=(b,) if (a,b)==(0,1) else (a,b)
        for u in ends:
            neighbors[v].append(u);neighbors[u].append(v)
    return neighbors

def step(s,adj):
    nxt=0
    for i,nb in enumerate(adj):
        b=0
        for j in nb:
            b ^= (s>>j)&1
        nxt |= b<<i
    return nxt

def classify_one(s,adj):
    seen={};x=s;k=0
    while x not in seen:
        seen[x]=k
        x=step(x,adj)
        k+=1
    return (seen[x],k-seen[x])

def predicted_counts(n):
    N=n*(n+1)//2
    if n%2:
        p={1:2**(n-3),2:2**(2*(n-3))-2**(n-3),7:2**n-2**(n-3)}
        p[14]=2**(2*n)-sum(p.values())
        return p,{0:2**(2*n),1:2**N-2**(2*n)}
    p={1:2,2:2}
    ranks=[N,2*n,n+3,6,5,4,3,2]
    atmost={t:2**(N-r+2) for t,r in enumerate(ranks)}
    q={0:4}
    for t in range(1,8): q[t]=atmost[t]-atmost[t-1]
    return p,q

def check():
    for n in range(3,6):
        adj=build(n);N=len(adj)
        byentry=Counter();byperiod=Counter();orbits=set()
        for state in range(1<<N):
            t,p=classify_one(state,adj)
            byentry[t]+=1;byperiod[p]+=1
            if t==0:
                cyc=[];x=state
                for j in range(p):cyc.append(x);x=step(x,adj)
                orbits.add(min(cyc))
        p,q=predicted_counts(n)
        assert dict(byperiod)=={k:v*(2**(N-2*n) if n%2 else 2**(N-2)) for k,v in p.items() if v>0},(n,byperiod,p)
        assert dict(byentry)=={k:v for k,v in q.items() if v>0},(n,byentry,q)
        expected_orbits=sum(p[k]//k for k in p)
        assert len(orbits)==expected_orbits,(n,len(orbits),expected_orbits)
        print('states n=%d count=%d periods=%s first-entry=%s orbits=%d PASS'%(n,1<<N,dict(byperiod),dict(byentry),len(orbits)))
    print('ALL_STATE_CHECKS_PASS')
if __name__=='__main__':check()
