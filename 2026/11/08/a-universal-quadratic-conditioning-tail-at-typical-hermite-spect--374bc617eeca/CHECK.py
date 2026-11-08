"""Reproducible checks of the Hermite-zero conditioning formulas.

Pure Python 3 standard library; confirms algebraic identities and compares
independent numerical integrals with the proposed closed expressions.
This script supplies finite checks, not a substitute for the theorem's proof.
"""
from fractions import Fraction as F
from math import exp, sqrt


def simpson(fun, left, right, intervals=12000):
    assert intervals % 2 == 0
    step = (right-left)/intervals
    summ = fun(left) + fun(right)
    for j in range(1, intervals):
        summ += (4 if j & 1 else 2)*fun(left+j*step)
    return summ*step/3


def surv_numeric(n, k):
    a, b = n+1., float(n)
    e = (a*a+b*b)/(a+b)
    c = 4*a*a*b*b/e
    q = (k-1.)/(k+1.)
    # Direct ratio density integrated on t<1 and t>1 after t -> 1/t.
    fun = lambda t: c*t*(1-t*t)*((b+a*t*t)**(-3)+(a+b*t*t)**(-3))
    return simpson(fun, q, 1.)


def antiderivative(a, b, y):
    return (1/F(b+a*y)-F(a+b, 2*(b+a*y)**2))/F(a*a)


def surv_exact(n, k):
    a, b = n+1, n
    e = F(a*a+b*b, a+b)
    c = F(2*a*a*b*b, 1)/e
    q = F(k-1, k+1)
    return c*(antiderivative(a,b,F(1))-antiderivative(a,b,q*q)
             +antiderivative(b,a,F(1))-antiderivative(b,a,q*q))


def tail_const(n):
    a,b=n+1,n
    return F(32*a*a*b*b, (a*a+b*b)*(a+b)**2)


def gaussian_step_form(n, t):
    a,b = n+1.,float(n)
    e=(a*a+b*b)/(a+b)
    c=4*a*a*b*b/e
    return c*t*abs(1-t*t)/(b+a*t*t)**3


def signed_moments(n):
    a,b=n+1,n
    e=F(a*a+b*b,a+b)
    assert F(a*a+b*b,a+b)==e
    assert F(a*a, a*a+b*b)+F(b*b,a*a+b*b)==1
    assert F(a*a-b*b, (a+b)*1) == 1


for n in (1,2,3,5,11,50):
    signed_moments(n)
    for k in (1,2,3,7,11,25,51):
        analytic=float(surv_exact(n,k))
        direct=surv_numeric(n,k)
        assert abs(analytic-direct)<2e-9, (n,k,analytic,direct)
    # Sharp large-k constant is obtained independently by the exact CDF.
    for k in (1000,10000):
        approximate=k*k*float(surv_exact(n,k))
        target=float(tail_const(n))
        assert abs(approximate-target)<2e-4, (n,k,approximate,target)

# Limit in Hermite order for k=1,2,3,9.
for k in (1,2,3,9):
    expected=4*k*k/(k*k+1)**2
    assert abs(float(surv_exact(100000,k))-expected)<2e-5

# The same first-intensity formula derived from asymmetric exponentials.
for n in (1,2,7,50):
    a,b=n+1,n
    avg_abs=F(a*a+b*b,a+b)
    expected=F(2*n+1,2)+F(1,4*n+2)
    assert avg_abs==expected
print('HERMITE_PALM_CONDITIONING_CHECKS_PASSED')
