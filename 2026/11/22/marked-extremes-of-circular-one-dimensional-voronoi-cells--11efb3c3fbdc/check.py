#!/usr/bin/env python3
"""Independent finite sanity checks for circular Voronoi extreme-cell theorem.
Analytical convergence is established in RESULT.md; tests here are finite checks only.
"""
import math
import random
from fractions import Fraction

# Beta(2,n-2) survival by independently evaluated finite binomial sum.
for n in range(3,35):
    for den in (3, 7, 13):
        t = Fraction(1, den)
        beta_tail = sum(Fraction(math.comb(n-1,k))*t**k*(1-t)**(n-1-k) for k in range(2))
        claimed = (1-t)**(n-2)*(1+(n-2)*t)
        assert beta_tail == claimed, (n,den)

# Independent Riemann integration of joint adjacent exceedances, using E2=y
# and independent exponential tails for E1 and E3.
for u in (0.4, 1.0, 2.0, 4.0, 7.0):
    segments = 80000
    h = (u+20)/segments
    approx = 0.0
    for j in range(segments):
        y = (j+0.5)*h
        one = math.exp(-max(u-y,0))
        approx += h*math.exp(-y)*one*one
    exact = 2*math.exp(-u)-math.exp(-2*u)
    assert abs(approx-exact) < 5e-7, (u,approx,exact)

# Finite, seeded Monte Carlo: mark and maximum of exponential two-spacings.
rng = random.Random(20261117)
n = 600
m = 6000
shape = []
maxzero = 0
center = math.log(n)+math.log(math.log(n))
for _ in range(m):
    e = [rng.expovariate(1.0) for _ in range(n)]
    total = sum(e)
    best = max(range(n), key=lambda i:e[i]+e[(i+1)%n])
    left,right = e[best],e[(best+1)%n]
    shape.append(left/(left+right))
    if n*(left+right)/total <= center:
        maxzero += 1
assert abs(sum(shape)/m-0.5)<0.025
assert abs(sum(v*v for v in shape)/m-1/3)<0.100
assert abs(maxzero/m-math.exp(-1))<0.09
print('PASS: exact Beta checks, adjacent-tail quadrature, seeded finite simulations')
print('Finite diagnostics: mean skew %.5f, second moment %.5f, P(max<=center) %.5f' %
      (sum(shape)/m,sum(v*v for v in shape)/m,maxzero/m))
