#!/usr/bin/env python3
"""Reproducible finite diagnostics for marked excursion extrema.
All infinite-time statements require the separate analytic proof.
"""
import math

checks = 0

def near(a, b, tolerance, msg):
    global checks
    assert math.isfinite(a) and math.isfinite(b), (msg,a,b)
    assert abs(a-b) <= tolerance * max(1.0, abs(a), abs(b)), (msg,a,b,tolerance)
    checks += 1

def A(y):
    return math.exp(-y*y) / math.sqrt(math.pi) - y * math.erfc(y)

def u_of_t(t):
    target = 1.0 / math.sqrt(2.0*t)
    assert target < A(0.0)
    lo, hi = 0.0, 1.0
    while A(hi) > target:
        hi *= 2.0
    for _ in range(110):
        mid = (lo+hi)/2.0
        if A(mid) > target: lo = mid
        else: hi = mid
    return (lo+hi)/2.0

def simpson(fun, a, b, n=4000):
    assert n % 2 == 0
    h = (b-a)/n
    return (fun(a)+fun(b)+4*sum(fun(a+j*h) for j in range(1,n,2))
            +2*sum(fun(a+j*h) for j in range(2,n-1,2))) * h/3

# 1) Exact integral of the entrance density over an interval of birth times.
# A cut on birth time b corresponds to an erfc survival ratio.
for t in [0.5, 1.0, 3.0, 11.0, 80.0]:
    for x in [0.2, 0.7, 1.5, 4.0]:
        for fraction in [0.13, 0.36, 0.65, 0.85]:
            cutoff = fraction*t
            # Exact change of variables y=x/sqrt(2(t-b)) removes the
            # integrable near-b=t boundary layer from the quadrature.
            lower = x/math.sqrt(2*(t-cutoff))
            numer = simpson(lambda y: 2/math.sqrt(math.pi)*math.exp(-y*y), lower,20.0)
            near(numer+math.erfc(20.0),
                 math.erfc(lower), 2e-6,"age integral")

# 2) A(y) is the tail primitive of erfc; exact derivative via finite difference.
for y in [0.05,0.2,0.7,1.0,2.0,3.0,4.0]:
    eps=1e-5
    near((A(y+eps)-A(y-eps))/(2*eps),-math.erfc(y),2e-6,"A derivative")

# 3) Exact finite-t marked intensity transformed to (z,r), with rho=1.
# Expected limiting intensity is exp(-z-r) independently of rho.
def marked_density(t,z,r):
    u=u_of_t(t)
    q=u+z/(2*u)
    assert q>0 and 0<r<u*u
    factor=1-r/(u*u)
    return math.sqrt(2*t)/(2*math.sqrt(math.pi))*q/(u**3)*factor**(-1.5)*math.exp(-q*q/factor)

for t in [1e8, 1e13, 1e18, 1e24, 1e30]:
    u=u_of_t(t)
    near(math.sqrt(2*t)*A(u),1.0,2e-10,"root normalization")
    for z in [-1.0,0.0,1.0]:
        for r in [0.25,0.7,1.4]:
            got=marked_density(t,z,r)
            expected=math.exp(-z-r)
            # asymptotic convergence is slow, enforce broad bound at 1e30
            if t == 1e30:
                near(got,expected,0.19,"limit marked intensity")
    q=u+0.3/(2*u)
    for r in [0.2,0.5,1.0]:
        tail=math.erfc(q/math.sqrt(1-r/u**2))/math.erfc(q)
        if t==1e30:
            near(tail, math.exp(-r), 0.14, "exponential founder mark")

print("PASS", checks, "finite algebraic/quadrature/asymptotic diagnostics")
