#!/usr/bin/env python3
"""Standalone diagnostics for a discrete predator/prey runaway theorem.

The finite checks here corroborate algebraic formulas and limit approximations;
the mathematical proof in RESULT.md establishes infinite-time convergence.
Requires Python 3 and mpmath (pip package).
"""
from fractions import Fraction as Q
import math
from mpmath import mp

alpha, xi, c, delta, gamma = Q(6, 5), Q(2), Q(1, 2), Q(11, 20), Q(4)
a = 1-c
H = 1+alpha*xi
k = xi-a*H
s = xi/H-delta
xstar = (xi-delta*H)/(delta-a)
ystar = (H+xstar)/a*(1-xstar/gamma)
assert (H, k, s, xstar, ystar) == (Q(17, 5), Q(3, 10), Q(13, 340), Q(13, 5), Q(21, 5))
assert alpha>1 and 0<c<1 and a<delta<xi/H and 0<xstar<gamma
P = lambda x: (a*x+xi)/(H+x)-delta
assert P(xstar)==0 and P(Q(1))==Q(1, 55) and P(gamma)==-Q(7, 740)
# The interior point has a real expanding and a real contracting multiplier.
J11=(1-xstar/gamma)*(1+xstar/(H+xstar))
J12=-a*xstar/(H+xstar)
J21=-k*ystar/(H+xstar)**2
B=J12*J21
assert 0<B<J11 and J11-B>0
T=float(J11+1)
D=float(J11-B)
l1=(T+math.sqrt(T*T-4*D))/2
l2=(T-math.sqrt(T*T-4*D))/2
assert l1>1 and 0<l2<1
# Strict rational wedge has q=exp(1/55), theta=exp(-3/22).
eps,Y=Q(1),Q(10)
assert eps<xstar and Y>(H+eps)/a
assert 1-a*Y/(H+eps)==-Q(3,22)

mp.dps=90
Hm=mp.mpf(H.numerator)/H.denominator
am=mp.mpf(a.numerator)/a.denominator
gm=mp.mpf(gamma.numerator)/gamma.denominator
xm=mp.mpf(xi.numerator)/xi.denominator
dm=mp.mpf(delta.numerator)/delta.denominator
sm=xm/Hm-dm

def approximate(n):
    logx=mp.log(mp.mpf(1)/4)
    logy=mp.log(mp.mpf(10))
    for j in range(n):
        x=mp.exp(logx)
        y=mp.exp(logy)
        logx += 1-x/gm-am*y/(Hm+x)
        logy += (am*x+xm)/(Hm+x)-dm
    L=mp.exp(logy-n*sm)
    C=am*L/(Hm*(mp.exp(sm)-1))
    logK=logx-n+C*(mp.exp(n*sm)-1)
    return L,logK
L1,k1=approximate(50)
L2,k2=approximate(80)
assert abs(L1-L2)<mp.mpf('1e-38'), (L1,L2)
assert abs(k1-k2)<mp.mpf('1e-38'), (k1,k2)
assert abs(L2-mp.mpf('9.84562775756377433227'))<mp.mpf('1e-18')
assert abs(k2-mp.mpf('-1.32704685670356087502'))<mp.mpf('1e-18')
print('witness: alpha=6/5 xi=2 c=1/2 delta=11/20 gamma=4')
print('equilibria: (gamma,0), (13/5,21/5)')
print('interior Floquet eigenvalues:',l1,l2)
print('L:',mp.nstr(L2,25))
print('log K:',mp.nstr(k2,25))
print('REFUGE_ESCAPE_VERIFY_OK')
