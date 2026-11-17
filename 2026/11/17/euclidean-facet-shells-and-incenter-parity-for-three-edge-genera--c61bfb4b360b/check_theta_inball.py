#!/usr/bin/env python3
"""Exact finite checks for Euclidean inballs of three-edge parallel-path graphs.

For each graph, independently enumerate integer feasible potentials, retain those
with connected saturated-edge graph, and compare norms/ranks with the formula.
Only standard-library exact rational arithmetic is used.
"""
from itertools import product
from math import comb
from fractions import Fraction


def connected_tight(m, vals):
    # Ordered vertices: terminal A, terminal B, then u_i, then v_i.
    n = 2*m+2
    adj = [[] for _ in range(n)]
    for i in range(m):
        for x,y in ((0,2+i), (2+i,2+m+i), (2+m+i,1)):
            if abs(vals[x]-vals[y])==1:
                adj[x].append(y)
                adj[y].append(x)
    seen={0}; pending=[0]
    while pending:
        x=pending.pop()
        for y in adj[x]:
            if y not in seen:
                seen.add(y); pending.append(y)
    return len(seen)==n


def raw_facets(m):
    vals=[]
    for term in range(-3,4):
        states=[(u,v) for u in range(-1,2) for v in range(term-1,term+2)
                if abs(u-v)<=1]
        for statevec in product(states,repeat=m):
            z=(0,term)+tuple(s[0] for s in statevec)+tuple(s[1] for s in statevec)
            if connected_tight(m,z): vals.append(z)
    return vals


def centered_norm_squared(z):
    n=len(z); S=sum(z)
    return Fraction(sum(v*v for v in z)*n-S*S,n)


def rank_q(rows):
    if not rows: return 0
    a=[[Fraction(t) for t in row] for row in rows]
    r=0
    for c in range(len(a[0])):
        piv=next((i for i in range(r,len(a)) if a[i][c]),None)
        if piv is None: continue
        a[r],a[piv]=a[piv],a[r]
        q=a[r][c]
        for k in range(c,len(a[r])): a[r][k]/=q
        for i in range(r+1,len(a)):
            q=a[i][c]
            if q:
                for k in range(c,len(a[i])): a[i][k]-=q*a[r][k]
        r+=1
        if r==len(a):break
    return r


def predicted(m):
    eps=m%2
    R=Fraction(5*m+1,2)-Fraction(2*eps,m+1)
    T=(2 if eps==0 else 4)*comb(m,m//2)
    dim=m+1 if eps==0 else m
    return R,T,dim


def normal_row(z):
    n=len(z); S=sum(z)
    return [n*t-S for t in z]


def checks():
    checked=0; facets=0
    for m in range(3,6):
        raw=raw_facets(m)
        assert len(raw)==2*(3**m+1),(m,len(raw))
        norms=[centered_norm_squared(z) for z in raw]
        r=max(norms)
        contacts=[z for z,v in zip(raw,norms) if v==r]
        rank=rank_q([normal_row(z) for z in contacts])
        e,t,d=predicted(m)
        assert r==e and len(contacts)==t and 2*m+1-rank==d, (m,r,e,len(contacts),t,rank,d)
        checked+=1; facets+=len(raw)
    print('RAW_INTEGER_FEASIBLE_TIGHT_GRAPH_VERTICES_PASS', 'models=',checked,'facets=',facets)
    signed=0
    for m in range(3,9):
        # Independent full-edge-gradient assignment for d=+1; d=-1 by negation.
        potentials=[]
        for words in product((0,1,2), repeat=m):
            pairs=[((-1,0),(1,0),(1,2))[w] for w in words]
            z=(0,1)+tuple(x[0] for x in pairs)+tuple(x[1] for x in pairs)
            potentials.append(z)
        potentials.append((0,3)+tuple(1 for _ in range(m))+tuple(2 for _ in range(m)))
        norms=[centered_norm_squared(z) for z in potentials]
        peak=max(norms); contact=[z for z,v in zip(potentials,norms) if v==peak]
        e,t,d=predicted(m)
        assert peak==e and 2*len(contact)==t
        rank=rank_q([normal_row(z) for z in contact]); assert 2*m+1-rank==d
        signed+=2*len(potentials)
    print('FULL_SIGNED_PATH_POTENTIAL_VARIANCE_AND_RANK_PASS', 'models=',6,'potentials=',signed)
    print('THREE_EDGE_GENERALIZED_THETA_INBALL_ALL_CHECKS_PASS')

if __name__=='__main__': checks()
