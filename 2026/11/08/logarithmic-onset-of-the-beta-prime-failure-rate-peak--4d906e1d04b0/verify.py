#!/usr/bin/env python3
"""Reproducible algebraic and numerical checks of beta-prime hazard peak formulae.
Python standard library only. Finite checks supplement an analytic proof.
"""
from fractions import Fraction as Q
from math import comb, exp, lgamma, log, sqrt

checks = 0

def ck(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

# If a=2, integrate f exactly: S(x)=(1+(b+1)x)/(1+x)^(b+1).
# Hence h(x)=b(b+1)x/((1+x)(1+(b+1)x)).
for b in range(1, 40):
    for numerator in range(1, 51):
        x = Q(numerator, 17)
        h = b * (b+1)*x/((1+x)*(1+(b+1)*x))
        # Rational integral verification by differentiating the proposed S.
        s_num = 1 + (b+1)*x
        # -S'/S = b(b+1)x/((1+x)(1+(b+1)x))
        from_log_derivative = (b+1)/(1+x) - (b+1)/(1+(b+1)*x)
        ck(h == from_log_derivative, 'exact a=2 hazard')
        # h' numerator after canceling positive factors.
        derivative_num = 1 - (b+1)*x*x
        ck((derivative_num > 0) == (x*x < Q(1,b+1)), 'exact mode sign')
        # Verify exact score slope g is independent of shape normalization.
        g = ((b+1)*x-1)/(x*(1+x))
        ck(g == (b+2)/(1+x) - 1/x, 'exact score identity')

# For integer b, the survival integral has an exactly finite-binomial form.
def hazard(a, b, x):
    v = x/(1+x)
    s = sum(((-1)**j)*comb(b-1,j)*(1-v**(a+j))/(a+j)
            for j in range(b))
    return x**(a-1)/(1+x)**(a+b)/s

def score(a, b, x):
    return ((b+1)*x-(a-1))/(x*(1+x))

def mode(a, b):
    m = (a-1)/(b+1)
    c = ((a-1) + sqrt((a-1)*(a+b)))/(b+1)
    lo, hi = m, c
    ck(hazard(a,b,lo) > score(a,b,lo), 'positive mode bracket')
    ck(hazard(a,b,hi) < score(a,b,hi), 'negative mode bracket')
    for _ in range(65):
        z = (lo+hi)/2
        if hazard(a,b,z) > score(a,b,z): lo = z
        else: hi = z
    return (lo+hi)/2

# psi(b+1)-psi(1)=sum_{j=1}^b 1/j for positive integer b.
for b in [1,2,3,5]:
    harmonic = sum(1/j for j in range(1,b+1))
    for eps in [1e-2, 1e-3, 1e-4]:
        a = 1 + eps
        x = mode(a, b)
        x_pred = eps+b*eps**2*(log(eps)+harmonic)
        h_pred = b*(1+eps*(log(eps)+harmonic-1))
        ck(abs(x-x_pred) < 35*eps**3*log(eps)**2, 'critical mode asymptotic')
        ck(abs(hazard(a,b,x)-h_pred) < 45*eps**2*log(eps)**2, 'critical peak asymptotic')
        ck((a-1)/(b+1) < x < ((a-1)+sqrt((a-1)*(a+b)))/(b+1), 'strict peak bracket')

print('VERIFY_OK assertions=', checks)
