"""Independent finite-dimensional consistency checks for cyclic geometric-window Gabor bases.

Requires NumPy; run with python check_geometric_masks.py.
The proof for arbitrary dimensions is in RESULT.md, not in this finite test.
"""
import itertools
import math
import numpy as np


def direct_matrix(q, m, rho, translations):
    n = q * m
    x = np.arange(n)
    g = rho ** x
    return np.column_stack([
        np.exp(2j * np.pi * b * x / m) * np.roll(g, t)
        for t in translations for b in range(m)
    ])


def predicted_rank(q, m, translations):
    return sum(len({((t // m) + (j < (t % m))) % q
                    for t in translations}) for j in range(m))


def spectrum(q, m, rho):
    return sorted(
        m * rho ** (2 * j) * (1 - rho ** (q * m)) ** 2
        / (1 + rho ** (2 * m) - 2 * rho ** m
           * math.cos(2 * math.pi * k / q))
        for j in range(m) for k in range(q)
    )


def sharp_bounds(q, m, rho):
    c = 1.0 if q % 2 == 0 else math.cos(math.pi / q)
    r = rho ** m
    a = m * rho ** (2 * (m - 1)) * (1 - rho ** (q * m)) ** 2 / (1 + r*r + 2*c*r)
    b = m * (1 - rho ** (q * m)) ** 2 / (1 - r) ** 2
    return a, b


def optimal_r(q, m):
    c = 1.0 if q % 2 == 0 else math.cos(math.pi / q)
    alpha = (m - 1) / m
    def slope(r):
        return (1+c) * r * (1+r) / ((1-r) * (1+r*r+2*c*r))
    lo, hi = 0.0, 1.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if slope(mid) < alpha:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def run():
    tested = 0
    full_spectra = 0
    for q, m in [(2, 2), (3, 2), (2, 4), (3, 3), (4, 2), (2, 5)]:
        n = q * m
        for rho in (0.49, 0.71):
            for translations in itertools.combinations(range(n), q):
                a = direct_matrix(q, m, rho, translations)
                s = np.linalg.svd(a, compute_uv=False)
                rank = int(np.sum(s > 1e-8))
                assert rank == predicted_rank(q, m, translations)
                coset = any(set(translations) == {r + m*t for t in range(q)}
                            for r in range(m))
                assert (rank == n) == coset
                tested += 1
                if coset:
                    vals = sorted(s**2)
                    target = spectrum(q, m, rho)
                    assert np.allclose(vals, target, atol=1e-9, rtol=1e-9)
                    lo, hi = sharp_bounds(q, m, rho)
                    assert abs(vals[0] - lo) < 1e-9
                    assert abs(vals[-1] - hi) < 1e-9
                    determinant = m**n * rho**(q*m*(m-1)) * (1-rho**n)**(2*m*(q-1))
                    assert abs(np.prod(vals)/determinant - 1) < 1e-8
                    full_spectra += 1
    for q in range(2, 9):
        for m in range(2, 8):
            rstar = optimal_r(q, m)
            assert 0 < rstar < 1
            def condition(r):
                rho = r ** (1 / m)
                aa, bb = sharp_bounds(q, m, rho)
                return bb / aa
            for factor in (0.99, 0.95):
                assert condition(rstar) < condition(rstar * factor)
                assert condition(rstar) < condition(rstar + (1-rstar)*(1-factor))
            if q % 2 == 0:
                alpha = (m - 1) / m
                explicit = (math.sqrt(1+alpha*alpha)-1) / alpha
                assert abs(explicit-rstar) < 1e-12
    print(f'CHECK_OK masks={tested} full_spectra={full_spectra} optimizer_pairs=42')


if __name__ == '__main__':
    run()
