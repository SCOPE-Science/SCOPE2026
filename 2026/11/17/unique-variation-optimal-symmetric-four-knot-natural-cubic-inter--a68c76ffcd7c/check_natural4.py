#!/usr/bin/env python3
"""Reproducible exact interval and finite-data checks for four-knot natural splines."""
from fractions import Fraction as Q
from math import isqrt, sqrt
import random

class I:
    def __init__(self,lo,hi=None):
        if isinstance(lo,I): self.lo,self.hi=lo.lo,lo.hi; return
        self.lo=Q(lo);self.hi=Q(lo if hi is None else hi)
        assert self.lo<=self.hi
    @staticmethod
    def of(x):return x if isinstance(x,I) else I(x)
    def __add__(self,b):
        b=I.of(b);return I(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,b):return self+-I.of(b)
    def __rsub__(self,b):return I.of(b)+-self
    def __mul__(self,b):
        b=I.of(b);p=[a*c for a in (self.lo,self.hi) for c in (b.lo,b.hi)];return I(min(p),max(p))
    __rmul__=__mul__
    def __truediv__(self,b):
        b=I.of(b);assert b.lo>0 or b.hi<0
        return self*I(1/b.hi,1/b.lo)
    def __rtruediv__(self,b):return I.of(b)/self
    def __pow__(self,p):
        if p==0:return I(1)
        return self*(self**(p-1))

def sqrt_I(q,decimal_places=27):
    q=Q(q);assert q>=0
    scale=10**decimal_places
    lo=isqrt(q.numerator*scale*scale//q.denominator)
    return I(Q(lo,scale),Q(lo+1,scale))

def val_gain_interval(r):
    r=Q(r); R=I(r); d=(R+2)*(3*R+2)
    s=sqrt_I(9*r*r+18*r+12)
    vs=(2*R+2-s/3)/(3*R+2)
    # v falls within (1/3,1/2); interval operations preserve exact enclosure
    F=R*R*vs*(1-vs)*(3*R*(1-vs)+4-2*vs)/d
    rt3=sqrt_I(3)
    O=1+2*F+4*R/(3*rt3*d)
    C=1+8/(3*rt3*R*(R+2))
    return O,C

rlo=Q('1.42882553');rhi=Q('1.42882554')
a,b=val_gain_interval(rlo);assert (a-b).hi<0
c,d=val_gain_interval(rhi);assert (c-d).lo>0
print('EXACT_RATIONAL_OPTIMAL_RATIO_BRACKET_PASS',str(rlo),str(rhi))

# For any fixed positive r, derivative sign on the outer interval and
# unique interior maximum in middle follow from positive polynomial factors.
# This uses exact sample evaluations merely to guard transcription.
for numerator in range(1,101):
    r=Q(numerator,23)
    D=(r+2)*(3*r+2)
    M1=-12*(r+1)/D;M2=6*r/D
    assert D>4*(r+1)
    assert M1<0 and M2>0
    for j in range(21):
        v=Q(j,20)
        F=r*r*v*(1-v)*(3*r*(1-v)+4-2*v)/D
        cubic=(r*r/Q(6))*(M1*((1-v)**3-(1-v))+M2*(v**3-v))
        assert F==cubic
    Ms=6/(r*(r+2))
    assert Ms>0
print('EXACT_NATURAL_SPLINE_CURVATURE_AND_MIDDLE_CUBIC_IDENTITIES_PASS',100*21)

# Numerical quadrature-free finite-data stress checks: variation computed
# by all real stationary points of each cubic segment, not sample grid sums.
def spline_variation(r,data):
    h=[1.0,float(r),1.0]
    slopes=[(data[i+1]-data[i])/h[i] for i in range(3)]
    v1=6*(slopes[1]-slopes[0]);v2=6*(slopes[2]-slopes[1]);d=4*(1+r)**2-r*r
    M=[0.0,(2*(1+r)*v1-r*v2)/d,(2*(1+r)*v2-r*v1)/d,0.0]
    var=0.0
    for i in range(3):
        hh=h[i]; a=0.5*hh*hh*(M[i+1]-M[i]);b=hh*hh*M[i]
        c=(data[i+1]-data[i])-hh*hh*(2*M[i]+M[i+1])/6
        roots=[]
        if abs(a)>1e-13:
            delta=b*b-4*a*c
            if delta>0:
                roots=[(-b-sqrt(delta))/(2*a),(-b+sqrt(delta))/(2*a)]
        elif abs(b)>1e-13:roots=[-c/b]
        ts=[0.0]+sorted(t for t in roots if 1e-13<t<1-1e-13)+[1.0]
        def prim(t):return a*t**3/3+b*t*t/2+c*t
        var+=sum(abs(prim(ts[k+1])-prim(ts[k])) for k in range(len(ts)-1))
    return var

def closed_gains(r):
    d=(r+2)*(3*r+2)
    v=(2*r+2-sqrt(9*r*r+18*r+12)/3)/(3*r+2)
    F=r*r*v*(1-v)*(3*r*(1-v)+4-2*v)/d
    return 1+2*F+4*r/(3*sqrt(3)*d),1+8/(3*sqrt(3)*r*(r+2))

random.seed(945)
for r in [0.04,0.2,0.5,1,1.2,1.42882553,2,6,30]:
    o,c=closed_gains(r)
    assert abs(spline_variation(r,[0,1,1,1])-o)<3e-10
    assert abs(spline_variation(r,[0,0,1,1])-c)<3e-10
    for _ in range(150):
        vals=[random.uniform(-2,2) for j in range(4)]
        vd=sum(abs(vals[j+1]-vals[j]) for j in range(3))
        assert spline_variation(r,vals)<=max(o,c)*vd+1e-9
print('ALL_SINGLE_JUMP_EXTREMIZERS_AND_GENERAL_DATA_STRESS_PASS',9*150)

rstar=1.4288255306294739
ostar,cstar=closed_gains(rstar)
assert abs(ostar-cstar)<1e-12
assert max(ostar,cstar)<max(closed_gains(1))
print('OPTIMAL_GAIN_AND_UNIFORM_MESH_COMPARISON_PASS',f'{ostar:.15f}',f'{max(closed_gains(1)):.15f}')
print('ALL_NATURAL_FOUR_KNOT_VARIATION_CHECKS_PASS')
