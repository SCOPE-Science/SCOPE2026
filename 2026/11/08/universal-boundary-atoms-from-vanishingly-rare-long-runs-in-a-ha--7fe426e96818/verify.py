#!/usr/bin/env python3
"""Finite reproducibility checks for a rare-long-run harmonic active particle.

The analytic weak-convergence statement and universal Wasserstein estimate
are established in RESULT.md; numerical checks do not prove these statements.
"""
from fractions import Fraction as F
from math import factorial, tanh, comb, exp

checks = 0

def check(test, label):
    global checks
    assert bool(test), label
    checks += 1

def moments_two_point(t0, long_run, mean, kmax=4):
    """Exact renewal reward moment recursion, evaluated in float arithmetic."""
    p = (mean - t0)/(long_run - t0)
    assert 0 < p < 1
    ph = [1.] + [(1-p)*exp(-n*t0)+p*exp(-n*long_run)
                   for n in range(1,kmax+1)]
    z = [1.]
    for n in range(1,kmax+1):
        right = 0.
        for j in range(n):
            cc = sum(comb(n-j,h) * (-1)**(n-j-h) * ph[j+h]
                     for h in range(n-j+1))
            right += comb(n,j)*(-1)**j*cc*z[j]
        z.append(right/(1-(-1)**n*ph[n]))
    age = [1.] + [(1-ph[j])/(j*mean) for j in range(1,kmax+1)]
    out = [1.]
    for n in range(1,kmax+1):
        q = 0.
        for j in range(n+1):
            diffz = sum(comb(j,h)*(-1)**(j-h)*z[h] for h in range(j+1))
            q += comb(n,j)*age[j]*diffz
        out.append(q)
    return out

# Rational enclosure for a = tanh(9/20) and the limiting fourth cumulant.
u = F(9,10)
s = sum((u**k)/factorial(k) for k in range(15))
upper_e = s + u**15 / factorial(15) / (1-u/16)
a_low = (s-1)/(s+1)
a_high = (upper_e-1)/(upper_e+1)
a = tanh(.45)
check(float(a_low) < a < float(a_high), "tanh rational bracket")
check(float(upper_e - s) < 2e-13, "exponential bracket width")

def kur_expr(x):
    return -2+10*x-12*x*x-F(2,3)*x*x*x

# Sign-safe interval evaluation: positive term takes the lower bound,
# negative terms take the upper bound.
k_lower = -2+10*a_low-12*a_high*a_high-F(2,3)*a_high**3
k_upper = -2+10*a_high-12*a_low*a_low-F(2,3)*a_low**3
check(k_lower > F(329,10000), "strict rational cumulant bound")
check(k_upper < F(33,1000), "rational upper cumulant bound")
m2_inf = 1-2*a
m4_inf = 1-2*a-F(2,3)*a**3
k_inf = m4_inf - 3*m2_inf*m2_inf
check(float(k_lower) < float(k_inf) < float(k_upper), "cumulant enclosure")
check(abs(float(m2_inf)-0.15620198949998415) < 1e-13,"second moment value")
check(abs(float(m4_inf)-0.10613698665670379) < 1e-13,"fourth moment value")

# Independently integrate the deterministic-orbit density with composite Simpson.
def simpson(fun, lo, hi, n=20000):
    assert n%2 == 0
    h = (hi-lo)/n
    v = fun(lo)+fun(hi)
    for k in range(1,n):
        v += (4 if k%2 else 2)*fun(lo+k*h)
    return v*h/3

t = .9
for j, predicted in [(0,1.),(2,1-2*a/t),(4,1-2*(a+a**3/3)/t)]:
    actual = simpson(lambda x: x**j/(t*(1-x*x)), -a, a)
    check(abs(actual-predicted)<2e-12, "periodic density integral degree %d" % j)

# Universal W1 estimate implies a rigorously positive fourth cumulant
# for every L >= 300, without relying on numerical finite-L samples.
p300=F(1,10)/(F(300)-F(9,10))
epsilon300=F(29,5)*p300
check(F(16)*epsilon300 < F(329,10000), "all L>=300 rigorous positivity")
check(float(16*epsilon300)<.032, "finite clock strict margin")

# Independent affine-at-flips / equilibrium-age recursion for several L.
for long_run in (10.,20.,100.,300.,1000.,10000.):
    mm = moments_two_point(.9,long_run,1.,4)
    p = .1/(long_run-.9)
    eps = 5.8*p
    check(0 < mm[2] < 1, "second moment bounds at L=%s"%long_run)
    check(0 < mm[4] < 1, "fourth moment bounds at L=%s"%long_run)
    check(abs(mm[2]-float(m2_inf)) <= 2*eps+2e-12,
          "W1 second-moment diagnostic at L=%s"%long_run)
    check(abs(mm[4]-float(m4_inf)) <= 4*eps+2e-12,
          "W1 fourth-moment diagnostic at L=%s"%long_run)
    actual_k = mm[4] - 3*mm[2]**2
    check(abs(actual_k-float(k_inf)) <= 16*eps+2e-12,
          "cumulant bound diagnostic at L=%s"%long_run)
    if long_run>=300:
        check(actual_k>0, "strict positive kurtosis at L=%s"%long_run)

check(abs((1/5)-3*(1/3)**2-(-2/15))<1e-14,
      "exponential-run comparison")
print('PASS:',checks,'deterministic assertions; limit proof is analytical')
