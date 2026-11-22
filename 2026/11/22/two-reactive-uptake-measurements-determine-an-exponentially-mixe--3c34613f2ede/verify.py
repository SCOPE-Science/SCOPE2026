"""Numerical reproduction for the two-rate exponential-bed inverse theorem.
Only finite consistency tests; the mathematical proof is separate.
"""
from __future__ import annotations
import math
import random
from scipy.optimize import brentq
from scipy.special import kve


def ratio_bessel(x: float) -> float:
    assert x > 0
    return float(kve(0, x) / kve(1, x))


def conductance(diffusivity: float, length: float, rate: float) -> float:
    x = 2 * length * math.sqrt(rate / diffusivity)
    return math.sqrt(diffusivity * rate) * ratio_bessel(x)


def measured_velocity(diffusivity: float, length: float, rate: float, theta: float, km: float) -> float:
    u = theta * conductance(diffusivity, length, rate)
    return km * u / (km + u)


def reconstruct(v1: float, v2: float, k1: float, k2: float, theta: float, km: float):
    assert 0 < k1 < k2 and theta > 0 and km > 0
    assert 0 < v1 < km and 0 < v2 < km
    t1 = km * v1 / (km - v1)
    t2 = km * v2 / (km - v2)
    r = math.sqrt(k2/k1)
    rho = t2/t1
    if not (r < rho < r*r):
        raise ValueError('not feasible')
    def rr(x):
        return r * ratio_bessel(r*x) / ratio_bessel(x)
    lo = 1e-12
    hi = 1.0
    while rr(hi) > rho:
        hi *= 2
        if hi > 1e8:
            raise ArithmeticError('root beyond numerical range')
    root = brentq(lambda x: rr(x)-rho, lo, hi, xtol=2e-14, rtol=2e-14)
    D = (t1/(theta*math.sqrt(k1)*ratio_bessel(root)))**2
    ell = root * math.sqrt(D) / (2*math.sqrt(k1))
    return D, ell, root


def check():
    rng = random.Random(20261117)
    count = 0
    for _ in range(2000):
        D = 10 ** rng.uniform(-1.5, 1.5)
        k1 = 10 ** rng.uniform(-1, 1)
        r = 1.2 + rng.uniform(0, 2.8)
        k2 = k1*r*r
        theta = 10 ** rng.uniform(-.4, .4)
        km = 10 ** rng.uniform(.5, 1.5)
        x = 10**rng.uniform(-1.5, 1.2)
        ell = .5*x*math.sqrt(D/k1)
        v1 = measured_velocity(D,ell,k1,theta,km)
        v2 = measured_velocity(D,ell,k2,theta,km)
        assert 0 < v1 < v2 < km
        count += 1
        tp1 = km * v1/(km-v1)
        tp2 = km * v2/(km-v2)
        assert r < tp2/tp1 < r*r
        count += 1
        DH, ellH, xH = reconstruct(v1,v2,k1,k2,theta,km)
        assert abs(DH/D-1) < 2e-10 and abs(ellH/ell-1) < 2e-10, (D, DH, ell, ellH)
        count += 2
        assert abs(xH/x-1) < 2e-10
        count += 1
    for r in (1.01, 1.2, 2, 10):
        xs=[10**(-5 + k*7/1000) for k in range(1001)]
        previous = None
        for x in xs:
            f=ratio_bessel(x)
            H=x*(1-f**4)-2*f**3
            assert H > -1e-10
            count+=1
            rr=r*ratio_bessel(r*x)/f
            if previous is not None:
                assert rr < previous
                count+=1
            previous=rr
        assert r < rr < r*r
        count+=1
    # Exact input example: D=1, ell=1/2, k1=1, k2=4, theta=1, km=3.
    u1,u2=conductance(1,.5,1),conductance(1,.5,4)
    v1,v2=measured_velocity(1,.5,1,1,3),measured_velocity(1,.5,4,1,3)
    assert abs(u1-.6994839355937723) < 1e-12
    assert abs(u2-2*ratio_bessel(2)) < 1e-12
    assert abs(reconstruct(v1,v2,1,4,1,3)[0]-1) < 1e-12
    assert abs(reconstruct(v1,v2,1,4,1,3)[1]-.5) < 1e-12
    count+=4
    print(f'{count} supplementary assertions passed')
    print(f'exact-input example: U1={u1:.12g}, U2={u2:.12g}, v1={v1:.12g}, v2={v2:.12g}')

if __name__ == '__main__': check()
