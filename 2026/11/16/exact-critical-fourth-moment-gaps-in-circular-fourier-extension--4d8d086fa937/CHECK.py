"""Finite consistency checks for the critical circular Bessel moment identities.

Requires scipy and Python 3. Numerical quadrature is not an infinite proof.
"""
import math
from fractions import Fraction
from scipy.integrate import quad
from scipy.special import jv


def odd_harmonic(n):
    return sum((Fraction(1, 2*j-1) for j in range(1, n+1)), Fraction(0))

checks=0
for n in range(1, 7):
    exact=float(odd_harmonic(n))/(n*n*math.pi**2)
    # Two independent integrals: positive radial Bessel and oscillating logarithmic-angle.
    t_rad=quad(lambda r: jv(n,r)**4/r if r else 0.0,0,1600,epsabs=2e-9,limit=3000)[0]
    t_ang=-2/(n*math.pi**2)*quad(lambda theta: math.sin(4*n*theta)*math.log(math.sin(theta)) if theta>0 else 0.0,0,math.pi/2,epsabs=1e-11)[0]
    assert abs(t_rad-exact)<6e-8, (n,t_rad,exact)
    assert abs(t_ang-exact)<1e-9, (n,t_ang,exact)
    checks+=2
for j in range(1, 6):
    exact=2/(math.pi**2*(2*j-1))
    for R in (400, 800, 1600):
        partial=quad(lambda r:r*(jv(j-1,r)**4-jv(j,r)**4),0,R,epsabs=2e-8,limit=4000)[0]
        assert abs(partial-exact)<1.0/R, (j,R,partial,exact)
        checks+=1
for m in range(4):
    for n in range(m+1, 7):
        s=sum(Fraction(1,2*j-1) for j in range(m+1,n+1))
        assert s==odd_harmonic(n)-odd_harmonic(m)
        checks+=1
print('PASS:',checks,'finite checks (not an infinite proof)')
