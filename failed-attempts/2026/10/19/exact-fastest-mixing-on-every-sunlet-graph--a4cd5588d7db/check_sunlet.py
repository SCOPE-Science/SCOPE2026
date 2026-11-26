"""Exact identities and independent matrix checks for sunlet fastest-mixing weights."""
import math
import random
import numpy as np
import sympy as sp

x = sp.symbols('x', positive=True)
den = x*x + 2*x + 2
p = x*(x+1)/den
q = (x+2)/(2*den)
mu = 2*(x+1)/den
assert sp.factor(p+2*q-1) == 0
assert sp.factor(1-mu-x*x/den) == 0
assert sp.factor(mu**2-p**2-(1-p)**2-x*(x+2)*(2-x*x)/den**2) == 0
assert sp.factor(mu-(1-2*p)-x*(x+2)/den) == 0
assert sp.factor(p*p+(q*x*x)**2-(x/2)**2) == 0
assert sp.factor((1-p-q*x*x+x/2)-mu) == 0
# This checks the unsquared first-order condition of the strictly convex bound.
assert sp.factor((p-(x*x/2)**2*(1-p))-(1-x*x/2)*(x/2)) == 0


def matrix(n, ps, qr):
    # Peripheral vertices 0..n-1; pendant vertices n..2*n-1.
    P = np.zeros((2*n, 2*n), dtype=np.float64)
    for j in range(n):
        k = (j+1) % n
        P[j,k] = P[k,j] = qr
        P[j,n+j] = P[n+j,j] = ps
    P[np.diag_indices_from(P)] = 1 - P.sum(axis=1)
    return P


def exact_candidate(n):
    z = math.sqrt(1-math.cos(2*math.pi/n))
    d = z*z+2*z+2
    return z*(z+1)/d, (z+2)/(2*d), 2*(z+1)/d

random.seed(370910)
num_matrices = 0
num_parameter_trials = 0
for n in list(range(3, 31)) + [32, 40, 48, 64, 90]:
    ps, qr, target = exact_candidate(n)
    P = matrix(n, ps, qr)
    eigen = np.linalg.eigvalsh(P)
    val = np.max(np.abs(eigen[:-1]))
    assert abs(eigen[-1]-1) < 5e-13
    assert abs(val-target) < 2e-12, (n, val, target)
    assert P.min() > -1e-13 and np.max(np.abs(P-P.T)) < 1e-14
    assert np.max(np.abs(P.sum(axis=1)-1)) < 5e-13
    num_matrices += 1
    for trial in range(150):
        p1 = random.random()
        q1 = random.random()*(1-p1)/2
        t = 1-math.cos(2*math.pi/n)
        # The plus Fourier eigenvalue is a LOWER bound for arbitrary orbit weights.
        low = 1-p1-q1*t+math.hypot(p1,q1*t)
        assert low >= target-2e-12, (n,p1,q1,low,target)
        num_parameter_trials += 1

# Full finite-dimensional brute test on n=4 for an independent random subset of orbit weights.
for trial in range(200):
    p1 = random.random()
    q1 = random.random()*(1-p1)/2
    eig = np.linalg.eigvalsh(matrix(4,p1,q1))
    assert np.max(np.abs(eig[:-1])) >= exact_candidate(4)[2] - 1e-12
    num_matrices += 1

print(f'PASS symbolic identities; {num_matrices} independent full-matrix spectra; '
      f'{num_parameter_trials} random Fourier lower-bound tests; '
      f'boundary parameter intervals x^2 <= 3/2 proved analytically in RESULT.md.')
