#!/usr/bin/env python3
"""Exact finite checks for the stated dihedral trace formula."""
from functools import lru_cache
from math import gcd

def cyc_graph(n):
    e=set()
    for i in range(n):e.add(tuple(sorted((i,(i+1)%n))))
    return e

def myc_graph(n):
    e=set(cyc_graph(n))
    for i in range(n):
        for j in ((i-1)%n,(i+1)%n): e.add(tuple(sorted((i,n+j))))
        e.add((n+i,2*n))
    return e

def orbits(perm,N):
    unused=set(range(N));oo=[]
    while unused:
        u=min(unused); v=u; o=[]
        while v not in o:
            o.append(v);v=perm[v]
        assert v==u
        unused.difference_update(o);oo.append(o)
    return oo

def poly_at_minus_one(adj):
    @lru_cache(None)
    def rec(mask):
        if not mask:return 1
        v=max((i for i in range(len(adj)) if mask>>i&1),key=lambda i:(adj[i]&mask).bit_count())
        return rec(mask&~(1<<v))-rec(mask&~(1<<v)&~adj[v])
    return rec((1<<len(adj))-1)

def orbit_lefschetz(N,edges,perm):
    oo=orbits(perm,N); mp={v:j for j,o in enumerate(oo) for v in o}; forbidden=set()
    for a,b in edges:
        if mp[a]==mp[b]:forbidden.add(mp[a])
    allowed=[i for i in range(len(oo)) if i not in forbidden]; ix={i:j for j,i in enumerate(allowed)}
    adj=[0]*len(allowed)
    for a,b in edges:
        u,v=mp[a],mp[b]
        if u in ix and v in ix and u!=v:
            i,j=ix[u],ix[v];adj[i]|=1<<j;adj[j]|=1<<i
    return -poly_at_minus_one(adj)

def fixed_face_lefschetz(N,edges,perm):
    adj=[0]*N
    for a,b in edges:adj[a]|=1<<b;adj[b]|=1<<a
    total=0
    def visit(mask,available):
        nonlocal total
        if not available:
            t=mask; moved=0
            while t:
                bit=t&-t;v=bit.bit_length()-1
                moved|=1<<perm[v];t-=bit
            if moved==mask:
                cycles=len(orbits_of_selected(mask,perm))
                total-=(-1)**cycles
            return
        bit=available&-available;v=bit.bit_length()-1
        visit(mask,available&~bit)
        visit(mask|bit,(available&~bit)&~adj[v])
    visit(0,(1<<N)-1)
    return total

def orbits_of_selected(mask,perm):
    unseen={i for i in range(len(perm)) if mask>>i&1};o=[]
    while unseen:
        a=min(unseen);v=a;one=[]
        while v not in one:
            one.append(v);v=perm[v]
        assert v==a
        unseen.difference_update(one);o.append(one)
    return o

def p(n):
    a,b=1,0
    for _ in range(n):a,b=b,b-a
    return a

def cycle_minus_one(n):
    vals=(2,1,-1,-2,-1,1)
    return vals[n%6]

def expected_mu(n,shift,reflect):
    if not reflect:return cycle_minus_one(gcd(n,shift))
    if n%2:return p((n-1)//2)
    m=n//2
    return p(m+1) if shift%2==0 else p(m-2)

if __name__=='__main__':
    num=0; num_direct=0
    for n in range(3,15):
        edges=myc_graph(n)
        for reflect in (False,True):
            shifts=range(n) if n<=12 else ([0,1,2,3,4,n//2] if not reflect else [0,1])
            for shift in shifts:
                perm=[((shift-i)%n if reflect else (i+shift)%n) for i in range(n)]
                perm += [n+((shift-i)%n if reflect else (i+shift)%n) for i in range(n)]+[2*n]
                obs=orbit_lefschetz(2*n+1,edges,perm)
                exp=expected_mu(n,shift,reflect)
                assert obs==exp,(n,shift,reflect,obs,exp)
                cperm=perm[:n]
                cobs=orbit_lefschetz(n,cyc_graph(n),cperm)
                assert obs==-cobs,(n,shift,reflect,obs,cobs)
                num+=1
                if n<=8:
                    direct=fixed_face_lefschetz(2*n+1,edges,perm)
                    assert direct==obs,(n,shift,reflect,direct,obs)
                    num_direct+=1
    # at n=3..75, rational full quotient invariant count via expected exact characters
    for n in range(3,76):
        d=n//3+(1 if n%3==2 else 0)
        dim=1 if n%3 else 2
        trace_id=(-1)**d*expected_mu(n,0,False)
        assert trace_id==dim,(n,trace_id,dim)
        total=sum((-1)**d*expected_mu(n,k,False) for k in range(n))
        total+=sum((-1)**d*expected_mu(n,k,True) for k in range(n))
        rank=total//(2*n)
        assert total%(2*n)==0
        assert rank==int(n%12 in (1,11)),(n,rank)
    print('PASS: orbit-graph Lefschetz tests =',num)
    print('PASS: independent fixed-face signed-chain tests =',num_direct)
    print('PASS: full dihedral averaged invariant ranks for n=3..75 = 73')
    print('PASS: all predicted integer-valued traces agree in tested ranges')
