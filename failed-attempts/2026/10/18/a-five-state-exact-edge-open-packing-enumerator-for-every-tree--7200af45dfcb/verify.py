#!/usr/bin/env python3
"""Brute-force cross-check of a tree edge-open-packing enumerator."""
from itertools import product
from collections import Counter
import random

def conv(p,q):
    z=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): z[i+j]+=a*b
    return trim(z)

def trim(p):
    while len(p)>1 and not p[-1]:p.pop()
    return p

def add(p,q):
    o=[0]*max(len(p),len(q))
    for i,x in enumerate(p):o[i]+=x
    for i,x in enumerate(q):o[i]+=x
    return trim(o)

def sub(p,q):
    o=[0]*max(len(p),len(q))
    for i,x in enumerate(p):o[i]+=x
    for i,x in enumerate(q):o[i]-=x
    assert min(o)>=0, (p,q,o)
    return trim(o)

def zshift(p):return [0]+p

def polynomial(n,edges):
    g=[[] for _ in range(n)]
    for u,v in edges:g[u].append(v);g[v].append(u)
    par=[-1]*n; order=[0];par[0]=0
    for v in order:
        for u in g[v]:
            if par[u]<0:par[u]=v;order.append(u)
    assert len(order)==n
    F=[None]*n
    for v in reversed(order):
        a=[1];d=[1];e_big=[1];linear_d=[0];linear_de=[0]
        for u in g[v]:
            if par[u]!=v:continue
            au,bu,cu,du,eu=F[u]
            A=add(add(au,bu),cu)
            a=conv(a,A)
            linear_d=add(conv(linear_d,au),conv(d,zshift(du)))
            linear_de=add(conv(linear_de,au),conv(d,zshift(add(du,eu))))
            e_big=conv(e_big,add(au,zshift(du)))
            d=conv(d,au)
        b=linear_de
        c=sub(sub(e_big,d),linear_d)
        e=sub(e_big,d)
        F[v]=a,b,c,d,e
    return add(add(F[0][0],F[0][1]),F[0][2])

def brute(n,edges):
    m=len(edges);C=Counter()
    for mask in range(1<<m):
        B=[i for i in range(m) if mask>>i&1]
        valid=True
        for i in range(len(B)):
            for j in range(i+1,len(B)):
                e=edges[B[i]];f=edges[B[j]]
                for h,third in enumerate(edges):
                    if h in (B[i],B[j]):continue
                    if (third[0] in e and third[1] in f) or (third[1] in e and third[0] in f):
                        valid=False;break
                if not valid:break
            if not valid:break
        if valid:C[mask.bit_count()]+=1
    return [C[i] for i in range(m+1)]

def prufer(seq,n):
    deg=[1]*n
    for v in seq:deg[v]+=1
    edges=[]
    for v in seq:
        leaf=next(i for i in range(n) if deg[i]==1)
        edges.append((leaf,v));deg[leaf]-=1;deg[v]-=1
    leaves=[i for i in range(n) if deg[i]==1]
    edges.append(tuple(leaves))
    return edges

def run():
    count=0;subsets=0
    for n in range(1,8):
        itr=[()] if n<=2 else product(range(n),repeat=n-2)
        for seq in itr:
            edges=[] if n==1 else [(0,1)] if n==2 else prufer(seq,n)
            a=polynomial(n,edges);b=brute(n,edges)
            if a!=trim(b):raise AssertionError((n,seq,edges,a,b))
            count+=1;subsets+=2**len(edges)
    rng=random.Random(1729)
    for n in range(8,51):
        for _ in range(20):
            ed=[(i,rng.randrange(i)) for i in range(1,n)]
            p=polynomial(n,ed)
            assert sum(p)>0 and len(p)<=n
    print(f'VERIFICATION_OK labeled_trees={count} edge_subsets={subsets} random_larger_trees={43*20}')

if __name__=='__main__': run()
