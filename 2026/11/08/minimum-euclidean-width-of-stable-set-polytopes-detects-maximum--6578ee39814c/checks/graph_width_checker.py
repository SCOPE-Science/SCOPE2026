#!/usr/bin/env python3
"""Independent finite checks of stable-set polytope minimum widths and near-minimizers.

No finite test is asserted to certify an all-order theorem.
"""
from itertools import combinations
from math import sqrt
from random import Random

def masks_of_stable_sets(n, edges):
    return [s for s in range(1 << n) if not any(((s >> a)&1) and ((s >> b)&1) for a,b in edges)]

def masks_of_cliques(n, edges):
    e=set(edges)
    return [s for s in range(1,1 << n) if all((a,b) in e for a in range(n) for b in range(a+1,n) if (s>>a)&1 and (s>>b)&1)]

def chromatic(n,edges):
    adj=[0]*n
    for a,b in edges:adj[a]|=1<<b;adj[b]|=1<<a
    def feasible(i,colors,used,k):
        if i==n:return True
        for c in range(min(used+1,k)):
            if not adj[i]&colors[c]:
                colors[c]|=1<<i
                if feasible(i+1,colors,max(used,c+1),k):return True
                colors[c]^=1<<i
        return False
    return next(k for k in range(1,n+1) if feasible(0,[0]*k,0,k))

def support_width(u,stable):
    sums=[sum(u[i] for i in range(len(u)) if (s>>i)&1) for s in stable]
    return max(sums)-min(sums)

def random_poset_comparability(n,rng):
    order=list(range(n));rng.shuffle(order)
    r=[[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if rng.random()<rng.random():r[order[i]][order[j]]=True
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if r[i][k] and r[k][j]:r[i][j]=True
    return [(i,j) for i in range(n) for j in range(i+1,n) if r[i][j] or r[j][i]]

def random_perfect_graph(n,rng,kind):
    if kind==0:return random_poset_comparability(n,rng)
    if kind==1:
        parts=[rng.randrange(min(n,5)) for _ in range(n)]
        return [(i,j) for i in range(n) for j in range(i+1,n) if parts[i]!=parts[j]]
    if kind==2:
        parts=[rng.randrange(min(n,5)) for _ in range(n)]
        return [(i,j) for i in range(n) for j in range(i+1,n) if parts[i]==parts[j]]
    if kind==3:
        parts=[rng.randrange(2) for _ in range(n)]
        return [(i,j) for i in range(n) for j in range(i+1,n) if parts[i]!=parts[j] and rng.random()<0.7]
    endpoints=[(a:=rng.randrange(2*n+1),a+rng.randrange(n+1)) for _ in range(n)]
    return [(i,j) for i in range(n) for j in range(i+1,n) if max(endpoints[i][0],endpoints[j][0])<=min(endpoints[i][1],endpoints[j][1])]

def verify():
    rng=Random(982156)
    cases=directions=near=contacts=0
    for n in range(1,10):
        for kind in range(5):
            for _ in range(18):
                edges=random_perfect_graph(n,rng,kind)
                cliques=masks_of_cliques(n,edges)
                q=max(s.bit_count() for s in cliques)
                assert q==chromatic(n,edges),(n,edges,q)
                mc=[s for s in cliques if s.bit_count()==q]
                stable=masks_of_stable_sets(n,edges)
                for s in mc:
                    u=[int(bool((s>>i)&1)) for i in range(n)]
                    assert support_width(u,stable)==1
                    contacts+=1
                for z in range(30):
                    if z%5==0:
                        m=rng.choice(mc)
                        u=[(1 if (m>>i)&1 else 0)+(rng.choice([-1,0,1]) if rng.random()<.2 else 0) for i in range(n)]
                    else:
                        u=[rng.randrange(-4,5) for _ in range(n)]
                    d=sum(x*x for x in u)
                    if not d:continue
                    w=support_width(u,stable)
                    assert q*w*w>=d-1e-9,(n,q,u,w,d)
                    directions+=1
                    ww=w/sqrt(d);delta=q*ww*ww-1
                    if q==1 or ww*ww<1/(q-1)-1e-12:
                        bound=sqrt(max(0,delta)+delta*delta/(ww*ww))+sqrt(q)*(ww-1/sqrt(q))
                        best=min(sqrt(sum((u[i]/sqrt(d)-sign*int(bool((m>>i)&1))/sqrt(q))**2 for i in range(n))) for m in mc for sign in (-1,1))
                        assert best<=bound+1e-9,(n,q,u,best,bound)
                        near+=1
                cases+=1
    return cases,directions,near,contacts

if __name__=='__main__':
    print('STABLE_SET_MINIMUM_WIDTH_CHECKS_PASSED graphs,directions,near_cases,clique_contacts=',*verify())
