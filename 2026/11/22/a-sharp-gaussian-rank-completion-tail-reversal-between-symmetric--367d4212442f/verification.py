#!/usr/bin/env python3
"""Reproduce exact inverse identities and scalar Gaussian tail checks."""
import math
import random
from sympy import Matrix, eye, Rational, zeros
from scipy.integrate import quad
from scipy.special import k0, ndtr

def blockdiag_null(C):
    m = C.rows
    A = zeros(m + 1)
    A[1:,1:] = C
    return A

def formula(C, p, q):
    h = C.inv()
    x, y = p[0], q[0]
    u = p[1:,:]
    v = q[1:,:]
    m = C.rows
    M = zeros(m + 1)
    M[0,0] = (1 + (v.T*h*u)[0])/(x*y)
    M[0,1:] = -v.T*h/y
    M[1:,0] = -h*u/x
    M[1:,1:] = h
    return M

rng = random.Random(417)
checks=0
for m in range(1,6):
    for trial in range(75):
        T = Matrix([[rng.randrange(-2,3) for _ in range(m)] for __ in range(m)])
        C = T.T*T + eye(m)
        p = Matrix([rng.choice([-4,-3,-2,-1,1,2,3,4]) for _ in range(m+1)])
        q = Matrix([rng.choice([-4,-3,-2,-1,1,2,3,4]) for _ in range(m+1)])
        for a,b in ((p,q),(p,p)):
            B = blockdiag_null(C)+a*b.T
            M = formula(C,a,b)
            assert B*M == eye(m+1)
            assert M*B == eye(m+1)
            assert B.det() != 0
            checks+=3

# High-accuracy product-normal small-ball identity: f(t)=K_0(|t|)/pi.
for eps in (1.e-3,1.e-4,1.e-5,1.e-6,1.e-7):
    probability = (2 / math.pi) * quad(k0, 0, eps, epsabs=1e-14)[0]
    ratio = probability / (eps*math.log(1/eps))
    assert 2/math.pi < ratio < 1.2
    checks+=1

# Half-normal small-ball asymptotic (symmetric rank-one projection).
for R in (1.e4, 1.e6, 1.e8):
    exact = 2*ndtr(1/math.sqrt(R))-1
    assert abs(exact*math.sqrt(R)/math.sqrt(2/math.pi)-1) < 5e-5
    checks+=1
print(f'PASS {checks} exact-matrix and scalar-distribution assertions')
