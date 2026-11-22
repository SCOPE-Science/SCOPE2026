#!/usr/bin/env python3
"""Independent arithmetic and vector checks for curvature of circular trefoils.

Python 3 standard library only. Numerical tests supplement, rather than replace,
the exact polynomial/Descartes proof in the accompanying result.
"""
import math
from fractions import Fraction as Q


def V(R,c):
    return 4*(R+c)**2 + 9

def N(R,c):
    u=R+c
    return V(R,c)*((9*c+4*u)**2+225*(1-c*c))-144*u*u*(1-c*c)

def F(R,c):
    return (80*c**5 -464*R*c**4 -(1792*R*R+864)*c**3
          -(1792*R**3+5508*R)*c*c
          -(464*R**4+5508*R*R+5508)*c
          +80*R**5-864*R**3-3321*R)

def squared_curvature(R,c):
    return N(R,c)/V(R,c)**3

def vector_curvature_squared(R,t):
    c=math.cos(3*t); s=math.sin(3*t); u=R+c
    # Orthogonal cylindrical coordinates of the velocity and acceleration.
    v=(-3*s,2*u,3*c)
    a=(-9*c-4*u,-12*s,-9*s)
    dot=lambda x,y:sum(xx*yy for xx,yy in zip(x,y))
    return (dot(v,v)*dot(a,a)-dot(v,a)**2)/dot(v,v)**3

def coeffs(z):
    return [
      2187-405*z+2916*z**2+864*z**4+80*z**5,
      5751-2025*z+8748*z**2+3456*z**3+3392*z**4+400*z**5,
      -10530-15714*z+5832*z**2+6656*z**3+4928*z**4+800*z**5,
      -44226-52866*z-20168*z**2-768*z**3+3072*z**4+800*z**5,
      -58617-72089*z-37420*z**2-7680*z**3+608*z**4+400*z**5,
      -25925-33317*z-17252*z**2-3712*z**3-64*z**4+80*z**5,
    ]

def bisect_root(fun,lo,hi,iterations=100):
    v=fun(lo)
    assert v*fun(hi)<0
    for _ in range(iterations):
        mid=(lo+hi)/2
        if fun(mid)*v>0:lo=mid;v=fun(mid)
        else:hi=mid
    return (lo+hi)/2

rstar=bisect_root(lambda R:20*R**3-156*R**2-417*R-484,10,11)
assert abs(rstar-10.1012691095328)<1e-11
for R in [1.01,1.3,2,3.25,5,8,10,10.2,20]:
  for t in [0.032,0.111,0.333,0.76,1.321,2.09]:
    c=math.cos(3*t)
    a=squared_curvature(R,c);b=vector_curvature_squared(R,t)
    assert math.isclose(a,b,rel_tol=4e-12,abs_tol=2e-13),(R,t,a,b)
  for c in [-.8,-.3,.15,.75]:
    h=1e-5
    numerical=(squared_curvature(R,c+h)-squared_curvature(R,c-h))/(2*h)
    analytic=8*F(R,c)/V(R,c)**4
    assert math.isclose(numerical,analytic,rel_tol=4e-8,abs_tol=1e-10),(R,c,numerical,analytic)

# Polynomial identity with exact rational arithmetic at rational test pairs.
for R in [Q(101,100),Q(3,2),Q(2),Q(5),Q(11)]:
    z=R-1
    for y in [Q(1,3),Q(1),Q(7,2),Q(5)]:
        cc=(y-1)/(y+1)
        lhs=(y+1)**5*F(R,cc)
        rhs=sum(g*y**i for i,g in enumerate(coeffs(z)))
        assert lhs==rhs,(R,y,lhs,rhs)

# Exact signs at disjoint intervals guarantee ordered unique positive roots
# of coefficients 2,3,4,5 (their shifted-polynomial coefficients have one sign change).
for i,lo,hi in [(2,Q(2),Q(5,2)),(3,Q(3),Q(4)),(4,Q(6),Q(7)),(5,Q(10),Q(11))]:
    assert coeffs(lo-1)[i]<0<coeffs(hi-1)[i]
for R in [Q(1),Q(7,5),Q(2),Q(3),Q(4),Q(6),Q(8),Q(10),Q(11),Q(20)]:
    a=coeffs(R-1)
    assert a[0]>0 and a[1]>0
    signs=[1 if x>0 else -1 for x in a]
    assert sum(x!=y for x,y in zip(signs,signs[1:]))<=1,(R,signs)

for R in [1.01,2,3.25,5,10]:
    assert F(R,-1)>0>F(R,1)
    cr=bisect_root(lambda c:F(R,c),-1,1)
    assert -1<cr<1
    # Sign changes from increasing to decreasing squared curvature.
    assert F(R,(cr-1)/2)>0>F(R,(cr+1)/2)
for R in [10.2,11,20]:
    assert F(R,-1)>0 and F(R,1)>0

# The inner equator has three zero-curvature points only at R = 13/4.
assert N(Q(13,4),Q(-1))==0
assert N(Q(13,4),Q(0))>0
assert N(Q(13,4),Q(1))>0

# At threshold, outer-equator curvature has a quartically flat maximum.
def Fr(R,c):
    return (-464*c**4-3584*R*c**3-(5376*R**2+5508)*c**2
            -(1856*R**3+11016*R)*c
            +400*R**4-2592*R**2-3321)
def Fc(R,c):
    return (400*c**4-1856*R*c**3-(5376*R*R+2592)*c*c
            -(3584*R**3+11016*R)*c
            -(464*R**4+5508*R*R+5508))
P=-Fr(rstar,1)/Fc(rstar,1)
assert P>0
split=math.sqrt(2*P)/3
for delta in [1e-2,1e-3,1e-4,1e-5]:
    R=rstar-delta
    cr=bisect_root(lambda c:F(R,c),-1,1)
    measured=math.acos(cr)/3/math.sqrt(delta)
    assert abs(measured/split-1)<0.03,(delta,measured,split)
print('TREFOIL_CURVATURE_VERTEX_BIFURCATION_CHECKS_OK')
print(f'R_star={rstar:.13f}, lambda_star={1/rstar:.13f}, split_coefficient={split:.13f}')
