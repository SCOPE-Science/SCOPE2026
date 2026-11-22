#!/usr/bin/env python3
"""Exact certificate for a three-level halving ladder under stationary AR(1) oracle noise.

Python >=3.10 and SymPy >=1.11. There is no random sampling or floating-point
step in the proof checks. Run: python verify.py
"""
from itertools import permutations
from math import comb
import sympy as S

x, rho, t = S.symbols('x rho t', real=True)
orderings = list(permutations((1, 2, 4)))
F = {}
for order in orderings:
    h = [a*x for a in order]
    w = [h[i]*S.prod(1-h[j] for j in range(i+1, 3)) for i in range(3)]
    F[''.join(map(str, order))] = S.factor(sum(
        w[i]*w[j]*rho**abs(i-j) for i in range(3) for j in range(3)
    ))

rho_minus = -x*(24*x*x-24*x+7)/(1-4*x*x)
rho_plus = x/(2*(1-x)*(1-2*x))
assert S.factor(F['142']-F['421'] + 4*x*x*(rho-1)*(-4*rho*x*x+rho+24*x**3-24*x*x+7*x)) == 0
assert S.factor(F['412']-F['421']-4*x*x*(rho-1)*(4*rho*x*x-6*rho*x+2*rho-x)) == 0
assert S.factor((F['142']-F['421']).subs(rho,rho_minus)) == 0
assert S.factor((F['412']-F['421']).subs(rho,rho_plus)) == 0

# Positivity of a polynomial over the unit interval follows from nonnegative
# Bernstein coefficients at its exact polynomial degree. At least one positive
# coefficient makes it strictly positive throughout (0,1).
def bernstein_nonnegative(poly):
    P = S.Poly(S.expand(poly),t)
    if P.is_zero:
        return True
    n = P.degree()
    for k in range(n+1):
        b = sum(P.nth(j)*S.binomial(k,j)/S.binomial(n,j)
                for j in range(k+1))
        assert b >= 0, (poly, n, k, b)
    return True

# Prove that the two thresholds lie in (-1,0) and (0,1), and are ordered:
# after substituting x=t/4, each numerator/denominator is certified.
def nonnegative_on_quarter(expr, strict=True):
    expr=S.cancel(expr)
    num, den=S.fraction(expr)
    num=S.factor(num.subs(x,t/4))
    den=S.factor(den.subs(x,t/4))
    if den.subs(t,S.Rational(1,2)) < 0:
        num=-num; den=-den
    bernstein_nonnegative(num)
    bernstein_nonnegative(den)
    assert den.subs(t,0) > 0 and den.subs(t,1) > 0
    assert num.subs(t,S.Rational(1,2)) > 0
    if strict:
        assert num.subs(t,1) > 0
    return True

for expr in [-rho_minus, 1+rho_minus, rho_plus, 1-rho_plus,
             rho_plus-rho_minus]:
    nonnegative_on_quarter(expr)

# On each displayed rho interval, (F_other-F_best)/(1-rho)
# is affine in rho and nonnegative precisely when nonnegative at both
# interval ends. Check every one of 30 endpoint certificates exactly.
count = 0
for winner, ends in [('142',[-1,rho_minus]),
                     ('421',[rho_minus,rho_plus]),
                     ('412',[rho_plus,1])]:
    for order in F:
        if order==winner:
            continue
        quotient=S.cancel((F[order]-F[winner])/(1-rho))
        assert S.Poly(quotient,rho).degree() <= 1
        for endpoint in ends:
            val=S.cancel(quotient.subs(rho,endpoint))
            if val != 0:
                nonnegative_on_quarter(val)
            count += 1

# The two-step ordering identity is verified for generic rates and rho.
a,b,L=S.symbols('a b L',real=True)
D=S.factor((a*(1-L*b))**2+b*b+2*rho*a*b*(1-L*b)
           -(b*(1-L*a))**2-a*a-2*rho*a*b*(1-L*a))
assert S.factor(D-2*L*a*b*(a-b)*(rho-1))==0

# Rational point tests, independent of endpoint certification.
for xx in [S.Rational(1,25),S.Rational(1,10),S.Rational(1,5),S.Rational(1,4)]:
    rm=S.factor(rho_minus.subs(x,xx)); rp=S.factor(rho_plus.subs(x,xx))
    for rr,winner in [((-1+rm)/2,'142'),((rm+rp)/2,'421'),((rp+1)/2,'412')]:
        v={k:S.factor(f.subs({x:xx,rho:rr})) for k,f in F.items()}
        assert all(v[winner]<v[k] for k in v if k!=winner)

xx=S.Rational(1,5)
assert rho_minus.subs(x,xx)==-S.Rational(79,105)
assert rho_plus.subs(x,xx)==S.Rational(5,24)
assert F['142'].subs({x:xx,rho:-S.Rational(9,10)})==S.Rational(628,15625)  # 0.040192
assert F['412'].subs({x:xx,rho:S.Rational(1,2)})==S.Rational(7699,15625)
print('PASS: 30 exact Bernstein endpoint comparisons, five threshold inequalities,')
print('generic two-step swap identity, symbolic threshold equations,')
print('12 strict rational witness checks, and both benchmark values')
