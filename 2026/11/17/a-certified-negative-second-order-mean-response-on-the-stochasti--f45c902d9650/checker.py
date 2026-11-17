#!/usr/bin/env python3
"""Exact rational interval certificate for the small-parametric-noise coefficient."""
from fractions import Fraction as F

class I:
    def __init__(self,lo,hi=None):
        self.lo=F(lo); self.hi=F(lo if hi is None else hi)
        assert self.lo<=self.hi
    @staticmethod
    def cv(x): return x if isinstance(x,I) else I(x)
    def __add__(self,o):
        o=I.cv(o);return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+-I.cv(o)
    def __rsub__(self,o):return I.cv(o)+-self
    def __mul__(self,o):
        o=I.cv(o);z=[a*b for a in (self.lo,self.hi) for b in (o.lo,o.hi)];return I(min(z),max(z))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=I.cv(o); assert not(o.lo<=0<=o.hi),'zero denominator'
        return self*I(1/o.hi,1/o.lo)
    def __rtruediv__(self,o):return I.cv(o)/self
    def sq(self):
        if self.lo>=0:return I(self.lo*self.lo,self.hi*self.hi)
        if self.hi<=0:return I(self.hi*self.hi,self.lo*self.lo)
        return I(0,max(self.lo*self.lo,self.hi*self.hi))
    def within(self,a,b):return F(a)<self.lo and self.hi<F(b)
    def show(self):return tuple(float(x) for x in (self.lo,self.hi))

lam=F(7,2)
def f(x):return lam*x*(1-x)
lo=F(500884210307217,10**15);hi=F(500884210307219,10**15)
def iterate(x,n=4):
    for _ in range(n):x=f(x)
    return x
# sign change of f^4(x)-x across an interval, with 4th return derivative < 1.
assert iterate(lo)>lo and iterate(hi)<hi
x=[I(lo,hi)]
for _ in range(3):x.append(f(x[-1]))
a=[lam*(1-2*p) for p in x]
c=[p*(1-p) for p in x]
A=I(1)
for ai in a:A=A*ai
assert A.within(F(-31,1000),F(-30,1000)),A.show()

# v_(j+1)=a_j^2 v_j+c_j^2, normalized to Var(xi)=1
P=I(1)
for ai in a:P=P*ai.sq()
T=I(0)
for j in range(4):
    factor=I(1)
    for k in range(j+1,4):factor=factor*a[k].sq()
    T=T+c[j].sq()*factor
v=[T/(1-P)]
for i in range(3):v.append(a[i].sq()*v[-1]+c[i].sq())
# b_(j+1)=a_j b_j-lam*v_j
H=I(0)
for j in range(4):
    factor=I(1)
    for k in range(j+1,4):factor=factor*a[k]
    H=H+v[j]*factor
b=[-lam*H/(1-A)]
for i in range(3):b.append(a[i]*b[-1]-lam*v[i])
# noise xi uniform [-1,1], variance =1/3 and four phases average
B=sum(b,I(0))/12
assert B.within(F(-548,1000),F(-546,1000)),B.show()
assert all(0<c0.lo and c0.hi<1 for c0 in x)
print('CHECKED: f^4(x0)-x0 has opposite signs at rational interval ends')
print('CHECKED: 4-cycle multiplier lies in (-0.031,-0.030)')
print('CHECKED: variance/mean recursions yield -0.548 < coefficient < -0.546')
print('cycle',*[p.show() for p in x])
print('coefficient',B.show())
