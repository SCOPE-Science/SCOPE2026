#!/usr/bin/env python3
"""Standalone checks of an exact two-color rainbow-connection enumerator."""
from math import comb, factorial
from fractions import Fraction
from collections import Counter

def predicted_polynomial(m):
    # Power series exact arithmetic using a separate elementary convolution implementation.
    def mul(a,b):
        o=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):o[i+j]+=x*y
        return o
    def powpoly(base,k):
        p=[1]
        for _ in range(k):p=mul(p,base)
        return p
    out=[0]*(2*m*(m-1)+1)
    for k in range(m+1):
        factors=[powpoly([1,0,0,0,1],comb(k,2)),powpoly([1,0,1],2*k*(m-k)),powpoly([1,1],4*comb(m-k,2))]
        prod=[1]
        for factor in factors:prod=mul(prod,factor)
        for d,c in enumerate(prod):out[d]+=(-1)**k*comb(m,k)*c
    return out

def direct_hist(m):
    # Original graph: vertices (i,side) indexed 2*i+side.
    E=[]
    for u in range(2*m):
      for v in range(u+1,2*m):
        if u//2 != v//2:E.append((u,v))
    assert len(E)==2*m*(m-1)
    edges={tuple(sorted(e)):i for i,e in enumerate(E)}
    checks=[]
    for i in range(m):
        u=2*i;v=u+1
        pairs=[]
        for w in range(2*m):
            if w not in (u,v):
                pairs.append((edges[tuple(sorted((u,w)))],edges[tuple(sorted((v,w)))]))
        checks.append(pairs)
    hist=Counter()
    events=[Counter() for _ in range(1<<m)]
    for bits in range(1<<len(E)):
        failing=0
        for i,pairs in enumerate(checks):
            if all(((bits>>a)&1)==((bits>>b)&1) for a,b in pairs):failing |= 1<<i
        # Independent graph-geodesic definition: each missing pair has a rainbow 2-path.
        if failing == 0:hist[bits.bit_count()]+=1
        for mask in range(1<<m):
            if failing & mask==mask:events[mask][bits.bit_count()]+=1
    return [hist[i] for i in range(len(E)+1)],events

def intersection_formula(m,k):
    def conv(a,b):
        o=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):o[i+j]+=x*y
        return o
    res=[1]
    for basic,num in [([1,0,0,0,1],comb(k,2)),([1,0,1],2*k*(m-k)),([1,1],4*comb(m-k,2))]:
        for _ in range(num):res=conv(res,basic)
    return res

def value_at(arr,p):
    return sum(Fraction(v)*p**i*(1-p)**(len(arr)-1-i) for i,v in enumerate(arr))

for m in (2,3):
    polynomial=predicted_polynomial(m)
    direct,events=direct_hist(m)
    assert polynomial==direct,(m,polynomial,direct)
    for mask,cnt in enumerate(events):
        formula=intersection_formula(m,mask.bit_count())
        assert [cnt.get(i,0) for i in range(len(polynomial))] == formula,(m,mask)
    for p in [Fraction(1,4),Fraction(1,2),Fraction(3,4)]:
        probability=value_at(direct,p)
        q=p*p+(1-p)*(1-p); a=p**4+(1-p)**4
        rhs=sum((-1)**k*comb(m,k)*a**comb(k,2)*q**(2*k*(m-k)) for k in range(m+1))
        assert probability==rhs,(m,p,probability,rhs)
    print('DIRECT_GRAPH_AND_ALL_INTERSECTIONS_OK',m,sum(direct),len(polynomial))

for m,expected in [(2,10),(3,3416),(4,15775808)]:
    poly=predicted_polynomial(m)
    assert sum(poly)==expected
    assert poly==poly[::-1]
    assert min(poly)>=0
    assert poly[0]==0 and poly[-1]==0
    print('POLYNOMIAL_COEFFICIENTS_NONNEGATIVE_SYMMETRIC_OK',m,expected)
print('VERIFY_OK')
