"""Numerical independent checks for shortest-path crossing of the core of a flat Möbius band.

Usage: python verify_core_crossing.py
Requires numpy and scipy; the mathematical derivation is in RESULT.md.
"""
import math
import numpy as np
from scipy.integrate import quad


def closed_probability(w):
    assert w > 0
    if w <= 1.0:
        return 0.5 - w*w/8.0
    return (4.0*math.log(w) + 3.0)/(8.0*w*w)


def integral_probability(w):
    a = w*w/4.0
    upper = min(a, .25)
    # Set q=upper*s^2 to make the log integrable with no singular evaluation.
    def f(s):
        if s == 0.0:
            return 0.0
        q = upper*s*s
        return (1 - 4*q)*math.log(a/q)*2*upper*s/(2*a)
    return quad(f, 0, 1, epsabs=2e-13, epsrel=2e-13, limit=300)[0]


def simulate(w, n, seed):
    # Independent point coordinates on the actual quotient fundamental rectangle.
    rng = np.random.default_rng(seed)
    L = 2.713
    h = w*L/2
    x = rng.uniform(0, L, size=(n,2))
    y = rng.uniform(-h, h, size=(n,2))
    delta = np.abs(x[:,0]-x[:,1])
    direct_sq = delta**2 + (y[:,0]-y[:,1])**2
    flipped_sq = (L-delta)**2 + (y[:,0]+y[:,1])**2
    # Ties have probability zero; crossing is determined by the signs of the
    # lifted path's endpoint transverse coordinates.
    flipped = flipped_sq < direct_sq
    cross = np.logical_or(flipped & (y[:,0]*y[:,1]>0),
                          (~flipped) & (y[:,0]*y[:,1]<0))
    return cross.mean()


def check():
    for w in [.03, .25, .8, .999, 1.0, 1.001, 1.8, 4.0, 15.0]:
        exact = closed_probability(w)
        quad_value = integral_probability(w)
        assert abs(exact - quad_value) < 2e-12, (w,exact,quad_value)
    N = 650000
    for i,w in enumerate([.25, .8, 1.0, 1.4, 3.0, 7.0]):
        exact = closed_probability(w)
        empirical = simulate(w, N, 38071 + i)
        sigma = math.sqrt(exact*(1-exact)/N)
        assert abs(exact-empirical)<6*sigma+0.0002, (w,empirical,exact)
    # Global monotonicity in the two branches; independent mesh scan.
    xs = np.exp(np.linspace(math.log(.001), math.log(1000.), 10001))
    ps = np.array([closed_probability(float(x)) for x in xs])
    assert np.all(np.diff(ps)<0)
    assert abs(closed_probability(1.)-.375)<1e-14
    # By symbolic differentiation: third derivative is 0 from left, 4 from right.
    # Check C^2 matching analytically at w=1 via displayed derivative formulas.
    p0 = .5-1./8
    p1 = (4*math.log(1)+3)/(8*1)
    dl = -1./4
    dr = -(4*math.log(1)+1)/(4*1)
    d2l = -1./4
    d2r = (12*math.log(1)-1)/(4*1)
    assert p0==p1 and dl==dr and d2l==d2r
    print('MOBIUS_CORE_CROSSING_LAW_OK',N,6)

if __name__ == '__main__':
    check()
