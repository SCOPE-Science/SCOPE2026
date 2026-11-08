#!/usr/bin/env python3
"""Reproducible checks for the sketched harmonic Ritz positivity threshold.

Requires Python 3 and NumPy; runs in exact-arithmetic reasoning plus numerical tests.
This script is supplementary evidence, not a substitute for the proof.
"""
import math
import numpy as np

rng = np.random.default_rng(20261104)
checks = 0

# Algebraic two-by-two witnesses. For A=diag(1,k), b=(sqrt(k),1),
# S^T S=[[1,-eps],[-eps,1]], one has
# G=2*k-eps*sqrt(k)*(k+1) and
# F=k*(k+1-2*eps*sqrt(k)).
for kappa in (1.01, 1.2, 2., 9., 25., 100., 10000.):
    c = 2*math.sqrt(kappa)/(kappa+1)
    assert 0 < c < 1
    b = np.array([math.sqrt(kappa), 1.0])
    A = np.diag([1., kappa])
    z = A@b
    for eps in (c/3., 0.99*c, (c+1)/2., 0.999999):
        W = np.array([[1., -eps],[-eps, 1.]])
        g = z@W@b
        f = z@W@z
        g_ref = 2*kappa-eps*math.sqrt(kappa)*(kappa+1)
        f_ref = kappa*(kappa+1-2*eps*math.sqrt(kappa))
        scale=max(1., abs(g_ref), abs(f_ref))
        assert abs(g-g_ref)/scale < 2e-12
        assert abs(f-f_ref)/scale < 2e-12
        assert min(np.linalg.eigvalsh(W)) > 0
        assert f > 0
        assert (g > 0) == (eps < c)
        assert (f/g > 0) == (eps < c)
        checks += 1

# The limiting geometry ratio is exactly the eigenvalue-endpoint minimum.
for kappa in (1.2, 2., 9., 500.):
    w = np.array([math.sqrt(kappa), 1.0])
    A = np.diag([1., kappa])
    ratio = float(w@A@w)/(np.linalg.norm(w)*np.linalg.norm(A@w))
    assert math.isclose(ratio, 2*math.sqrt(kappa)/(kappa+1), abs_tol=1e-14)
    checks += 1

# Random SPD problems, with actual polynomial Krylov bases, and random
# symmetric sketch distortions of norm below c_kappa. This tests that
# every eigenvalue of H=G^{-1}F has strictly positive real part.
for case in range(750):
    n = 5
    mat = rng.normal(size=(n,n))
    Q, _ = np.linalg.qr(mat)
    # controlled, separated eigenvalues avoid bad conditioned Krylov basis
    ev = np.linspace(1.0, rng.uniform(1.5, 6.0), n)
    A = Q@np.diag(ev)@Q.T
    cond = ev[-1]/ev[0]
    c = 2*math.sqrt(cond)/(cond+1)
    b = rng.normal(size=n)
    m = int(rng.integers(1,4))
    B = np.column_stack([np.linalg.matrix_power(A,j)@b for j in range(m)])
    B,_ = np.linalg.qr(B)
    R = rng.normal(size=(n,n)); E=(R+R.T)/2
    E *= (0.95*c)/np.linalg.norm(E,2)
    W = np.eye(n)+E
    Z=A@B
    G=Z.T@W@B
    F=Z.T@W@Z
    H=np.linalg.solve(G,F)
    vals=np.linalg.eigvals(H)
    assert min(vals.real) > 0
    assert min(np.linalg.eigvalsh((G+G.T)/2)) > 0
    checks += 1

# Exact-rational identity at kappa=9: b=(3,1), A=diag(1,9).
# G=18-30eps, F=90-54eps; epsilon=3/5 is exact singular boundary.
from fractions import Fraction
k=Fraction(9); eps=Fraction(3,5)
assert 2*k-eps*3*(k+1)==0
assert k*(k+1)-2*eps*27 > 0
checks += 1
print('VERIFY_OK', checks, 'checks')
