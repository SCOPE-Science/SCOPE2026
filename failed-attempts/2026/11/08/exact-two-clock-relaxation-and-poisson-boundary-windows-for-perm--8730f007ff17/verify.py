#!/usr/bin/env python3
"""Finite, independently reproducible checks for the population-map identities."""
import math

PI = [1, 2, 3, 0]  # A single four-cycle on coordinates 1,...,4 (zero based here).
M = len(PI)

def perm(v):
    return [v[PI[k]] for k in range(M)]

def revperm(v):
    out = [0.0] * M
    for k, nxt in enumerate(PI):
        out[nxt] = v[k]
    return out

def q(v, a):
    pv = perm(v)
    return [a*v[k] + (1-a)*pv[k] for k in range(M)]

def iterate(x, a):
    z = x[-1]
    nxt = [2*z*y for y in q(x[:-1], a)]
    nxt.append(z*z+(1-z)*(1-z))
    return nxt

def norm(v):
    return math.sqrt(sum(a*a for a in v))

def diff(v, w):
    return norm([a-b for a,b in zip(v,w)])

def pois(v, t, backward=False):
    res = [0.0] * len(v)
    walk = v[:]
    mass = math.exp(-t)
    for k in range(75):
        for j in range(len(v)):
            res[j] += mass*walk[j]
        walk = revperm(walk) if backward else perm(walk)
        mass *= t/(k+1)
    return res

p = [0.07, 0.13, 0.41, 0.39]
z = 0.3
u = 2*z-1
for a in (0.0, 0.17, 0.5, 0.93, 1.0):
    x = [(1-z)*v for v in p] + [z]
    direction = p[:]
    for n in range(15):
        zr = (1+u**(2**n))/2
        exact = [(1-zr)*v for v in direction] + [zr]
        assert diff(x, exact) < 3e-14, (a,n, x,exact)
        x = iterate(x, a)
        direction = q(direction, a)
print('EXACT_NONLINEAR_LINEAR_FACTORISATION_OK')

for t in (0.3, 1.7, 4.0):
    for residue in range(4):
        n = 4000 + residue
        a = t/n
        d = p[:]
        for _ in range(n): d = q(d,a)
        pred = pois(p,t,backward=True)
        for _ in range(residue): pred = perm(pred)
        assert diff(d,pred) < 0.0017, ('near_zero',t,residue,d,pred)
    n = 4001
    a = 1-t/n
    d = p[:]
    for _ in range(n): d = q(d,a)
    pred = pois(p,t,backward=False)
    assert diff(d,pred) < 0.0017, ('near_one',t,d,pred)
print('BOTH_ENDPOINT_POISSON_WINDOWS_OK')

for a in (0.12,0.33,0.5,0.91):
    rho = math.sqrt(1-4*a*(1-a)*math.sin(math.pi/4)**2)
    # Fourier first harmonic, its exact l2 ratio equals rho per step.
    c = [math.cos(2*math.pi*k/4) for k in range(4)]
    for n in (1,3,13):
        d=c[:]
        for _ in range(n): d=q(d,a)
        assert abs(norm(d)/norm(c)-rho**n) < 4e-14
print('SHARP_SPECTRAL_FACTOR_OK')
print('PERMUTATION_QUADRATIC_POISSON_VERIFICATION_OK')
