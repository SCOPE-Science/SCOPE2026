"""Standalone symbolic and exact-rational checks for a copula mixing envelope.

Requires Python 3 and sympy. The finite tests support, but do not replace,
the analytic proof in RESULT.md.
"""
from fractions import Fraction
from math import sqrt, exp
import sympy as S

x, y, a, s, n = S.symbols('x y a s n', real=True)
f = x*(1-x)/(1+a*x)
g = S.factor(S.diff(f,x))
C = x*y*(1+a)*(1+a*x*y)/((1+a*x)*(1+a*y))
assert S.factor(C-x*y-a*f*(y*(1-y)/(1+a*y))) == 0
assert S.factor(g-(1-2*x-a*x*x)/(1+a*x)**2)==0
assert S.factor(g - ((1+a)/(1+a*x)**2-1)/a)==0
assert S.simplify(S.integrate((1+a*x)**-2,(x,0,1))-1/(1+a))==0
# Use exact antiderivatives; alpha=0 follows by continuity.
J_expr = S.factor(( ((1+a)**2-(1+a)**(-1))/(3*a) - 1)/a**2)
assert S.factor(J_expr-1/(3*(1+a)))==0
assert S.factor(S.diff(C,x,y)-(1+a)*(1+a*x*y*(2+a*x)*(2+a*y))/((1+a*x)**2*(1+a*y)**2))==0
# The admissibility polynomial for negative alpha is exact.
t = S.symbols('t',real=True)
assert S.expand(1-t*(2-t)**2-(1-t)*(t*t-3*t+1))==0
# For each n, the derivative of the positive-shape beta envelope
# changes sign exactly at s = 1+sqrt(n).
logder = n/(s-1)+(n-4)/(s+1)-(2*n-2)/s
assert S.factor(logder-2*(n-(s-1)**2)/(s*(s*s-1)))==0

def b(sval,m):
    ell=abs(sval*sval-1)/(3*sval*sval)
    return 2*abs(sval-1)/(sval+1)**3 * ell**(m-1)

s02=(S.sqrt(5)-1)/2
s0=sqrt((sqrt(5)-1)/2)
assert S.simplify(s02-S.Rational(39,50)**2).is_positive
assert S.simplify(S.Rational(787,1000)**2-s02).is_positive
assert 27*(1-Fraction(787,1000)) > (1+Fraction(787,1000))**3
lo=Fraction(39,50)
B2lo=2*(1-lo)/(1+lo)**3 * ((1-lo*lo)/(3*lo*lo))
assert B2lo < Fraction(1,54)
assert S.simplify(s02-S.Rational(4,7)).is_positive
# Exact ordering at lag one and all later lags follows from brackets,
# monotonicity on the negative branch, and lambda_neg < 1/4.
for m in range(1,16):
    u=1+sqrt(m)
    for tt in [u*0.7+0.3, u, u*1.3]:
        if tt <= 1: continue
        assert b(u,m)>=b(tt,m)-1e-13
    if m==1:
        assert b(s0,m)>b(u,m)
    else:
        assert b(u,m)>b(s0,m)
# Exact value of the n=2 positive benchmark at a=3 (s=2).
assert b(Fraction(2),2)==Fraction(1,54)
scaled_values=[]
for m in (20, 100, 1000, 10000):
    u=1+sqrt(m)
    scaled=(m*(u-1)/(u+1)**3)*(1-1/(u*u))**(m-1)
    scaled_values.append(scaled)
assert 0 < scaled_values[0] < scaled_values[1] < scaled_values[2] < scaled_values[3] < exp(-1)
assert abs(scaled_values[-1]-exp(-1))<0.02
print('PASS: exact algebra, positivity cutoffs, derivative, rational brackets, and finite sanity tests')
print('negative boundary s0=',s0)
for m in (1,2,3,4):
 print('lag',m,'negative_endpoint',b(s0,m),'positive_optimum',b(1+sqrt(m),m))
