#!/usr/bin/env python3
"""Exact checks for optimal closed-neighbourhood domination in small affine planes."""
from itertools import product, combinations

def add(a,b,q):
    return a^b if q==4 else (a+b)%q

def mul(a,b,q):
    if q!=4:return a*b%q
    out=0
    for k in range(2):
        if (b>>k)&1:out ^= a<<k
    for k in (3,2):
        if out&(1<<k):out ^= 0b111<<(k-2)
    return out

def affine(q):
    points=list(product(range(q),repeat=2))
    lines=[]
    for slope in range(q):
        for intercept in range(q):
            lines.append(frozenset((x,add(mul(slope,x,q),intercept,q)) for x in range(q)))
    for intercept in range(q):
        lines.append(frozenset((intercept,y) for y in range(q)))
    assert len(lines)==q*(q+1) and len(set(lines))==len(lines)
    assert all(len(L)==q for L in lines)
    assert all(sum(p in L for L in lines)==q+1 for p in points)
    return points,lines

def run(q):
    P,L=affine(q); lp=len(P); n=lp+len(L)
    nbr=[0]*n
    for i,p in enumerate(P):
        for j,line in enumerate(L):
            if p in line:
                nbr[i] |= 1<<(lp+j)
                nbr[lp+j] |= 1<<i
    full=(1<<n)-1
    actual=set()
    for Ap in combinations(range(lp),q):
        pm=sum(1<<i for i in Ap)
        cov=pm
        for i in Ap:cov |= nbr[i]
        remaining_lines=(full^cov)>>lp
        if remaining_lines.bit_count()>q-1: continue
        for Bl in combinations(range(len(L)),q-1):
            bm=sum(1<<(lp+j) for j in Bl)
            total=cov|bm
            for j in Bl:total |= nbr[lp+j]
            if total==full:actual.add(pm|bm)
    predicted=set()
    for k,B in enumerate(L):
        subset_points=sum(1<<P.index(p) for p in B)
        other_parallel=[j for j,C in enumerate(L) if j!=k and not B.intersection(C)]
        assert len(other_parallel)==q-1
        subset_lines=sum(1<<(lp+j) for j in other_parallel)
        predicted.add(subset_points|subset_lines)
    assert actual==predicted,(q,len(actual),len(predicted),len(actual^predicted))
    diff_counts={}
    for i,s in enumerate(sorted(actual)):
        for t in sorted(actual)[i+1:]:
            changes=(s^t).bit_count()//2
            diff_counts[changes]=diff_counts.get(changes,0)+1
    expected={(q+1):(q+1)*q*(q-1)//2, (2*q-2):((q*(q+1))**2-(q+1)*q*q)//2}
    expected={d:sum(v for x,v in [(q+1,(q+1)*q*(q-1)//2),(2*q-2,((q*(q+1))**2-(q+1)*q*q)//2)] if x==d) for d in set([q+1,2*q-2])}
    assert diff_counts==expected,(diff_counts,expected)
    print(f'q={q}: {n} vertices, {len(actual)} optimal sets, pairwise changes {diff_counts}, verified')

if __name__=='__main__':
    for q in (2,3,4):run(q)
