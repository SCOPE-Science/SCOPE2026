#!/usr/bin/env python3
"""Exact finite corroboration for Coxeter descent-profile Fourier-rank theorem."""
from itertools import permutations
from functools import lru_cache

def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a

def transform(a):
    a=a[:]; n=len(a).bit_length()-1
    for bit in range(n):
        mask=1<<bit
        for i in range(len(a)):
            if i&mask: continue
            x,y=a[i],a[i|mask]
            a[i],a[i|mask]=x+y,x-y
    return a

def induced_even(n, mask, typ):
    adj=[set() for _ in range(n)]
    for i in range(1,n-1):
        adj[i].add(i+1);adj[i+1].add(i)
    if typ=='D': adj[0].add(2);adj[2].add(0)
    else: adj[0].add(1);adj[1].add(0)
    seen=set()
    for i in range(n):
        if not (mask>>i)&1 or i in seen:continue
        stack=[i];seen.add(i);count=0
        while stack:
            u=stack.pop();count+=1
            for v in adj[u]:
                if ((mask>>v)&1) and v not in seen:
                    seen.add(v);stack.append(v)
        if count&1:return False
    return True

def signed_descent_counts(n,typ):
    out=[0]*(1<<n)
    for perm in permutations(range(1,n+1)):
        for mask in range(1<<n):
            if typ=='D' and mask.bit_count()%2: continue
            w=[-v if mask>>j&1 else v for j,v in enumerate(perm)]
            d=int((-w[1]>w[0]) if typ=='D' else (w[0]<0))
            for i in range(1,n):
                if w[i-1]>w[i]:d|=1<<i
            out[d]+=1
    return out

def prufer_tree(code,n):
    degrees=[1]*n
    for v in code:degrees[v]+=1
    edges=[]
    for v in code:
        u=next(i for i,d in enumerate(degrees) if d==1)
        edges.append((u,v));degrees[u]-=1;degrees[v]-=1
    u,v=[i for i,d in enumerate(degrees) if d==1]
    edges.append((u,v));return edges

def count_even_subsets(n,edges):
    adj=[set() for _ in range(n)]
    for u,v in edges: adj[u].add(v);adj[v].add(u)
    total=0
    for mask in range(1<<n):
        seen=set();ok=True
        for x in range(n):
            if x in seen or not (mask>>x)&1:continue
            seen.add(x);todo=[x];k=0
            while todo:
                v=todo.pop();k+=1
                for u in adj[v]:
                    if (mask>>u)&1 and u not in seen:
                        seen.add(u);todo.append(u)
            if k%2:ok=False;break
        total+=ok
    return total

def run():
    for typ in ('B','D'):
        for n in range(4,8):
            w=transform(signed_descent_counts(n,typ))
            got={i for i,x in enumerate(w) if x!=0}
            want={i for i in range(1<<n) if induced_even(n,i,typ)}
            assert got==want and len(got)==fib(n+1),(typ,n)
    # Enumerate every labelled tree through five vertices; retain maximum-degree-three cases.
    for n in range(2,6):
        for code in __import__('itertools').product(range(n), repeat=n-2):
            e=prufer_tree(code,n)
            deg=[0]*n
            for a,b in e:deg[a]+=1;deg[b]+=1
            if max(deg)<=3:assert count_even_subsets(n,e)==fib(n+1),(n,e)
    # Sharp boundary of the degree-three hypothesis.
    assert count_even_subsets(5,[(0,i) for i in range(1,5)])==9
    print('PASS: type B/D Fourier masks, Fibonacci ranks, all small subcubic trees, degree-four boundary')
if __name__=='__main__':run()
