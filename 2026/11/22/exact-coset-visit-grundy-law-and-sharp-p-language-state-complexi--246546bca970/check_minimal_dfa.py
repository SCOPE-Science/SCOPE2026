#!/usr/bin/env python3
"""Construct and minimize the P-position DFA for finite quotient groups."""
from itertools import permutations
from collections import deque

def cyclic(n):
    return list(range(n)),lambda x,y:(x+y)%n,lambda x:(-x)%n,0

def klein():
    return list(range(4)),lambda x,y:x^y,lambda x:x,0

def symmetric3():
    g=list(permutations(range(3)))
    idx={a:i for i,a in enumerate(g)}
    mul=lambda x,y: idx[tuple(g[x][g[y][i]] for i in range(3))]
    inv=lambda x: idx[tuple(g[x].index(i) for i in range(3))]
    return list(range(6)),mul,inv,idx[tuple(range(3))]

def check(label, Q, mul,inv,e):
    # Explicitly realize all distinct normalized visit sets and freshness bits.
    q=len(Q); ix={v:i for i,v in enumerate(Q)}
    state=lambda T,f:(frozenset(T),bool(f))
    start=state({e},True)
    todo=deque([start]); reached={start}
    trans={}
    while todo:
        T,f=todo.popleft()
        for y in Q:
            U={mul(inv(y),x) for x in T}|{e}
            nxt=state(U,y not in T)
            trans[(T,f),y]=nxt
            if nxt not in reached:
                reached.add(nxt);todo.append(nxt)
    assert len(reached)==2**q, (label,q,len(reached))
    # Independent Myhill-Nerode partition refinement (Moore's algorithm).
    part={s:int(s[1]) for s in reached}
    rounds=0
    while True:
        descriptors={s:(part[s],tuple(part[trans[s,y]] for y in Q)) for s in reached}
        unique={desc:i for i,desc in enumerate(sorted(set(descriptors.values())))}
        nxt={s:unique[descriptors[s]] for s in reached}
        rounds+=1
        if len(set(nxt.values()))==len(set(part.values())):
            assert all((part[a]==part[b])==(nxt[a]==nxt[b]) for a in reached for b in reached)
            break
        part=nxt
    assert len(set(nxt.values()))==2**q,(label,len(set(nxt.values())))
    # The one-letter separator works for all differing normalized T, if freshness same.
    for a in reached:
        for b in reached:
            if a==b:continue
            if a[1]!=b[1]:continue
            y=next(iter(a[0]^b[0]))
            assert trans[a,y][1]!=trans[b,y][1]
    print(label,'quotient_order',q,'reachable',len(reached),'minimal',len(set(nxt.values())),'rounds',rounds)

if __name__=='__main__':
    for r in range(1,7):check('Z'+str(r),*cyclic(r))
    check('V4',*klein())
    check('S3',*symmetric3())
    print('PASS minimal DFA spectrum')
