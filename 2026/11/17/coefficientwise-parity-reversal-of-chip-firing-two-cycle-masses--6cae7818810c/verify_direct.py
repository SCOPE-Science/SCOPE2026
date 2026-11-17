#!/usr/bin/env python3
"""Independent graph adjacency and exact mass counting, with direct dynamics checks."""
from collections import defaultdict
from itertools import product
from math import comb

def adjacency(n,twisted):
    adj=[set() for _ in range(2*n)]
    def edge(u,v):adj[u].add(v);adj[v].add(u)
    for i in range(n):
        edge(2*i,2*i+1)
        for r in range(2):
            edge(2*i+r,2*((i+1)%n)+(r^(int(twisted and i==n-1))))
    assert all(len(neigh)==3 for neigh in adj)
    return adj

def step(x,adj):
    fired=[int(x[v]>=3) for v in range(len(adj))]
    return tuple(x[v]-3*fired[v]+sum(fired[w] for w in adj[v]) for v in range(len(adj)))

def from_cut(n,twisted,do_dynamics=False):
    adj=adjacency(n,twisted)
    out=defaultdict(int)
    seen=0
    for mask in range(1<<(2*n)):
        choices=[]
        for v in range(2*n):
            f=(mask>>v)&1
            cut=sum(f!=((mask>>u)&1) for u in adj[v])
            if not cut:break
            lo=3 if f else 3-cut
            choices.append(range(lo,lo+cut))
        if len(choices)!=2*n:continue
        p={0:1}
        for rg in choices:
            nxt=defaultdict(int)
            for mass,count in p.items():
                for value in rg:nxt[mass+value]+=count
            p=nxt
        for k,c in p.items():out[k]+=c
        if do_dynamics:
            for x in product(*choices):
                y=step(x,adj)
                assert y!=x and step(y,adj)==x
                assert all(int(x[v]>=3)==((mask>>v)&1) for v in range(2*n))
                assert sum(x)==sum(y)
                seen+=1
    assert all(c%2==0 for c in out.values())
    return {k:c//2 for k,c in out.items()},seen

def discrepancy(n):
    ans=defaultdict(int)
    for j in range(n//2+1):
        c=n*comb(n-j,j)//(n-j)
        assert c*(n-j)==n*comb(n-j,j)
        for e in (3*n+2*j,5*n+2*j):
            for h in range(2*n-4*j+1):
                ans[e+h]+=(-1)**n*c*comb(2*n-4*j,h)
    if n%2==0:ans[5*n]+=2
    return dict(ans)

for n in range(3,8):
    p,_=from_cut(n,False,do_dynamics=(n<=4))
    m,_=from_cut(n,True,do_dynamics=(n<=4))
    diff=discrepancy(n)
    assert {k:p.get(k,0)-m.get(k,0) for k in range(3*n,7*n+1)}=={k:diff.get(k,0) for k in range(3*n,7*n+1)}
    assert all(p.get(k,0)-m.get(k,0)==0 for k in set(p)|set(m) if not 3*n<=k<=7*n)
    assert all(((-1)**n)*(p.get(k,0)-m.get(k,0))>0 for k in range(3*n,7*n+1))
    assert all(p.get(k,0)==p.get(10*n-k,0) for k in p)
    assert all(m.get(k,0)==m.get(10*n-k,0) for k in m)
    print(f'n={n}: P={sum(p.values())}, M={sum(m.values())}, diff={sum(diff.values())}, degree_support=[{3*n},{7*n}]: PASS')
print('independent direct enumeration, all small cases and dynamics: PASS')
