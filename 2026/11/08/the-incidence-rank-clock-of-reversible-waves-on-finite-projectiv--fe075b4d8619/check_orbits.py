#!/usr/bin/env python3
"""Direct local vertex updates on projective point-line incidence networks."""
from itertools import product

def graph(p):
    # Coordinates over a prime field, independently constructed.
    reps={}
    for vec in product(range(p),repeat=3):
        if vec==(0,0,0):continue
        h=next(z for z in vec if z!=0)
        w=tuple(z*pow(h,-1,p)%p for z in vec)
        reps[w]=1
    coordinates=sorted(reps)
    v=len(coordinates)
    adj=[[] for _ in range(2*v)]
    for i,x in enumerate(coordinates):
        for j,y in enumerate(coordinates):
            if sum(a*b for a,b in zip(x,y))%p==0:
                adj[i].append(v+j)
                adj[v+j].append(i)
    assert v==p*p+p+1
    return adj

def step(state,adj):
    n=len(adj);x,y=state
    out=0
    for i,ngb in enumerate(adj):
        h=(y>>i)&1
        for j in ngb:h^=(x>>j)&1
        out|=h<<i
    return out,x

def least_period(state,adj,cap):
    s=state
    for i in range(1,cap+1):
        s=step(s,adj)
        if s==state:return i
    return None

def main():
    seed=0x987654321
    for p,period,allowed in ((2,12,{1,2,3,4,6,12}),(3,6,{1,2,3,6}),(5,6,{1,2,3,6})):
        adj=graph(p)
        n=len(adj);mask=(1<<n)-1
        observed=set()
        samples=0
        for i in range(18000):
            seed=(1103515245*seed+12345)&((1<<64)-1)
            x=seed&mask
            seed=(1103515245*seed+12345)&((1<<64)-1)
            y=seed&mask
            m=least_period((x,y),adj,period)
            assert m in allowed,(p,m)
            observed.add(m);samples+=1
        # Every individual coordinate basis pair is checked too.
        for j in range(2*n):
            state=((1<<j),0) if j<n else (0,(1<<(j-n)))
            m=least_period(state,adj,period)
            assert m in allowed
            observed.add(m);samples+=1
        assert period in observed
        print(f'plane_order={p} graph_vertices={n} direct_states_checked={samples} observed_periods={sorted(observed)} maximal_period={period}')
    print('PASS: local updates exhibit no forbidden periods and attain the claimed maximum.')
if __name__=='__main__':main()
