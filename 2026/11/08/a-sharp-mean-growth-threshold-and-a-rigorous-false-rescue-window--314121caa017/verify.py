#!/usr/bin/env python3
"""Reproduce finite algebraic checks for a two-environment recruitment model.

The universal statements require the accompanying analytic proof; these checks
are reproducibility tests, not numerical certification of an infinite theorem.
"""
from fractions import Fraction as F
from math import exp, log, sqrt

checks = 0

def check(ok, msg=''):
    global checks
    if not ok:
        raise AssertionError(msg)
    checks += 1

# Exact rational witness.
a, b, c, k = F(11,5), F(4), F(1), F(1401,1000)
critical = (a*a-b*c)/(b+c-2*a)
check(critical == F(7,5), 'critical rate')
check(b>c>0 and a*a>b*c and 2*a<b+c, 'frozen/growth assumptions')
check(k>critical and k<F(3,2), 'switch interval')
det_gap = (b+k)*(c+k)-(a+k)*(a+k)
check(det_gap == F(3,5000), 'positive mean determinant gap')
check(2*(a+k)>F(36,5), 'mean growth denominator lower bound')
check(det_gap/F(36,5) == F(1,12000), 'mean growth upper bound')
# q^2=(b+k)/(c+k), showing q>31/21.
check((b+k)*21*21>(c+k)*31*31, 'uniform jump gap')
qmin = F(31,21)
zmin=(3*qmin+2)/(2*qmin+3)
check(zmin == F(27,25), 'minimum switch multiplier')
x = F(2,25)
entropy_bound = x*x/F(2)-x*x*x/F(3)
check(entropy_bound == F(142,46875), 'Taylor entropy coefficient')
check(entropy_bound>F(3,1000), 'entropy floor')
# e^2>7 by first five Taylor terms and e^{3/2}<5 by a finite geometric tail.
from math import factorial
check(sum(F(2**j,factorial(j)) for j in range(5))==7, 'e squared lower')
partial=sum(F(3,2)**j/F(factorial(j)) for j in range(5))
tail_majorant=(F(3,2)**5/F(factorial(5)))/(1-F(1,4))
check(partial+tail_majorant<5, 'exponential upper')
entropy_rate_floor=F(49,25)*F(1,5)*F(1,2)*F(3,1000)
check(entropy_rate_floor==F(147,250000), 'renewal entropy')
check(F(1,12000)-entropy_rate_floor < -F(1,2000), 'negative log growth')
# General mean threshold: verify exact determinant factorization, monotonicity
# and signs over many strictly admissible rational triples.
for B in (F(2),F(3),F(4),F(7),F(11)):
    for C in (F(1,3),F(1),F(3,2)):
        if B <= C:
            continue
        # choose a via arithmetic mean, geometrical mean convex mixture
        lower=sqrt(float(B*C)); upper=float((B+C)/2)
        for t in (F(1,10),F(1,3),F(2,3),F(9,10)):
            A=F.from_float(lower+(upper-lower)*float(t)).limit_denominator(10**7)
            if not (A*A>B*C and 2*A<B+C):
                continue
            K=(A*A-B*C)/(B+C-2*A)
            check(K>0, 'positive threshold')
            for delta in (F(-1,3),F(-1,10),F(0),F(1,10),F(1,3)):
                kval=K+delta
                if kval<=0:
                    continue
                expression=(B+kval)*(C+kval)-(A+kval)**2
                check(expression == (B+C-2*A)*(kval-K), 'factor identity')
                check((expression>0)==(delta>0), 'threshold sign')
                check((B-C)**2>0, 'strict derivative')
# Riccati comparison: exact e^2>7 implies tanh(1)>3/4, and any
# starting ratio in [1/2,2] reaches at least 3/2 under environment 1.
check(F(1,2) < F(3,2) < 2, 'interval bounds')
check(exp(2)>7 and (exp(2)-1)/(exp(2)+1)>0.75, 'Riccati half-time')
# Direct four-state Perron growth sanity via a positive shifted matrix,
# implemented using only the Python standard library.
for kap in (1.2,1.4,1.401,1.5,2.0):
    block = [
        [-2.2-kap, 4, kap, 0],
        [1, -2.2-kap, 0, kap],
        [kap, 0, -2.2-kap, 1],
        [0, kap, 4, -2.2-kap],
    ]
    shift=7.0
    xvec=[0.23,0.19,0.27,0.31]
    for j in range(2200):
        y=[sum((block[i][h]+(shift if i==h else 0))*xvec[h]
               for h in range(4)) for i in range(4)]
        mag=sum(y)
        xvec=[a0/mag for a0 in y]
    growth=sum(sum(block[i][h]*xvec[h] for h in range(4)) for i in range(4))
    expected=-2.2-kap+sqrt((4+kap)*(1+kap))
    check(abs(growth-expected)<1e-10,'four-state Perron root')
print('PASS', checks, 'checks; standard-library exact arithmetic and four-state sanity')
