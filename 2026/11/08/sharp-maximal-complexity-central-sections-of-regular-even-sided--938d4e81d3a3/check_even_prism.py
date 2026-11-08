"""Independent edge-intersection and quadrature checks for even regular prisms.

Run: python3 check_even_prism.py
Requires Python 3, numpy, scipy (scipy only for optional quadrature).
"""
import math
import numpy as np


def law(n, h):
    assert n >= 4 and n % 2 == 0 and h > 0
    a = math.pi / n
    z = 1.0 / math.sqrt(1.0 + h * h)
    return n / math.pi * (2 * math.asin(math.sin(a) * z)
                          - math.asin(math.sin(2 * a) * z))


def optimum(n):
    c = math.cos(math.pi / n)
    return math.sqrt(3 * c * c - 1)


def edges(n):
    return ([(j, (j + 1) % n) for j in range(n)]
            + [(j + n, n + (j + 1) % n) for j in range(n)]
            + [(j, j + n) for j in range(n)])


def independent_section_counts(normals, n, h):
    phi = 2 * math.pi * np.arange(n) / n
    xy = np.stack((np.cos(phi), np.sin(phi)), axis=-1)
    V = np.vstack((np.column_stack((xy, np.full(n, h))),
                   np.column_stack((xy, np.full(n, -h)))))
    dot = normals @ V.T
    result = np.zeros(normals.shape[0], dtype=np.int32)
    for v, w in edges(n):
        result += dot[:, v] * dot[:, w] < 0
    return result


def check():
    from scipy.integrate import quad
    rng = np.random.default_rng(825001)
    normals = rng.standard_normal((190000, 3))
    normals /= np.linalg.norm(normals, axis=1)[:, None]
    samples = 0
    for n in (4, 6, 8, 12, 20):
        hm = optimum(n)
        assert hm > 0
        for h in (0.5 * hm, hm, 1.7 * hm):
            counts = independent_section_counts(normals, n, h)
            samples += len(counts)
            assert int(counts.min()) >= 4
            assert int(counts.max()) <= n + 2
            assert np.all(counts % 2 == 0)
            empirical = float(np.mean(counts == n + 2))
            symbolic = law(n, h)
            assert abs(empirical - symbolic) < 0.005, (n, h, empirical, symbolic)
            # Independently integrate the unsimplified distribution over azimuth.
            def fn(phi):
                u = math.cos(phi)
                v = math.cos(2*math.pi/n - phi)
                return u/math.hypot(h, u) - v/math.hypot(h, v)
            integral = n / math.pi * quad(fn, 0, math.pi / n,
                                           epsabs=2e-14, epsrel=2e-14)[0]
            assert abs(symbolic - integral) < 3e-13, (n, h, integral, symbolic)
        assert law(n, hm) > law(n, hm/2)
        assert law(n, hm) > law(n, hm*1.7)
        print('n', n, 'half-height_max', hm, 'p_max', law(n, hm))
    # The square-prism optimum is a cube when R=1.
    assert abs(optimum(4)-1/math.sqrt(2)) < 1e-14
    assert abs(law(4, optimum(4)) -
               (1-6/math.pi*math.asin(1/3))) < 1e-14
    # Exact n=6 optimizer is sqrt(5)/2.
    assert abs(optimum(6)-math.sqrt(5)/2) < 1e-14
    for n in (100, 1000):
        asymptotic = 2*math.pi**2/(3*math.sqrt(3)*n*n)
        ratio = law(n, optimum(n))/asymptotic
        assert abs(ratio-1) < 0.001
    print('EVEN_PRISM_MAXIMAL_SECTIONS_OK samples=', samples)


if __name__ == '__main__':
    check()
