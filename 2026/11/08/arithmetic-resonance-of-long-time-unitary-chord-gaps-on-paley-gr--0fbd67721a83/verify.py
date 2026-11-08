#!/usr/bin/env python3
"""Exact interval and finite-field checks for the Paley unitary-gap theorem.
No third-party packages. Run: python3 verify.py
"""
from fractions import Fraction as F
from math import isqrt, factorial, sin, pi

class Interval:
    def __init__(self, lo, hi=None):
        self.lo=F(lo); self.hi=F(lo if hi is None else hi)
        assert self.lo<=self.hi
    def __add__(self, other):
        other=other if isinstance(other,Interval) else Interval(other)
        return Interval(self.lo+other.lo,self.hi+other.hi)
    __radd__=__add__
    def __neg__(self):return Interval(-self.hi,-self.lo)
    def __sub__(self,other):return self+(-other if isinstance(other,Interval) else Interval(-other))
    def __rsub__(self,other):return Interval(other)-self
    def __mul__(self,other):
        other=other if isinstance(other,Interval) else Interval(other)
        xs=[self.lo*other.lo,self.lo*other.hi,self.hi*other.lo,self.hi*other.hi]
        return Interval(min(xs),max(xs))
    __rmul__=__mul__
    def __truediv__(self,other):
        other=other if isinstance(other,Interval) else Interval(other)
        assert other.lo*other.hi>0
        return self*Interval(1/other.hi,1/other.lo)
    def __rtruediv__(self,other):return Interval(other)/self
    def __repr__(self):return f'[{float(self.lo):.15g},{float(self.hi):.15g}]'

def atan_bounds(z,terms=70):
    z=F(z); s=sum(((-1)**k * z**(2*k+1)/F(2*k+1) for k in range(terms)),F(0))
    e=z**(2*terms+1)/F(2*terms+1)
    return Interval(s,s+e) if terms%2==0 else Interval(s-e,s)

def sqrt_bounds(n,decimal_places=70):
    den=10**decimal_places
    fl=isqrt(n*den*den)
    return Interval(F(fl,den),F(fl+1,den))

def cos_taylor(z,kmax):
    return sum(((-1)**k * z**(2*k)/factorial(2*k) for k in range(kmax+1)),F(0))

def cos_bounds(arg):
    # cos decreases on [0,pi], and the Taylor expansion alternates here.
    return Interval(cos_taylor(arg.hi,19),cos_taylor(arg.lo,20))

PI=16*atan_bounds(F(1,5))-4*atan_bounds(F(1,239))
assert F(3)<PI.lo and PI.hi<F(22,7)
SQ3=sqrt_bounds(3); SQ5=sqrt_bounds(5)
C3=12/PI-18*SQ3/(PI*PI)
R49=(101-15*SQ5-28*cos_bounds(PI/7)-28*cos_bounds(2*PI/7))/(12*PI)
R9=3/PI
assert R49.hi<C3.lo<C3.hi<R9.lo
print('Certified rational interval values:')
for name,v in [('non-square Paley',C3),('Paley 49',R49),('Paley 9',R9)]:
    print(name,repr(v),'width',float(v.hi-v.lo))

def nearest_chord_avg(gaps,samples=160000):
    a,b=gaps
    s=0.
    for j in range(samples):
        t=2*pi*(j+0.5)/samples
        s+=2*min(abs(sin(a*t/2)),abs(sin(b*t/2)),abs(sin((a+b)*t/2)))
    return s/samples

for gaps,target in [((1,1),R9),((1,3),R49)]:
    obs=nearest_chord_avg(gaps)
    assert abs(obs-float((target.lo+target.hi)/2))<0.000002,(gaps,obs)
    print('Direct period quadrature',gaps,format(obs,'.12f'))

def field_graph(p,d=None):
    if d is None:
        els=list(range(p))
        sub=lambda x,y:(x-y)%p
        mul=lambda x,y:(x*y)%p
    else:
        els=[(a,b) for a in range(p) for b in range(p)]
        sub=lambda x,y:((x[0]-y[0])%p,(x[1]-y[1])%p)
        mul=lambda x,y:((x[0]*y[0]+d*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
    zero=els[0]; squares={mul(z,z) for z in els if z!=zero}
    assert len(squares)==(len(els)-1)//2
    q=len(els); k=(q-1)//2; lam=(q-5)//4; mu=(q-1)//4
    adj=[[int(x!=y and sub(y,x) in squares) for y in els] for x in els]
    assert all(sum(row)==k for row in adj)
    for i in range(q):
        for j in range(i+1,q):
            assert adj[i][j]==adj[j][i]
            common=sum(adj[i][h]*adj[j][h] for h in range(q))
            assert common==(lam if adj[i][j] else mu)
    print(f'GF({q}) Paley graph checked: degree={k}, common neighbors={lam}/{mu}')

field_graph(5)
field_graph(3,2) # 2 is a quadratic nonresidue modulo 3
field_graph(7,3) # 3 is a quadratic nonresidue modulo 7
print('ALL_CHECKS_PASS')
