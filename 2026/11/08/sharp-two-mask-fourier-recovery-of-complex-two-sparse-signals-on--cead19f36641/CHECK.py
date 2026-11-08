"""Reproducibility checks for bounded-contrast two-mask cyclic Fourier phase retrieval.

Requires Python 3 and NumPy. All tests are finite supplements to the proof.
"""
import math
import numpy as np


def observe(x, mask):
    return np.abs(np.fft.fft(mask * x)) ** 2


def autocorrelation(intensity):
    return np.fft.ifft(intensity)


def reconstruct(y1, y2, tol=1.e-7):
    n = len(y1)
    assert n >= 3 and n % 2 == 1
    weights = 2.0 ** (np.arange(n) / (n - 1) - 1)
    rho = 2 ** (1 / (n - 1))
    c1, c2 = autocorrelation(y1), autocorrelation(y2)
    z = np.zeros(n, dtype=complex)
    E = c1[0].real
    if abs(E) < tol:
        return z
    lags = [d for d in range(1, n) if abs(c1[d]) > tol * E]
    if not lags:
        j = round((math.log(c2[0].real / E) / (2 * math.log(rho))) + n - 1)
        assert 0 <= j < n
        z[j] = math.sqrt(E)
        return z
    d = lags[0]
    assert len(lags) == 2
    ratio = c2[d] / c1[d]
    assert abs(ratio.imag) < 1.e-7 * (1 + abs(ratio))
    s = round(math.log(ratio.real) / math.log(rho) + 2 * (n - 1))
    candidates = [(u, v) for u in range(n) for v in range(u + 1, n)
                  if u + v == s and ((v-u) % n == d or (u-v) % n == d)]
    assert len(candidates) == 1, (n, d, s, candidates)
    u, v = candidates[0]
    A = (c2[0].real - weights[v]**2 * E) / (weights[u]**2 - weights[v]**2)
    assert A > 0
    z[u] = math.sqrt(A)
    z[v] = c1[(v-u)%n] / z[u]
    return z


def check():
    rng = np.random.default_rng(102)
    tested = 0
    pair_signatures = 0
    for n in (3, 5, 7, 9, 11, 15, 21, 31):
        weights = 2.0 ** (np.arange(n) / (n - 1) - 1)
        assert abs(weights[0] - .5) < 1.e-14
        assert abs(weights[-1] - 1) < 1.e-14
        signatures = {}
        for u in range(n):
            for v in range(u + 1, n):
                sig = (u+v, min((v-u)%n, (u-v)%n))
                assert sig not in signatures, (n, sig, signatures.get(sig), (u,v))
                signatures[sig] = (u,v)
                pair_signatures += 1
                for _ in range(3):
                    x = np.zeros(n, dtype=complex)
                    x[u] = (0.4 + rng.random()) * np.exp(2j*np.pi*rng.random())
                    x[v] = (0.4 + rng.random()) * np.exp(2j*np.pi*rng.random())
                    z = reconstruct(observe(x, np.ones(n)), observe(x, weights))
                    x_adjusted = x * np.conj(x[u]) / abs(x[u])
                    assert np.linalg.norm(z-x_adjusted) < 1.e-7, (n, u, v, z, x_adjusted)
                    tested += 1
        for j in range(n):
            x = np.zeros(n, dtype=complex)
            x[j] = 0.37 - 1.18j
            z = reconstruct(observe(x, np.ones(n)), observe(x, weights))
            assert np.linalg.norm(z-abs(x[j])*np.eye(n)[j]) < 1.e-8
            tested += 1
    # Even orders: for every real mask the two conjugated antipodal inputs agree.
    for n in (4, 6, 8, 10, 12, 16, 28):
        u, v = 1, 1+n//2
        a, b = 1+0j, .6+1.2j
        x = np.zeros(n, complex)
        xp = np.zeros(n, complex)
        x[u], x[v] = a, b
        xp[u], xp[v] = a.conjugate(), b.conjugate()
        assert not np.allclose(x, xp)
        for _ in range(7):
            mask = rng.uniform(.1, 1., n)
            assert np.max(np.abs(observe(x, mask) - observe(xp, mask))) < 1.e-12
            tested += 1
    print('CHECK_OK phase_recovery_tests=%d exact_support_signatures=%d' % (tested, pair_signatures))


if __name__ == '__main__':
    check()
