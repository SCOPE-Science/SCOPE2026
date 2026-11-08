#!/usr/bin/env python3
"""Exact GF(2) power, fixed-space, and sample-orbit checks on two-defect trees.
Only the Python standard library is required.
"""
from itertools import product
import random

def tree(code,n):
    deg=[1]*n
    for v in code:deg[v]+=1
    ed=[]
    for v in code:
        leaf=next(k for k in range(n) if deg[k]==1)
        ed.append((leaf,v));deg[leaf]-=1;deg[v]-=1
    a,b=[i for i in range(n) if deg[i]==1]
    ed.append((a,b))
    return ed

def distance(edges,n,a,b):
    adj=[[] for _ in range(n)]
    for x,y in edges:adj[x].append(y);adj[y].append(x)
    q=[a];dist={a:0}
    for v in q:
        for w in adj[v]:
            if w not in dist:dist[w]=dist[v]+1;q.append(w)
    return dist[b]

def adjacency(edges,n):
    out=[0]*n
    for a,b in edges:out[a]^=1<<b;out[b]^=1<<a
    return out

def apply(A,cols):
    out=[]
    for z in cols:
        v=0
        while z:
            p=z&-z;v^=A[p.bit_length()-1];z^=p
        out.append(v)
    return out

def rk(cols):
    B={}
    for z in cols:
        while z:
            i=z.bit_length()-1
            if i in B:z^=B[i]
            else:B[i]=z;break
    return len(B)

def rem(a,b):
    while a and a.bit_length()>=b.bit_length():a^=b<<(a.bit_length()-b.bit_length())
    return a

def gcd(a,b):
    while b:a,b=b,rem(a,b)
    return a

def gf2fixdim(m,t):
    q=(1<<(m+1))-1
    sq=0
    for k in range(m+1):
        if q>>k&1:sq|=1<<(2*k)
    return gcd(sq,(1<<t)|1).bit_length()-1

rng=random.Random(713911)
checks=0;fixed_checks=0;sample_orbits=0;by_n={}
for n in (4,6,8,10,12,14,18,22):
    checked=0
    # Include small hand-constructed candidates before filtering by the degree condition.
    for trial in range(15000):
        if trial==0:
            code=(0,)*(max(0,n//2-1))+(1,)*(max(0,n//2-1))
            if len(code)!=n-2:continue
        else:
            code=tuple(rng.randrange(n) for _ in range(n-2))
        deg=[1]*n
        for x in code:deg[x]+=1
        ev=[i for i in range(n) if deg[i]%2==0]
        if len(ev)!=2:continue
        ed=tree(code,n);d=distance(ed,n,*ev);m=d+1
        A=adjacency(ed,n)
        ident=[1<<k for k in range(n)]
        B=ident[:]
        for _ in range(n):B=apply(A,B)
        assert rk(B)==2*m,(n,d,'periodic dimension')
        C=ident[:]
        for t in range(1,2*(m+1)+1):
            fixed_checks+=1
            C=apply(A,C)
            fixed=n-rk([C[i]^ident[i] for i in range(n)])
            assert fixed==gf2fixdim(m,t),(n,d,t,fixed,gf2fixdim(m,t))
        checked+=1;checks+=1
        if n<=10 and checked<=4:
            L=2*(m+1)
            fix=[0]*(L+1)
            for state in range(1<<n):
                z=state
                for t in range(1,L+1):
                    zz=0
                    for i,row in enumerate(A):
                        if (row&z).bit_count()%2:zz|=1<<i
                    z=zz
                    if z==state:fix[t]+=1
            assert fix[L]==(1<<(2*m)),(n,d,'periodic population')
            for t in range(1,L+1):
                assert fix[t]==(1<<gf2fixdim(m,t)),(n,d,t,fix[t])
            sample_orbits+=(1<<n)
        if checked>=12:break
    assert checked>=3,(n,checked)
    by_n[n]=checked
print('DYNAMICS_CHECK_OK', 'trees=',checks,'GF2_fixed_space_tests=',fixed_checks, 'direct_state_inputs=',sample_orbits,'by_n=',by_n)
