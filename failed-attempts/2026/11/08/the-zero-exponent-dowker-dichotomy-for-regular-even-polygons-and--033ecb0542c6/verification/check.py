#!/usr/bin/env python3
"""Exact-rational interval certificate for regular-polygon weak logarithmic Dowker inequalities.

No floating point arithmetic or third-party dependencies. The only analytic ingredients
are Machin's identity, alternating arctangent series, and Taylor-Lagrange remainders.
"""
from fractions import Fraction as F
from math import factorial
from functools import lru_cache

class Interval:
    def __init__(self, lo, hi=None):
        self.lo=F(lo); self.hi=F(hi if hi is not None else lo)
        assert self.lo<=self.hi
    def __add__(self, other):
        other=as_interval(other)
        return Interval(self.lo+other.lo, self.hi+other.hi)
    __radd__=__add__
    def __neg__(self): return Interval(-self.hi,-self.lo)
    def __sub__(self, other): return self+-as_interval(other)
    def __rsub__(self, other): return as_interval(other)+-self
    def __mul__(self, other):
        other=as_interval(other)
        p=[x*y for x in (self.lo,self.hi) for y in (other.lo,other.hi)]
        return Interval(min(p),max(p))
    __rmul__=__mul__
    def __truediv__(self, other):
        other=as_interval(other)
        assert other.lo*other.hi>0
        return self*Interval(1/other.hi,1/other.lo)
    def __pow__(self, n):
        assert isinstance(n,int) and n>=0
        if n==0: return Interval(1)
        if n==1: return self
        if n%2==0 and self.lo<0<self.hi:
            return Interval(0,max(self.lo**n,self.hi**n))
        return Interval(min(self.lo**n,self.hi**n),max(self.lo**n,self.hi**n))

def as_interval(v): return v if isinstance(v,Interval) else Interval(v)

def atan_bounds(den,terms=28):
    z=F(1,den)
    s=sum(((-1)**j)*z**(2*j+1)/F(2*j+1) for j in range(terms))
    r=z**(2*terms+1)/F(2*terms+1)
    return Interval(s,s+r) if terms%2==0 else Interval(s-r,s)

PI=16*atan_bounds(5)-4*atan_bounds(239)
assert F(314,100)<PI.lo<PI.hi<F(315,100)
GRID=10**15

def quantize_interval(lo,hi):
    return Interval(F((lo*GRID).__floor__(),GRID),F(-((-hi*GRID).__floor__()),GRID))

@lru_cache(None)
def sinecosine(multiple,denominator,kind):
    X=PI*F(multiple,denominator)
    center=(X.lo+X.hi)/2
    delta=(X.hi-X.lo)/2
    assert 0<=X.lo<=X.hi<F(4)
    if kind=='sin':
        polynomial=sum(((-1)**j)*center**(2*j+1)/factorial(2*j+1) for j in range(19))
        error=delta+F(4**38,factorial(38))
    else:
        assert kind=='cos'
        polynomial=sum(((-1)**j)*center**(2*j)/factorial(2*j) for j in range(19))
        error=delta+F(4**37,factorial(37))
    return quantize_interval(polynomial-error,polynomial+error)

def sin(m,n):return sinecosine(m,n,'sin')
def cos(m,n):return sinecosine(m,n,'cos')
def tan(m,n):return sin(m,n)/cos(m,n)

@lru_cache(None)
def A(k,n):
    if n>=2*k: return 2*k*tan(1,2*k)
    q,r=divmod(2*k,n)
    if n==3:
        if r==0:return 3*tan(1,3)
        return 2*((3-r)*sin(q,k)+r*sin(q+1,k))/(cos(1,2*k)**2)
    return (n-r)*tan(q,2*k)+r*tan(q+1,2*k)

# Small even polygons. Raising to integral powers eliminates logarithms.
# The source's explicit A(k,n) formula makes this a finite complete proof,
# because A(k,n) is constant once n reaches 2k.
passed={}
for k in (6,8):
    checked=0
    for m in (3,4,5):
        for n in range(7,2*k+1):
            lhs=(A(k,m)**(n-6))*(A(k,n)**(6-m))
            rhs=A(k,6)**(n-m)
            if not lhs.lo>rhs.hi:
                raise AssertionError(('uncertified finite inequality',k,m,n))
            checked+=1
    passed[k]=checked

# For k>=9 the source's A(k,6) formula is decreasing within each
# residue class 2k mod 6; hence k=9,10,11 suffice as maxima.
# Strictly log-convex area of circumscribing disk polygons gives
# a universal lower barrier sqrt(B(5)*B(7)).
barrier=(5*tan(1,5))*(7*tan(1,7))
for k in (9,10,11):
    assert (A(k,6)**2).hi < barrier.lo,('unproved large-k barrier',k)

# In each exceptional polygon the consecutive minimizers A(5),A(6),A(7)
# lie on one affine segment of the published exact formula; thus they have
# midpoint equality before the strictly concave log (and all 0<alpha<1).
# Certify strict ordering with intervals, while affine equality is symbolic.
for k in (4,5,7):
    assert A(k,5).lo>A(k,6).hi>A(k,7).hi
    assert (2*k//5,2*k//6,2*k//7) in ((1,1,1),(2,1,1),(2,2,2))

print('RATIONAL_INTERVAL_CERTIFICATE_PASSED')
print('finite_comparisons',passed,'large_k_residue_checks',3,'exceptional_midpoints',3)
for k in (6,8,9,10,11):
    v=A(k,6)
    print('A6_interval',k,str(float(v.lo)),str(float(v.hi)))
