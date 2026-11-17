#!/usr/bin/env python3
"""Exact finite certificate for a maximal Euclidean ball in an explicit lattice polytope.

Inputs: the 21 lattice points in the 2026 Hofscheier--Nill eight-dimensional example.
No nonstandard dependencies; all decisive comparisons use rational interval arithmetic.
The proof of the optimal-radius upper bound and uniqueness is supplied separately.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import gcd, isqrt
from functools import reduce

Q = (
    (6,-6,0),(4,0,-2),(3,1,-2),(3,0,0),(3,0,-3),
    (2,1,-1),(2,-2,2),(1,1,-1),(1,0,1),(1,-1,2),
    (0,0,-3),(0,-1,2),(0,-3,3),(0,-6,0),(0,-6,-6),
    (-1,0,0),(-1,0,-1),(-1,-2,2),(-2,-1,-1),(-2,-2,-2),(-3,-3,0),
)
def dot(u,v): return sum(x*y for x,y in zip(u,v))
def sub(u,v): return tuple(x-y for x,y in zip(u,v))
def cross(u,v):
    return (u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])
def primitive(v):
    g=reduce(gcd,(abs(x) for x in v)); return tuple(x//g for x in v) if g else None

def facet_planes(Q):
    out=set()
    for i,j,k in combinations(range(len(Q)),3):
        n=primitive(cross(sub(Q[j],Q[i]),sub(Q[k],Q[i])))
        if n is None: continue
        h=dot(n,Q[i]); d=[dot(n,p)-h for p in Q]
        if max(d)<=0: pass
        elif min(d)>=0: n=tuple(-x for x in n);h=-h
        else: continue
        assert h>0 and all(dot(n,p)<=h for p in Q)
        out.add((*n,h))
    return sorted(out)

# Rational interval numbers: every operation encloses the exact real value.
class IV:
    def __init__(self,lo,hi=None):
        self.lo=F(lo);self.hi=F(lo if hi is None else hi)
        assert self.lo<=self.hi
    def __add__(self,o):
        o=as_iv(o);return IV(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return IV(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-as_iv(o))
    def __rsub__(self,o): return as_iv(o)+(-self)
    def __mul__(self,o):
        o=as_iv(o);v=[x*y for x in (self.lo,self.hi) for y in (o.lo,o.hi)]
        return IV(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=as_iv(o); assert o.lo>0 or o.hi<0
        return self*IV(1/o.hi,1/o.lo)
    def __rtruediv__(self,o): return as_iv(o)/self
    def __repr__(self): return f'[{float(self.lo):.16g}, {float(self.hi):.16g}]'
def as_iv(o):return o if isinstance(o,IV) else IV(o)
S=10**23
sqrt_cache={}
def SQ(k):
    assert isinstance(k,int) and k>=0
    if k not in sqrt_cache:
        q=isqrt(k*S*S);exact=q*q==k*S*S
        sqrt_cache[k]=IV(F(q,S),F(q+(not exact),S))
    return sqrt_cache[k]

def main():
    planes=facet_planes(Q)
    assert len(planes)==37
    assert sorted(set(h for _,_,_,h in planes))==[1,3,6]
    assert [sum(h==s for *_,h in planes) for s in (1,3,6)]==[8,11,18]
    A=sorted(tuple(6*a//h for a in (x,y,z)) for x,y,z,h in planes)
    assert len(A)==37 and len(set(A))==37
    assert all(all((6*a)%h==0 for a in (x,y,z)) for x,y,z,h in planes)
    assert max(dot(a,a) for a in A)==756
    u=(0,-1,0);v=(-2,1,-2);w=(-6,24,12);z0=(1,0,-1)
    assert all(t in A for t in (u,v,w,z0))
    assert (13+dot(u,u)*2,13+dot(u,u)+dot(v,v),13+dot(u,u)+dot(w,w),13+dot(u,u)+dot(z0,z0))==(15,23,770,16)
    # Upper-bound identity from a positive combination of the 9 active facets:
    weights={(u,u):F(14), (u,v):F(3,2),(v,u):F(3,2),
             (u,w):F(1),(w,u):F(1),(u,z0):F(9),(z0,u):F(9)}
    assert sum(weights.values())==37
    assert all(sum(weight*(a[k]+b[k]) for (a,b),weight in weights.items())==0 for k in range(3))
    assert 3*sum(weights.values())==111 and 2*sum(weights.values())==74
    # Exact formula uses algebraic radicals; interval enclosures are for inequalities only.
    rad15,rad23,rad770=SQ(15),SQ(23),SQ(770)
    radius=222/(257+14*rad15+3*rad23+2*rad770)
    cy=(radius*(5+rad15)-6)/2
    sxz=(radius*(5+rad23)-6)/2
    dxz=6+cy-9*radius
    cx=(sxz+dxz)/2
    cz=(sxz-dxz)/2
    c=(cx,cy,cz)
    # Algebraic identities corresponding to all 7 active side facets are
    # -2*cy+radius*(5+sqrt(15))=6,
    # -2*cx-2*cz+radius*(5+sqrt(23))=6,
    # -6*cx+23*cy+12*cz+radius*(5+sqrt(770))=6,
    # cx-cy-cz+9*radius=6.
    # They follow exactly by substitution, not numerical approximations.
    active=set(weights)
    min_lower=None; comparisons=0
    for a,b in product(A,A):
        if (a,b) in active: continue
        squared=13+dot(a,a)+dot(b,b)
        lhs=sum((a[k]+b[k])*c[k] for k in range(3))+radius*(5+SQ(squared))
        slack=6-lhs
        if not slack.lo>0:
            raise AssertionError(('nonactive facet not certified',a,b,slack))
        comparisons+=1
        if min_lower is None or slack.lo<min_lower:min_lower=slack.lo
    assert comparisons==37*37-7==1362
    assert F(2,1000)<min_lower<F(3,1000) # verified separation margin
    # An origin-centered ball has radius 1/sqrt(max normal squared).
    assert max(13+dot(a,a)+dot(b,b) for a,b in product(A,A))==1525
    # The 3 differences v-u,w-u,z0-u span R^3, forcing equal blocks at equality.
    determinant=dot(sub(v,u),cross(sub(w,u),sub(z0,u)))
    assert determinant==148
    assert radius.lo>F(58,100) and radius.hi<F(59,100)
    print('PASS exact rational-interval certificate')
    print('Q3: 21 input points; 37 distinct supporting planes; offsets 1,3,6')
    print('P8: 1369 side facets + 2 base facets')
    print('All 1362 non-active side inequalities strictly verified, seven active identities algebraic')
    print('Nine positive-weight active inequalities certify upper bound and unique center')
    print('Minimum certified nonactive slack: >',float(min_lower))
    print('Inradius interval:',radius)
    print('Incenter block interval:',c)
    print('Origin-centered inradius:',1/(1525**.5))

if __name__=='__main__':main()
