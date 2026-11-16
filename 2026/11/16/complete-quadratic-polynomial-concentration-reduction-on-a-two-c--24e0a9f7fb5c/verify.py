"""Independent, reproducible checks of the quarter-ball quadratic concentration reduction.
Requires Python 3, numpy and scipy. All identities in the mathematical proof are exact;
finite checks corroborate rather than replace that argument.
"""
from math import gamma, pi, sqrt, comb
from itertools import combinations_with_replacement
import numpy as np
from scipy.linalg import eigh
from scipy.special import gammaln
from numpy.polynomial.legendre import leggauss


def absolute_ball_moment(d, exponents):
    assert len(exponents) == d
    z = gammaln(d / 2 + 1) - gammaln((d + sum(exponents)) / 2 + 1)
    z += sum(gammaln((a + 1) / 2) - gammaln(.5) for a in exponents)
    return float(np.exp(z))


def signed_moment(d, exponents, quadrant):
    if any(a % 2 for a in exponents[2:]):
        return 0.
    if not quadrant and any(a % 2 for a in exponents[:2]):
        return 0.
    return absolute_ball_moment(d, exponents) / (4 if quadrant else 1)


def poly(d, terms):
    """terms: list (coefficient, list of (coordinate index, power))."""
    result = {}
    for c, exponents in terms:
        alpha = [0] * d
        for i, power in exponents:
            alpha[i] += power
        alpha = tuple(alpha)
        result[alpha] = result.get(alpha, 0) + c
    return {a: v for a, v in result.items() if v}


def matrix(d, vectors, quadrant):
    out = np.zeros((len(vectors), len(vectors)), dtype=float)
    for i, f in enumerate(vectors):
        for j, g in enumerate(vectors[:i + 1]):
            value = 0.
            for a, u in f.items():
                for b, v in g.items():
                    ex = tuple(x + y for x, y in zip(a, b))
                    value += u * v * signed_moment(d, ex, quadrant)
            out[i, j] = out[j, i] = value
    return out


def spectrum(d, vectors):
    G = matrix(d, vectors, False)
    K = matrix(d, vectors, True)
    return eigh(K, G, eigvals_only=True)


def construction(d):
    assert d >= 3
    scalar = [
        poly(d, [(1, [])]),
        poly(d, [(1, [(0, 1)]), (1, [(1, 1)])]),
        poly(d, [(1, [(0, 2)]), (1, [(1, 2)])]),
        poly(d, [(1, [(0, 1), (1, 1)])]),
    ]
    anti = [
        poly(d, [(1, [(0, 1)]), (-1, [(1, 1)])]),
        poly(d, [(1, [(0, 2)]), (-1, [(1, 2)])]),
    ]
    vec = [
        poly(d, [(1, [(2, 1)])]),
        poly(d, [(1, [(0, 1), (2, 1)]), (1, [(1, 1), (2, 1)])]),
    ]
    vecanti = [poly(d, [(1, [(0, 1), (2, 1)]), (-1, [(1, 1), (2, 1)])])]
    m = d - 2
    residual = poly(d, [(1, [(j, 2)]) for j in range(2, d)]
                    + [(-m / d, []), (m / d, [(0, 2)]), (m / d, [(1, 2)])])
    return scalar, anti, vec, vecanti, residual


def analytic_small_eigenvalues(d):
    c = ((d + 2) * sqrt(d + 4) * gamma(d / 2 + 1)
         / (8 * sqrt(2 * pi) * gamma((d + 5) / 2)))
    D = np.array([[(1 - 2 / pi) / 4, c], [c, 1 / 4]])
    V = np.array([[1 / 4, 2 * c], [2 * c, (1 + 2 / pi) / 4]])
    a = (1 - 2 / pi) / 4
    return D, V, a


def full_basis(d):
    vectors = [poly(d, [(1, [])])]
    for i in range(d):
        vectors.append(poly(d, [(1, [(i, 1)])]))
    for i in range(d):
        for j in range(i, d):
            vectors.append(poly(d, [(1, [(i, 1), (j, 1)])]))
    return vectors


def check(d):
    scalar, anti, vec, vecanti, residual = construction(d)
    D, V, a = analytic_small_eigenvalues(d)
    eD = spectrum(d, anti)
    eV = spectrum(d, vec)
    eA = spectrum(d, vecanti)
    assert np.max(np.abs(eD - np.linalg.eigvalsh(D))) < 3e-12
    assert np.max(np.abs(eV - np.linalg.eigvalsh(V))) < 3e-12
    assert abs(eA[0] - a) < 3e-12
    assert abs(spectrum(d, [residual])[0] - .25) < 3e-12
    # The conditional-mean residual is orthogonal in both inner products to the 4 scalar modes.
    for q in (False, True):
        R = matrix(d, scalar + [residual], q)
        assert np.max(np.abs(R[:4, 4])) < 3e-12
    qdim = d * (d - 3) // 2
    predicted = list(spectrum(d, scalar)) + list(eD)
    predicted += list(eV) * (d - 2)
    predicted += [a] * (d - 2) + [.25] * (qdim + 1)
    actual = spectrum(d, full_basis(d))
    assert len(predicted) == len(actual) == (d + 1) * (d + 2) // 2
    assert np.max(np.abs(np.sort(predicted) - actual)) < 4e-11
    assert abs(actual.sum() - len(actual) / 4) < 4e-11
    return actual[0], actual[-1]


def independent_disk_quadrature(d):
    # Independent polar integration of the 2-dimensional marginal density.
    # Used ONLY on the four scalar basis polynomials; no gamma moment table enters here.
    scalar, *_ = construction(d)
    nodes, weights = leggauss(90)
    radial = (nodes + 1) / 2
    rw = weights / 2
    theta = (nodes + 1) * pi / 4
    tw = weights * pi / 4
    R = radial[:, None]
    T = theta[None, :]
    x, y = R * np.cos(T), R * np.sin(T)
    vals = np.array([np.broadcast_to(np.ones_like(x + y), x.shape), x + y, x * x + y * y, x * y])
    jac = d / (2 * pi) * R * (1 - R * R) ** ((d - 2) / 2) * rw[:, None] * tw[None, :]
    Q = np.einsum('aij,bij,ij->ab', vals, vals, jac)
    K = matrix(d, scalar, True)
    return np.max(np.abs(Q - K))


if __name__ == '__main__':
    for d in range(3, 13):
        lo, hi = check(d)
        print(f'd={d}: min={lo:.12f}, max={hi:.12f}, full/reduced/trace PASS')
    err = independent_disk_quadrature(4)
    print(f'd=4 independent polar integration max entry error {err:.3g}')
    assert err < 3e-13
    print('ALL CHECKS PASSED')
