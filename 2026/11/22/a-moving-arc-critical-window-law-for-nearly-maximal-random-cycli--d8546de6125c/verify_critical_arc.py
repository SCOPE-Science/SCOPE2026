#!/usr/bin/env python3
"""Independent numerical spot checks for the moving-arc triangle-area crossover.

Analytical proof is in RESULT.md. Requires scipy; checks are not a certificate
for continuum quantifiers or historical priority.
"""
from math import pi, sin, cos, sqrt, acos, isclose
from scipy.integrate import quad
from scipy.optimize import brentq

LC = 2*pi/3
A_STAR = 3*sqrt(3)/4
GAMMA = 3*sqrt(3)/16
BETA = sqrt(3)/4

def envelope(s):
    return sin(s/2)*(1-cos(s/2))

def profile(lam):
    q = 1+4*GAMMA*min(lam, 0)**2
    end = 2*lam+sqrt(q/GAMMA)
    start = max(0, 2*lam-sqrt(q/GAMMA))
    if end <= start:
        return 0.0
    integral = quad(lambda w: w*sqrt(max(0, q-GAMMA*(w-2*lam)**2)),
                    start, end, epsabs=1e-11, epsrel=1e-11, limit=200)[0]
    return 3*integral/(2*LC**3*sqrt(BETA))

def exact_probability(half_arc, deficit):
    """1D quadrature of exact 3D ordered-angle probability."""
    L=half_arc
    M=envelope(min(2*L, 4*pi/3))
    target=M-deficit
    peak=min(2*L, 4*pi/3)
    left=brentq(lambda s: envelope(s)-target, 1e-9, peak, xtol=1e-14)
    right=2*L
    if 2*L>4*pi/3 and envelope(2*L)<target:
        right=brentq(lambda s: envelope(s)-target, 4*pi/3, 2*L, xtol=1e-14)
    def integrand(s):
        threshold=cos(s/2)+target/sin(s/2)
        if threshold>=1:
            return 0.0
        return 2*(2*L-s)*acos(max(-1, threshold))
    breaks=[peak] if left<peak<right else None
    volume=quad(integrand,left,right,points=breaks,epsabs=1e-13,
                epsrel=1e-10,limit=250)[0]
    return 3*volume/(4*L**3)

def check():
    assert isclose(envelope(4*pi/3), A_STAR, rel_tol=1e-13)
    assert isclose(profile(0), 6*3**.25/pi**3, rel_tol=1e-10)
    for lam in [0.9, 2.0, 5.0]:
        assert isclose(profile(lam), 4*pi*lam/LC**3, rel_tol=5e-10)
    # Verify exact geometry against the sine-chord formula for three sample triples.
    for xyz in [(0.2,0.7,1.9),(-1.3,-0.4,1.5),(-2.0,-0.1,2.0)]:
        a,b,c=xyz
        s=c-a
        d=b-(a+c)/2
        area=0.5*(sin(b-a)+sin(c-b)-sin(c-a))
        assert isclose(area,sin(s/2)*(cos(d)-cos(s/2)),rel_tol=1e-12)
    # Independent direct 3-variable integration reduced exactly to a 1D quadrature.
    for lam in [-2.,-0.5,0.,0.5,1.,3.]:
        eps=1e-5
        p=exact_probability(LC+lam*sqrt(eps),eps)
        comparison=p/(eps**1.5)
        limit=profile(lam)
        assert limit>0
        assert abs(comparison/limit-1)<0.04, (lam, comparison, limit)
    for lam in [-100.,-300.]:
        asym=1/(40*LC**3*GAMMA**2*sqrt(BETA)*lam**2)
        assert abs(profile(lam)/asym-1)<0.04,(lam,profile(lam),asym)
    print('MOVING_ARC_AREA_CRITICAL_WINDOW_CHECKS_OK')

if __name__ == '__main__':
    check()
