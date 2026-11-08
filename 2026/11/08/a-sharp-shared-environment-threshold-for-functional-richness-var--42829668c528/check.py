#!/usr/bin/env python3
"""Exact arithmetic checks of a paired-guild shared-environment variance theorem."""
from fractions import Fraction
from itertools import product
from math import comb
import sympy as s


def rising(x, n):
    out = Fraction(1)
    for i in range(n):
        out *= x + i
    return out


def direct(g, p, theta):
    """Sum each binary survival configuration from a Beta-binomial exchangeable law."""
    alpha, beta = p * theta, (1-p) * theta
    den = rising(theta, 2*g)
    mean = Fraction(0)
    second = Fraction(0)
    prob_total = Fraction(0)
    for surv in product((0, 1), repeat=2*g):
        k = sum(surv)
        w = rising(alpha, k) * rising(beta, 2*g-k) / den
        y = sum(int(surv[2*i] or surv[2*i+1]) for i in range(g))
        prob_total += w
        mean += w*y
        second += w*y*y
    assert prob_total == 1
    return second-mean*mean


def moments(g, p, theta):
    q = 1-p
    u = q*(q*theta+1)/(theta+1)
    v = q*(q*theta+1)*(q*theta+2)*(q*theta+3)/((theta+1)*(theta+2)*(theta+3))
    return g*u+g*(g-1)*v-g*g*u*u


def symbolic_check():
    x, p, g = s.symbols('x p g')
    q=1-p
    u = q*(q*x+1)/(x+1)
    v = q*(q*x+1)*(q*x+2)*(q*x+3)/((x+1)*(x+2)*(x+3))
    V = g*u+g*(g-1)*v-g*g*u*u
    cs = [
        -6*(12*g*q-11*g+5),
        -6*(12*g*q*q+8*g*q-23*g+12*q+7),
        -102*g*q*q+82*g*q+90*g-18*q*q-156*q+7,
        -34*g*q*q+86*g*q+18*g-40*q*q-106*q+29,
        8*g*q*q+20*g*q-28*q*q-22*q+11,
        (4*g-6)*q*q+1,
    ]
    H = sum(c*x**i for i,c in enumerate(cs))
    deriv = g*p*(p-1)*H/((x+1)**3*(x+2)**2*(x+3)**2)
    assert s.cancel(s.diff(V,x)-deriv)==0
    qc=(11*g-5)/(12*g)
    B=12*g*q*q+8*g*q-23*g+12*q+7
    assert s.factor(B.subs(p,1-qc)+(67*g*g-66*g+35)/(12*g))==0
    return True


def main():
    symbolic_check()
    ncases=0
    for g in range(2,6):
        for p in (Fraction(1,10), Fraction(1,5), Fraction(1,2), Fraction(4,5)):
            for theta in (Fraction(1,3), Fraction(1,1), Fraction(3,2)):
                assert direct(g,p,theta)==moments(g,p,theta)
                ncases+=1
    g,p,theta=2,Fraction(1,5),Fraction(1,3)
    v=moments(g,p,theta)
    assert v==Fraction(2052,3125)
    assert v>Fraction(16,25)
    assert v>Fraction(288,625)
    # Additional exact endpoint/derivative-value consistency at selected rational parameters.
    x=s.symbols('x',positive=True)
    for g in [2,3,5,10]:
        for p in [s.Rational(1,10), s.Rational(1,2)]:
            q=1-p
            u=q*(q*x+1)/(x+1)
            v4=q*(q*x+1)*(q*x+2)*(q*x+3)/((x+1)*(x+2)*(x+3))
            vv=g*u+g*(g-1)*v4-g*g*u*u
            assert s.limit(vv,x,0)==g*g*p*(1-p)
            assert s.limit(vv,x,s.oo)==g*(2*p-p*p)*(1-p)**2
    print('PASS: symbolic identity, coefficient normalization,',ncases,'complete configuration comparisons, endpoint limits and rational witness')


if __name__=='__main__':
    main()
