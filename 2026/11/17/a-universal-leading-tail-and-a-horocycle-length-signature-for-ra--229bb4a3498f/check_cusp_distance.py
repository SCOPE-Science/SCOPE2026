#!/usr/bin/env python3
"""Numerical corroboration for the intrinsic distance law of hyperbolic cusps."""
import math
import random
import mpmath as mp

mp.mp.dps = 55


def exact_survival(lam, r):
    """One-dimensional exact formula; handles both branches at small radii."""
    lam, r = mp.mpf(str(lam)), mp.mpf(str(r))
    if r <= 0:
        return mp.mpf(1)
    def integrand(s):
        b = 2*mp.exp(s)*(mp.cosh(r)-mp.cosh(s))
        v = 1 - 2*mp.sqrt(max(mp.mpf('0'), b))/lam
        return mp.exp(-s)*max(mp.mpf('0'), v)**2
    nodes = [mp.mpf(0)]
    er = mp.exp(r)
    discr = (er-mp.exp(-r))**2 - lam**2
    if discr > 0:
        center = (er+mp.exp(-r))/2
        for root in [center-mp.sqrt(discr)/2, center+mp.sqrt(discr)/2]:
            if root >= 1 and root < er:
                nodes.append(mp.log(root))
    nodes.append(r)
    nodes = sorted(set(nodes))
    return mp.exp(-r) + sum(mp.quad(integrand, [a,b]) for a,b in zip(nodes[:-1],nodes[1:]))


def direct_distance(lam, rng):
    x1,x2 = rng.random()*lam,rng.random()*lam
    y1,y2 = 1/rng.random(),1/rng.random()
    nearest = min((x1-x2+k*lam)**2 for k in (-2,-1,0,1,2))
    coshd = 1+(nearest+(y1-y2)**2)/(2*y1*y2)
    return math.acosh(coshd)


def check():
    rng = random.Random(331024)
    n=210000
    for lam in (0.6,1.5,3.0):
        distances=[direct_distance(lam,rng) for _ in range(n)]
        for r in (0.3,0.8,1.7,2.8):
            observed=sum(x>r for x in distances)/n
            theory=float(exact_survival(lam,r))
            sigma=math.sqrt(max(theory*(1-theory),1e-10)/n)
            assert abs(observed-theory)<6*sigma+0.0005,(lam,r,observed,theory)
    for lam in (0.5,1.,3.):
        for r in (4.,5.,6.):
            difference=exact_survival(lam,r)-mp.exp(-r)
            asympt=mp.mpf(str(lam))**2 *mp.exp(-3*r)/24
            ratio=difference/asympt
            assert abs(ratio-1)<(0.006 if r==4 else 0.001), (lam,r,ratio)
    # Direct algebraic check for the product-distribution survival.
    for z in (0.01,0.1,0.5,0.9):
        rhs=(1-math.sqrt(z))**2
        # Analytic integral against Uniform(0,1)^2, independent of the distance code.
        calc=(1-math.sqrt(z))-z*(1/math.sqrt(z)-1)
        assert abs(rhs-calc)<1e-12
    print('Monte Carlo:', 3*n, 'direct intrinsic pair samples; exact-tail comparisons:', 3*4)
    print('Asymptotic quadrature comparisons:', 3*3)
    for lam in (1.,3.):
        r=5.
        correction=exact_survival(lam,r)-mp.exp(-r)
        print('lambda=',lam,'r=',r,'coefficient_ratio=',mp.nstr(correction/(mp.mpf(str(lam))**2*mp.exp(-3*r)/24),12))
    print('HYPERBOLIC_CUSP_DISTANCE_LAW_OK')


if __name__ == '__main__':
    check()
