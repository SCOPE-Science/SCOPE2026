#!/usr/bin/env python3
"""Independent arithmetic and illustrative quadrature for a Gaussian-radial law.
Run: python verify.py. Requires Python 3.10+; optional illustrative quadrature uses SciPy and NumPy.
All infinite-dimensional statements need the paper's analytic bounds, not this finite checker.
"""
from fractions import Fraction
from math import prod

def chi_moment(df, power):
    """Integer raw moments of chi-square(df) for nonnegative integer power."""
    return prod(df + 2*j for j in range(power))

def critical_second_moment(d):
    # E[U^2 (U+W-d-2)^2] with U=chi_1^2 and W=chi_{d-1}^2.
    u=lambda p: chi_moment(1,p)
    w=lambda p: chi_moment(d-1,p)
    return (u(4) + 2*u(3)*w(1)+u(2)*w(2)
            -2*(d+2)*(u(3)+u(2)*w(1))+(d+2)**2*u(2))

for d in range(2,501):
    assert critical_second_moment(d) == 6*(d+6)
    eta=Fraction(2,d+2)
    EY= -2*eta + (d+2)*eta**2
    assert EY == 0
    EY2=eta**4*critical_second_moment(d)
    assert EY2 == Fraction(96*(d+6),(d+2)**4)

# A small optional deterministic generalized-Gauss-Laguerre integration sanity test.
try:
    import numpy as np
    from scipy.special import roots_genlaguerre, gamma
    from scipy.optimize import brentq
except ImportError:
    print('Exact integer/rational tests passed; optional SciPy quadrature unavailable.')
else:
    for d in (20,40,80,160):
        x,wx=roots_genlaguerre(95,-.5)
        y,wy=roots_genlaguerre(95,(d-3)/2)
        U=2*x[:,None]
        T=U+2*y[None,:]
        weights=wx[:,None]*wy[None,:]/(gamma(.5)*gamma((d-1)/2))
        def elog(s):
            F=1+s*U*(s*T-2)
            assert np.all(F>0)
            return float(np.sum(weights*np.log(F)))
        c=2/(d+2)
        assert elog(c)<0
        assert elog(c+30/d**3)>0
        root=brentq(elog,c,c+100/d**3)
        assert 0 < d**3*(root-c)<40
        print(f'd={d}: scaled local root offset {d**3*(root-c):.6f}')
    print('Exact checks and illustrative quadrature passed.')
