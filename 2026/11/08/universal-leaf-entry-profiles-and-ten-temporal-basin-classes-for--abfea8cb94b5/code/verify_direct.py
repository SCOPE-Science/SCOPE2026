#!/usr/bin/env python3
"""Independent labelled-vertex evolution checks for 3-state excitable networks."""
from itertools import product
from collections import Counter,defaultdict

def graph(r,s):
    N=r+s+1
    nbr=[[] for _ in range(N)]
    for u in range(r+1):
        for v in range(u+1,r+1):
            nbr[u].append(v);nbr[v].append(u)
    for v in range(r+1,N):
        nbr[0].append(v);nbr[v].append(0)
    return nbr

def step(state,nbr):
    nxt=list(state)
    for v,c in enumerate(state):
        if c==1: nxt[v]=2
        elif c==2:nxt[v]=0
        else:nxt[v]=1 if any(state[w]==1 for w in nbr[v]) else 0
    return tuple(nxt)

def formula(r,s,t,p):
    R=2**r;S=2**s;P=3**s;Q=3**r-2**(r+1)+1
    if p==3:return Q*(3,S-1,P-1,P-1,P-S)[t]
    return (1,2*R*S-1,(2*R-1)*P,
            (2*R-1)*P-R*S+R-1,
            (2*R-1)*P-R*S-R+1)[t]

def check(r,s):
    nbr=graph(r,s);N=len(nbr)
    census=Counter();basins=defaultdict(Counter)
    for original in product(range(3),repeat=N):
        path=[original]
        for _ in range(8):path.append(step(path[-1],nbr))
        assert path[7]==path[4]
        times=[]
        for t in range(5):
            if path[t]==path[t+1]:times.append((t,1))
            if path[t]==path[t+3]:times.append((t,3))
        assert times
        t,p=min(times)
        assert (t,p) in {(i,j) for i in range(5) for j in (1,3)}
        census[t,p]+=1
        if p==3:
            recurring=path[t:t+3]
            cycle=min(tuple(recurring[i:]+recurring[:i]) for i in range(3))
            basins[cycle][t]+=1
    assert sum(census.values())==3**N
    for t in range(5):
        for p in (1,3):
            assert census[t,p]==formula(r,s,t,p), (r,s,t,p,census[t,p],formula(r,s,t,p))
    Q=3**r-2**(r+1)+1
    assert len(basins)==Q,(r,s,len(basins),Q)
    expected=(3,2**s-1,3**s-1,3**s-1,3**s-2**s)
    for h in basins.values():
        assert tuple(h[t] for t in range(5))==expected,(r,s,h)
    return 3**N

def main():
    cases=0;states=0
    for r in range(2,6):
        for s in range(1,6):
            if 3**(r+s+1)>180000: continue
            states+=check(r,s);cases+=1
    assert states==392040 and cases==20,(states,cases)
    print(f'PASS: direct graph evolution of {states} labelled states across {cases} graph sizes')
    print('PASS: F^7=F^4, complete ten-class census, primitive cycles')
    print('PASS: every individual three-cycle has universal five-layer basin profile')

if __name__=='__main__':main()
