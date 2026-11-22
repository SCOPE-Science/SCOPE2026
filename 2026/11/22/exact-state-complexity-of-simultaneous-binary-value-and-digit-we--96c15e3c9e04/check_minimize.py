#!/usr/bin/env python3
"""Independently minimize complete binary value/digit-count residue automata.
Usage: python3 check_minimize.py
"""
from collections import deque, Counter

def minimal(m,k,a,b):
    start=(0,0); seen={start}; q=deque([start]); order=[]
    while q:
        st=q.popleft(); order.append(st)
        for bit in (0,1):
            nxt=((2*st[0]+bit)%m,(st[1]+bit)%k)
            if nxt not in seen: seen.add(nxt); q.append(nxt)
    assert len(order)==m*k,(m,k,len(order))
    ix={st:i for i,st in enumerate(order)}
    d=[(ix[((2*r)%m,p)],ix[((2*r+1)%m,(p+1)%k)]) for r,p in order]
    part=[int(st==(a,b)) for st in order]
    while True:
        sig=[(part[i],part[d[i][0]],part[d[i][1]]) for i in range(len(order))]
        names={sig:i for i,sig in enumerate(sorted(set(sig)))}
        new=[names[s] for s in sig]
        if len(set(new))==len(set(part)):
            return len(set(new)),len(order)
        part=new

def oddpart(m):
    t=0
    while not m%2: m//=2;t+=1
    return m,t

cases=0;targets=0
for m in range(1,31):
    u,t=oddpart(m)
    for k in range(1,7):
        choice=[(0,0),(m-1,k-1),(m//2,k//2)]
        if m<=13 and k<=4: choice=[(a,b) for a in range(m) for b in range(k)]
        for a,b in sorted(set(choice)):
            got,reach=minimal(m,k,a,b)
            want=u*k+t
            assert got==want,(m,k,a,b,got,want)
            assert reach==m*k
            targets+=1
        cases+=1
print('PASS: direct reachable-state BFS and iterative Moore partition refinement')
print(f'{cases} parameter pairs, {targets} target residue pairs; m=1..30, k=1..6')
for m,k in ((3,2),(4,2),(6,2),(8,3),(12,2),(24,3),(30,4)):
    u,t=oddpart(m);print(f'm={m} k={k}: {minimal(m,k,0,0)[0]} minimal states (u={u}, t={t})')
