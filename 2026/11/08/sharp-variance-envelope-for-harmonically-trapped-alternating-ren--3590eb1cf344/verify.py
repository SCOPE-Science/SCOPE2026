"""Independent stationary-variance checks for alternating renewal confinement.
Only scientific reproducibility; no provenance assertions.
"""
import math
from fractions import Fraction


def formula(k, v, m, phi):
    return (v / k) ** 2 * (1 - 2 * (1 - phi) / (k * m * (1 + phi)))


def periodic_independent(k, v, m):
    h = k * m
    B = v / k
    alpha = math.exp(-h)
    # Start at -B tanh(h/2); integrate square on the positive run.
    x0 = -B * (1-alpha) / (1+alpha)
    c = x0 - B
    return B*B + 2*B*c*(-math.expm1(-h))/h + c*c*(-math.expm1(-2*h))/(2*h)


def markov_independent(k, v, m):
    # Generator stationarity E[X sigma]=v/(k+2/m), E[X^2]=v/k E[X sigma].
    return v*v/(k*(k+2/m))


def erlang2_independent(k, v, m):
    # Two exponential substages of rate 2/m per holding period; orientation
    # autocovariance is exp(-lambda*t)*cos(lambda*t)
    # with lambda=2/m, obtained by solving the four-state Markov cycle.
    lam = 2/m
    return v*v/k*(k+lam)/((k+lam)**2+lam**2)

cases=0
for k in (0.2,0.7,1.,2.,5.):
    for v in (0.4,1.,3.):
        for m in (0.25,1.,2.5):
            h = k*m
            p = math.exp(-h)
            actual = formula(k,v,m,p)
            assert math.isclose(actual,periodic_independent(k,v,m),rel_tol=3e-12,abs_tol=3e-12)
            assert math.isclose(actual,(v/k)**2*(1-2*math.tanh(h/2)/h),rel_tol=3e-12,abs_tol=3e-12)
            markov_phi=1/(1+h)
            assert math.isclose(formula(k,v,m,markov_phi),markov_independent(k,v,m),rel_tol=3e-12,abs_tol=3e-12)
            erlang_phi=(1+h/2)**-2
            assert math.isclose(formula(k,v,m,erlang_phi),erlang2_independent(k,v,m),rel_tol=3e-12,abs_tol=3e-12)
            assert actual < formula(k,v,m,erlang_phi) < formula(k,v,m,markov_phi) < (v/k)**2
            cases+=5
# Completely separate exact rational Markov two-phase identity.
for ik in range(1,14):
    for im in range(1,12):
        k=Fraction(ik,7);m=Fraction(im,5);v=Fraction(3,2)
        phi=1/(1+k*m)
        assert formula(k,v,m,phi)==v*v/(k*(k+2/m))
        cases+=1
# Arbitrary two-point mean-preserving spreads in convex order (Jensen verified numerically).
for im in range(1,21):
    m=im/8
    for frac in (0.1,0.25,0.4,0.6,0.8):
        a=m*frac;b=m*(2-frac)
        phi=(math.exp(-a)+math.exp(-b))/2
        assert phi>math.exp(-m)
        assert formula(1,1,m,phi)>formula(1,1,m,math.exp(-m))
        cases+=1
print(f'PASS: {cases} independent assertions')
