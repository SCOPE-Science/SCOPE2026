#!/usr/bin/env python3
"""Independent numerical checks of flat Möbius-band boundary-distance formulas.

This standalone verifier uses only the Python standard library. Run:
    python3 verify_mobius.py
It checks deck-transformation minimization, the derived CDF and mean,
normalization, and inverse classification on representative widths.
"""
import math
import random


def exact_deck_distance(t, u, a, b):
    """Compute distance by the separate minimization over deck translates."""
    xt, yt = (t % a), (b if t < a else -b)
    xu, yu = (u % a), (b if u < a else -b)
    # A horizontal displacement greater than a cannot be shortest;
    # [-4,4] safely includes both parity-class minimizers.
    return min(math.hypot(xt - (xu + k*a), yt - ((-1)**k)*yu)
               for k in range(-4, 5))


def formula_distance(t, u, a, b):
    delta = abs(t-u)
    s = min(delta, 2*a-delta)
    return min(s, math.hypot(a-s, 2*b))


def cdf(r, a, b):
    if r <= 0:
        return 0.
    if b >= a/2:
        return min(r/a, 1.)
    critical = a/2+2*b*b/a
    if r < 2*b:
        return r/a
    if r < critical:
        return (r + math.sqrt(max(0.,r*r-4*b*b)))/a
    return 1.


def mean_formula(a, b):
    if b >= a/2:
        return a/2
    critical = a/2+2*b*b/a
    return critical/2 + 2*b*b/a*math.asinh((a-critical)/(2*b))


def midpoint_mean(a, b, n=100000):
    return sum(min((i+.5)*a/n, math.hypot(a-(i+.5)*a/n,2*b))
               for i in range(n))/n


def main():
    rng=random.Random(261103)
    total_pair_checks=0
    total_cdf_checks=0
    tested_cases=[(1.0,.035),(2.0,.25),(2.0,.7),(2.0,.999),(2.0,1.0),(2.0,1.3),(4.0,3.1)]
    for a,b in tested_cases:
        for _ in range(30000):
            t,u=(2*a*rng.random() for _ in range(2))
            d0=exact_deck_distance(t,u,a,b)
            d1=formula_distance(t,u,a,b)
            assert abs(d0-d1) < 4e-13 * max(1,a), (a,b,t,u,d0,d1)
            total_pair_checks+=1
        assert abs(midpoint_mean(a,b)-mean_formula(a,b))<2e-7 * max(1,a)
        cap=a/2+2*b*b/a if b<a/2 else a
        radii=sorted({.05*a,.15*a,.4*a,.7*a,2*b*.99,2*b*1.01,.9*cap,.99*cap,cap,1.01*cap})
        for r in radii:
            # Independent midpoint integration of distance in offset variable.
            n=25000
            freq=sum(formula_distance(0,(j+.5)*2*a/n,a,b)<=r for j in range(n))/n
            # Quadrature error is O(1/n) at jump boundaries.
            assert abs(freq-cdf(r,a,b))<1.3e-4,(a,b,r,freq,cdf(r,a,b))
            total_cdf_checks+=1
        assert cdf(0.,a,b)==0. and cdf(cap,a,b)==1.
        assert abs(cdf(.01*min(2*b,a),a,b)-.01*min(2*b,a)/a)<1e-14
        if b < a/2:
            recovered_b=.5*math.sqrt(a*(2*cap-a))
            assert abs(recovered_b-b)<1e-12*max(1,a)
        else:
            # All wide bands have the same full boundary-distance kernel.
            for s in [0,a/8,a/4,a/2,3*a/4,a]:
                assert formula_distance(0,s,a,b)==s
    print('MOBIUS_BOUNDARY_LAW_OK', 'deck_pairs='+str(total_pair_checks),
          'independent_cdf_checks='+str(total_cdf_checks),
          'mean_quadratures='+str(len(tested_cases)),
          'inverse_checks='+str(len(tested_cases)))

if __name__=='__main__':
    main()
