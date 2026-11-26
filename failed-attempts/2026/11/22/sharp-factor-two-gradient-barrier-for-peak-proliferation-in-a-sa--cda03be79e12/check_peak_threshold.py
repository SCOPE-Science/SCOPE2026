#!/usr/bin/env python3
"""Independent standard-library diagnostics for a two-state saturating transport model.

Infinite parameter-range theorems are proved analytically in RESULT.md; finite
checks here test transcriptions, a radical witness, and differentiations.
"""
import math
from fractions import Fraction

checks = 0

def check(cond, label):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(label)

# Exact witness at q=5/2 and y=atanh(1/3).
check(2 * 9072**2 - 12281**2 == 13779407, 'integer certificate')
check(2 * 9072**2 > 12281**2, 'positive radical gap')
check(Fraction(126, 125) > 1, 'central maximum')

def H(y, q, A, B, C):
    if y == 0:
        return C + B * q
    return (C + B * math.tanh(q*y)/math.tanh(y)) * math.cosh(y)**2

def log_derivative(x, u, g, v0, v1, gamma0, gamma1):
    t = math.tanh(u*x)
    if x == 0:
        return 0.0
    den = v0*v0 - v1*v1*t*t
    return 2*t/den*(u*v1*v1*(1-t*t)-gamma0*v1-gamma1*v0*math.tanh(g*x)/t)

def direct_derivative(x, u, g, v0, v1, gamma0, gamma1):
    def ip(y):
        t, s = math.tanh(u*y), math.tanh(g*y)
        return -2*(gamma0*v1*t + gamma1*v0*s)/(v0*v0-v1*v1*t*t)
    def logpref(y):
        t = math.tanh(u*y)
        return -math.log(v0*v0-v1*v1*t*t)
    d = 1e-5
    # Independent numerical differentiation of the algebraic prefactor.
    return (logpref(x+d)-logpref(x-d))/(2*d)+ip(x)

for q in (0.1, 0.5, 1.0, 1.25, 1.9, 1.99, 2.0):
    for B,C in ((1.0, 0.1), (0.03, 0.9), (3.0, 2.0)):
        prev = H(0.0,q,1,B,C)
        for i in range(1,101):
            y = 3*i/100
            new = H(y,q,1,B,C)
            check(new > prev, ('strict H increase',q,B,C,i))
            prev = new

for q in (0.6, 1.0, 2.0, 2.05, 2.5, 3, 4):
    for i in range(1,81):
        x = i / 40
        d1 = log_derivative(x,1,q,2.5,1,0.8,0.5)
        d2 = direct_derivative(x,1,q,2.5,1,0.8,0.5)
        check(abs(d1-d2)<2e-9, ('log derivative',q,i,d1,d2))

# Exact witness, with a strict nonzero sign margin at all three points.
q=2.5; u=1; v0=2; v1=1; b=21/125
check(H(0,q,1,2*b,b)>1, 'explicit center')
y0=0.5*math.log(2)
check(H(y0,q,1,2*b,b)<0.99, 'exact witness interior')
check(H(3,q,1,2*b,b)>1, 'explicit tail')
check(log_derivative(1e-3,1,q,v0,v1,b,b)<0,'center decreasing')
check(log_derivative(y0,1,q,v0,v1,b,b)>0,'interior increasing')
check(log_derivative(3,1,q,v0,v1,b,b)<0,'tail decreasing')

# For every queried q>2, construct the analytic family at a sufficiently small y.
for q in (2.01,2.05,2.1,2.5,3.0,4.0,10.0):
    L=max(2.0,8.0/(q*(q*q-4)))
    def K(y): return H(y,q,1,L,1)
    base=K(0)
    candidates=[i/5000 for i in range(1,3001)]
    ym=min(candidates,key=K)
    km=K(ym)
    check(km<base,('sharpness family',q))
    b=0.5*(1/base+1/km)
    check(b*base>1 and b*km<1 and b*K(4)>1,('sign sequence',q))
print('PASS:',checks,'deterministic checks; universal results use the analytic proof')
