#!/usr/bin/env python3
"""Exact rational and independent numerical checks for two-site wrapped Erlang kernels.
Run: python3 VERIFY.py. Uses only the Python standard library.
Finite checking supplements the printed algebraic proof; it is not its substitute.
"""
from fractions import Fraction as F
from math import exp, log, factorial, sqrt

COUNT = 0

def check(condition, description):
    global COUNT
    COUNT += 1
    if not condition:
        raise AssertionError(description)

def power_sum(q, j):
    if j == 0: return 1 / (1 - q)
    if j == 1: return q / (1 - q)**2
    if j == 2: return q*(1 + q) / (1 - q)**3
    if j == 3: return q*(1 + 4*q + q*q) / (1 - q)**4
    raise ValueError('stage degree must be at most three')

def polynomial(k, q, z):
    from math import comb
    m = k-1
    return sum(comb(m,j)*power_sum(q,j)*z**(m-j) for j in range(m+1))

def product(k, q, z):
    return polynomial(k,q,z)*polynomial(k,q,1-z)

def factorization(k, q, z):
    t=z*(1-z)
    if k == 1: return 1/(1-q)**2
    if k == 2: return q/(1-q)**4 + t/(1-q)**2
    if k == 3: return q*(1+q)**2/(1-q)**6 + t*t/(1-q)**2
    if k == 4:
        return q*(q*q+4*q+1)**2/(1-q)**8 - 3*q*t*t/(1-q)**4 + t**3/(1-q)**2
    raise ValueError('stage must be at most four')

# Exact-rational polynomial identities, including asymmetric site locations.
qs=[F(1,2),F(1,3),F(1,10),F(1,100),F(2,3),F(7,11),F(17,19)]
zs=[F(i,32) for i in range(33)] + [F(1,7),F(3,11),F(9,13)]
for q in qs:
    for z in zs:
        for k in range(1,5):
            check(product(k,q,z)==factorization(k,q,z), f'factorization k={k}, q={q}, z={z}')
        t=z*(1-z)
        check(product(2,q,z)-product(2,q,F(0))==t/(1-q)**2, 'two-stage monotonic law')
        check(product(3,q,z)-product(3,q,F(0))==t*t/(1-q)**2, 'three-stage monotonic law')

# Exact boundary comparison for four stages at q = 1/2.
q=F(1,2)
t=F(1,4)
check(product(4,q,F(0))==F(1352), 'endpoint polynomial value')
check(product(4,q,F(1,2))==F(21609,16), 'antipode polynomial value')
check(product(4,q,F(1,10))-product(4,q,F(1,2))==F(19469,15625), 'strict finite-distance reversal')
check(product(4,q,F(0))-product(4,q,F(1,2))==F(23,16), 'contact/antipode difference')

q0=7-4*sqrt(3);q1=5-2*sqrt(6)
check(0<q0<q1<1, 'threshold order')
check(abs((1-q0)**2-12*q0)<1e-13, 'first boundary')
check(abs((1-q1)**2-8*q1)<1e-13, 'second boundary')

# Directly sum wrapped Erlang densities to check the exact winding formulas.
# The exponential factor cancels in the two-off-diagonal product.
for k in range(1,5):
    for q in (0.02,0.08,0.2,0.5,0.8):
        for z in (0.0,0.07,0.25,0.5,0.73,0.99):
            brute=sum((z+n)**(k-1)*q**n for n in range(500))
            analytic=polynomial(k,q,z)
            check(abs(brute-analytic)<1e-9*(1+abs(analytic)), 'independent winding sum')

# Perron eigenvalue monotonic with off-diagonal product for unequal site qualities.
for k in range(1,5):
    q=.5
    self_kernel=polynomial(k,q,0.0)
    v=[]
    for z in (0.05,0.1,0.25,0.5):
        product_ij=q*product(k,q,z)
        w1,w2=1.7,0.6
        rho=(self_kernel*(w1+w2)+sqrt(self_kernel**2*(w1-w2)**2+4*w1*w2*product_ij))/2
        v.append(rho)
    if k==1:
        check(max(v)-min(v)<1e-12, 'memoryless equality')
    if k in (2,3):
        check(all(a<b for a,b in zip(v,v[1:])), 'balanced stage two/three')
    if k==4:
        check(all(a>b for a,b in zip(v,v[1:])), 'four-stage reversal at q=1/2')

# Phase diagram numerical checks for generic q away from exact thresholds.
for q in (0.001,0.03,0.06,0.08,0.095,0.15,0.5,0.8):
    f0=product(4,q,0.0)
    fh=product(4,q,0.5)
    check((fh>f0)==(q<q0), 'global transition sign')
    t_star=2*q/(1-q)**2
    if t_star<.25:
        z=(1-sqrt(1-4*t_star))/2
        check(product(4,q,z)<min(f0,fh), 'interior minimum')
    else:
        check(all(product(4,q,i/100)>product(4,q,(i+1)/100) for i in range(50)), 'monotone to antipode')

print(f'PASS: {COUNT} deterministic assertions; four exact factorizations; sharp stage-four transition')
