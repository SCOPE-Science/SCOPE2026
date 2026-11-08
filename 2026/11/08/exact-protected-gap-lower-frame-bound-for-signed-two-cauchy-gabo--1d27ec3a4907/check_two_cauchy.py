#!/usr/bin/env python3
"""Finite checks for a signed two-Cauchy critical Gabor frame theorem.

Numerical tests only; the universal frame-bound formula follows from the
concavity and endpoint argument in RESULT.md.
"""
import cmath
import math
import random

PI = math.pi
RNG = random.Random(20261104)
checks = 0


def eq(x, y, tol=2e-8):
    global checks
    assert abs(x-y) <= tol*max(1.,abs(x),abs(y)), (x,y)
    checks += 1


def frame_fiber(alpha, u, v, first_residue, R, theta, omega):
    """alpha * |Zak(g)|**2 for omega scaled to the unit Zak cell [0,1]."""
    t = u/v
    k = -math.log(u)/math.log(t)
    s = t**omega
    z = cmath.exp(1j*theta)
    a = u*s**k - R*v*s**(k+1)
    b = u*v*s**k*(1-R*s)
    f = 2*PI*abs(first_residue)/math.sqrt(alpha)*abs(a-b*z)
    f /= abs(1-u*z)*abs(1-v*z)
    return f*f


def protected_formula(alpha,u,v,first_residue,R):
    t=u/v
    lo=t*(1+v)/(1+u)
    hi=(1-v)/(1-u)
    assert lo<R<hi
    K=4*PI**2*abs(first_residue)**2/alpha
    return K*min((v*(R-lo)/(1+v))**2,((hi-R)/(1-v))**2)


# Exact shape and endpoint identities, supplemented by a dense deterministic grid.
accepted = 0
for case in range(230):
    u,v = sorted((RNG.uniform(0.06,0.97),RNG.uniform(0.02,0.92)), reverse=True)
    if u+v+u*v <= 1+0.015:
        continue
    t = u/v
    lo = t*(1+v)/(1+u)
    hi = (1-v)/(1-u)
    eq((hi-lo)*v*(1-u*u), (u-v)*(u*v+u+v-1), 1e-10)
    for frac in (0.04,0.26,0.49,0.75,0.96):
        ratio = lo+frac*(hi-lo)
        alpha=RNG.uniform(0.3,2.5)
        a=RNG.uniform(0.5,2)
        predicted=protected_formula(alpha,u,v,a,ratio)
        boundary=min(frame_fiber(alpha,u,v,a,ratio,math.pi,0),
                     frame_fiber(alpha,u,v,a,ratio,0,1))
        eq(predicted,boundary)
        for j in range(13):
            for h in range(17):
                z=frame_fiber(alpha,u,v,a,ratio,math.pi*h/16,j/12)
                assert z >= predicted-1e-10*max(1,predicted), (case,frac,h,j,z,predicted)
                checks += 1
    # Unique max-min residue choice, checked against the meeting of the two branches.
    Rstar=((1+v)*hi+v*(1-v)*lo)/(1+2*v-v*v)
    opt=protected_formula(1.,u,v,1.,Rstar)
    closed=4*PI**2*(v*(hi-lo)/(1+2*v-v*v))**2
    eq(opt,closed)
    for zz in (.03,.4,.9):
        probe=protected_formula(1.,u,v,1.,lo+zz*(hi-lo))
        assert probe <= opt+1e-10*max(1,opt)
        checks += 1
    accepted += 1

# Verify the Zak closed form against symmetric partial sums for single Cauchy poles.
# The cutoff is finite and the comparison is intentionally not called an identity proof.
for alpha,w,x,phase in ((1.,.12,.31,.37),(.7,.24,.18,.63), (1.2,.33,.83,.41)):
    cutoff = 17000
    s = 0j
    for n in range(-cutoff,cutoff+1):
        s += cmath.exp(2j*PI*n*phase)/(x-alpha*n-1j*w)
    r = math.exp(-2*PI*w/alpha)
    z = cmath.exp(-2j*PI*x/alpha)
    exact=(2j*PI/alpha)*cmath.exp(2j*PI*phase*x/alpha)*math.exp(2*PI*w*phase/alpha)*r*z/(1-r*z)
    eq(s,exact,3e-4)

assert accepted >= 75
print('TWO_CAUCHY_PROTECTED_GAP_CHECKS_PASS',checks,'cases',accepted)
