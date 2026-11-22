#!/usr/bin/env python3
"""Reproducibility diagnostics for polynomial Hardy--Volterra self-commutators.

Requires Python 3.10+ and NumPy; all infinite-dimensional assertions are proved
analytically in RESULT.md and are not certified by this finite checker.
"""
import math
import numpy as np

checks = 0

def check(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1


def exact_entry(n, j, b):
    """K_{n,n+j} for n >= degree, j >= 0, using the infinite matrix."""
    d = len(b)
    return sum(b[l - 1] * b[l + j - 1].conjugate() *
               ((n + l + j) ** (-2) - (n * (n + j)) ** (-1))
               for l in range(1, d - j + 1))


def leading(j, b):
    d = len(b)
    return -sum((2*l+j)*b[l-1]*b[l+j-1].conjugate()
                for l in range(1, d-j+1))


def finite_matrix(b, size):
    t = np.zeros((size, size), dtype=complex)
    for n in range(size):
        for k, bk in enumerate(b, start=1):
            if n+k < size:
                t[n+k,n] = bk/(n+k)
    return t.conj().T@t - t@t.conj().T


def symbol(b, theta):
    z = np.exp(1j*theta)
    bfun = sum(b[k-1]*z**k for k in range(1,len(b)+1))
    cfun = sum(k*b[k-1]*z**k for k in range(1,len(b)+1))
    return -2*np.real(np.conj(bfun)*cfun)

cases = [[1+0j], [1+0j, 0.7+0j], [1+2j, -0.3+0.7j, 0.4-0.1j],
         [0.9+0j, 1+0j, 1.1j]]
size = 76
for b in cases:
    d = len(b)
    K = finite_matrix(b, size)
    check(np.max(np.abs(K-K.conj().T)) < 1e-12, 'selfadjointness')
    for n in range(d, size - 2*d - 1, 4):
        for j in range(d):
            check(abs(K[n,n+j]-exact_entry(n,j,b)) < 5e-13,
                  f'exact matrix n={n},j={j}')
    for j in range(d):
        for n in (100, 300, 900, 2700, 8100):
            diff = abs(n**3 * exact_entry(n,j,b) - leading(j,b))
            check(diff <= (150*d*d*sum(abs(x)**2 for x in b)/n),
                  f'asymptotic remainder n={n},j={j}: {diff}')
    theta = np.arange(2048)*2*np.pi/2048
    sym = symbol(b,theta)
    check(np.max(np.abs(np.imag(sym))) < 1e-15,'real symbol')
    for j in range(d):
        fourier = np.mean(sym*np.exp(1j*j*theta))
        check(abs(fourier-leading(j,b)) < 2e-12,
              f'Fourier coefficient j={j}')

# Collective three-frequency example: a phase transition which no pair sees.
b = [0.9+0j,1+0j,1.1j]
for l in range(3):
    for m in range(l+1,3):
        u,v = abs(b[l]),abs(b[m])
        check(u<v, 'monotone derivative coefficients')
        gap = (v-u)*((m+1)*v-(l+1)*u)
        check(gap>0, 'strict uniform pairwise negative principal symbol')
check(473**2*3 > 779**2, 'positive trinary symbol at pi/3')
check(symbol(b,np.pi/3) > 0.75, 'numeric trinary positivity')

# Finite eigenvalue counts compared to the spectral counting asymptotic.
# The boundary of the finite section contributes O(degree) exceptional values.
for b,threshold in [([1+0j], 2e-6), ([1+0j,.7+0j],2e-6),
                    ([0.9+0j,1+0j,1.1j],1e-5)]:
    theta = np.arange(16384)*2*np.pi/16384
    w = symbol(b,theta)
    cp = np.mean(np.maximum(w,0)**(1/3))
    cm = np.mean(np.maximum(-w,0)**(1/3))
    eig = np.linalg.eigvalsh(finite_matrix(b,340))
    pcount = np.sum(eig>threshold)
    ncount = np.sum(eig< -threshold)
    exp_negative = cm*threshold**(-1/3)
    check(abs(ncount-exp_negative) < max(8,0.18*exp_negative),
          f'finite negative counting: {ncount}, {exp_negative}')
    if cp > 0.05:
        exp_positive = cp*threshold**(-1/3)
        check(abs(pcount-exp_positive) < max(6,0.40*exp_positive),
              f'finite positive counting: {pcount}, {exp_positive}')

print(f'VERIFICATION_OK {checks}')
