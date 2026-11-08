#!/usr/bin/env python3
"""Reproducible finite-field and dimension feasibility checks for a unit-density extremum.
No search/network dependencies; standard library only.
"""
from itertools import product
from math import prod
from fractions import Fraction

def irreducible_quadratic(p):
    for a,b in product(range(p),repeat=2):
        if all((r*r+a*r+b)%p for r in range(p)):
            return a,b
    raise AssertionError('no irreducible quadratic')

def field(p):
    aa,bb=irreducible_quadratic(p)
    el=list(product(range(p),repeat=2))
    zero=(0,0);one=(1,0);theta=(0,1)
    def add(x,y):return ((x[0]+y[0])%p,(x[1]+y[1])%p)
    def mul(x,y):
        c=(x[0]*y[0]-bb*x[1]*y[1])%p
        d=(x[0]*y[1]+x[1]*y[0]-aa*x[1]*y[1])%p
        return c,d
    def power(x,k):
        y=one
        while k:
            if k&1:y=mul(y,x)
            x=mul(x,x);k>>=1
        return y
    assert all(mul(power(x,p*p-1),x)==x for x in el if x!=zero)
    return el,zero,one,theta,add,mul,power

def partitions_min_atleast2(n,lo=2):
    if n==0:
        yield ()
    for k in range(lo,n+1):
        for rest in partitions_min_atleast2(n-k,k):
            yield (k,)+rest

def possible_radical_degree(j,fields):
    achievable={0}
    for f in fields:
        reachable=set(achievable)
        for a in list(achievable):
            for k in range(1,j//f+1):reachable.add(a+k*f)
        achievable=reachable
    return j in achievable

for p in (2,3,5):
    el,zero,one,theta,add,mul,power=field(p)
    q=p*p
    E=list(product(el,repeat=2))
    def rprod(x,y):
        a,b=x;c,d=y
        return (mul(a,c),add(mul(a,d),mul(b,power(c,p))))
    unit_count=0
    for a,b in E:
        unit=(a!=zero)
        unit_count+=unit
        if p<=3:
            if unit:
                ainverse=power(a,q-2)
                inv=(ainverse,mul(mul((-ainverse[0]%p,-ainverse[1]%p),b),power(ainverse,p)))
                assert rprod((a,b),inv)==(one,zero)
                assert rprod(inv,(a,b))==(one,zero)
            else:
                assert rprod((a,b),(zero,one))==(zero,zero)
    assert unit_count==q*(q-1)
    assert rprod((zero,one),(theta,zero)) != rprod((theta,zero),(zero,one))
    if p==2:
        for x,y,z in product(E,repeat=3):
            assert rprod(rprod(x,y),z)==rprod(x,rprod(y,z))
    whole_units=unit_count*(p**3-1)
    assert whole_units == p**7*(1-Fraction(1,p*p))*(1-Fraction(1,p**3))
    print(f'p={p}; quadratic={irreducible_quadratic(p)}; |T|={p**4}; T-units={unit_count}; |R|={p**7}; R-units={whole_units}; R-nonunits={p**7-whole_units}')

opts=[]
for d in range(2,7):
    for dims in partitions_min_atleast2(d):
        if len(dims)<2:continue
        if possible_radical_degree(7-d,dims):opts.append((dims,7-d))
assert opts==[((2,3),2)],opts
for p in (2,3,5,7):
    top=(1-Fraction(1,p*p))*(1-Fraction(1,p**3))
    assert top > 1-Fraction(1,p)
    assert top > (1-Fraction(1,p))*(1-Fraction(1,p*p))
print('n=7 semisimple-field profiles of degree >=2 with radical and >=2 factors:',opts)
print('VERIFY_OK')
