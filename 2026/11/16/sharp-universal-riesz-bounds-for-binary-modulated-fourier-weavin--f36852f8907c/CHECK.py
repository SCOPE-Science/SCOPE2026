"""Finite consistency checks for sharp two-phase Fourier weaving bounds.

Requires numpy and scipy. Checks are finite diagnostics, not a proof
of universal infinite-dimensional assertions.
"""
import numpy as np
from scipy.linalg import svdvals


def fourier_sinc(theta, j, k):
    # <e_j, exp(2*pi*i*theta*t)e_k> on L2[0,1]
    x = theta + k - j
    return np.exp(1j * np.pi * x) * np.sinc(x)


def assert_bounds(theta, indices, shifted):
    # Compute the exact L2 Gram matrix of the selected finite family;
    # there is no truncation of the output Fourier spectrum here.
    freq = np.array([j + (theta if j in shifted else 0.) for j in indices])
    diff = freq[None, :] - freq[:, None]
    gram = np.exp(1j * np.pi * diff) * np.sinc(diff)
    evals = np.linalg.eigvalsh(gram)
    lo, hi = 1-np.sin(np.pi*abs(theta)), 1+np.sin(np.pi*abs(theta))
    assert evals.min() >= lo - 2.e-12, (theta, evals.min(), lo)
    assert evals.max() <= hi + 2.e-12, (theta, evals.max(), hi)
    return evals.min(), evals.max()


def main():
    count = 0
    indices = np.arange(-6, 7)
    rng = np.random.default_rng(3050)
    for theta in [0, .01, .10, .25, .40, .49, -.20, -.48]:
        for _ in range(25):
            S = set(indices[rng.random(len(indices)) < .5])
            assert_bounds(theta, indices, S)
            count += 1
    # The half-line cross Gram is a positive shifted Hilbert matrix.
    for theta in [.1, .25, .4, .49, .5]:
        previous = 0.
        for N in (16, 32, 64, 128):
            k = np.arange(N)
            H = 1. / (k[:, None] + k[None, :] + 1-theta)
            c_norm = np.sin(np.pi * theta)/np.pi * svdvals(H)[0]
            assert c_norm < np.sin(np.pi*theta) + 1.e-10
            assert c_norm > previous
            previous = c_norm
            count += 2
    # Correct exact phase relation above the critical phase: a boundary
    # Hardy function maps to its reflected negative-frequency partner.
    t = (np.arange(12000)+.5)/12000
    z = np.exp(2j*np.pi*t)
    for theta in (.51,.60,.75,.90,.99):
        alpha=1-theta
        A=(1-z)**(-alpha)
        v=z**(-1)*np.conj(A)
        residual=np.max(np.abs(np.exp(2j*np.pi*theta*t)*v - np.exp(-1j*np.pi*alpha)*A))
        assert residual < 1.e-9, residual
        count += 1
    # At the critical phase, the explicitly reflected approximants have
    # bounded normalized residual compared with increasing L2 norm.
    t=(np.arange(131072)+.5)/131072
    z=np.exp(2j*np.pi*t)
    vals=[]
    for r in (.85,.95,.985,.995,.999):
        A=(1-r*z)**(-.5)
        v=z**(-1)*np.conj(A)
        D=np.exp(-1j*np.pi*t)*A-1j*v
        vals.append((np.mean(np.abs(D)**2),np.mean(np.abs(A)**2)))
        count+=1
    assert vals[-1][0] < 4.0*vals[0][0]
    assert vals[-1][1] > 2.0*vals[0][1]
    print(f'PASS: {count} finite checks; critical residual-to-norm data: {vals}')


if __name__ == '__main__':
    main()
