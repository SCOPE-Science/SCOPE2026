"""Supplementary exact and numerical checks for a two-route connectivity allocation theorem.

Run: python verify.py
Requires: Python 3.10+ and SymPy. The analytic proof in RESULT.md is essential;
finite tests are consistency checks and not a substitute for its quantifiers.
"""
from fractions import Fraction
from math import exp, log, sqrt, isclose
from itertools import product
from random import Random
import sympy as S

checks = 0

def check(c, msg="assertion"):
    global checks
    assert c, msg
    checks += 1

s, x, u, v = S.symbols('s x u v', positive=True)
f = lambda t: s*t*(1-t)/(1-s*(1-t)**2)
D = -s*(u-v)*((1-s)*(u+v-1)+s*u*v)/((1-s*(1-u)**2)*(1-s*(1-v)**2))
check(S.factor(f(u)-f(v)-D)==0, 'derivative sign factorization')
C=s*(1-x*x)**2
E=1-(1-s*(1-x)**2)**2
check(S.factor(E-C-s*(1-x)**2*((1-s)*(1-2*x)-(1+s)*x*x))==0,'difference factorization')
y=S.sqrt(1-s)/(S.sqrt(2)+S.sqrt(1-s))
check(S.simplify(((1-s)*(1-2*x)-(1+s)*x*x).subs(x,y))==0,'critical root')
check(S.factor((E-C).subs({s:S.Rational(1,2),x:S.Rational(1,3)}))==0,'sharp tie')
check(C.subs({s:S.Rational(1,2),x:S.Rational(1,3)})==S.Rational(32,81),'exact success')


def success(sv, B, b):
    qa=sv*(-exp(-b/2))**2 if False else sv*(-__import__('math').expm1(-b/2))**2
    qb=sv*(-__import__('math').expm1(-(B-b)/2))**2
    return qa+qb-qa*qb

def critical(sv):
    return 4*log(1+sqrt(2/(1-sv)))

check(isclose(critical(.5),4*log(3),rel_tol=1e-14))
R=Random(20261119)
for sv in (.0001,.01,.1,.2,.5,.75,.9,.99,.9999):
    Bc=critical(sv)
    for factor in (.01,.1,.25,.5,.8,.9,.99,1.,1.01,1.1,1.25,1.5,2.,5.):
        B=Bc*factor
        conc=success(sv,B,0.)
        split=success(sv,B,B/2)
        if factor<1: check(conc>split-2e-14)
        if factor>1: check(split>conc-2e-14)
        if factor==1: check(isclose(conc,split,rel_tol=1e-12,abs_tol=1e-12))
        best=max(conc,split)
        for i in range(1001):
            b=B*i/1000
            check(success(sv,B,b)<=best+2e-13, (sv,B,b))
        for _ in range(300):
            b=B*R.random()
            check(success(sv,B,b)<=best+2e-13)
        # Check Jensen within each route independently under fixed route budgets.
        for _ in range(100):
            b=B*R.random()
            e1=b*R.random(); e2=b-e1
            check((1-exp(-e1))*(1-exp(-e2)) <= (1-exp(-b/2))**2+2e-14)

# One-link-per-route variant is always uniquely equal-funded.
for sv in (.01,.2,.5,.9,.99):
    for B in (.01,.1,1.,3.,10.,100.):
        def r1(b):
            q=sv*(-__import__('math').expm1(-b)); t=sv*(-__import__('math').expm1(-(B-b)))
            return q+t-q*t
        mid=r1(B/2)
        for i in range(999):
            b=B*(i+.5)/1000
            check(r1(b)<=mid+1e-13)
print('PASS:',checks,'exact identities, optimizer grid checks, and one-link comparisons')
