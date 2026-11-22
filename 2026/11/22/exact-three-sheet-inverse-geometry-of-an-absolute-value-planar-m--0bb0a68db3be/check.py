#!/usr/bin/env python3
"""Standalone exact-boundary and numerical inverse-sheet regression for a planar map.

The analytical proof, not this finite checker, establishes the global theorem.
"""
from fractions import Fraction as Q
from math import sqrt, isclose
from random import Random

D=Q(5,4)
A=Q(5,2); K=Q(1); H=Q(1)

def bounds(v):
    k0=D*A/K
    b0=-A*v/H
    low=b0-(D*A-K*v)**2/(4*D*K*H)
    high=b0+(D*A+K*v)**2/(4*D*K*H)
    return k0,b0,low,high

def predicted(u,v):
    k0,b0,lo,hi=bounds(v)
    if v<=-k0:
        return 3 if lo<u<b0 else (2 if u in (lo,b0) else 1)
    if v>=k0:
        return 3 if b0<u<hi else (2 if u in (b0,hi) else 1)
    return 3 if lo<u<hi else (2 if u in (lo,hi) else 1)

def roots(u,v):
    out=[]
    for side in (-1,1):
        if side>0:
            aa=D*K/H; bb=(K*v-D*A)/H
        else:
            aa=-D*K/H; bb=-(D*A+K*v)/H
        cc=-A*v/H-u
        disc=float(bb*bb-4*aa*cc)
        if disc< -1e-9:continue
        disc=max(0.,disc)
        for y in ((-float(bb)+sqrt(disc))/(2*float(aa)),(-float(bb)-sqrt(disc))/(2*float(aa))):
            if side*y< -1e-9:continue
            if not any(abs(y-z)<1e-8 for z in out):out.append(y)
    out.sort()
    for y in out:
        x=-(float(v)+float(D)*y)/float(H)
        uu=x*(float(A)-float(K)*abs(y))
        vv=-float(H)*x-float(D)*y
        assert isclose(uu,float(u),abs_tol=2e-7,rel_tol=2e-7),(u,v,y,uu)
        assert isclose(vv,float(v),abs_tol=2e-7,rel_tol=2e-7)
    return out

def main():
    # The origin has three distinct regular preimages, with signs +, -, +.
    actual=roots(Q(0),Q(0))
    assert len(actual)==3 and all(isclose(x,y,abs_tol=1e-9) for x,y in zip(actual,[-2.5,0.,2.5]))
    for y,sgn in zip(actual,(+1,-1,+1)):
        x=-float(D)*y/float(H)
        if y==0:
            det=-float(A*D)
        else:
            jac11=float(A)-float(K)*abs(y)
            jac12=-float(K)*x*(1 if y>0 else -1)
            det=jac11*(-float(D))-jac12*(-float(H))
        assert sgn*det>0
        assert isclose(abs(det),float(A*D),abs_tol=1e-9)
    # Exact rational target levels at both folds and the switching crease.
    for v in [Q(-6),-D*A/K,Q(-2),Q(0),Q(1),D*A/K,Q(6)]:
        _,base,lo,hi=bounds(v)
        for u in [lo,base,hi,lo-Q(1),hi+Q(1),(lo+base)/2,(base+hi)/2]:
            if u in (lo,hi,base) or v in (-D*A/K,D*A/K):
                got=len(roots(u,v)); want=predicted(u,v)
                assert got==want,(u,v,got,want)
    rng=Random(73281)
    counts={1:0,2:0,3:0}
    for _ in range(1800):
        v=Q(rng.randrange(-100,101),10)
        u=Q(rng.randrange(-250,251),10)
        got=len(roots(u,v));want=predicted(u,v)
        assert got==want,(u,v,got,want)
        counts[got]+=1
    assert counts[1]>100 and counts[3]>100
    print('FOLD_CREASE_VERIFY_OK')

if __name__=='__main__':main()
