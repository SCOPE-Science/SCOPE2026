#!/usr/bin/env python3
"""Standalone arithmetic and quadrature checks for quartic rigid-flow area laws.
The infinite-parameter theorem is proved analytically in RESULT.md.
"""
from fractions import Fraction
import math

def delta(theta, kind):
    s2 = math.sin(theta/2.0)**2
    if kind == 2:
        return 6.0*s2
    if kind == 4:
        return 4.0*s2*s2*(2.0+math.cos(theta))
    raise ValueError(kind)

def area(R, kind, panels=16000):
    # Even angular potential around its sole maximum, at 0 mod 2*pi.
    lo, hi = 0.0, math.pi
    for _ in range(90):
        mid = (lo+hi)/2
        if delta(mid, kind)<R**(-3):
            lo = mid
        else:
            hi = mid
    cutoff = hi
    # Integrate in log-angle coordinates to resolve singularly small caps.
    upper = math.log(math.pi/cutoff)
    step = upper/panels
    def g(u):
        theta = cutoff*math.exp(u)
        return theta*delta(theta,kind)**(-2.0/3)
    accum = g(0.0)+g(upper)
    for j in range(1,panels):
        accum += (4 if j%2 else 2)*g(j*step)
    return R*R*cutoff+(step/3)*accum

def main():
    # Exact factorization of the flattened potential in Q[cos(theta)].
    for numerator, denominator in [(k, 31) for k in range(-31,32)]:
        u=Fraction(numerator,denominator)
        assert 2-3*u+u**3 == (1-u)**2*(2+u)
    c2=Fraction(3,2)
    c4=Fraction(3,4)
    expected2=4/math.sqrt(float(c2))
    expected4=(8/5)*float(c4)**(-1/4)
    got2=area(1000.0,2)/1000**0.5
    got4=area(1000.0,4)/1000**1.25
    assert abs(got2-expected2)/expected2<0.02, (got2,expected2)
    assert abs(got4-expected4)/expected4<0.001, (got4,expected4)
    assert abs(delta(1e-3,2)/1e-6-float(c2))<2e-6
    assert abs(delta(1e-2,4)/1e-8-float(c4))<3e-5
    print('QUARTIC_RIGID_EXACT_POTENTIAL_FACTOR_OK cases=63')
    print('QUARTIC_RIGID_AREA_PHASE_CHECK_OK R=1000 exponents=1/2,5/4')
    print('normalized=%.9f,%.9f limits=%.9f,%.9f'%(got2,got4,expected2,expected4))
if __name__=='__main__':
    main()
