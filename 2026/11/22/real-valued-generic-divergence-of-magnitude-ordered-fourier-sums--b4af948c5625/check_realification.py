"""Finite Fourier checks of conjugate-pair realification on odd cyclic products.

This checks the elementary spectral identity used in the proof; the separate
existential large-threshold input is a cited theorem, not tested here.
Run with: python3 check_realification.py (numpy required).
"""
import itertools
import numpy as np


def coefficient_threshold(a, delta):
    coeff = np.fft.fftn(a) / a.size
    return np.fft.ifftn(coeff * (np.abs(coeff) >= delta) * a.size)


def realify(P, p):
    zeta = np.exp(2j * np.pi * np.arange(p) / p)
    return 2 * np.real(P[..., None] * zeta)


def check(p, d, seed):
    rng = np.random.default_rng(seed)
    shape = (p,) * d
    P = rng.normal(size=shape) + 1j * rng.normal(size=shape)
    P /= np.max(np.abs(P))
    R = realify(P, p)
    assert np.max(np.abs(R.imag)) == 0.0
    coeff_P = np.fft.fftn(P) / P.size
    coeff_R = np.fft.fftn(R) / R.size
    assert np.max(np.abs(coeff_R[..., 1] - coeff_P)) < 8e-13
    for idx in itertools.product(range(p), repeat=d):
        neg = tuple((-i) % p for i in idx)
        assert abs(coeff_R[idx + (p-1,)] - np.conj(coeff_P[neg])) < 8e-13
        for s in range(2, p-1):
            assert abs(coeff_R[idx + (s,)]) < 8e-13
        assert abs(coeff_R[idx + (0,)]) < 8e-13
    candidates = np.unique(np.abs(coeff_P).flatten())
    picks = [0.22 * float(np.max(candidates)), 0.43 * float(np.max(candidates)), 0.78 * float(np.max(candidates)), 1.2 * float(np.max(candidates))]
    for delta in picks:
        lhs = coefficient_threshold(R, delta)
        rhs = realify(coefficient_threshold(P, delta), p)
        assert np.max(np.abs(lhs - rhs)) < 1e-10, (p, d, delta, np.max(np.abs(lhs-rhs)))
    # A pointwise good complex threshold implies a good phase at some s.
    for delta in picks:
        TP = coefficient_threshold(P, delta)
        TR = coefficient_threshold(R, delta)
        assert np.min(np.max(np.abs(TR), axis=-1) - np.abs(TP)) > -1e-10
    return len(picks)


def check_separation():
    p = 3
    rng = np.random.default_rng(1789)
    P1 = rng.normal(size=p) + 1j*rng.normal(size=p)
    P2 = rng.normal(size=p) + 1j*rng.normal(size=p)
    P1 /= np.max(np.abs(P1)); P2 /= np.max(np.abs(P2))
    R1=realify(P1,p); R2=realify(P2,p)
    m1 = np.min(np.abs(np.fft.fftn(R1).flatten()/R1.size)[np.abs(np.fft.fftn(R1).flatten()/R1.size)>1e-8])
    c1=0.1; c2=c1*m1/8
    f = c1*R1[:,:,None,None]+c2*R2[None,None,:,:]
    F2 = np.fft.fftn(R2)/R2.size
    delta = c2 * max(abs(F2.flatten())) * 0.37
    target = c1*R1[:,:,None,None] + c2*coefficient_threshold(R2, delta/c2)[None,None,:,:]
    actual = coefficient_threshold(f, delta)
    assert np.max(np.abs(target-actual)) < 1e-10
    return float(np.max(np.abs(target-actual)))


if __name__ == '__main__':
    checks=0
    for p,d in [(3,1),(3,2),(5,1),(5,2),(7,1),(9,1)]:
        for seed in range(5):
            checks += check(p,d,seed+1309)
    err=check_separation()
    print('PASS: %d regular-threshold realification identities, conjugate-frequency checks, and phase-max inequalities' % checks)
    print('PASS: two-block coefficient-level separation, maximum error %.3g' % err)
    print('LIMIT: these finite tests do not verify the large-amplitude finite-model theorem or generic Baire argument')
