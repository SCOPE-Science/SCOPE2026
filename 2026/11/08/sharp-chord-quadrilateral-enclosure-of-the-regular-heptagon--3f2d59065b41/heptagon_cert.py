#!/usr/bin/env python3
"""Exact rational interval certificate for the minimum chord quadrilateral of a regular heptagon.
Run: python3 heptagon_cert.py  (Python standard library only).
"""
from fractions import Fraction as Q
from itertools import combinations

class Interval:
    def __init__(self, a, b=None):
        self.a = Q(a); self.b = Q(a if b is None else b)
        assert self.a <= self.b
    @staticmethod
    def wrap(other): return other if isinstance(other, Interval) else Interval(other)
    def __add__(self, other):
        o=self.wrap(other);return Interval(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return Interval(-self.b,-self.a)
    def __sub__(self,other):return self+-self.wrap(other)
    def __rsub__(self,other):return self.wrap(other)+-self
    def __mul__(self,other):
        o=self.wrap(other)
        z=[self.a*o.a,self.a*o.b,self.b*o.a,self.b*o.b]
        return Interval(min(z),max(z))
    __rmul__=__mul__
    def __truediv__(self,other):
        o=self.wrap(other);assert o.a*o.b>0
        return self*Interval(1/o.b,1/o.a)

# c = cos(pi/7) is the unique root of 8c^3 -4c^2 -4c +1 in (0.9,0.91).
# The enclosing rational endpoints are certified by opposite polynomial signs.
LOW=Q(9009688679024,10**13)
HIGH=Q(9009688679025,10**13)
f=lambda t:8*t**3-4*t**2-4*t+1
assert Q(9,10)<LOW<HIGH<Q(91,100)
assert f(LOW)<0<f(HIGH)
# f'(t)=24t^2-8t-4 is positive on [0.9,0.91] since f''(t)>0.
assert 24*Q(9,10)**2 - 8*Q(9,10) - 4 > 0
assert 48*Q(9,10)-8>0
x=Interval(LOW,HIGH)

def add(p,q):
    z=[Q(0)]*max(len(p),len(q))
    for i,v in enumerate(p):z[i]+=v
    for i,v in enumerate(q):z[i]+=v
    return trim(z)
def trim(p):
    while len(p)>1 and not p[-1]:p.pop()
    return p
def mul(p,q):
    z=[Q(0)]*(len(p)+len(q)-1)
    for i,v in enumerate(p):
        for j,w in enumerate(q):z[i+j]+=v*w
    return trim(z)
def neg(p):return [-v for v in p]
def sub(p,q):return add(p,neg(q))
def scalar(k,p):return [k*v for v in p]
def evalpoly(p,interval):
    out=Interval(0)
    for v in reversed(p):out=out*interval+v
    return out

def rem_f(p):
    p=p[:]
    while len(p)>=4:
        q=p[-1]/8
        k=len(p)-4
        for j,v in enumerate([Q(1),Q(-4),Q(-4),Q(8)]):p[k+j]-=q*v
        p=trim(p)
    return p

one=[Q(1)]; X=[Q(0),Q(1)]
# U_k(x)=sin((k+1)theta)/sin(theta), theta=pi/7.
U=[one,scalar(2,X)]
for m in range(2,14):U.append(sub(mul(scalar(2,X),U[-1]),U[-2]))
T=[one,X]
for m in range(2,7):T.append(sub(mul(scalar(2,X),T[-1]),T[-2]))
def S(m):return ([Q(0)] if m==0 else U[abs(m)-1] if m>0 else neg(U[abs(m)-1]))
def h(j):return X if j%2 else one

def area_scaled(ind):
    # Return 2*sin(pi/7) times the area of the four supporting half-plane intersection.
    ans=Interval(0)
    for i in range(4):
        a,b=ind[i],ind[(i+1)%4]
        d=(b-a)%14
        ha=evalpoly(h(a),x);hb=evalpoly(h(b),x)
        ca=evalpoly(T[d],x);su=evalpoly(U[d-1],x)
        assert su.a>0
        ans+=(2*ha*hb-(ha*ha+hb*hb)*ca)/su
    return ans

winner=(1,3,7,11)
ideal=area_scaled(winner)
count_bounded=0
count_optimizers=0
min_gap=None
min_positive_slack=None
zero_slacks=0
for ind in combinations(range(14),4):
    gaps=[(ind[(i+1)%4]-ind[i])%14 for i in range(4)]
    if max(gaps)>=7:continue
    count_bounded+=1
    # Prove all four consecutive line intersections meet all four halfspaces.
    # For endpoint normals a,b and another normal k, the slack times
    # sin((b-a)*pi/7)/sin(pi/7) is the polynomial below.
    for i in range(4):
        a=ind[i];b=a+gaps[i]
        for k0 in ind:
            if k0 in (a,b%14):continue
            k=k0 if k0>=a else k0+14
            numer=sub(sub(mul(h(k0),S(gaps[i])),mul(h(a),S(b-k))),mul(h(b%14),S(k-a)))
            reduced=rem_f(numer)
            if not any(reduced):
                zero_slacks+=1
                continue
            z=evalpoly(numer,x)
            assert z.a>0, ('vertex feasibility',ind,a,b,k0,str(z.a),str(z.b))
            if min_positive_slack is None or z.a<min_positive_slack:min_positive_slack=z.a
    A=area_scaled(ind)
    if all(k%2==1 for k in ind) and sorted(gaps)==[2,4,4,4]:
        count_optimizers+=1
        assert A.a<=ideal.b and A.b>=ideal.a
    else:
        gap=A.a-ideal.b
        assert gap>0, ('minimization',ind, float(gap))
        if min_gap is None or gap<min_gap:min_gap=gap

assert count_bounded==511
assert count_optimizers==7
assert zero_slacks==14
# Check the formula: the seven optimizers are four edge-supporting lines,
# with cyclic normal gaps (2,4,4,4); hence area is
# cos(pi/7)^2 * [tan(pi/7) + 3*tan(2*pi/7)].
print('HEPTAGON_CHORD_QUADRILATERAL_EXACT_OK',
      'bounded_four_line_sets',count_bounded,
      'optimizers',count_optimizers,
      'exact_zero_slacks',zero_slacks,
      'minimum_scaled_area_gap_gt',float(min_gap),
      'minimum_strict_slack_gt',float(min_positive_slack))
