"""Exact and numerical checks for the sharp lower fourth-moment resonance law.

Run with Python 3.9+; no third-party dependencies.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product
from math import cos, pi

# Integer-coefficient bivariate polynomials in (t,r), as (degree_t, degree_r).
def mon(i, j, c=1):
    return {(i, j): Q(c)}
def add(*ps):
    out = defaultdict(Q)
    for p in ps:
        for k, v in p.items():
            out[k] += v
    return {k: v for k, v in out.items() if v}
def mul(*ps):
    out = {(0, 0): Q(1)}
    for p in ps:
        nxt = defaultdict(Q)
        for (a,b),v in out.items():
            for (c,d),w in p.items():
                nxt[(a+c,b+d)] += v*w
        out = {k:v for k,v in nxt.items() if v}
    return out
def neg(p):
    return {k:-v for k,v in p.items()}
def sub(a,b):
    return add(a, neg(b))
def scaled(p, c):
    return {k: v*c for k,v in p.items()}
T, R, ONE = mon(1,0), mon(0,1), mon(0,0)
T2, R2 = mul(T,T), mul(R,R)
T4, R4 = mul(T2,T2), mul(R2,R2)
# A(z) = 2*[(3/2)(1+z^4)+6 z^2-2z], B(z)=(1+z^2)^2.
AT = add(scaled(add(ONE,T4),3), scaled(T2,12), scaled(T,-4))
AR = add(scaled(add(ONE,R4),3), scaled(R2,12), scaled(R,-4))
BT = mul(add(ONE,T2),add(ONE,T2))
BR = mul(add(ONE,R2),add(ONE,R2))
G = add(scaled(mul(R2,R),3),scaled(R2,-3),scaled(R,-3),ONE)
# P_r(t)=r(2-3r)t^2+(2-6r-2r^2)t+3+6r-6r^2.
PP = add(mul(add(scaled(R,2),scaled(R2,-3)),T2),
         mul(add(scaled(ONE,2),scaled(R,-6),scaled(R2,-2)),T),
         scaled(ONE,3),scaled(R,6),scaled(R2,-6))
# Algebraic certificate: f_-(t)-f_-(r)=(t-r)^2 P/(BT BR)
# whenever G(r)=0. Before specialization the residual is
# -2 (t-r) G(r) (1+t^2) / (BT BR).
left = sub(mul(AT,BR),mul(AR,BT))
right = add(scaled(mul(mul(sub(T,R),sub(T,R)),PP),2),
            scaled(mul(sub(T,R),G,add(ONE,T2)),-4))
assert left == right, (len(left),len(right))
print('EXACT_BIVARIATE_ALGEBRAIC_STABILITY_CERTIFICATE_OK',len(left))

# An independent exact integral: f=Re(u e^{imt}+v e^{int}), rational
# real amplitudes are sufficient to test the resonance coefficient and
# each generic fourth-order zero-sum relation (not an infinite proof).
def moment4(m,n,a,b):
    c = {m:Q(a,2),-m:Q(a,2),n:Q(b,2),-n:Q(b,2)}
    return sum((c[x]*c[y]*c[z]*c[w] for x,y,z,w in product(c,repeat=4)
                if x+y+z+w==0),Q(0))
for m in range(1,19):
    for n in range(m+1,27):
        for a,b in ((1,1),(1,2),(2,-3),(4,0),(0,5)):
            lhs=moment4(m,n,a,b)
            rhs=Q(3,8)*(a**4+b**4)+Q(3,2)*a*a*b*b
            if n==3*m:rhs+=Q(1,2)*a*a*a*b
            assert lhs==rhs,(m,n,a,b,lhs,rhs)
print('EXACT_FOURIER_ZERO_SUM_FOURTH_MOMENTS_OK',sum(26-m for m in range(1,19))*5)

# Bisection isolates the root in (1/4,3/10); exact rational signs
# of the cubic guarantee isolation and the signs for P's coefficients.
def cub(q):return 3*q**3-3*q**2-3*q+1
lo,hi=Q(1,4),Q(3,10)
assert cub(lo)>0 and cub(hi)<0
for _ in range(160):
    md=(lo+hi)/2
    if cub(md)>0:lo=md
    else:hi=md
r=float((lo+hi)/2)
kappa=1.5+(3*r*r-2*r)/(1+r*r)**2
assert 1.2206918950 < kappa < 1.2206918951
assert r*(2-3*r)>0 and 2-6*r-2*r*r>0 and 3+6*r-6*r*r>0
p=lambda x:r*(2-3*r)*x*x+(2-6*r-2*r*r)*x+3+6*r-6*r*r
for x in (0,.03,.1,.277648275535624,.8,1.1,2.7,40):
    fm=1.5+(3*x*x-2*x)/(1+x*x)**2
    rem=(x-r)**2*p(x)/((1+x*x)**2*(1+r*r)**2)
    assert abs(fm-kappa-rem)<1e-10
assert abs(208*kappa**3-1224*kappa*kappa+2268*kappa-1323)<1e-7
print('SHARP_ALGEBRAIC_ENDPOINT_AND_POSITIVE_STABILITY_OK',format(r,'.15f'),format(kappa,'.15f'))

# A completely separate sampled quadrature of both resonant and generic waves.
N=32768
for m,n,a,b,phi in ((1,3,1,-r,0),(1,3,1,r,0),(1,3,1,2,.71),(1,2,2,3,0),(2,5,1,2,.3),(2,6,1,-r,0)):
    xs=[a*cos(m*2*pi*j/N)+b*cos(n*2*pi*j/N+phi) for j in range(N)]
    m2=sum(x*x for x in xs)/N
    m4=sum(x**4 for x in xs)/N
    target=Q(3,8)*(a**4+b**4)+Q(3,2)*a*a*b*b
    if n==3*m:target+=.5*a**3*b*cos(phi)
    assert abs(m4-float(target))<1e-11
    assert abs(m2-(a*a+b*b)/2)<1e-11
print('INDEPENDENT_QUADRATURE_CONSISTENCY_OK 6')
print('ALL_TWO_TONE_REVERSE_FOURTH_MOMENT_CHECKS_OK')
