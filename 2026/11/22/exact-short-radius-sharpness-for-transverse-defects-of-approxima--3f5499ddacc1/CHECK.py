"""Supplementary finite diagnostics for the explicit short-radius witness.

Analytic inequalities in RESULT.md, not this finite sampling, prove the theorem.
Requires Python 3 with NumPy; no network access or auxiliary data.
"""
import math
import numpy as np

rng = np.random.default_rng(20261121)


def coordinates(t, r):
    t = np.asarray(t, dtype=float)
    a = max(0.0, r - 1.0)
    z = np.zeros((t.size, 2), dtype=float)
    neg = t < 0
    mid = (t >= 0) & (t <= r)
    pos = t > r
    z[neg, 0] = t[neg]
    # Cancellation-safe equivalent of sqrt(r)-sqrt(r-2*a*t).
    if a > 0:
        z[neg, 1] = (2 * a * t[neg]) / (np.sqrt(r - 2 * a * t[neg]) + math.sqrt(r))
    z[mid, 1] = (r + 1.0) * t[mid] / r
    z[pos, 0] = t[pos] - r
    z[pos, 1] = np.sqrt((r + 1.0) ** 2 + 2 * (t[pos] - r))
    return z


def one_case(r):
    # Mix neighboring points, different pieces and logarithmically separated tails.
    n = 5000
    p = rng.uniform(-1, 1, n)
    q = rng.uniform(-1, 1, n)
    mags_p = 10.0 ** rng.uniform(-9, 6, n)
    mags_q = 10.0 ** rng.uniform(-9, 6, n)
    def sample(z, mags):
        out = np.where(z < -0.34, -mags, np.where(z > 0.34, r + mags, r * (z + 0.34) / 0.68))
        return out
    x = sample(p, mags_p)
    y = sample(q, mags_q)
    # Include boundary and immediate-offset stress tests.
    x[:12] = [-1e-7, -1e-3, -1, -100, 0, 0, r, r, -1e4, r + 1e-7, r/2, -1e-10]
    y[:12] = [0, r, r, r+1e-7, r, r+1e-6, r+1e-5, r+1e4, r, r+100, r+1e-7, r]
    xx = coordinates(x,r)
    yy = coordinates(y,r)
    delta = np.linalg.norm(xx-yy,axis=1) - np.abs(x-y)
    # Absolute distortions remain bounded by one, up to roundoff in sqrt/subtraction.
    worst = np.max(np.abs(delta))
    if worst > 1 + 2e-8:
        j = int(np.argmax(np.abs(delta)))
        raise AssertionError((r, x[j], y[j], delta[j]))
    # Exact origin and target with positive radius.
    assert np.linalg.norm(coordinates(np.array([0]),r)[0]) < 1e-12
    assert abs(coordinates(np.array([r]),r)[0,1] - (r+1)) < 1e-12
    # Each tail is asymptotically the horizontal unit vector.
    tail = coordinates(np.array([-1e12,1e12]),r)
    assert np.max(np.abs(tail[:,0]/np.array([-1e12,1e12])-1)) < 1e-8
    assert np.max(np.abs(tail[:,1]))/1e12 < 1e-4
    return n

radii = [1e-5,0.001,0.01,0.1,0.3,0.6,0.9,1.0,1.01,1.1,1.3,1.6,1.9,1.99,1.9999,2.0]
radii += list(rng.uniform(0.0001, 2, 64))
checks=0
for r in radii:
    checks += one_case(float(r))
print('SHORT_RADIUS_EPSILON_ISOMETRY_DIAGNOSTIC_OK', checks)
