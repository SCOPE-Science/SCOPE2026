#!/usr/bin/env python3
"""Exact checks for two mirror-symmetric noisy threshold queries.

Uses only Python's fractions and integer arithmetic. Finite checks supplement
an analytical proof; they do not certify any literature-absence assertion.
"""
from fractions import Fraction as Q
from math import isclose, sqrt

N = 0


def check(ok, message):
    global N
    if not ok:
        raise AssertionError(message)
    N += 1


def integrate_exact(delta, t):
    """Compute the full posterior Bayes risk by integrating each true-bit interval."""
    p, e = (1+delta)/2, (1-delta)/2
    intervals = [
        (Q(0),t,(0,0)),
        (t,1-t,(1,0)),
        (1-t,Q(1),(1,1)),
    ]
    risk=Q(0)
    probs=[]
    for y1 in (0,1):
        for y2 in (0,1):
            mass=Q(0);first=Q(0);second=Q(0)
            for a,b,truth in intervals:
                w=(p if y1==truth[0] else e)*(p if y2==truth[1] else e)
                mass += w*(b-a)
                first += w*(b*b-a*a)/2
                second += w*(b**3-a**3)/3
            probs.append(mass)
            if mass:
                risk += second-first**2/mass
    check(sum(probs)==1,'response masses')
    return risk


def formula(delta,t):
    if delta==1 and t==0:
        return Q(1,12)
    return Q(1,12)-2*delta**2*t**2*(1-t)**2/(1-delta**2+4*delta**2*t)


for d in [Q(0),Q(1,8),Q(1,4),Q(1,2),Q(3,4),Q(1)]:
    for t in [Q(0),Q(1,20),Q(1,7),Q(1,4),Q(1,3),Q(2,5),Q(1,2)]:
        check(integrate_exact(d,t)==formula(d,t),f'risk identity {d},{t}')

check(formula(Q(1),Q(1,3))==Q(1,108),'noiseless trisection')
check(formula(Q(1),Q(1,2))==Q(1,48),'noiseless midpoint')
check(formula(Q(1,2),Q(1,2))==Q(7,120),'noisy midpoint')
check(formula(Q(1,2),Q(1,3))==Q(85,1404),'noisy trisection')

# The theoretical optimum is an algebraic number; check polynomial residual
# and compare the exact-risk formula using float arithmetic at several strengths.
for d in (0.01,0.05,0.1,0.25,0.5,0.75,0.9,0.99,1.0):
    s=d*d
    t=(2*s-1+sqrt(1+2*s-2*s*s))/(6*s)
    check(1/3-1e-9<=t<=0.5+1e-9,'optimizer range')
    check(isclose(3*s*t*t+(1-2*s)*t-(1-s)/2,0.0,abs_tol=1e-11),'optimizer stationary')
    risk=float(formula(d,t))
    for other in [0.0,1/6,1/3,0.4,0.45,0.49,0.5]:
        check(risk<=float(formula(d,other))+1e-12,'competitor risk')
check((1-2*Q(1,4))**2==Q(1,4),'noise normalization')

print('EXACT_CHECKS_OK',N)
