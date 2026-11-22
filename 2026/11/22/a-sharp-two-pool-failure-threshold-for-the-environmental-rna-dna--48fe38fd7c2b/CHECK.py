#!/usr/bin/env python3
"""Independent, finite supplementary checks for a two-pool eRNA/eDNA decay theorem.

The analytic proof is in RESULT.md; this script does not certify an infinite domain.
Standard-library only; deterministic and reproducible.
"""
from fractions import Fraction
from math import exp, log


def P(q, x):
    return q*q*x**4 - 4*q*q*x**3 - 6*q*x*x - 4*x + 1


def F(q, x):
    return q*x*(1-2*x-q*x*x) / ((1+q*x)*(1+q*x*x))


def raw_F(q, x):
    return q*x/(1+q*x)-2*q*x*x/(1+q*x*x)


def Pprime(q, x):
    return 4*q*q*x**3-12*q*q*x*x-12*q*x-4


def bisection(fn, lo, hi, n=100):
    a, b = lo, hi
    fa, fb = fn(a), fn(b)
    assert fa * fb < 0, (a, b, fa, fb)
    for _ in range(n):
        m=(a+b)/2
        if fn(m)*fa>0:
            a,fa=m,fn(m)
        else:
            b,fb=m,fn(m)
    return (a+b)/2


assert 3*24**20 > 25**20
assert 16*1088**20 < 1285**20
assert F(Fraction(1),Fraction(1,3)) == Fraction(1,20)
checks=3
for qint in (1,2,3,5,11,23):
    q=Fraction(qint)
    c=1/(1+(1+float(q))**0.5)
    root=bisection(lambda x:P(float(q),x),0.0,1.0)
    assert 0 < root < c < 1
    assert P(q,Fraction(0))==1
    assert P(q,Fraction(1))==-3*(q+1)**2
    for j in range(1,1001):
        x=Fraction(j,1002)
        assert F(q,x)==raw_F(q,x)
        assert Pprime(q,x)<0
        checks+=2
    for j in range(1,100):
        x=j/100
        h=1e-6
        num_deriv=(F(float(q),x+h)-F(float(q),x-h))/(2*h)
        exact_form=float(q)*float(P(float(q),x))/((1+float(q)*x)**2*(1+float(q)*x*x)**2)
        assert abs(num_deriv-exact_form)<2e-5, (q,x,num_deriv,exact_form)
        checks+=1

root=bisection(lambda x:P(1.,x),0.,1.)
peak=F(1.,root)
assert abs(root-.1895910507314648)<1e-12
assert abs(peak-.08997983978549)<1e-11
assert peak>1/20
x_l=bisection(lambda x:F(1.,x)-.05,.00000001,root)
x_r=bisection(lambda x:F(1.,x)-.05,root,1/(1+2**.5))
t_min,t_max=-log(x_r),-log(x_l)
assert 0<t_min<t_max
Q=lambda t:exp(-t/20)*(1+exp(-2*t))/(1+exp(-t))
assert Q(0)>4/5>Q(log(3))
assert Q(log(16))>4/5>Q(200)
assert Q(t_min)<Q(t_max)
assert abs(t_min-log(3))<1e-9
checks+=12
print('PASS: %d deterministic supplementary checks' % checks)
print('quartic root x* = %.15f, threshold s* = %.15f' % (root,peak))
print('minimum time = %.12f, maximum time = %.12f' % (t_min,t_max))
print('values at ln 3 and ln 16: %.12f, %.12f' % (Q(log(3)),Q(log(16))))
