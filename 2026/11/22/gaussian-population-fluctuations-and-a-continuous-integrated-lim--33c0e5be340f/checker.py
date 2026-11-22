#!/usr/bin/env python3
"""Numerical consistency checks for excursion-occupancy fluctuation identities.

Standard-library only. These finite checks complement, and do not replace,
the analytic compensated-Poisson proofs in RESULT.md.
"""
import math
import random

RHO = 1.37
KAPPA = 2.0 * RHO * math.sqrt(2.0 / math.pi)
checks = 0


def check(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def close(x, y, tolerance=1e-10):
    check(abs(x-y) <= tolerance * (1.0+abs(x)+abs(y)),
          f"mismatch: {x!r} vs {y!r}")


def cov(s, t):
    return KAPPA*(math.sqrt(max(s,t))-math.sqrt(abs(t-s)))


def joint_means(s, t):
    assert 0 <= s <= t
    shared = KAPPA * (math.sqrt(t)-math.sqrt(t-s))
    left = KAPPA*math.sqrt(s) - shared
    right = KAPPA*math.sqrt(t) - shared
    return left, right, shared


def int_cov(s, t):
    if s > t:
        s,t=t,s
    return KAPPA*((2./3.)*s*t**1.5 -(2./15.)*s**2.5
                  -(4./15.)*t**2.5 +(4./15.)*(t-s)**2.5)


def midpoint_integral_cov(s, t, steps=280):
    ds, dt = s/steps, t/steps
    accum = math.fsum(cov((j+.5)*ds, (k+.5)*dt)
                      for j in range(steps) for k in range(steps))
    return accum*ds*dt


def tangent_cov(t0, eps, u, v):
    return (cov(t0+eps*u, t0+eps*v)-cov(t0+eps*u, t0)
            -cov(t0, t0+eps*v)+cov(t0, t0))/math.sqrt(eps)


def tangent_limit(u, v):
    return KAPPA*(math.sqrt(u)+math.sqrt(v)-math.sqrt(abs(u-v)))


def poisson(lam, rng):
    assert 0 <= lam < 20
    limit=math.exp(-lam)
    count=0
    prod=1.0
    while prod > limit:
        count += 1
        prod *= rng.random()
    return count-1


# Exact partition and one-time means, including all boundaries.
for s in [0,1,2,4,9,16,25,64,101]:
    for t in [x for x in [0,1,2,4,9,16,25,64,101] if x>=s]:
        left, right, shared=joint_means(s,t)
        check(min(left,right,shared) >= -1e-12,'negative Poisson category')
        close(left+shared,KAPPA*math.sqrt(s))
        close(right+shared,KAPPA*math.sqrt(t))
        close(shared,cov(s,t))
        close(cov(s,t),cov(t,s))
        close(cov(s,s),KAPPA*math.sqrt(s))

# Independent double quadrature of the integrated covariance.
for s,t in [(0,0),(1,1),(1,4),(4,9),(9,25),(16,16),(25,36)]:
    close(int_cov(s,t),int_cov(t,s))
    close(int_cov(s,s),4*KAPPA*s**2.5/15.)
    quadrature=midpoint_integral_cov(s,t)
    close(int_cov(s,t),quadrature,tolerance=0.00022)

# One-quarter self-similarity, increment moments and nonstationarity.
for s in [0,1,4,9,25]:
    for t in [1,4,9,25,36]:
        for scale in [0.1,0.5,2,5]:
            close(cov(scale*s,scale*t),math.sqrt(scale)*cov(s,t))
        if s<=t:
            v=cov(t,t)+cov(s,s)-2*cov(s,t)
            check(v >= -1e-12,'negative increment variance')
            check(v <= 2*KAPPA*math.sqrt(t-s)+1e-11,'increment bound')

# Strict difference of the variance of equal-length increments at two origins.
h=1.0
v_at_zero=cov(h,h)
t0=10000.
v_late=cov(t0+h,t0+h)+cov(t0,t0)-2*cov(t0+h,t0)
check(v_late>1.99*v_at_zero,'nonstationary increments mismatch')

# Local tangent covariance at every strictly positive origin.
for t0 in [0.5, 1, 7, 100]:
    for u,v in [(0,0),(0,1),(1,1),(1,4),(4,9),(3,5)]:
        target=tangent_limit(u,v)
        for eps,tolerance in [(1e-4,0.015),(1e-5,0.006),(1e-6,0.002)]:
            close(tangent_cov(t0,eps,u,v),target,tolerance)

# Approximate PSD for randomly chosen time configurations from indicator Gram law.
rng = random.Random(20261114)
for _ in range(500):
    times=sorted(rng.uniform(0,30) for j in range(6))
    a=[rng.uniform(-1,1) for j in range(6)]
    q=sum(a[i]*a[j]*cov(times[i],times[j]) for i in range(6)
          for j in range(6))
    check(q >= -1e-10,'covariance matrix not positive semidefinite')

# Bivariate-Poisson sampling against the exact shared category.
s,t=4.,9.
a,b,c=joint_means(s,t)
ns=30000
p_x=p_y=p_xy=0.
for _ in range(ns):
    left=poisson(a,rng)
    right=poisson(b,rng)
    shared=poisson(c,rng)
    x,y=left+shared,right+shared
    p_x+=x/ns
    p_y+=y/ns
    p_xy+=x*y/ns
close(p_x,KAPPA*math.sqrt(s),tolerance=0.02)
close(p_y,KAPPA*math.sqrt(t),tolerance=0.02)
close(p_xy-p_x*p_y,cov(s,t),tolerance=0.06)

# Centered Poisson third cumulant of a single rescaled count tends to zero.
for t in [1,4,9,16]:
    vals=[KAPPA*math.sqrt(t)/T**0.25 for T in [16,256,4096]]
    check(vals[0] > vals[1] > vals[2] > 0,'third cumulant scaling')
    close(vals[0]/vals[1],2)
    close(vals[1]/vals[2],2)

print(f'PASS: {checks} finite numerical and structural consistency checks')
print('NOTE: Analytic Poisson-integral and tightness proofs, not these checks,')
print('      establish the infinite-dimensional asymptotic statements.')
