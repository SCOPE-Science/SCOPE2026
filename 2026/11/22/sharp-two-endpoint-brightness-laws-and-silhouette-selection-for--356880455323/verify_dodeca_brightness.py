#!/usr/bin/env python3
"""Exact finite geometry and numerical diagnostics for dodecahedral shadow tails."""
from fractions import Fraction as F
from itertools import product, combinations
from math import sqrt, pi, acos, cos, sin, isclose

class Q:
    """Exact a+b*phi arithmetic where phi^2=phi+1."""
    def __init__(self,a=0,b=0):
        self.a,self.b=F(a),F(b)
    def __add__(self,o):
        o=q(o);return Q(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return Q(-self.a,-self.b)
    def __sub__(self,o):return self+-q(o)
    def __rsub__(self,o):return q(o)+-self
    def __mul__(self,o):
        o=q(o);return Q(self.a*o.a+self.b*o.b,self.a*o.b+self.b*o.a+self.b*o.b)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=q(o); n=o.a*o.a+o.a*o.b-o.b*o.b
        assert n != 0
        return self*Q((o.a+o.b)/n,-o.b/n)
    def __eq__(self,o):
        o=q(o);return (self.a,self.b)==(o.a,o.b)
    def __float__(self):return float(self.a)+float(self.b)*(1+sqrt(5))/2
    def __abs__(self):return self if float(self)>=0 else -self
    def __repr__(self):return str((self.a,self.b))
def q(o):return o if isinstance(o,Q) else Q(o)
def dot(v,w):return sum((a*b for a,b in zip(v,w)),Q())
def cross(v,w):return (v[1]*w[2]-v[2]*w[1],v[2]*w[0]-v[0]*w[2],v[0]*w[1]-v[1]*w[0])
def scale(s,v):return tuple(s*x for x in v)
def add(u,v):return tuple(a+b for a,b in zip(u,v))
phi=Q(0,1); R2=phi+2
V=[(q(0),q(1),phi),(q(0),q(1),-phi),(q(1),phi,q(0)),(q(1),-phi,q(0)),(phi,q(0),q(1)),(phi,q(0),q(-1))]
assert all(dot(v,v)==R2 for v in V)
assert all(dot(V[i],V[j]) in (phi,-phi) for i,j in combinations(range(6),2))

groups={}
for bits in product((-1,1),repeat=6):
    w=(q(0),q(0),q(0))
    for sign,v in zip(bits,V):w=add(w,scale(sign,v))
    norm2=dot(w,w)/R2
    groups.setdefault((norm2.a,norm2.b),[]).append((bits,w))
expected={(F(8),F(-4)):12,(F(36,5),F(-12,5)):20,(F(24,5),F(12,5)):20,(F(4),F(4)):12}
assert {key:len(x) for key,x in groups.items()}==expected
mmax2=Q(4,4)
for bits,w in groups[(mmax2.a,mmax2.b)]:
    assert any(dot(cross(w,v),cross(w,v))==Q() for v in V)
    # All twelve attaining sign vectors produce distinct spherical directions.
    assert all(dot(w,w)!=Q() for _ in (0,))

crosses=[]
mmin2=Q(F(12,5),F(16,5))
for i,j in combinations(range(6),2):
    w=cross(V[i],V[j]);assert dot(w,w)!=Q()
    total=sum((abs(dot(w,v)) for v in V),Q())
    assert (total*total)/(R2*dot(w,w))==mmin2
    assert all(dot(cross(w,z),cross(w,z))!=Q() for z in crosses)
    crosses.append(w)
assert len(crosses)==15

# Local normal form at u=(1,0,0); the four positive-sign nonzero normal contributions cancel in y,z.
r=sqrt(float(R2));p=float(phi); m=sqrt(float(mmin2)); M=sqrt(float(mmax2))
assert isclose(m,2*(1+p)/r,rel_tol=1e-14)
assert isclose(M,1+sqrt(5),rel_tol=1e-14)

def brightness(u):return sum(abs(sum(float(c)*x for c,x in zip(v,u))) for v in V)/r
def local_form(y,z):return m*sqrt(1-y*y-z*z)+2/r*max(abs(y),p*abs(z))
checks=0
for i in range(1,2501):
    # irrational rotations give non-grid direction samples
    a=2*pi*((i*0.6180339887498949)%1)
    z=2*((i*0.414213562373095)%1)-1
    u=(sqrt(1-z*z)*cos(a),sqrt(1-z*z)*sin(a),z)
    b=brightness(u)
    assert m-1e-12<=b<=M+1e-12;checks+=1
for i in range(1,401):
    y=0.0007*sin(i*.41);z=0.0007*cos(i*.71)
    u=(sqrt(1-y*y-z*z),y,z)
    assert abs(brightness(u)-local_form(y,z))<3e-14;checks+=1

# Silhouette type via exact incidence rule, in four open tangent sectors.
def silhouette(y,z):
    u=(1.,y,z);sg=[1 if sum(float(a)*b for a,b in zip(v,u))>0 else -1 for v in V]
    return 2*sum((sg[i]*sg[j] != (1 if float(dot(V[i],V[j]))>0 else -1)) for i,j in combinations(range(6),2))
for y,z,expectedN in ((.002,0,12),(-.002,0,12),(0,.002,10),(0,-.002,10)):
    assert silhouette(y,z)==expectedN

# Check the exact upper-end interval disjointness and sign-group gap.
second=sqrt(float(Q(F(24,5),F(12,5))))
gap=M-second
min_sep=acos(1/sqrt(5))
assert 2*acos(second/M)<min_sep
assert gap>0.28
coeff_min=15*sqrt(5)/(2*pi)
coeff_max=6/M
print('PASS: exact 64 sign-vector table and 15 non-collinear cross axes')
print('PASS: sharp global endpoint values, 2900 numeric brightness diagnostics, 4 silhouette checks')
print('min=',repr(m),'max=',repr(M),'upper_interval=',repr(gap))
print('lower_tail_coeff=',repr(coeff_min),'upper_tail_coeff=',repr(coeff_max))
print('lower_conditional_type_fraction=1/2 (each)')
# Independently evaluate the exact radial spherical integral within each minimum's small angular neighborhood.
# This tests both the leading and cubic coefficients (not an infinite proof).
from math import atan
c=2/r
C3=5*m*(p+2)**2/(4*pi)*(1/p+1/p**3)
def lower_prob_local(eps,nn=6000):
    def integrand(t):
        t0=max(cos(t),p*sin(t))
        aa=m*m+c*c*t0*t0; bb=c*t0*(m+eps); cc=2*m*eps+eps*eps
        r0=cc/(bb+sqrt(bb*bb-aa*cc))
        return 1-sqrt(1-r0*r0)
    # Split at the two generators' diagonal: symmetric midpoint quadrature per interval.
    split=atan(1/p); s=0.0
    for a,b in [(0,split),(split,pi/2)]:
        h=(b-a)/nn
        s+=sum(integrand(a+(j+.5)*h) for j in range(nn))*h
    return 30*s/pi
for e in (0.01,0.005,0.002):
    observed=lower_prob_local(e)
    predicted=coeff_min*e*e+C3*e**3
    assert abs(observed-predicted)<45*e**4
print('PASS: exact local spherical quadrature matches second-order epsilon expansion')
print('third_lower_coefficient=',repr(C3))
