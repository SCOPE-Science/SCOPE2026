#!/usr/bin/env python3
"""Standalone exhaustive finite checks for forest complexes of regular graph covers.
Requires only Python 3 standard library. No external files needed.
"""
from math import gcd
from itertools import combinations

def forest(v, edges):
    p=list(range(v))
    def root(x):
        while p[x]!=x:
            p[x]=p[p[x]];x=p[x]
        return x
    for a,b in edges:
        a,b=root(a),root(b)
        if a==b: return False
        p[a]=b
    return True

def signed_fixed_euler(v, edges, s, k):
    N=len(edges); assert N<=15
    trace= -1 # empty face has reduced chain degree -1
    for mask in range(1,1<<N):
        chosen=[i for i in range(N) if mask>>i&1]
        moved=[(i//k)*k+((i%k+s)%k) for i in chosen]
        if sorted(moved)!=chosen:continue
        if not forest(v,[edges[i] for i in chosen]):continue
        inv=sum(moved[i]>moved[j] for i in range(len(moved)) for j in range(i+1,len(moved)))
        trace+=(-1)**(len(chosen)-1+inv)
    return trace

def run(k,n,base):
    if len(base)*k>15:return None
    v=n*k
    edges=[((a*k+t),(b*k+(t+c)%k)) for (a,b,c) in base for t in range(k)]
    rows=[]
    for s in range(k):
        d=gcd(k,s)
        if s==0:d=k
        orbits=[];seen=set()
        for i in range(len(edges)):
            if i in seen:continue
            orb=[];x=i
            while x not in seen:
                orb.append(x);seen.add(x);x=(x//k)*k+((x%k+s)%k)
            orbits.append(orb)
        qe=[]
        for orb in orbits:
            u,w=edges[orb[0]]
            qe.append(((u//k)*d+u%k%d,(w//k)*d+w%k%d))
        for bits in range(1<<len(orbits)):
            sel=[j for j in range(len(orbits)) if bits>>j&1]
            down=forest(n*d,[qe[j] for j in sel])
            up=forest(v,[edges[i] for j in sel for i in orbits[j]])
            if down!=up: raise AssertionError((k,n,base,s,bits,down,up))
        alternating=sum((-1)**bits.bit_count() for bits in range(1<<len(orbits)) if forest(n*d,[qe[j] for j in range(len(orbits)) if bits>>j&1]))
        beta=(-1)**(n*d-1)*alternating
        L=signed_fixed_euler(v,edges,s,k)
        toptrace=(-1)**(v-2)*L
        predicted=(-1)**(v-n*d)*beta
        assert toptrace==predicted,(k,n,base,s,toptrace,predicted)
        rows.append((s,n*d,len(orbits),beta,toptrace))
    return rows

cases=[
    (2,3,[(0,1,0),(1,2,0),(2,0,1)]),
    (3,3,[(0,1,0),(1,2,0),(2,0,1)]),
    (4,3,[(0,1,0),(1,2,0),(2,0,1)]),
    (2,4,[(a,b,int(a==0 and b==1)) for a,b in combinations(range(4),2)]),
    (3,2,[(0,1,0),(0,1,1),(0,1,2)]),
    (2,2,[(0,1,0),(0,1,1)]),
    (3,1,[(0,0,1)]),
    (4,1,[(0,0,1)]),
    (3,1,[(0,0,1),(0,0,0)]),
]
for k,n,base in cases:
    rows=run(k,n,base)
    if rows is None:continue
    print('cover', k,n,len(base), 'quotient-subgroup data [shift, vertices, edge orbits, beta, trace]:',rows)
print('REGULAR_COVER_FOREST_EXACT_PASS cases=',len(cases))

def run_klein_four():
    k=4;n=2; base=[(0,1,0),(0,1,1),(0,1,2)]
    v=n*k
    edges=[(a*k+t,b*k+(t^c)) for a,b,c in base for t in range(k)]
    for H in ([0],[0,1],[0,2],[0,3],[0,1,2,3]):
        cosets=[]; which={}
        for u in range(n):
            for t in range(k):
                if (u,t) in which:continue
                c=sorted({t^h for h in H});z=len(cosets)
                cosets.append((u,c));which.update({(u,x):z for x in c})
        ors=[];seen=set()
        for i in range(len(edges)):
            if i in seen:continue
            a=i//k;t=i%k;orb=sorted({a*k+(t^h) for h in H});seen.update(orb);ors.append(orb)
        qe=[(which[(edges[orb[0]][0]//k,edges[orb[0]][0]%k)],which[(edges[orb[0]][1]//k,edges[orb[0]][1]%k)]) for orb in ors]
        alt=0
        for mask in range(1<<len(ors)):
            selected=[j for j in range(len(ors)) if mask>>j&1]
            d=forest(len(cosets),[qe[j] for j in selected]);u=forest(v,[edges[i] for j in selected for i in ors[j]])
            assert d==u,(H,mask)
            if d: alt+=(-1)**len(selected)
        beta=(-1)**(len(cosets)-1)*alt
        print('Klein-four subgroup',H,'quotient vertices',len(cosets),'edge orbits',len(ors),'beta',beta)
        if len(H)==2:
            s=H[1]
            L=-1
            for mask in range(1<<len(edges)):
                if mask==0:continue
                inds=[i for i in range(len(edges)) if mask>>i&1]
                moved=[(i//k)*k+((i%k)^s) for i in inds]
                if sorted(moved)!=inds or not forest(v,[edges[i] for i in inds]):continue
                inv=sum(moved[i]>moved[j] for i in range(len(inds)) for j in range(i+1,len(inds)))
                L+=(-1)**(len(inds)-1+inv)
            assert (-1)**(v-2)*L==(-1)**(v-len(cosets))*beta
    print('KLEIN_FOUR_NONCYCLIC_SUBGROUP_PASS')
run_klein_four()
