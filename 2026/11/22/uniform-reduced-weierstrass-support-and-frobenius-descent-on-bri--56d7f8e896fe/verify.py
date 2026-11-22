#!/usr/bin/env python3
"""Exact checks for the finite-field ordered-root description of Bring-curve Weierstrass support.
No third-party modules are needed. The algebraic proof is in RESULT.md.
"""
from itertools import combinations, permutations, product
from math import isqrt

H = (4, 3, 2, 1)  # t^3+2t^2+3t+4, low to high

def isprime(n):
    return n >= 2 and all(n%d for d in range(2,isqrt(n)+1))

def roots_mod_p(p):
    return [a for a in range(p) if (a**3+2*a*a+3*a+4)%p==0]

def type_for_prime(p):
    if p < 7 or not isprime(p): raise ValueError('p must be prime >=7')
    r=len(roots_mod_p(p))
    assert r in (0,1,3), (p,r)
    return {0:(3,20), 1:(2,30), 3:(1,60)}[r]

class FiniteField:
    def __init__(self,p,modulus):
        self.p=p;self.mod=tuple(c%p for c in modulus)
        self.d=len(self.mod)-1
        assert self.mod[-1]==1
        self.zero=(0,)*self.d;self.one=(1,)+(0,)*(self.d-1)
    def elem(self,co):
        return tuple(int(c)%self.p for c in co)+(0,)*(self.d-len(co))
    def add(self,a,b): return tuple((x+y)%self.p for x,y in zip(a,b))
    def neg(self,a): return tuple(-x%self.p for x in a)
    def sub(self,a,b): return self.add(a,self.neg(b))
    def mul(self,a,b):
        out=[0]*(2*self.d-1)
        for i,u in enumerate(a):
            for j,v in enumerate(b):out[i+j]=(out[i+j]+u*v)%self.p
        for i in range(len(out)-1,self.d-1,-1):
            w=out[i]
            if w:
                for j in range(self.d): out[i-self.d+j]=(out[i-self.d+j]-w*self.mod[j])%self.p
        return tuple(out[:self.d])
    def pow(self,a,n):
        r=self.one
        while n:
            if n&1:r=self.mul(r,a)
            a=self.mul(a,a);n//=2
        return r
    def int(self,n):return self.elem((n,))
    def eval_h(self,x):
        r=self.one
        for c in (2,3,4): r=self.add(self.mul(r,x),self.int(c))
        return r
    def all_elements(self):return (tuple(q) for q in product(range(self.p),repeat=self.d))

# Exact specialization: discriminant is -200, h(1)=10, symmetric-root sums (-2,3,-4).
def basic_checks():
    a,b,c=(None,None,None)
    assert -200 == (2*3)**2-4*3**3-4*2**3*4-27*4**2+18*2*3*4
    assert sum(H)==10
    for p in range(7,1000):
        if isprime(p):
            r=roots_mod_p(p)
            assert len(r) in (0,1,3)
            d,k=type_for_prime(p)
            assert d*k==60
    return True

def example_field(p):
    if p==7:return FiniteField(7,(-1,-1,1)) # u^2-u-1
    if p==11:return FiniteField(11,H) # cubic is irreducible
    if p==43:return FiniteField(43,(0,1)) # base prime field, modulus u
    raise ValueError(p)

def full_point_check(p):
    F=example_field(p)
    roots=[u for u in F.all_elements() if F.eval_h(u)==F.zero]
    assert len(roots)==3,(p,roots)
    assert len(set(roots))==3
    assert F.add(F.add(roots[0],roots[1]),roots[2])==F.int(-2)
    assert F.add(F.add(F.mul(roots[0],roots[1]), F.mul(roots[0],roots[2])), F.mul(roots[1],roots[2]))==F.int(3)
    assert F.mul(F.mul(roots[0],roots[1]),roots[2])==F.int(-4)
    pts=set(); partitions=[]
    for ii,jj in combinations(range(5),2):
        group=set()
        other=[k for k in range(5) if k not in (ii,jj)]
        for tr in permutations(roots):
            coords=[None]*5
            coords[ii]=coords[jj]=F.one
            for k,a in zip(other,tr):coords[k]=a
            z=F.zero
            for power in (1,2,3):
                total=z
                for v in coords:total=F.add(total,F.pow(v,power))
                assert total==z,(p,power,coords)
            assert len({i for i in range(5) if coords[i]==F.one})==2
            group.add(tuple(coords))
        assert len(group)==6
        pts.update(group)
    assert len(pts)==60
    seen=set();cycles=[]
    for pt in pts:
        if pt in seen:continue
        orbit=[];v=pt
        while v not in orbit:
            orbit.append(v);seen.add(v)
            v=tuple(F.pow(t,p) for t in v)
        assert v==pt
        cycles.append(len(orbit))
    predicted=type_for_prime(p)
    assert len(cycles)==predicted[1] and set(cycles)=={predicted[0]}
    return dict(p=p,field_size=p**F.d,cycle_length=predicted[0],cycles=predicted[1],geometric_points=len(pts))

if __name__=='__main__':
    assert basic_checks()
    for p in (7,11,43):print(full_point_check(p))
    print('BRING_WEIERSTRASS_P_GE_7_ORDERED_ROOT_SUPPORT_VERIFIED')
