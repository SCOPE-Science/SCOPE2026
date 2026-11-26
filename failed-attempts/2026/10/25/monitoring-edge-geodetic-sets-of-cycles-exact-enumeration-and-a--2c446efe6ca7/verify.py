#!/usr/bin/env python3
"""Direct shortest-path monitoring verifier for cycle counting identities."""
from collections import deque, Counter
from math import comb

def distance(n, start, blocked_edge=None):
    neighbors = lambda v: [(v-1)%n,(v+1)%n]
    d=[n+1]*n
    d[start]=0
    queue=deque([start])
    while queue:
        v=queue.popleft()
        for w in neighbors(v):
            if blocked_edge is not None and {v,w}==set(blocked_edge):continue
            if d[w]>d[v]+1:
                d[w]=d[v]+1;queue.append(w)
    return d

def brute(n):
    before=[distance(n,u) for u in range(n)]
    monitor=[[0]*n for _ in range(n)]
    for e in range(n):
        blocked=(e,(e+1)%n)
        after=[distance(n,u,blocked) for u in range(n)]
        for u in range(n):
            for v in range(u+1,n):
                if after[u][v]>before[u][v]:
                    monitor[u][v]|=1<<e
    full=(1<<n)-1
    labels=[False]*(1<<n)
    for s in range(1<<n):
        mask=0
        for u in range(n):
            if s>>u&1:
                for v in range(u+1,n):
                    if s>>v&1:
                        mask |= monitor[u][v]
        labels[s]=mask==full
    allcount=Counter(s.bit_count() for s,ok in enumerate(labels) if ok)
    mins=Counter()
    for s,ok in enumerate(labels):
        if ok and all(not labels[s & ~(1<<u)] for u in range(n) if s>>u&1):
            mins[s.bit_count()]+=1
    h=(n-1)//2
    predicted=Counter()
    for s in range(1<<n):
        if not s: continue
        selected=[u for u in range(n) if s>>u&1]
        if all((selected[(i+1)%len(selected)]-selected[i])%n in range(1,h+1) for i in range(len(selected))):
            predicted[s.bit_count()]+=1
    if n==3: expected=Counter({3:1})
    elif n==4: expected=Counter({4:1})
    elif n%2:
        expected=Counter({3:n*(n*n-1)//24})
    else:
        expected=Counter({3:n*(n-2)*(n-4)//24,4:n*(n-2)//8})
    assert allcount==predicted,(n,allcount,predicted)
    assert mins==expected,(n,mins,expected)
    return n,dict(sorted(allcount.items())),dict(sorted(mins.items()))

if __name__=='__main__':
    for n in range(3,17):
        x=brute(n)
        print(*x)
    print('VERIFY_OK')
