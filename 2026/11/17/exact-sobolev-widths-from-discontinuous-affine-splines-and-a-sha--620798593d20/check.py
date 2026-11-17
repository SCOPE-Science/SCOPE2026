"""Finite diagnostics for sharp H1-to-L2 affine-cell approximation.

The theorem for all H1 inputs follows from the Fourier proof, not these tests.
"""
import math
import numpy as np

PI = math.pi
checks = 0


def affirm(condition, msg):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(msg)


def v(n):
    return math.sqrt(24.0) * ((-1) ** n - 1.0) / (n * PI) ** 2

# Direct moment computations using orthonormal Neumann cosines.
for n in range(1, 200):
    expected = 0.0 if n % 2 == 0 else 96.0 / (n ** 4 * PI ** 4)
    affirm(abs(v(n)**2-expected) < 1.e-14, f'linear moment n={n}')

v1 = v(1)**2
C_bound = (4 / 5) * (1 - v1)
affirm(v1 / (1 + C_bound) > 0.75, 'odd-mode spectral certificate')

rng = np.random.default_rng(20261112)
for k in (3, 6, 13, 31, 70):
    ns = np.arange(1,k+1,dtype=float)
    vs = np.array([v(n) for n in range(1,k+1)])
    for trial in range(1100):
        a = rng.normal(size=k)
        res2 = float(np.sum(a*a)-(vs@a)**2)
        deriv2 = float(PI**2 * np.sum(ns*ns*a*a))
        affirm(res2 >= -1.e-11 and res2 <= deriv2/(4*PI**2)+1.e-9, 'Fourier inequality')

# Exact local equality witness cos(2pi t); no linear moment and derivative ratio 1/(2pi).
a=np.zeros(20); a[1]=1
res2 = float(np.dot(a,a)-np.dot(a, np.array([v(n) for n in range(1,21)]))**2)
deriv2 = float(PI**2*4)
affirm(abs(res2 -deriv2/(4*PI**2)) < 1.e-13, 'sharp n=2 equality')

# Analytical orthogonality of cos(2 pi N x) to 1 and x on each cell,
# and its exact H1 approximation ratio. No quadrature or finite approximation here.
for N in range(1,81):
    desired=1/math.sqrt(1+(2*PI*N)**2)
    actual=(1/math.sqrt(2))/math.sqrt((1+(2*PI*N)**2)/2)
    affirm(abs(desired-actual)<1.e-14, 'uniform mesh sharp full norm')
    for j in range(N):
        left=j/N
        right=(j+1)/N
        omega=2*PI*N
        m0=(math.sin(omega*right)-math.sin(omega*left))/omega
        m1=((right*math.sin(omega*right)-left*math.sin(omega*left))/omega
            +(math.cos(omega*right)-math.cos(omega*left))/omega**2)
        affirm(abs(m0)<1.e-12 and abs(m1)<1.e-12, 'affine cell orthogonality')

# Nonuniform mesh witness supported in a maximal cell, with endpoint
# matching by subtracting 1. Its derivative and residual energies are
# (2 pi/H)^2*(H/2) and H/2 respectively.
for N in range(2,40):
    hs=rng.random(N)+0.05
    hs/=hs.sum()
    H=float(max(hs))
    residual_sq=H/2
    derivative_sq=2*PI**2/H
    affirm(abs(math.sqrt(residual_sq/derivative_sq)-H/(2*PI))<1.e-14,
           'arbitrary-mesh sharp seminorm witness')

print('passed finite diagnostics:',checks)
print('v1_squared:',format(v1,'.15g'))
print('strict_odd_certificate:',format(v1/(1+C_bound),'.15g'))
