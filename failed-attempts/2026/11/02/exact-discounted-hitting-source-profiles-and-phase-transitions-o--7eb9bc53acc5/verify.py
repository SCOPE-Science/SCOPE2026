#!/usr/bin/env python3
"""Exact rational checks of discounted first-hit coverage on friendship graphs.

Usage: python3 verify.py
Only Python standard library required. Graph and linear system are constructed
from their original definitions; no quotient graph or symbolic proof formulas
are used to compute graph-side support.
"""
from fractions import Fraction as Q
from itertools import product
from collections import Counter
from math import factorial


def graph(m):
    n=2*m+1
    nbr=[[] for _ in range(n)]
    for i in range(m):
        u,v=2*i+1,2*i+2
        for a,b in [(0,u),(0,v),(u,v)]:
            nbr[a].append(b); nbr[b].append(a)
    assert len(nbr[0])==2*m
    assert all(len(x)==2 for x in nbr[1:])
    return nbr


def exact_support(neighbors, mask, lam):
    n=len(neighbors)
    unpinned=[v for v in range(n) if not (mask>>v)&1]
    if not unpinned:
        return [Q(1)]*n
    pos={v:i for i,v in enumerate(unpinned)}
    size=len(unpinned)
    mat=[[Q(0) for _ in range(size+1)] for _ in range(size)]
    for row,v in enumerate(unpinned):
        mat[row][row]=Q(1)
        a=lam/Q(len(neighbors[v]))
        for u in neighbors[v]:
            if u in pos:
                mat[row][pos[u]]-=a
            else:
                mat[row][-1]+=a
    # Gauss-Jordan elimination using rational arithmetic, independently
    # re-solving the pinned first-step equations for every source set.
    for c in range(size):
        piv=next(r for r in range(c,size) if mat[r][c])
        mat[piv],mat[c]=mat[c],mat[piv]
        d=mat[c][c]
        mat[c]=[x/d for x in mat[c]]
        for r in range(size):
            if r==c or not mat[r][c]:continue
            d=mat[r][c]
            mat[r]=[mat[r][j]-d*mat[c][j] for j in range(size+1)]
    ans=[Q(1)]*n
    for v,i in pos.items():ans[v]=mat[i][-1]
    for v in range(n):
        if (mask>>v)&1:continue
        assert ans[v] == lam*sum((ans[w] for w in neighbors[v]),Q(0))/len(neighbors[v])
    return ans


def analytic_min(m,lam,a,b,c,center):
    d=lam/(2-lam)
    if center:
        if a:return d
        if b:return lam
        return Q(1)
    den=2*m-2*lam*a*d-lam*lam*b/Q(2)
    num=lam*(b*(1+lam/Q(2))+2*c)
    x=num/den
    if a:return d*x
    if b:return lam*(1+x)/2
    return x


def formula_profile(m,lam,threshold):
    # Count source sets by exact number of sources, classified by occupancy
    # (none/one/both) in each triangle plus hub pinned/unpinned.
    out=Counter()
    for a in range(m+1):
        for b in range(m-a+1):
            c=m-a-b
            mult=factorial(m)//(factorial(a)*factorial(b)*factorial(c))*2**b
            for center in (False,True):
                if not center and b+c==0:continue
                if analytic_min(m,lam,a,b,c,center)>=threshold:
                    out[b+2*c+int(center)]+=mult
    return out


def claimed_min(m,lam,tau):
    d=lam/(2-lam)
    if m==1:
        if tau<=d:return (1,3)
        if tau<=lam:return (2,3)
        return (3,1)
    beta=lam*lam/(lam*lam+4*m*(1-lam))
    alpha=lam*((2+lam)*m+lam)/(4*m-lam*lam*(m-1))
    assert Q(0)<beta<d<alpha<lam<Q(1)
    if tau<=beta:return (1,2*m+1)
    if tau<=d:return (1,1)
    if tau<=alpha:return (m+1,2**m+m*2**(m-1))
    if tau<=lam:return (m+1,2**m)
    return (2*m+1,1)


def run():
    total=0
    for m,lam in product(range(1,6),(Q(1,2),Q(2,3),Q(4,5))):
        # More exact tests around every conjectured threshold, including
        # boundary equality in addition to arbitrary interior fractions.
        d=lam/(2-lam)
        criticals=[Q(0),lam,Q(1),d]
        if m>1:
            criticals += [lam*lam/(lam*lam+4*m*(1-lam)),
                          lam*((2+lam)*m+lam)/(4*m-lam*lam*(m-1))]
        s=sorted(set(criticals))
        thresholds=set(t for t in s if t>0)
        thresholds.update((u+v)/2 for u,v in zip(s,s[1:]))
        thresholds.update((Q(1,5), Q(1,3), Q(3,5), Q(7,10),Q(9,10)))
        neighbors=graph(m)
        bysize={}
        for mask in range(1,1<<(2*m+1)):
            h=exact_support(neighbors,mask,lam)
            bysize[mask]=(mask.bit_count(),min(h))
        for tau in sorted(thresholds):
            direct=Counter()
            for size,value in bysize.values():
                if value>=tau:direct[size]+=1
            predicted=formula_profile(m,lam,tau)
            assert direct==predicted,(m,lam,tau,direct,predicted)
            minimum=min(direct)
            assert claimed_min(m,lam,tau)==(minimum,direct[minimum]),(m,lam,tau)
            total+=1
        print('EXACT_SUBSET_PROFILES_OK',m,str(lam),'source_sets',len(bysize),'thresholds',len(thresholds))
    print('EXACT_FINITE_PROFILES_OK',total)
    print('VERIFY_OK')

if __name__=='__main__':run()
