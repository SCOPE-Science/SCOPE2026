#!/usr/bin/env python3
"""Self-contained finite enumeration and independent one-point profile checks."""
from collections import Counter, defaultdict, deque
from itertools import product
from math import comb

WITNESSES = {
 'A': [(0,1),(0,2),(0,3),(4,1),(5,1),(6,2),(7,3),(4,8),(6,9)],
 'A_dual': [(1,0),(2,0),(3,0),(1,4),(1,5),(2,6),(3,7),(8,4),(9,6)],
 'B': [(0,1),(0,2),(0,3),(4,1),(5,1),(6,2),(4,7),(6,8),(9,7)],
 'C': [(0,1),(0,2),(0,3),(4,1),(5,2),(4,6),(7,6),(8,6),(7,9)]
}
EXPECTED = {2:(1,1),3:(2,2),4:(3,3),5:(6,6),6:(10,10),7:(22,22),8:(42,42),9:(94,94),10:(203,201)}

def centers(g):
    n=len(g)
    if n<=2: return list(range(n))
    degree=[len(x) for x in g]
    leaves=deque(i for i,d in enumerate(degree) if d<=1)
    left=n
    while left>2:
        k=len(leaves);left-=k
        for _ in range(k):
            u=leaves.popleft()
            for v in g[u]:
                degree[v]-=1
                if degree[v]==1: leaves.append(v)
    return list(leaves)

def canon(g,colors=None):
    def root(u,p):
        tag='' if colors is None else str(colors[u])
        return '('+tag+''.join(sorted(root(v,u) for v in g[u] if v!=p))+')'
    c=centers(g)
    if len(c)==1:return root(c[0],-1)
    a,b=c
    return '['+''.join(sorted((root(a,b),root(b,a))))+']'

def grow(limit):
    gs=[[[]]]
    for n in range(1,limit+1):
        yield n,gs
        nxt={}
        for g in gs:
            for v in range(n):
                h=[list(x) for x in g]+[[v]]
                h[v].append(n)
                nxt.setdefault(canon(h),h)
        gs=list(nxt.values())

def bipartition(g):
    c=[-1]*len(g);c[0]=0
    q=deque([0])
    while q:
        v=q.popleft()
        for u in g[v]:
            if c[u]==-1:c[u]=1-c[v];q.append(u)
            else: assert c[u]!=c[v]
    return c

def polynomial(n,edges):
    # Independent weighted ideal/filter formula plus a biclique correction.
    lower=[0]*n;upper=[0]*n
    for a,b in edges:upper[a]|=1<<b;lower[b]|=1<<a
    ideals=Counter();filters=Counter()
    for mask in range(1<<n):
        if all((not(mask>>b&1)) or (lower[b]&mask)==lower[b] for b in range(n)):
            ideals[mask.bit_count()]+=1
        if all((not(mask>>a&1)) or (upper[a]&mask)==upper[a] for a in range(n)):
            filters[mask.bit_count()]+=1
    out=Counter()
    for d,k in ideals.items():out[(d,0)]+=k
    for d,k in filters.items():out[(0,d)]+=k
    out[(0,0)]-=1
    for a in range(n):
        d=upper[a].bit_count()
        for k in range(1,d+1):out[(1,k)]+=comb(d,k)
    for b in range(n):
        d=lower[b].bit_count()
        for k in range(1,d+1):out[(k,1)]+=comb(d,k)
    out[(1,1)]-=len(edges)
    return tuple(sorted((i,j,z) for (i,j),z in out.items() if z))

def direct(n,edges):
    low=[0]*n;up=[0]*n
    for a,b in edges:low[b]|=1<<a;up[a]|=1<<b
    result=Counter()
    for states in product(range(3),repeat=n):
        L=sum(1<<i for i,s in enumerate(states) if s==1)
        U=sum(1<<i for i,s in enumerate(states) if s==2)
        if any((low[b]&L)!=low[b] for b in range(n) if L>>b&1):continue
        if any((up[a]&U)!=up[a] for a in range(n) if U>>a&1):continue
        if any(up[a]&U!=U for a in range(n) if L>>a&1):continue
        result[(L.bit_count(),U.bit_count())]+=1
    return tuple(sorted((i,j,z) for (i,j),z in result.items() if z))

