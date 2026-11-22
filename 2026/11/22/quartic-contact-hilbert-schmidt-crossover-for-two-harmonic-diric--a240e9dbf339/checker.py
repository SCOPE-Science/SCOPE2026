"""Reproducible finite checks of a two-harmonic Dirichlet composition norm.

Requires Python 3 and scipy. Finite checks do not certify asymptotic theorems.
"""
import math
from scipy.integrate import quad
from scipy.special import zeta


def min_trig(a, b):
    return -a+b if b <= a/4 else -b-a*a/(8*b)


def gap(a, b, th):
    return a*math.cos(th)+b*math.cos(2*th)-min_trig(a, b)


def squared_hs(a, b, delta):
    # Work on [0, pi], splitting at minima for quadrature accuracy.
    points = [0.0, math.pi]
    if b > a/4:
        points.append(math.acos(-a/(4*b)))
    points.sort()
    val = 0.0
    for lo, hi in zip(points[:-1], points[1:]):
        seg = quad(lambda th: zeta(1+2*(delta+gap(a,b,th)), 1), lo, hi,
                   epsabs=1e-7, epsrel=1e-8, limit=250)[0]
        val += seg
    return val/math.pi


def phi(a, k):
    km = max(-k, 0)
    c = 1+8*km*km/a
    return 1/(4*math.sqrt(c)*math.sqrt(2*k+2*math.sqrt(km*km+a/8)))


def phi_integral(a, k):
    km = max(-k, 0)
    val = quad(lambda u: 1/(1+2*k*u*u+a*u**4/8+8*km*km/a),
               -math.inf, math.inf, epsabs=2e-11)[0]
    return val/(4*math.pi)


def fixed_constant(a, b):
    if b < a/4:
        return 1/(2*math.sqrt(2*(a-4*b)))
    if b > a/4:
        return 1/(2*math.sqrt(2*b*(1-a*a/(16*b*b))))
    return 2**(-7/4)*a**(-1/4)


def run():
    n = 0
    for a in (0.8, 2.0, 3.1):
        for b in (a/10, a/4, a/3, a):
            for th in (0.0, .25, .7, 1.7, math.pi):
                eta=a/4-b
                x=1+math.cos(th)
                completed=4*eta*x+2*b*x*x+2*max(-eta,0)**2/b
                assert abs(gap(a,b,th)-completed)<3e-13
                n += 1
        for k in (-2.0, -0.5, 0.0, 0.5, 2.0):
            assert math.isclose(phi(a,k),phi_integral(a,k), rel_tol=4e-10)
            n += 1
    a=2.0
    for b in (0.3,0.5,0.7):
        delta=0.0001
        scale=delta**(0.75 if b==a/4 else 0.5)
        observed=squared_hs(a,b,delta)*scale
        desired=fixed_constant(a,b)
        assert abs(observed/desired-1)<0.06, (b, observed, desired)
        n += 1
    for k in (-2.0, -0.5, 0.0, 0.5, 2.0):
        delta=0.0001
        observed=squared_hs(a,a/4-k*math.sqrt(delta),delta)*delta**0.75
        assert abs(observed/phi(a,k)-1)<0.06, (k, observed, phi(a,k))
        n += 1
    print('PASS:', n, 'finite symbolic-identity and numerical assertions')


if __name__ == '__main__':
    run()
