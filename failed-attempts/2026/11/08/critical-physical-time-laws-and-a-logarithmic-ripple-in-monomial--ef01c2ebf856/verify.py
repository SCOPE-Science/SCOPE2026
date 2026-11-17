#!/usr/bin/env python3
"""Reproducible numerical and exact-rational checks of the stated sewed-focus laws.
All universal statements are proved analytically in RESULT.md; these checks are finite.
Requires only Python 3 standard library.
"""
from fractions import Fraction
from math import exp, log, isclose


def section_radii(a, exponent, steps):
    r = a
    out = [r]
    for _ in range(steps):
        r = r ** exponent
        out.append(r)
    return out


def delayed_series(a, kappa):
    L = -log(a)
    total = a
    j = 1
    while True:
        v = exp(-L * exp(j * log(kappa))) if j * log(kappa) < 600 else 0.0
        if v < 2e-15:
            return total
        total += 2*v
        j += 1
        assert j < 1000000


def F_and_P(kappa, theta):
    assert kappa > 1
    s = 0.0
    for j in range(-100, 101):
        x = kappa**(j-theta)
        s += exp(-x) - (1.0 if j <= 0 else 0.0)
    return s, s-theta

# Exact polynomial branch-flight identities for published exponent ratio 8/4=2.
exact_tests = 0
for a in [Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1, 1), Fraction(5, 4)]:
    rad = section_radii(a, 2, 5)
    for r, nxt in zip(rad[:-1], rad[1:]):
        assert r**8 == nxt**4   # Upper/lower matching across x=0.
        assert nxt == r**2
        exact_tests += 1
    assert rad[2] == a**4

# Exact common-exponent case: all section orbits are periodic.
for a in [Fraction(1, 6), Fraction(4, 7), Fraction(1), Fraction(3)]:
    assert section_radii(a, 1, 4) == [a]*5
    exact_tests += 1

# Independent numerical checks of the exact physical crossing times.
for p,q,a in [(4,8,.4),(5,15,.8),(8,4,.5),(9,6,2.0)]:
    kap=q/p
    arr=section_radii(a,kap,6)
    for x,y in zip(arr[:-1],arr[1:]):
        assert isclose(x**q,y**p,rel_tol=2e-12,abs_tol=1e-14)
    assert isclose(arr[2],a**(kap**2),rel_tol=1e-12)

# Euler-Maclaurin comparison at fixed initial section radius (external E1
# integral evaluated by elementary Simpson quadrature after u=log(t/L)).
def E1(L):
    # E1(L) = integral_0^infty exp(-L exp(u)) du.
    end=18.0
    N=40000
    step=end/N
    s=0.0
    for j in range(N+1):
        u=j*step
        v=exp(-L*exp(u))
        s+=(1 if j in (0,N) else (4 if j%2 else 2))*v
    return s*step/3

for a in (.4,.8):
    L=-log(a)
    I=E1(L)
    predicted_cubic=a*(-L**3+3*L**2-L)/360
    errors=[]
    for h in (.2,.1,.05):
        actual=delayed_series(a,exp(h))
        leading=2*I/h+a*L*h/6
        errors.append((actual-leading)/h**3)
    assert abs(errors[-1]-predicted_cubic)<2e-6, (a,errors,predicted_cubic)

# Logperiodic finite-cutoff reorganization at fixed kappa.
for k in (2.0,3.0,4.0):
    for shift in (.11,.38,.69):
        N=12
        L=k**(-N-shift)
        a=exp(-L)
        S=(delayed_series(a,k)-a)/2
        F,P=F_and_P(k,shift)
        assert abs(S-(N+F)) < 10*L, (k,shift,S,N,F)
        assert abs(F_and_P(k,shift+1)[1]-P)<1e-10

# Nonzero numerically resolved ripple for kappa=4, analytic nonconstancy
# follows instead from the nonvanishing Gamma Fourier coefficient in proof.
assert abs(F_and_P(4,.25)[1]-F_and_P(4,.75)[1])>1e-3
print('SEWED_FOCUS_EXACT_BRANCH_IDENTITIES_OK',exact_tests)
print('SEWED_FOCUS_CRITICAL_E1_AND_LOGPERIODIC_CHECK_OK')
