"""Reproducible finite checks for a moment-collision theorem.

Run: python check_moment_collision.py
The theorem's strict convexity and intermediate-value steps are proved
analytically in RESULT.md, not inferred from numerical sampling.
"""
from fractions import Fraction as Q
import sympy as S

checks = 0

def test(condition, name):
    global checks
    assert bool(condition), name
    checks += 1

# Algebraically check the probability-generating-function factorization.
z = S.symbols('z')
for qv in (Q(1, 3), Q(2, 5), Q(3, 5), Q(5, 7)):
    for av in (Q(1, 7), Q(1, 2), Q(4, 5)):
        q, alpha = S.Rational(qv.numerator, qv.denominator), S.Rational(av.numerator, av.denominator)
        r = q * (q + alpha)/(1 + alpha*q)
        left = (1-alpha)*(1-q)/(1-q*z) + alpha*(1-q*q)/(1-q*q*z)
        right = (1-q)*(1+alpha*q)*(1-r*z)/((1-q*z)*(1-q*q*z))
        test(S.cancel(left-right) == 0, 'pgf factorization')
        a,b,c = q/(1-q), q*q/(1-q*q), r/(1-r)
        f = S.log(1+c*0)   # explicitly differentiate the full factorial-cumulant CGF
        t=S.symbols('t')
        L = -S.log(1-a*t)-S.log(1-b*t)+S.log(1-c*t)
        test(S.simplify(S.diff(L,t).subs(t,0)-(a+b-c))==0, 'kappa1')
        test(S.simplify(S.diff(L,t,2).subs(t,0)-(a*a+b*b-c*c))==0,'kappa2')
        test(S.simplify(S.diff(L,t,3).subs(t,0)-2*(a**3+b**3-c**3))==0,'kappa3')
        test(bool(b<c<a), 'strict pole location')

# Exact special rational point used to force two crossings.
q = S.Rational(3,5)
a = q/(1-q)
b = q*q/(1-q*q)
c = S.sqrt(a*a+b*b-1)
F = S.simplify(a**3+b**3-c**3)
test(S.simplify(F-(S.Integer(14553)-401*S.sqrt(401))/4096)==0, 'algebraic witness')
test(8409**2 - 401**3 == 6230080, 'positive integer discriminant')
test(8409**2 > 401**3, 'strict witness inequality')
test(S.simplify(c**2-(a+b-1)**2-S.Rational(7,16))==0, 'strict mean comparison')

# Numerical *diagnostic* of the two distinct intermediate-value branches.
import math

def F_of(q):
    a=q/(1-q); b=q*q/(1-q*q)
    c=math.sqrt(a*a+b*b-1)
    return a**3+b**3-c**3

def bisect(left,right,target):
    fleft=F_of(left)-target
    for _ in range(100):
        middle=(left+right)/2
        fm=F_of(middle)-target
        if fleft*fm<=0: right=middle
        else: left=middle; fleft=fm
    return (left+right)/2

lo=bisect(0.5,0.6,1.5)
hi=bisect(0.6,1/math.sqrt(2),1.5)
for root in (lo,hi):
    a=root/(1-root); b=root*root/(1-root*root)
    c=math.sqrt(a*a+b*b-1)
    r=c/(1+c)
    alpha=(r-root*root)/(root*(1-r))
    lam=1-a-b+c
    test(0<alpha<1 and lam>0, 'admissible interior parameters')
    test(abs(F_of(root)-1.5)<1e-11, 'third factorial cumulant')
    test(abs(lam+a+b-c-1)<1e-12, 'mean')
test(0.5<lo<0.6<hi<1/math.sqrt(2), 'distinct branches')
print('PASS:',checks,'checks; two numerical root diagnostics:',lo,hi)
