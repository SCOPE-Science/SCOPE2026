#!/usr/bin/env python3
"""Exact symbolic checks for a quartic-trap Gaussian stationary target.

Run: python3 verify_quartic_reset.py
Requires sympy. All moment identities below use rational arithmetic.
"""
from itertools import product
from math import factorial
import sympy as S

def gaussian_moment(exps, s):
    if any(k % 2 for k in exps):
        return S.Integer(0)
    ans = S.Integer(1)
    for k in exps:
        ans *= S.factorial2(k-1) * s ** (k//2) if k else 1
    return ans

def gaussian_expectation(expr, xs, s):
    poly = S.Poly(S.expand(expr), *xs)
    return S.factor(sum(coeff*gaussian_moment(monom, s)
                        for monom, coeff in poly.terms()))

def verify(d, a, c, D, s, degree=6):
    xs = S.symbols('x0:'+str(d))
    radius2 = sum(x*x for x in xs)
    t = S.factor((a-D/s)/(c*s))
    z = S.factor((d+2-t)/2)
    rstar = S.factor(c*s*(d*t + S.Max(d+2-t,0)**2/4))
    assert rstar > 0
    g = d*t + (d+2-t)*radius2/s - radius2**2/s**2
    qratio = S.expand(1-(c*s/rstar)*g)
    assert gaussian_expectation(qratio, xs, s) == 1
    if z>0:
        assert S.simplify(qratio-(c*s/rstar)*(radius2/s-z)**2)==0
    else:
        assert S.simplify(qratio-(c*s/rstar)*(radius2/s)*(radius2/s-2*z))==0
    count = 2
    for exps in product(range(degree+1), repeat=d):
        if sum(exps)>degree: continue
        f = S.prod(x**k for x,k in zip(xs,exps))
        # Original diffusion generator, independent of reset law.
        Lf = S.expand(-sum((a+c*radius2)*x*S.diff(f,x) for x in xs) +
                      D*sum(S.diff(f,x,2) for x in xs))
        residual = gaussian_expectation(Lf, xs, s) + rstar * (
            gaussian_expectation(qratio*f, xs, s) - gaussian_expectation(f, xs, s))
        assert residual == 0, (d,exps,residual)
        count += 1
    # The source required below the threshold is negative at its true maximizer.
    y_max = max(S.Integer(0), z)
    assert S.simplify(1-2*(d*t+(d+2-t)*y_max-y_max**2)/(rstar/(c*s))) == -1
    count+=1
    print(f'd={d}, a={a}, c={c}, D={D}, s={s}, t={t}, rate_min={rstar}, zero-radius-squared={s*z if z>0 else 0}: {count} exact checks')
    return count

if __name__ == '__main__':
    cases = [
        (1, S.Integer(2), S.Integer(1), S.Integer(1), S.Integer(1)),
        (1, S.Integer(5), S.Integer(1), S.Integer(1), S.Integer(1)),
        (2, S.Integer(6), S.Integer(1), S.Integer(1), S.Integer(1)),
        (3, S.Integer(6), S.Integer(1), S.Integer(1), S.Integer(1)),
        (4, S.Integer(6), S.Integer(1), S.Integer(1), S.Integer(1)),
        (2, S.Integer(1), S.Integer(1), S.Integer(2), S.Integer(1)),
        (2, S.Rational(3,2), S.Rational(1,3), S.Integer(2), S.Rational(3,2)),
    ]
    total = sum(verify(*row) for row in cases)
    print(f'PASS: {total} exact rational checks; analytic proof handles all dimensions and parameters.')
