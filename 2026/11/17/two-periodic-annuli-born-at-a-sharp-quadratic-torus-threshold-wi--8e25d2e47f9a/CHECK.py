"""Standalone elementary consistency tests for the toroidal quadratic-flow theorem.
Only standard Python is required; numerical quadrature is corroboration, not proof.
"""
from fractions import Fraction
from math import sqrt, pi, sin, cos, isclose

# Exact rational witness: a=2, R=1, |d|=2, s=4, eta^2=4.
s = Fraction(4)
e = Fraction(4)
D = 1 - 4 * e * (s - e)
u0 = -1 / (2 * e)
h = Fraction(1, 8)
u_minus, u_plus = u0-h, u0+h
assert D == 1
assert u0 == Fraction(-1, 8)
assert (u_minus, u_plus) == (Fraction(-1, 4), Fraction(0))
def F(u):
    return e * (1-u*u) - s - u
assert F(u_minus) == F(u_plus) == 0
assert F(u0) == Fraction(1, 16)
assert F(Fraction(-1)) < 0 and F(Fraction(1)) < 0
assert F(Fraction(-1, 10)) > 0

def simpson(f, low, high, n=4096):
    step=(high-low)/n
    total=f(low)+f(high)
    for j in range(1,n):
        total+=(4 if j%2 else 2)*f(low+j*step)
    return total*step/3

def J(s,u):
    return sqrt((s+u)*u*u+(1-u*u)/4)

def measured(a, delta):
    S=a*a
    t=sqrt(S*S-1)
    est=(S+t)/2
    eta=sqrt(est+delta)
    discr=1-4*eta*eta*(S-eta*eta)
    mid=-1/(2*eta*eta)
    width=sqrt(discr)/(2*eta*eta)
    def w(phi):
        u=mid+width*sin(phi)
        return J(S,u)/sqrt(1-u*u)
    area=4*pi*width*simpson(lambda phi:w(phi)*cos(phi),-pi/2,pi/2)
    weighted=8*pi*pi/eta*simpson(w,-pi/2,pi/2)
    ust=-S+t
    vs=sqrt(1-ust*ust)
    jc=J(S,ust)
    area_coeff=8*pi*jc/sqrt(est)
    weighted_limit=8*pi**3*jc/(sqrt(est)*vs)
    # Weighted latitude expectation of xi and xi^2.
    den=simpson(w,-pi/2,pi/2)
    first=simpson(lambda phi:w(phi)*sin(phi),-pi/2,pi/2)/den
    second=simpson(lambda phi:w(phi)*sin(phi)**2,-pi/2,pi/2)/den
    return area/sqrt(delta),area_coeff,weighted,weighted_limit,first,second

for delta in (1e-3,1e-4):
    ac,acl,w,wl,m1,m2=measured(2.0,delta)
    assert abs(ac/acl-1)<2e-3,(delta,ac,acl)
    assert abs(w/wl-1)<2e-3,(delta,w,wl)
    assert abs(m1)<0.45*sqrt(delta),(delta,m1)
    assert abs(m2-0.5)<0.2*sqrt(delta),(delta,m2)
print('QUADRATIC_TORUS_TWO_BANDS_AND_ARCSINE_CHECK_OK')
