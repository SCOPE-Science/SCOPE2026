#!/usr/bin/env python3
"""Reproducible exact checks for a temporary two-diet excursion inverse."""
from fractions import Fraction as F
from itertools import combinations
import math


def recover(d1, d2, d3):
    """For real data: recover (u,v,contrast), with positive contrast."""
    R = d2 / d1
    S = d3 / d1
    disc = 4*S - 3*R*R
    if d1 <= 0 or disc <= 0:
        raise ValueError('invalid signed data or coincident time bounds')
    root = math.sqrt(float(disc))
    u, v = (float(R) + root)/2, (float(R) - root)/2
    if not (0 < v < u < 1):
        raise ValueError('infeasible excursion history')
    return u, v, float(d1)/root


def exact_recover(u, v, contrast):
    ds = [contrast*(u**i-v**i) for i in (1, 2, 3)]
    R = ds[1] / ds[0]
    S = ds[2] / ds[0]
    disc = 4*S - 3*R*R
    assert disc == (u-v)**2
    assert (R+(u-v))/2 == u
    assert (R-(u-v))/2 == v
    assert ds[0]/(u-v) == contrast
    return 1


def symbolic():
    import sympy as sp
    u, v, amp = sp.symbols('u v amp')
    ds = sp.Matrix([amp*(u**i-v**i) for i in (1,2,3)])
    det = sp.factor(ds.jacobian([amp,u,v]).det())
    assert det == -amp**2*(u-v)**4
    R = sp.factor(ds[1]/ds[0]); S = sp.factor(ds[2]/ds[0])
    assert sp.factor(4*S-3*R**2) == (u-v)**2
    return 2


def numeric_arbitrary_rates():
    # Diagnostics only; continuous injectivity is proved by sign changes and Chebyshev interpolation.
    from scipy.optimize import least_squares
    import numpy as np
    rates_list = [(0.35, 1.2, 4.4), (0.5, 1.0, 2.0), (0.6, 3.7, 3.8)]
    count = 0
    for rates in rates_list:
        rates = np.array(rates)
        for a,b,amp in [(0.2,1.8,0.7),(1.0,1.5,2.3),(.1,3,1.1),(.5,2,5)]:
            d=amp*(np.exp(-rates*a)-np.exp(-rates*b))
            for a0,b0,amp0 in [(a+.01,b+.02,amp*1.01),(.4,2,2.5)]:
                # parametrize b=a+e^z, amp=e^w, both positive
                x0=np.log([max(a0,1e-5),max(b0-a0,1e-5),amp0])
                def err(x):
                    aa, ell, c=np.exp(x)
                    return c*(np.exp(-rates*aa)-np.exp(-rates*(aa+ell)))-d
                res=least_squares(err,x0,xtol=1e-13,ftol=1e-13,gtol=1e-13,max_nfev=2000)
                aa, ell, c=np.exp(res.x)
                assert np.max(abs(err(res.x))) < 1e-8
                assert abs(aa-a) < 1e-5 and abs(aa+ell-b) < 1e-5 and abs(c-amp)<1e-5
                count+=1
    return count


def main():
    n = symbolic()
    values = [F(i, 20) for i in range(1,20)]
    for v,u in combinations(values,2):
        for amp in (F(1,5), F(5,3), F(11,2)):
            n+=exact_recover(u,v,amp)
    assert n == 2 + 171*3
    assert all(math.isclose(x, y, rel_tol=1e-12, abs_tol=1e-12) for x, y in zip(recover(3.,3.,63./25.), (0.8, 0.2, 5.0)))
    n+=1
    n+=numeric_arbitrary_rates()
    print(f'ISOTOPIC_THREE_TISSUE_OK assertions={n} symbolic=2 rational={171*3} nonlinear_numeric=24')

if __name__ == '__main__':
    main()
