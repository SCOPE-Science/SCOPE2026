#!/usr/bin/env python3
"""Standalone arithmetic checks for the lognormal moment-alias epidemic theorem.

No third-party modules required. Analytic proof of infinite moment equality,
root uniqueness, and isolated exceptional seeds is in RESULT.md.
"""
from decimal import Decimal, getcontext
from math import exp, pi, sqrt, sin

getcontext().prec = 72
D = Decimal

def arctan_series(x, n=90):
    s = D(0)
    p = x
    for j in range(n):
        s += p / D(2*j+1) * (1 if j % 2 == 0 else -1)
        p *= x*x
    return s

PI = 16*arctan_series(D(1)/5) - 4*arctan_series(D(1)/239)

def sine_series(x, n=65):
    term = x
    res = term
    for j in range(1,n):
        term = -term*x*x / D((2*j)*(2*j+1))
        res += term
    return res

omega = 2*PI / D(9)
def phi(z):
    return (-z*z / D(18)).exp() / (D(3)*(2*PI).sqrt())
def difference(z):
    return (-( (-z).exp() / D(2))).exp() - (-(z.exp()/D(2))).exp()

# On each subinterval of [0,9/2], the positive part of -H(1/2)
# is bounded below using a decreasing Gaussian density, increasing
# difference function, and concavity of sine on [0,pi].
subtotal = D(0)
for j in range(18):
    a = D(j)/4
    b = D(j+1)/4
    s = min(sine_series(omega*a),sine_series(omega*b))
    subtotal += (b-a)*phi(b)*s*difference(a)
# Standard Mills inequality bounds Gaussian upper tail by 2 phi(9/2).
tail_bound = 2*phi(D(9)/2)
assert subtotal > D('0.1979'), subtotal
assert tail_bound < D('0.0864'), tail_bound
negative_bound = D('0.1979') - D('0.0864')
assert negative_bound > D('0.1115') - D('0.0000001')
# Attacks differ by at least 2*(4/5)*(9/10)*(-H(1/2)).
attack_gap_lower = D(2)*D(4)/D(5)*D(9)/D(10)*negative_bound
assert attack_gap_lower > D('0.16'), attack_gap_lower

# Illustrative quadrature, not used for the analytic proof.
def f_float(z):
    return exp(-z*z/18)/(3*sqrt(2*pi))
def laplace(a,q,half_steps=12000):
    left=-24.0;right=24.0;n=2*half_steps
    dx=(right-left)/n
    def fun(z):
        try: attenuation=exp(-q*exp(z))
        except OverflowError: attenuation=0.0
        return f_float(z)*(1+a*sin(2*pi*z/9))*attenuation
    res=fun(left)+fun(right)
    for j in range(1,n):
        res+=(4 if j%2 else 2)*fun(left+j*dx)
    return res*dx/3

def root(a,gamma,r=0.2):
    lo=0.0;hi=1/gamma
    for _ in range(60):
        q=(lo+hi)/2
        F=1-(1-r)*laplace(a,q)-gamma*q
        if F>0:lo=q
        else:hi=q
    return (lo+hi)/2

if __name__=='__main__':
    print('finite lower sum:',subtotal)
    print('Gaussian tail upper bound:',tail_bound)
    print('proved -H(1/2) >',negative_bound)
    print('proved attack-fraction separation >',attack_gap_lower)
    L0=laplace(0,0.5)
    H=(laplace(1,0.5)-laplace(-1,0.5))/2
    gamma=2*(0.2+0.8*(1-L0))
    qminus=root(-.9,gamma);qplus=root(.9,gamma)
    print('illustrative L0(1/2), H(1/2):',L0,H)
    print('illustrative gamma:',gamma)
    print('illustrative final pressures:',qminus,qplus)
    print('illustrative attack fractions:',gamma*qminus-.2,gamma*qplus-.2)
    assert H<-.1115 and qminus < .5 < qplus
    assert gamma*(qplus-qminus)>.16
    # Exact algebraic expression of the integer-moment sine multiplier is sin(2*pi*n)=0.
    for n in range(12):
        assert abs(sin(2*pi*n)) < 1e-13
    print('All arithmetic checks passed; infinite statements use the written proof.')
