#!/usr/bin/env python3
"""Rational interval witness and killed Green-kernel diagnostic for a Brownian reset model.
All arithmetic establishing the strict witness inequality is exact Fraction arithmetic.
"""
from fractions import Fraction as F
import math

class I:
    def __init__(self, low, high=None):
        self.lo=F(low); self.hi=F(low if high is None else high)
        assert self.lo<=self.hi
    def __add__(self,o):
        o=o if isinstance(o,I) else I(o)
        return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o):
        o=o if isinstance(o,I) else I(o)
        return self+(-o)
    def __rsub__(self,o): return I(o)+(-self)
    def __mul__(self,o):
        o=o if isinstance(o,I) else I(o)
        z=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return I(min(z),max(z))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=o if isinstance(o,I) else I(o)
        assert o.lo>0 or o.hi<0
        return self*I(F(1,o.hi),F(1,o.lo))
    def __repr__(self): return '[%.17g, %.17g]'%(float(self.lo),float(self.hi))

def exp_pos_bounds(x,N=100):
    x=F(x); assert 0<=x<N+2
    v=F(1); total=v
    for k in range(1,N+1):
        v=v*x/k; total+=v
    first=v*x/F(N+1)
    tail_ub=first/(1-x/F(N+2))
    return I(total,total+tail_ub)

def sinh_bounds(x):
    e=exp_pos_bounds(x)
    # e^-x is the reciprocal of e^x
    return (e-I(F(1,e.hi),F(1,e.lo)))/2

def mean_intervals(u,k,A):
    u=F(u);k=F(k);A=F(A)
    s1=sinh_bounds(k*u);s2=sinh_bounds(k*(1-u)); s=s1+s2
    big=sinh_bounds(k)
    explore=(big-s)/(k*k*s)
    distance=(2*s1*s2-k*(u*s2+(1-u)*s1))/(k*s)
    return explore,distance,explore+distance/A

u=F(1,100);A=F(3);k=F(10)
E,Delta,T=mean_intervals(u,k,A)
baseline=u*(1-u)/2
assert T.hi<baseline, (T,baseline)
# Green-kernel r=0 coefficient: exact elementary polynomial.
weak=u*(u-1)*(A*(5*u*u-5*u+1)-8*u*u+8*u-4)/(24*A)
assert weak==F(117623,800000000)>0
assert F(4392,1000000)<T.lo<T.hi<F(4394,1000000)
print('PASS: interval mean',T,'<',float(baseline))
print('PASS: initial derivative =',weak,'=',float(weak))

# Diagnostic independent quadrature of Brownian killed resolvent, not proof.
def simpson(f,a,b,n=12000):
    assert n%2==0
    h=(b-a)/n
    sm=f(a)+f(b)
    for j in range(1,n): sm+=(4 if j%2 else 2)*f(a+j*h)
    return sm*h/3

def green(x,y,k):
    return math.sinh(k*min(x,y))*math.sinh(k*(1-max(x,y)))/(k*math.sinh(k))

def closed_delta(x,k):
    a=math.sinh(k*x);b=math.sinh(k*(1-x));s=a+b
    return (2*a*b-k*(x*b+(1-x)*a))/(k*s)

for x,k in ((.01,10.0),(.2,1.5),(.33,3.2),(.45,8.0),(.05,.8)):
    p=(math.sinh(k*x)+math.sinh(k*(1-x)))/math.sinh(k)
    numerical=k*k*(simpson(lambda y: green(x,y,k)*(x-y),0,x)+simpson(lambda y: green(x,y,k)*(y-x),x,1))/p
    formula=closed_delta(x,k)
    assert abs(numerical-formula)<1e-10,(x,k,numerical,formula)
print('PASS: five independent Green-kernel quadratures')
