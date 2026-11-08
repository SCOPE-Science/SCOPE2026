"""Separate cubature verification for quadratic harmonic localization on a spherical lune.

Requires NumPy >= 1.24. Integrates the full quadratic Gram form by a tensor cubature
using an exact fourth-moment cubature for the transverse sphere, exact two-moment
radial interpolation, and independent high-order angular Gauss quadrature.
"""
import itertools
import math
import numpy as np


def transverse_nodes(m):
    a = 2.0 / (m + 2)
    b = m / (m + 2)
    for j in range(m):
        for s in (-1.0, 1.0):
            u = np.zeros(m)
            u[j] = s
            yield u, a / (2 * m)
    for signs in itertools.product((-1.0, 1.0), repeat=m):
        yield np.array(signs) / math.sqrt(m), b / 2**m


def basis(x):
    d = len(x)
    xx, yy = x[:2]
    z = x[2:]
    r2 = xx * xx + yy * yy
    v = [r2 - 2.0 / d, xx * xx - yy * yy, 2 * xx * yy]
    v.extend(xx * zi for zi in z)
    v.extend(yy * zi for zi in z)
    v.extend(zi * zi - z[-1] * z[-1] for zi in z[:-1])
    v.extend(z[i] * z[j] for i in range(len(z)) for j in range(i + 1, len(z)))
    return np.array(v)


def gramians(d, width):
    m = d - 2
    r1, r2 = 2 / d, 8 / (d * (d + 2))
    w1 = 4 * (r1 - r2)
    w2 = r1 - w1 / 2
    w0 = 1 - w1 - w2
    ts = [(0.0, w0), (0.5, w1), (1.0, w2)]
    ga, gw = None, None
    for k, (lo, hi) in enumerate(((0.0, 2 * math.pi), (-width / 2, width / 2))):
        nodes, weights = np.polynomial.legendre.leggauss(64)
        angles = (hi + lo) / 2 + nodes * ((hi - lo) / 2)
        ang_weights = weights * (hi - lo) / (4 * math.pi)
        rows, ws = [], []
        for t, wt in ts:
            for u, wu in transverse_nodes(m):
                for phi, wa in zip(angles, ang_weights):
                    x = np.concatenate((np.sqrt(t) * np.array([np.cos(phi), np.sin(phi)]), np.sqrt(1 - t) * u))
                    rows.append(basis(x))
                    ws.append(wt * wu * wa)
        X, W = np.array(rows), np.array(ws)
        gram = X.T @ (W[:, None] * X)
        if k == 0:
            ga = gram
        else:
            gw = gram
    return ga, gw


def predicted(d, width):
    m = d - 2
    p = width / (2 * math.pi)
    s = math.sin(width) / (2 * math.pi)
    c = math.cos(width)
    k = (d - 2) / d
    a = math.sqrt(c * c / 4 + k)
    vals = [p + s * (c / 2 + a), p + s * (c / 2 - a), p - s * c]
    vals.extend([p + s] * m)
    vals.extend([p - s] * m)
    vals.extend([p] * (m * (m + 1) // 2 - 1))
    return np.sort(vals)


def run():
    tests = 0
    for d in (3, 4, 5, 6, 8):
        for width in (0.3, 0.75, 1.3, 1.8, 2.5, 3.0):
            full, masked = gramians(d, width)
            L = np.linalg.cholesky(full)
            B = np.linalg.solve(L, masked)
            B = np.linalg.solve(L, B.T).T
            eig = np.linalg.eigvalsh((B + B.T) / 2)
            target = predicted(d, width)
            assert eig.shape == target.shape, (d, width, eig.shape, target.shape)
            assert np.max(np.abs(eig - target)) < 2e-11, (d, width, eig, target)
            tests += len(eig)
            assert eig.min() > -1e-12 and eig.max() < 1 + 1e-12
            tests += 2
            assert abs(np.sum(eig) - target.size * width / (2 * math.pi)) < 2e-11
            tests += 1
            s = math.sin(width) / (2 * math.pi)
            c = math.cos(width)
            k = (d - 2) / d
            plus = width/(2*math.pi)+s*(c/2+math.sqrt(c*c/4+k))
            minus = width/(2*math.pi)+s*(c/2-math.sqrt(c*c/4+k))
            high = plus if c > 2/d else width/(2*math.pi)+s
            low = width/(2*math.pi)-s if c > -2/d else minus
            assert abs(eig[-1]-high)<2e-11
            assert abs(eig[0]-low)<2e-11
            tests+=2
    # Verify transition degeneracy and ordering near both thresholds directly.
    for d in (3, 4, 7, 12):
        for target in (math.acos(2/d), math.acos(-2/d)):
            v = predicted(d, target)
            m = d-2
            if target < math.pi / 2:
                assert np.sum(abs(v - v[-1]) < 1e-10) == m+1
            else:
                assert np.sum(abs(v - v[0]) < 1e-10) == m+1
            tests += 1
    print(f'LUNE_QUADRATIC_CUBATURE_CHECKS_PASS {tests}')

if __name__ == '__main__':
    run()
