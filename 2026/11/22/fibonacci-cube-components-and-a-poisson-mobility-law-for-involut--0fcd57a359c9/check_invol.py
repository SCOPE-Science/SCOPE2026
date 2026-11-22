#!/usr/bin/env python3
"""Reproducibility: graph of self-inverse permutations under adjacent-position swaps."""
from collections import Counter, deque
from math import comb

def invols(n):
    p=[-1]*n
    def go():
        try: i=p.index(-1)
        except ValueError:
            yield tuple(x+1 for x in p);return
        p[i]=i
        yield from go()
        for j in range(i+1,n):
            if p[j]==-1:
                p[i]=j;p[j]=i
                yield from go()
                p[j]=-1
        p[i]=-1
    yield from go()

def signature(p):
    return tuple((i+1,p[i]) for i in range(len(p)) if p[i]>i+1 and p[i]!=i+2)

def adj(p):
    for i in range(len(p)-1):
        q=list(p);q[i],q[i+1]=q[i+1],q[i]
        if all(q[q[j]-1]==j+1 for j in range(len(p))):yield tuple(q)

def fib(n):
    a,b=0,1
    for _ in range(n):a,b=b,a+b
    return a

def pred_size(sig,n):
    removed={v-1 for e in sig for v in e}
    runs=[];k=0
    for i in range(n):
        if i in removed:
            if k:runs.append(k)
            k=0
        else:k+=1
    if k:runs.append(k)
    size=1;diam=0
    for t in runs:
        size*=fib(t+1)
        diam+=t-1
    return size,diam

def tel(n):
    t=[1,1]
    for k in range(2,n+1):t.append(t[-1]+(k-1)*t[-2])
    return t[n]

def check(n):
    words=set(invols(n));unvisited=words.copy(); comps=[];count_isolated=0;max_deg=0
    assert len(words)==tel(n)
    while unvisited:
        v=next(iter(unvisited));q=deque([v]);unvisited.remove(v);S={v}
        while q:
            u=q.popleft()
            neigh=set(adj(u));max_deg=max(max_deg,len(neigh))
            for w in neigh:
                assert w in words and signature(u)==signature(w)
                if w in unvisited:
                    unvisited.remove(w);S.add(w);q.append(w)
        sig=signature(v);size,diam=pred_size(sig,n)
        assert len(S)==size,(n,sig,len(S),size)
        # metric is Hamming distance between characteristic short-edge matching encodings
        if n<=8:
            for x in S:
                distances={x:0};rq=deque([x])
                while rq:
                    u=rq.popleft()
                    for w in adj(u):
                        if w not in distances:distances[w]=distances[u]+1;rq.append(w)
                assert len(distances)==len(S)
                for y,d in distances.items():
                    tx={(i+1,i+2) for i in range(n-1) if x[i]==i+2 and x[i+1]==i+1}
                    ty={(i+1,i+2) for i in range(n-1) if y[i]==i+2 and y[i+1]==i+1}
                    assert d==len(tx^ty)
                assert max(distances.values())<=diam
        comps.append((sig,len(S)))
        if len(S)==1:count_isolated+=1
    comp_formula=sum((-1)**j*comb(n-j,j)*tel(n-2*j) for j in range(n//2+1))
    assert len(comps)==comp_formula,(n,len(comps),comp_formula)
    assert sum(x[1] for x in comps)==tel(n)
    top=sorted([x[1] for x in comps],reverse=True)
    assert top[0]==fib(n+1)
    if n>=3: assert top[1]==fib(n-1)
    # degree expectation exact
    deg_sum=sum(len(set(adj(x))) for x in words)
    assert deg_sum==2*(n-1)*tel(n-2)
    print('n',n,'vertices',len(words),'components',len(comps),'isolated',count_isolated,'largest',top[:3],'maxdegree',max_deg,'edges',deg_sum//2)

if __name__=='__main__':
    for n in range(1,10): check(n)
    print('PASS')
