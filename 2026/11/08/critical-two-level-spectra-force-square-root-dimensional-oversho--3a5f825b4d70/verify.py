#!/usr/bin/env python3
"""Reproduce one-step positive-diagonal matrix-function fitting diagnostics.

No external packages or files are required. Uses multiplicities instead of dense matrices.
Analytic asymptotic and uniqueness proofs are in RESULT.md; checks are finite tests.
"""
import math
from fractions import Fraction


def residual(r, alpha):
    return 1.0 - (1.0 - r) * (1.0 + alpha*r)**2


def objective(n, h, t, alpha):
    return (n-1)*residual(h, alpha)**2 + residual(t, alpha)**2


def d_objective(n, h, t, alpha):
    def piece(r, mult):
        e = residual(r, alpha)
        de = -2*r*(1-r)*(1+alpha*r)
        return mult*2*e*de
    return piece(h, n-1) + piece(t, 1)


def minimize_nonnegative(n, h, t):
    # Exactly one positive stationary point by the sign pattern of the cubic.
    lo, hi = 0., 1.
    assert d_objective(n, h, t, lo) < 0
    while d_objective(n, h, t, hi) <= 0:
        hi *= 2
        assert hi < 1.0e10
    for _ in range(110):
        mid = (lo+hi)/2
        if d_objective(n, h, t, mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def exact_quartic_coefficients(n, h, t):
    total = [Fraction(0) for _ in range(5)]
    for mult, r in [(n-1,h),(1,t)]:
        c = [r, -2*r*(1-r), -r*r*(1-r)]
        for i, ci in enumerate(c):
            for j,cj in enumerate(c):
                total[i+j] += mult*ci*cj
    return total


def run():
    count = 0
    for m in (2,3,4,5,6,8):
        n = m**4
        a = Fraction(1,8)
        t = Fraction(1,2)
        h = 1-a/Fraction(m*m)
        c = exact_quartic_coefficients(n,h,t)
        assert c[1] < 0 and c[3] > 0 and c[4] > 0
        # Check the coefficient formula directly against exact evaluations.
        for z in (0, Fraction(1,2), 1, 2, 5, m):
            poly = sum(ci*z**i for i,ci in enumerate(c))
            f = lambda r: 1-(1-r)*(1+z*r)**2
            exact = (n-1)*f(h)**2 + f(t)**2
            assert poly == exact
            count += 1
    print('Exact rational quartic/uniqueness-sign checks:', count)
    print('m,n, alpha/m, spectral/sqrt(n), relative_Frob_squared, sign_error/n^.25')
    seen = []
    for m in (2,4,8,16,32,64,128,256,512,1024):
        n = m**4
        a = 1./8.
        t = 1./2.
        h = 1-a/(m*m)
        alpha = minimize_nonnegative(n,h,t)
        fhi,flo = residual(h,alpha),residual(t,alpha)
        basef2 = (n-1)*h*h + t*t
        fitted = objective(n,h,t,alpha)
        sn = max(abs(fhi),abs(flo)) / m**2
        sign_error = max(abs(math.sqrt(1-h)*(1+alpha*h)-1),
                         abs(math.sqrt(1-t)*(1+alpha*t)-1)) / m
        assert fitted < basef2
        assert abs(d_objective(n,h,t,alpha)) < 1.e-7 * max(1.,n)
        seen.append((m,alpha/m,sn,fitted/basef2,sign_error))
        print(m,n,*(format(v,'.10g') for v in seen[-1][1:]))
    # Increasing-dimension convergences; do not confuse checks with infinite proof.
    assert abs(seen[-1][1]-2)<.02
    assert abs(seen[-1][2]-.5)<.01
    assert abs(seen[-1][3]-.5)<.02
    assert abs(seen[-1][4]-1/math.sqrt(2))<.02
    for a,t in ((.10,.25),(.30,.40),(.05,.70),(.125,.5)):
        D=(1-t)*t*t
        beta=math.sqrt(a/(a*a+D*D))
        predicted_spike=a*D/(a*a+D*D)
        predicted_fit=D*D/(a*a+D*D)
        m=512; n=m**4
        h=1-a/(m*m)
        alpha=minimize_nonnegative(n,h,t)
        error=abs(residual(t,alpha))/m**2
        fit=objective(n,h,t,alpha)/n
        assert abs(alpha/m-beta)<.05
        assert abs(error-predicted_spike)<.025
        assert abs(fit-predicted_fit)<.04
        count+=3
    print('Independent formula/limit cross-checks:', count, 'PASS')

if __name__ == '__main__':
    run()
