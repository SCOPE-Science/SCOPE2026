#!/usr/bin/env python3
"""Independent small-volume checks of the prime-torus weak-absorption coefficient.
Usage: python3 verify.py
Requires numpy, scipy (for optional direct non-Hermitian diagonalization).
"""
import itertools, math
import numpy as np


def eigenblocks(primes):
    vals = [range((p + 1) // 2) for p in primes]
    for a in itertools.product(*vals):
        yield a, 2 * sum(math.cos(2 * math.pi * x / p) for p, x in zip(primes, a))


def factor(p, a):
    if a == 0:
        return np.array([[2 / p]], dtype=complex)
    z = np.exp(2j * np.pi * a / p)
    return np.array([[2, 1 + z.conjugate() ** 2], [1 + z ** 2, 2]], dtype=complex) / p


def exact_factors(p, a):
    if a == 0:
        return [2 / p]
    return [(2 - 2 * abs(math.cos(2 * math.pi * a / p))) / p,
            (2 + 2 * abs(math.cos(2 * math.pi * a / p))) / p]


def lower(primes):
    return math.prod((2 - 2 * math.cos(math.pi / p)) / p for p in primes)


def graph_adjacency(primes):
    n = math.prod(primes)
    A = np.zeros((n, n), dtype=float)
    vertices = list(itertools.product(*(range(p) for p in primes)))
    ids = {v: i for i, v in enumerate(vertices)}
    for i, v in enumerate(vertices):
        for j, p in enumerate(primes):
            for shift in (-1, 1):
                w = list(v)
                w[j] = (w[j] + shift) % p
                A[i, ids[tuple(w)]] = 1
    detector = np.array([int(all(x <= 1 for x in v)) for v in vertices])
    assert np.allclose(A, A.T)
    assert np.all(A.sum(axis=0) == 2*len(primes))
    assert detector.sum() == 2 ** len(primes)
    return A, detector


def test(primes, direct=False):
    values = list(eigenblocks(primes))
    unique = len({round(z, 10) for _, z in values})
    assert unique == len(values), ('unexpected eigenvalue collision', primes)
    mu = min(math.prod(min(exact_factors(p,a)) for p,a in zip(primes, alpha)) for alpha, _ in values)
    target = lower(primes)
    assert math.isclose(mu, target, rel_tol=1e-12, abs_tol=1e-14)
    min_alpha = tuple((p - 1)//2 for p in primes)
    assert [alpha for alpha,_ in values if math.isclose(math.prod(min(exact_factors(p,a)) for p,a in zip(primes,alpha)),mu,rel_tol=1e-10)] == [min_alpha]
    for alpha, _ in values:
        G = np.ones((1, 1), dtype=complex)
        for p,a in zip(primes,alpha):
            G = np.kron(G, factor(p,a))
        eigen = np.linalg.eigvalsh(G)
        expected = sorted(math.prod(x) for x in itertools.product(*(exact_factors(p,a) for p,a in zip(primes,alpha))))
        assert np.allclose(eigen, expected, atol=2e-14)
        assert eigen.min() > 0
    print('primes:', primes, 'N:', math.prod(primes), 'sectors:', len(values), 'slowest rate:', format(mu,'.14g'), 'min sector:', min_alpha)
    if direct:
        A, detector = graph_adjacency(primes)
        previous = None
        for eps in (0.08, 0.04, 0.02):
            eigen = np.linalg.eigvals(A - 1j * eps * np.diag(detector))
            decay = -max(np.imag(eigen))
            # Degenerate perturbation yields convergence to the sharp coefficient.
            error = abs(decay / eps - mu)/mu
            assert decay > 0
            assert error < 0.005, (eps,decay/eps,mu,error)
            if previous is not None:
                assert error <= previous * 1.05
            previous = error
            print('  eps=', eps, 'measured min decay=', format(decay,'.12g'), 'rate/eps=', format(decay/eps,'.12g'), 'rel_error=', format(error,'.6g'))


if __name__ == '__main__':
    for p, direct in [((5,7),True), ((5,11),True), ((7,11),True), ((5,7,11),False)]:
        test(p,direct)
    print('ALL CHECKS PASSED')
