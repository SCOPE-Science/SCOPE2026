"""Standalone finite checks for the noisy bounded-confidence freezing theorem.

The all-state infinite-time assertion is proved mathematically, not by this script.
"""
from fractions import Fraction as F
from math import comb, erfc, exp, pi, sqrt
from statistics import NormalDist
from random import Random

rng = Random(260521)
checks = 0

def eligible(x, radius):
    return [(i,j) for i in range(len(x)) for j in range(i+1,len(x))
            if abs(x[i]-x[j]) < radius]

# Direct subtraction of the rational two-agent update, with unequal utilities.
for _ in range(3000):
    x1 = F(rng.randint(-20,20),rng.randint(1,14))
    x2 = F(rng.randint(-20,20),rng.randint(1,14))
    u1 = F(rng.randint(1,30),rng.randint(1,15))
    u2 = F(rng.randint(1,30),rng.randint(1,15))
    mu = F(rng.randint(1,99),100)
    y1 = x1+2*mu*u2/(u1+u2)*(x2-x1)
    y2 = x2+2*mu*u1/(u1+u2)*(x1-x2)
    assert y1-y2 == (1-2*mu)*(x1-x2)
    checks += 1

# Exhaust the at-most-one-obstruction argument on sampled exact rational states.
for N in range(2,14):
    M = comb(N,2)
    for _ in range(100):
        radius = F(rng.randint(1,5),rng.randint(1,6))
        xx = [F(rng.randint(-100,100),rng.randint(1,10)) for _ in range(N)]
        pairs = eligible(xx,radius)
        if not pairs:
            continue
        i,j = pairs[0]
        centers = [xx[i]+5*k*radius for k in range(1,N+1)]
        available = [c for c in centers if all(abs(xx[h]-c)>2*radius
                                   for h in range(N) if h not in (i,j))]
        assert len(available)>=2
        mu = F(rng.randint(1,99),100)
        ui = F(rng.randint(1,50),rng.randint(1,20))
        uj = F(rng.randint(1,50),rng.randint(1,20))
        yi = xx[i]+2*mu*uj/(ui+uj)*(xx[j]-xx[i])
        yj = xx[j]+2*mu*ui/(ui+uj)*(xx[i]-xx[j])
        for y,c in ((yi,available[0]),(yj,available[1])):
            assert abs(c-y)+radius/2 < (5*N+4)*radius
            for h in range(N):
                if h not in (i,j):
                    assert abs(xx[h]-c)>2*radius
        assert abs(available[0]-available[1])>=5*radius
        assert M>=1
        checks += 1

# Check the exact Gaussian normalization and weak-noise equivalent.
for epsilon in (0.12,0.5,1.0):
    for sigma in (0.04,0.1,0.3,1.0):
        r = erfc(epsilon/(2*sigma))
        assert 0 < r < 1
        normal=NormalDist(0,sqrt(2)*sigma)
        two_tails=2*(1-normal.cdf(epsilon))
        assert abs(r-two_tails)<1e-12
        truncated=sum((1-r)**(t-1)*r for t in range(1,401))
        assert abs(truncated-(1-(1-r)**400))<1e-12
        checks += 1
for z in (4.0,5.0,6.0):
    exact = 1/erfc(z)
    asympt = sqrt(pi)*z*exp(z*z)
    assert 0.96 < exact/asympt < 1.04
    checks += 1
print(f"PASS: {checks} exact-rational geometry/update and Gaussian-tail checks")
