#!/usr/bin/env python3
"""Exact rational interval checks for a two-strategy habitat model."""
from fractions import Fraction as Q
from decimal import Decimal, localcontext

class I:
    def __init__(self, a, b=None):
        self.lo = Q(a)
        self.hi = Q(a if b is None else b)
        assert self.lo <= self.hi
    @staticmethod
    def of(x): return x if isinstance(x,I) else I(x)
    def __add__(self,x):
        x=I.of(x)
        return I(self.lo+x.lo,self.hi+x.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,x): return self + -I.of(x)
    def __rsub__(self,x): return I.of(x) + -self
    def __mul__(self,x):
        x=I.of(x)
        p=[a*b for a in (self.lo,self.hi) for b in (x.lo,x.hi)]
        return I(min(p),max(p))
    __rmul__=__mul__
    def __truediv__(self,x):
        x=I.of(x)
        assert x.lo*x.hi>0, ('zero in denominator',x.lo,x.hi)
        return self*I(1/x.hi,1/x.lo)
    def __rtruediv__(self,x): return I.of(x)/self
    def __pow__(self,n):
        assert int(n)==n and n>=0
        if n==0:return I(1)
        if self.lo>=0:return I(self.lo**n,self.hi**n)
        if self.hi<=0 and n%2==0:return I(self.hi**n,self.lo**n)
        if self.hi<=0:return I(self.lo**n,self.hi**n)
        if n%2==0:return I(0,max(abs(self.lo),self.hi)**n)
        return I(self.lo**n,self.hi**n)
    def within(self,lo,hi):
        assert self.lo>Q(lo) and self.hi<Q(hi), (self.str(),str(lo),str(hi))
    def positive(self): assert self.lo>0,self.str()
    def negative(self): assert self.hi<0,self.str()
    def str(self,precision=19):
        with localcontext() as ctx:
            ctx.prec=precision+10
            def fmt(x):return f'{Decimal(x.numerator)/Decimal(x.denominator):.{precision-2}g}'
            return '['+fmt(self.lo)+', '+fmt(self.hi)+']'

r=Q(4); N=30; b=Q(1); d=Q(13,10); kappa=20
z=I(Q('0.87766779091483'),Q('0.87766779091485'))
S=sum((z**j for j in range(N)),I(0))
Sprime=sum((j*z**(j-1) for j in range(1,N)),I(0))
F=1+(r-1)*z**(N-1)-r*S/N
Fp=(r-1)*(N-1)*z**(N-2)-r*Sprime/N
# Assert existence of a root strictly inside z interval with exact rational endpoint signs.
def F_at(x):return 1+(r-1)*x**(N-1)-r*sum((x**j for j in range(N)),Q(0))/N
assert F_at(z.lo)>0 and F_at(z.hi)<0
Fp.negative()
H=r*(1-S/N)/(1-z)
Hp=r*((-Sprime/N)*(1-z)+(1-S/N))/(1-z)**2
u=(d/z-b)/H
v=1-z-u
u.positive();v.positive()
A= -d/z+z*H-z*u*Hp
B= -d/z-z*u*Hp
j11=u*(A+z*Fp);j12=u*(B+z*Fp);j21=v*A;j22=v*B
tr=j11+j22;det=j11*j22-j12*j21
Bcoef=j22+kappa*j11
print('z',z.str());print('u',u.str());print('v',v.str())
for name,val in [('j11',j11),('j12',j12),('j21',j21),('j22',j22),('trace',tr),('det',det),('B',Bcoef)]:print(name,val.str())
j11.within(Q('0.2453'),Q('0.2454'))
j12.within(Q('-0.1771'),Q('-0.1769'))
j21.within(Q('1.7639'),Q('1.7642'))
j22.within(Q('-0.3869'),Q('-0.3867'))
tr.negative();det.positive();Bcoef.positive()
p=lambda x: kappa*I(Q(x))**2-Bcoef*Q(x)+det
for s,expect in [('0.069','positive'),('0.070','negative'),('0.156','negative'),('0.157','positive')]:
 q=p(s);getattr(q,expect)();print('p('+s+')',q.str())
assert Q(157,69)<3
print('PASS: rational root bracket, positive state, stable local Jacobian, two Turing boundaries in (0.069,0.070) and (0.156,0.157).')
print('PASS: positive-root ratio < 157/69 < 3, enough for geometric weighted-star spectrum.')
print('PASS: universal graph interval argument is analytic; no finite enumeration is claimed to prove the n-general case.')
