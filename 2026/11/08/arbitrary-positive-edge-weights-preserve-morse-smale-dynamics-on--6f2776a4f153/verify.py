"""Finite reproducibility checks for the weighted three-clock path theorem.

Run: python3 verify.py
The universal theorem is proved analytically; sampling is not a proof.
"""
import math
import random

PI = math.pi

def spectral(a, b):
    return a + b + math.sqrt(a*a - a*b + b*b)

def step(x, y, a, b, h):
    return (x + h * (2*a*math.sin(x) - b*math.sin(y)),
            y + h * (-a*math.sin(x) + 2*b*math.sin(y)))

def potential(x, y, a, b):
    return a*math.cos(x) + b*math.cos(y)

def eigen_slopes(a, b):
    e = math.sqrt(a*a + a*b + b*b)
    return ((a+b-e)/b, (a+b+e)/b)

def check():
    rnd = random.Random(13927)
    samples = 0
    for ratio in (0.0001, 0.01, 0.15, 0.4, 1.0, 2.5, 30.0, 10000.0):
        a, b = ratio, 1.0
        lam = spectral(a,b)
        lo, hi = eigen_slopes(a,b)
        assert lam > 2*max(a,b)
        assert 0 < lo < 1 < hi
        for factor in (0.01, 0.5, 0.999):
            h = factor / lam
            for _ in range(2500):
                x = rnd.random()*PI
                y = PI - x + rnd.random()*x
                xp, yp = step(x,y,a,b,h)
                tol = 5e-13
                assert -tol <= xp <= PI+tol, (ratio,factor,x,y,xp,yp)
                assert -tol <= yp <= PI+tol, (ratio,factor,x,y,xp,yp)
                assert xp+yp >= PI-tol, (ratio,factor,x,y,xp,yp)
                v0, v1 = potential(x,y,a,b), potential(xp,yp,a,b)
                assert v1 <= v0 + 2e-12*max(a,b), (ratio,factor,v0,v1)
                samples += 1
    # Each side of the spectral bound is tested at the attracting corner.
    for a,b in ((1,1),(10,1),(0.03,1)):
        lam=spectral(a,b)
        for h in (.999/lam, 1.001/lam):
            multiplier=1-h*lam
            assert (multiplier>0) == (h<1/lam)
    print(f'VERIFY_OK triangle_samples={samples} slope_cases=8 critical_spectral_cases=6')
    print('LIMIT: finite sampling supplements, but does not establish, the theorem')

if __name__ == '__main__':
    check()
