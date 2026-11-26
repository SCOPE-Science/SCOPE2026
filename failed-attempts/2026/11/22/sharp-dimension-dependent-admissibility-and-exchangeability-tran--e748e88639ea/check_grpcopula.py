"""Reproducible finite checks for the analytic GRP copula theorem.

Requires Python 3, sympy and mpmath. Exact algebraic identities are tested
at several dimensions; finite tests do not establish every-dimension results.
"""
from fractions import Fraction
import math
import sympy as S
import mpmath as mp

checks = 0

def check(predicate, name):
    global checks
    if not predicate:
        raise AssertionError(name)
    checks += 1

alpha = S.symbols('a', real=True)
for n in range(2, 5):
    xs = S.symbols(f'x1:{n+1}')
    prod_x = S.prod(xs)
    expr = S.prod(xs)*(1+alpha)**(n-1)*(1+alpha*prod_x)/S.prod(1+alpha*x for x in xs)
    density = expr
    for x in xs:
        density = S.diff(density,x)
    expected = (1+alpha)**(n-1)*(1+alpha*S.prod(x*(2+alpha*x) for x in xs))/S.prod((1+alpha*x)**2 for x in xs)
    check(S.cancel(density-expected)==0,f'density n={n}')
    for x in xs:
        marginal = expr.subs({v:S.Integer(1) for v in xs if v != x})
        check(S.cancel(marginal-x)==0, f'marginal n={n}')
    h0=lambda x: (1+alpha)*x/(1+alpha*x)
    h1=lambda x: (1+alpha)*x*x/(1+alpha*x)
    mixture=S.prod(h0(x) for x in xs)/(1+alpha)+alpha*S.prod(h1(x) for x in xs)/(1+alpha)
    check(S.cancel(expr-mixture)==0,f'two-component identity n={n}')
    check(S.cancel(S.diff(h0(xs[0]),xs[0])-(1+alpha)/(1+alpha*xs[0])**2)==0,'component 0')
    check(S.cancel(S.diff(h1(xs[0]),xs[0])-(1+alpha)*xs[0]*(2+alpha*xs[0])/(1+alpha*xs[0])**2)==0,'component 1')

# Rational examples: 3D validity for -1/8, failure in 4D;
# bivariate validity at -1/3, failure in 3D.
for s,n,valid in [(Fraction(1,8),3,True),(Fraction(1,8),4,False),
                  (Fraction(1,3),2,True),(Fraction(1,3),3,False),
                  (Fraction(1,4),2,True),(Fraction(1,4),3,False),
                  (Fraction(1,10),3,True),(Fraction(1,10),4,False)]:
    q=s*(2-s)**n
    check((q <= 1)==valid, f'finite cutoff s={s} n={n}')

mp.mp.dps=60
for n in [2,3,4,5,8,12]:
    root=mp.findroot(lambda s:s*(2-s)**n-1, (mp.mpf(2)**(-n),mp.mpf(2)**(-n)*mp.mpf('1.5')))
    check(root>mp.mpf(2)**(-n),'new interval larger than sufficient one')
    check(root<mp.mpf(2)/(n+1),'root before critical maximum')
    check(abs(root*(2-root)**n-1)<mp.mpf('1e-50'),'root equation')
    print(f'n={n} sharp negative cutoff -{mp.nstr(root,32)}')

# Rational covariance sign witness: C2(x,y)-xy at x=y=1/2.
for a,positive in [(S.Rational(-1,4),False),(S.Rational(-1,8),False),
                   (S.Rational(1,2),True),(S.Integer(2),True)]:
    x=S.Rational(1,2)
    diff=a*(x*(1-x)/(1+a*x))**2
    check(bool(diff>0)==positive,'rank-dependence sign')

print(f'CHECKS PASSED: {checks}')
print('The infinite-dimensional and exact-root claims require the written proof.')
