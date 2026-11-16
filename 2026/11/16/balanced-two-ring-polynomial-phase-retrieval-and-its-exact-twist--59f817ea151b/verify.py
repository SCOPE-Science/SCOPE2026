#!/usr/bin/env python3
"""Direct finite tests of balanced two-ring polynomial-intensity interpolation.

Uses real Hermitian polynomial matrices, not the analytic proof's rank-one assumption.
No extrapolation from these finite tests to all polynomial degrees is claimed.
"""
import math
import numpy as np


def sample_intensity(H, K, r, offset):
    theta = offset + np.pi * np.arange(2 * K) / K
    z = r * np.exp(1j * theta)
    V = z[:, None] ** np.arange(K + 1)[None, :]
    return np.einsum('nj,jk,nk->n', V.conj(), H, V).real


def recover_circle_fourier(y0, y1, K, r0, r1, delta):
    '''Return Fourier coefficients c_m(r_j), m=0,...,K, on each circle.'''
    assert abs(math.sin(K * delta)) > 1e-10
    fft0 = np.fft.fft(y0) / (2 * K)
    fft1 = np.fft.fft(y1) / (2 * K)
    # Nyquist DFT is the real combination of the top +/- K Fourier terms.
    x = fft0[K].real / (2 * r0 ** K)
    u = fft1[K].real / (2 * r1 ** K)
    y = (x * math.cos(K * delta) - u) / math.sin(K * delta)
    C = x + 1j * y
    a = np.array([fft0[m] for m in range(K)] + [r0 ** K * C], dtype=complex)
    b = np.array([fft1[m] * np.exp(-1j * m * delta) for m in range(K)] + [r1 ** K * C], dtype=complex)
    return a, b


def expected_coeff(H, K, r):
    # v* H v = sum H[j,k] (conj(z))^j z^k.
    return np.array([sum(H[j, j+m] * r ** (2*j+m) for j in range(K-m+1)) for m in range(K+1)])


def test():
    rng = np.random.default_rng(2608)
    count = 0
    worst = 0.0
    r0, r1 = 0.43, 0.81
    for K in (1, 2, 3, 4, 5, 7):
        for twist_factor in (0.25, 0.5, 0.73):
            delta = math.pi * twist_factor / K
            for rep in range(24):
                X = rng.normal(size=(K+1,K+1)) + 1j * rng.normal(size=(K+1,K+1))
                H = (X + X.conj().T)/2
                y0 = sample_intensity(H,K,r0,0.0)
                y1 = sample_intensity(H,K,r1,delta)
                got0, got1 = recover_circle_fourier(y0,y1,K,r0,r1,delta)
                want0, want1 = expected_coeff(H,K,r0), expected_coeff(H,K,r1)
                worst=max(worst,np.max(np.abs(got0-want0)),np.max(np.abs(got1-want1)))
                assert np.allclose(got0,want0,atol=3e-12,rtol=0)
                assert np.allclose(got1,want1,atol=3e-12,rtol=0)
                count+=1
        # Resonant angular grids: non-collinear polynomials have same intensity at every sample.
        for delta in (0.0, math.pi / K):
            p = np.zeros(K+1,complex); p[0]=1;p[K]=1j
            q = np.zeros(K+1,complex); q[0]=1;q[K]=-1j
            for r, off in ((r0, 0), (r1, delta)):
                z = r*np.exp(1j*(off + math.pi*np.arange(2*K)/K))
                assert np.max(np.abs(np.abs(np.polynomial.polynomial.polyval(z,p))**2-
                                        np.abs(np.polynomial.polynomial.polyval(z,q))**2))<2e-12
        # Coincident radii: monomial and constant are globally ambiguous on the circle.
        z = r0*np.exp(1j*(delta + np.pi*np.arange(2*K)/K))
        assert np.max(np.abs(np.abs(z**K)**2-r0**(2*K)))<2e-12
    for K in (1,2,3,7):
        for t in (0.12,0.42,0.73,1.1):
            d = t/K
            M = np.array([[1,0],[math.cos(K*d),-math.sin(K*d)]])
            singular = np.linalg.svd(M,compute_uv=False)
            exact = np.sqrt([1+abs(math.cos(K*d)),1-abs(math.cos(K*d))])
            assert np.allclose(singular,exact,rtol=5e-14,atol=1e-14)
        M=np.array([[1,0],[0,-1]])
        assert np.linalg.cond(M)==1.0
    print(f'BALANCED_TWO_RING_PHASE_RETRIEVAL_PASS hermitian_cases={count} degrees=1,2,3,4,5,7 maximum_coefficient_error={worst:.3g} resonance_and_equal_radius=checked')

if __name__=='__main__':
    test()
