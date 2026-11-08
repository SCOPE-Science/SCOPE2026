#!/usr/bin/env python3
"""Independent full-state recurrence test for an odd clique with one attached leaf.
No external dependencies beyond Python's standard library.
"""
from collections import deque
from math import comb


def transitions(m):
    core=2*m+1
    n=core+1
    neigh=[set(range(core)) for _ in range(core)] + [{0,core}]
    neigh[0].add(core)
    for i in range(core):
        neigh[i].add(i)
    out=[]
    for s in range(1<<n):
        t=[]
        for i,nb in enumerate(neigh):
            k=sum((s>>j)&1 for j in nb)
            if 2*k==len(nb):
                t.append(s)
            else:
                target=int(2*k<len(nb))
                t.append(s ^ (((s>>i&1)^target)<<i))
        out.append(set(t))
    return out


def terminal_scc(out):
    n=len(out)
    index=0; indices=[-1]*n;low=[0]*n;stack=[];on=[False]*n;classes=[]
    def dfs(u):
        nonlocal index
        indices[u]=low[u]=index;index+=1;stack.append(u);on[u]=True
        for v in out[u]:
            if indices[v]==-1:
                dfs(v);low[u]=min(low[u],low[v])
            elif on[v]:low[u]=min(low[u],indices[v])
        if low[u]==indices[u]:
            c=set()
            while True:
                v=stack.pop();on[v]=False;c.add(v)
                if v==u:break
            if all(out[v] <= c for v in c): classes.append(c)
    for u in range(n):
        if indices[u]==-1:dfs(u)
    return classes


def expected(m):
    core=2*m+1; n=core+1
    classes=[set(),set()]
    for state in range(1<<n):
        h=state&1; l=(state>>core)&1
        k=(state&((1<<core)-1)).bit_count()
        if l!=h and k in (m,m+1): classes[h].add(state)
    return classes


def main():
    total=0
    for m in range(1,5):
        out=transitions(m)
        got=terminal_scc(out); ex=expected(m)
        assert len(got)==2
        assert {frozenset(x) for x in got}=={frozenset(x) for x in ex}
        assert len(ex[0])==len(ex[1])==comb(2*m+1,m)
        assert all(any(t!=s for t in out[s]) for cls in got for s in cls)
        total+=len(out)
        print(f'm={m}: {len(out)} labelled states; two recurrent classes, {len(ex[0])} states each; no absorbing states')
    print(f'PASS: {total} complete state checks; all terminal SCCs match theorem')

if __name__=='__main__':main()
