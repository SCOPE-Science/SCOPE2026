"""Supplementary finite-section checks for Meixner forward-difference spectra.

Requirements: Python 3, NumPy, SciPy. Run `python check.py`.
These computations do not prove infinite eigenvalue counts or polynomial density.
"""
import math
import numpy as np
from scipy.linalg import eigh_tridiagonal


def jacobi(c, beta, n):
    k = np.arange(n, dtype=float)
    ak = np.sqrt((k + 1) / (c * (k + beta)))
    diag = np.r_[1.0, 1.0 + ak[:-1] ** 2]
    return diag, ak[:-1]


def direct_gram(c, beta, n):
    k = np.arange(n - 1, dtype=float)
    ak = np.sqrt((k + 1) / (c * (k + beta)))
    d = -np.eye(n)
    d[np.arange(n-1), np.arange(1,n)] = ak
    return d.T @ d


def test_gram():
    for c in (0.2, 0.7):
        for beta in (0.3, 0.9, 1.0, 2.5):
            n = 12
            diag, e = jacobi(c, beta, n)
            j = np.diag(diag) + np.diag(e, 1) + np.diag(e, -1)
            s = np.diag((-1.0) ** np.arange(n))
            assert np.max(np.abs(s @ direct_gram(c, beta, n) @ s-j)) < 1e-12


def trial_bound(c, beta, K, L):
    a = 1 / math.sqrt(c)
    E = (1+a)**2
    theta = math.pi/(L+1)
    lower = E - 2*a*(1-math.cos(theta)) + (1-beta)/(c*(K+L+beta-2))
    n = K+L+1
    k = np.arange(n, dtype=float)
    ak = np.sqrt((k + 1)/(c*(k+beta)))
    h = np.zeros(n)
    jj = np.arange(1,L+1)
    h[K:K+L] = np.sin(jj * theta)
    diag = np.r_[1.0, 1.0 + ak[:-1]**2]
    quotient = (np.dot(diag,h*h) + 2*np.dot(ak[:-1],h[:-1]*h[1:]))/np.dot(h,h)
    assert quotient + 1e-11 >= lower
    assert lower > E, (quotient,lower,E)


def test_spectral():
    for c in (0.25, 0.7):
        a = 1 / math.sqrt(c)
        E=(1+a)**2
        for beta in (0.3, 0.75):
            diag,e = jacobi(c,beta,350)
            ev = eigh_tridiagonal(diag,e, select='i',
                                  select_range=(346,349),eigvals_only=True)
            assert ev[-1] > E + 1e-3
            assert ev[-2] > E + 1e-3
        for beta in (1.0, 1.5, 3.0):
            diag,e = jacobi(c,beta,350)
            ev = eigh_tridiagonal(diag,e,select='i',
                                  select_range=(349,349),eigvals_only=True)[0]
            assert ev < E + 1e-10
    for c,beta,K,L in ((0.25,0.5,400,80),(0.7,0.3,500,100)):
        trial_bound(c,beta,K,L)

if __name__=='__main__':
    test_gram()
    test_spectral()
    print('PASS: 8 Gram identities, 10 finite spectral tests, 2 block inequalities')