def encode_poly(p):return tuple(p)

def main():
    for n,trees in grow(10):
        if n==1:continue
        reps={}
        for g in trees:
            colors=bipartition(g)
            for d in (colors,[1-x for x in colors]):
                k=canon(g,d)
                if k not in reps:
                    e=[(u,v) if d[u]==0 else (v,u) for u in range(n) for v in g[u] if u<v]
                    reps[k]=e
        fibres=defaultdict(list)
        for code,e in reps.items():
            p=polynomial(n,e)
            fibres[p].append(code)
            if n<=8:assert p==direct(n,e),(n,code)
        if n in EXPECTED:assert (len(reps),len(fibres))==EXPECTED[n],(n,len(reps),len(fibres))
        collisions=sorted((len(x) for x in fibres.values() if len(x)>1))
        print(f'n={n} free_trees={len(trees)} poset_types={len(reps)} polynomials={len(fibres)} fibre_sizes={collisions}')
        if n==10:
            assert collisions==[2,2]
            observed={tuple(sorted(x)) for x in fibres.values() if len(x)>1}
            assert len(observed)==2
            witness_codes=[]
            for name,edges in WITNESSES.items():
                g=[[] for _ in range(10)]
                col=[-1]*10
                for a,b in edges:
                    g[a].append(b);g[b].append(a)
                    if col[a] not in (-1,0) or col[b] not in (-1,1):raise AssertionError('inconsistent bipartition')
                    col[a]=0;col[b]=1
                assert all(len(x)>0 for x in g) and len(edges)==9
                witness_codes.append(canon(g,col))
            assert {tuple(sorted(witness_codes[:2])),tuple(sorted(witness_codes[2:]))}==observed
            assert len(set(witness_codes))==4
    for name,edges in WITNESSES.items():
        p=polynomial(10,edges)
        assert p==direct(10,edges),name
        assert sum(z for _,_,z in p)==(332 if name.startswith('A') else 340)
        print(f'witness={name} total={sum(z for _,_,z in p)} nonzero_coefficients={len(p)}')
    assert polynomial(10,WITNESSES['A'])==polynomial(10,WITNESSES['A_dual'])
    assert polynomial(10,WITNESSES['B'])==polynomial(10,WITNESSES['C'])
    assert polynomial(10,WITNESSES['A'])!=polynomial(10,WITNESSES['B'])
    h0=[1,5,12,20,26,28,26,20,12,5,1]
    h1=[1,5,12,20,27,30,27,20,12,5,1]
    mix={(1,1):9,(1,2):5,(2,1):5,(1,3):1,(3,1):1}
    for name,pure in [('A',h0),('A_dual',h0),('B',h1),('C',h1)]:
        coeff=Counter({(i,j):z for i,j,z in polynomial(10,WITNESSES[name])})
        expected=Counter({(i,0):z for i,z in enumerate(pure)})
        for i,z in enumerate(pure):expected[(0,i)]+=z
        expected[(0,0)]-=1
        for ij,z in mix.items():expected[ij]+=z
        assert coeff==expected,name
    def witness_code(name,reversed_order=False,uncolored=False):
        ed=WITNESSES[name]
        g=[[] for _ in range(10)]
        col=[-1]*10
        for a,b in ed:
            g[a].append(b);g[b].append(a);col[a]=0;col[b]=1
        if reversed_order:col=[1-i for i in col]
        return canon(g,None if uncolored else col)
    assert witness_code('A',True)==witness_code('A_dual')
    assert witness_code('A')!=witness_code('A',True)
    for name in ('B','C'):assert witness_code(name)==witness_code(name,True)
    assert witness_code('B',uncolored=True)!=witness_code('C',uncolored=True)
    print('PASS: two distinct size-two fibres at ten vertices; all four witnesses checked by independent ternary enumeration')

if __name__=='__main__':main()
