#!/usr/bin/env python3
"""Exact rational diagnostics for a quartic invariant-square heteroclinic theorem.

The global return-map and periodic-orbit proofs are in RESULT.md. Finite checks
below verify algebraic boundary data and a concrete strict-rational witness.
"""
from fractions import Fraction as Q

def coeffs(lam, a, b, c, d, e):
    return (Q(lam),Q(a),Q(b),Q(c),Q(d),Q(e))

def P0(x,y,z):
    lam,a,b,c,d,e=z
    return lam*x-y+a*x*x+b*x*y-a*y*y

def R0(x,y,z):
    lam,a,b,c,d,e=z
    return x+lam*y+c*x*x+d*x*y+e*y*y

def jac_corner(x,y,z):
    # As the factors (1-x^2),(1-y^2) vanish at a corner, the
    # Jacobian there is diagonal; derivatives computed directly.
    return (-2*x*P0(x,y,z), -2*y*R0(x,y,z))

def rho(z):
    lam,a,b,c,d,e=z
    g=c+e
    numerator=((1+lam)**2-b*b)*((1+lam)**2-(g+d)**2)
    denominator=((1-lam)**2-b*b)*((1-lam)**2-(g-d)**2)
    return numerator/denominator

def strong_chamber(z):
    lam,a,b,c,d,e=z
    return abs(lam)+abs(a)+abs(b)<1 and abs(lam)+abs(c)+abs(d)+abs(e)<1

# The exact strict witness: lambda=-1/100,a=b=e=0,c=1/4,d=-1/4.
eps=Q(1,100); h=Q(1,4)
z=coeffs(-eps,0,0,h,-h,0)
assert strong_chamber(z)
assert rho(z)==Q(32019867,26185967)
assert rho(z)>1
# Stable/unstable eigenvalues in order bottom-right, top-right,
# top-left, bottom-left, with incoming stable before outgoing unstable.
lam,a,b,c,d,e=z
g=c+e
vertices=[
    ((1,-1), (2*(1+lam-b), 2*(1-lam+g-d))),
    ((1,1),  (2*(1+lam+g+d),2*(1-lam-b))),
    ((-1,1), (2*(1+lam+b),2*(1-lam-g+d))),
    ((-1,-1),(2*(1+lam-g-d),2*(1-lam+b))),
]
product=Q(1)
for (x,y),(sigma,mu) in vertices:
    dx,dy=jac_corner(x,y,z)
    assert sigma>0 and mu>0
    if (x,y)==(1,-1) or (x,y)==(-1,1):
        assert dx==-sigma and dy==mu
    else:
        assert dx==mu and dy==-sigma
    product*=sigma/mu
assert product==rho(z)
# Equilibrium: y=-eps*x and x*(1+eps^2+h*(1+eps)*x)=0.
x_other=-(1+eps*eps)/(h*(1+eps))
assert x_other<-1
assert (1-eps)**4/((1+eps)**2*((1+eps)**2-4*h*h))==rho(z)
assert 4*h*h*(1+eps)**2>8*eps*(1+eps*eps)
assert h<(1-eps)/2
# Contrast on the same prescribed slice below the characteristic threshold.
low=coeffs(-eps,0,0,Q(1,20),-Q(1,20),0)
assert strong_chamber(low)
assert rho(low)<1
# Vary all six parameters in a small rational coefficient cube and
# independently compare the four Jacobian diagonal values to table rates.
for i in range(125):
    ztest=coeffs(
        Q(((7*i+3)%17)-8,200), Q(((11*i+2)%17)-8,200),
        Q(((13*i+4)%17)-8,200), Q(((5*i+6)%17)-8,200),
        Q(((3*i+5)%17)-8,200), Q(((9*i+7)%17)-8,200))
    assert strong_chamber(ztest)
    ll,aa,bb,cc,dd,ee=ztest
    gg=cc+ee
    table=[
        ((1,-1), 2*(1+ll-bb), 2*(1-ll+gg-dd)),
        ((1,1),  2*(1+ll+gg+dd),2*(1-ll-bb)),
        ((-1,1), 2*(1+ll+bb),2*(1-ll-gg+dd)),
        ((-1,-1),2*(1+ll-gg-dd),2*(1-ll+bb)),
    ]
    rr=Q(1)
    for (xx,yy),sig,mu in table:
        jx,jy=jac_corner(xx,yy,ztest)
        assert sig>0 and mu>0
        if (xx,yy) in ((1,-1),(-1,1)):
            assert jx==-sig and jy==mu
        else:
            assert jx==mu and jy==-sig
        rr*=sig/mu
    assert rr==rho(ztest)
# Exact nonvanishing and orientation checks on a rational mesh
# corroborate (but do not replace) coefficient-wise analytic bounds.
for zz in (z,low):
  for i in range(-101,102):
    t=Q(i,101)
    assert P0(t,-1,zz)>0 and P0(t,1,zz)<0
    assert R0(1,t,zz)>0 and R0(-1,t,zz)<0
print('SQUARE_HETEROCLINIC_VERIFY_OK')
