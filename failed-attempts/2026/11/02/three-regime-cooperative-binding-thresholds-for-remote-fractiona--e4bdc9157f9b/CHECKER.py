"""Independent finite numerical checks for remote Dirichlet fractional impurities.

Run: python CHECKER.py
Requires mpmath and numpy. Finite checks support, but cannot replace, proof.
"""
import math
import numpy as np
import mpmath as mp

mp.mp.dps = 50
HALF = mp.mpf('0.5')


def green(alpha, m, n):
    """Closed expression for the zero-energy sine-transform Green entry."""
    a = mp.mpf(str(alpha))
    m, n = int(m), int(n)
    if min(m, n) < 1:
        raise ValueError('positive half-line sites required')
    p, q = abs(m - n), m + n
    if a == HALF:
        return (mp.digamma(q + HALF) - mp.digamma(p + HALF)) / mp.pi
    if a == 1:
        return mp.mpf(min(m, n))
    fac = mp.gamma(1 - 2 * a) * mp.sin(mp.pi * a) / mp.pi
    f = lambda j: mp.gamma(j + a) / mp.gamma(j + 1 - a)
    return fac * (f(p) - f(q))


def integral_green(alpha, m, n):
    a = mp.mpf(str(alpha))
    f = lambda th: (2 / mp.pi) * mp.sin(m * th) * mp.sin(n * th) / (2 * mp.sin(th / 2))**(2 * a)
    return mp.quad(f, [mp.mpf('0'), mp.mpf('0.005'), mp.mpf('0.1'), mp.mpf('1'), mp.pi])


def continuum(alpha, x, y):
    a = mp.mpf(str(alpha))
    x, y = mp.mpf(str(x)), mp.mpf(str(y))
    beta = 2 * a - 1
    return ((x + y)**beta - abs(x - y)**beta) / (2 * mp.gamma(1 + beta) * mp.sin(mp.pi * beta / 2))


def c_short(alpha):
    a = mp.mpf(str(alpha))
    return 4**(-a) * mp.beta(HALF - a, HALF) / mp.pi


def close(a, b, tol, label):
    if abs(a - b) > tol:
        raise AssertionError(f'{label}: {a} != {b} (tolerance {tol})')


count = 0
for alpha, m, n in [(0.25, 2, 4), (0.5, 1, 2), (0.75, 1, 3), (1.0, 3, 4), (1.25, 2, 3)]:
    close(green(alpha, m, n), integral_green(alpha, m, n), mp.mpf('1e-22'), 'gamma versus sine integral')
    count += 1

for m in [1, 2, 8, 33]:
    for n in [1, 2, 9, 34]:
        close(green(1, m, n), min(m, n), mp.mpf('1e-30'), 'alpha=1 kernel')
        count += 1

x = [mp.mpf('1.0'), mp.mpf('2.5')]
w = np.array([1.0, 0.6])
for alpha in [0.25, 0.5, 0.75, 1.0, 1.25, 1.4]:
    R = 10**10 if alpha == 0.5 else 5000
    sites = [int(mp.floor(R * p)) for p in x]
    G = np.array([[float(green(alpha, p, q)) for q in sites] for p in sites])
    eig = np.linalg.eigvalsh(np.sqrt(w)[:, None] * G * np.sqrt(w)[None, :])
    assert eig[0] > 0
    c = 1 / eig[-1]
    if alpha < 0.5:
        target = 1 / (float(c_short(alpha)) * max(w))
        assert abs(c / target - 1) < 0.015
    elif alpha == 0.5:
        target = math.pi / max(w)
        assert abs(c * math.log(R) / target - 1) < 0.12
        offdiag = math.log(float((x[0] + x[1]) / abs(x[0] - x[1]))) / math.pi
        close(mp.mpf(G[0, 1]), mp.mpf(offdiag), mp.mpf('0.0001'), 'alpha=1/2 offdiag limit')
        count += 1
    else:
        K = np.array([[float(continuum(alpha, p, q)) for q in x] for p in x])
        ek = np.linalg.eigvalsh(np.sqrt(w)[:, None] * K * np.sqrt(w)[None, :])
        target = 1 / ek[-1]
        assert abs(c * R**(2 * alpha - 1) / target - 1) < 0.012
        assert ek[-1] > max(w * np.diag(K))
        count += 1
    count += 1

# A strict pairwise cooperative window at fractional order 3/4.
a = 0.75
K = np.array([[float(continuum(a, p, q)) for q in x] for p in x])
rho = K[0, 1] / math.sqrt(K[0, 0] * K[1, 1])
assert 0 < rho < 1
s = (1 + 1 / (1 + rho)) / 2  # between the cooperative threshold and 1
t = s / np.diag(K)
assert all(t * np.diag(K) < 1)
limit = np.sqrt(t)[:, None] * K * np.sqrt(t)[None, :]
assert np.linalg.eigvalsh(limit)[-1] > 1
for R in [400, 2000, 8000]:
    sites = [int(mp.floor(R * p)) for p in x]
    G = np.array([[float(green(a, p, q)) for q in sites] for p in sites])
    B = R**(1 - 2 * a) * np.sqrt(t)[:, None] * G * np.sqrt(t)[None, :]
    assert np.linalg.eigvalsh(B)[-1] > 1
    assert all(np.diag(B) < 1)
    count += 1

print(f'PASS {count} finite integral, spectral-scaling, and cooperative-binding assertions')
print('two-impurity limiting normalized correlation:', rho)
print('two-impurity strict cooperative spectral eigenvalue:', np.linalg.eigvalsh(limit)[-1])
