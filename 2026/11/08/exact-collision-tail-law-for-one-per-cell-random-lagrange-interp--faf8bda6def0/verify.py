"""Reproduce checks for the three-node stratified Lagrange weight tail.
Requires Python 3 with numpy. Numerical diagnostics do not prove tail or moments.
"""
import math
import numpy as np


def weights(nodes, z):
    w = np.ones((nodes.shape[0], nodes.shape[1]), dtype=float)
    for j in range(nodes.shape[1]):
        for k in range(nodes.shape[1]):
            if j != k:
                w[:, j] *= (z - nodes[:, k]) / (nodes[:, j] - nodes[:, k])
    return w


def simpson(f, a, b, even_n=20000):
    assert even_n % 2 == 0
    h = (b - a) / even_n
    return h / 3.0 * (f(a) + f(b) + 4 * sum(f(a + j*h) for j in range(1, even_n, 2))
                      + 2 * sum(f(a + j*h) for j in range(2, even_n, 2)))


def main():
    checks = 0
    rng = np.random.default_rng(20260324)
    n = 1200000
    x = np.column_stack([(j + rng.random(n)) / 3 for j in range(3)])
    w = weights(x, 0.5)
    assert np.max(abs(np.sum(w, axis=1) - 1)) < 1e-8
    assert np.max(abs(np.sum(w * x, axis=1) - 0.5)) < 1e-8
    assert np.max(abs(np.sum(w * x*x, axis=1) - 0.25)) < 1e-8
    checks += 3
    K = 9/16 - math.log(2)/2
    expectation = 3 * simpson(lambda u: ((0.5-u)/(1/3-u))**2, 2/3, 1)
    assert abs(K - 0.5*expectation) < 1e-11
    checks += 1
    for i in [1, 2]:
        b = i / 3
        others = np.array([0.82]) if i == 1 else np.array([0.16])
        C = (0.5-b) * np.prod((0.5-others)/(b-others))
        for eps in [1e-3, 1e-4, 1e-5, 1e-6]:
            if i == 1:
                nodes = np.array([[b-0.4*eps, b+0.6*eps, others[0]]])
            else:
                nodes = np.array([[others[0], b-0.4*eps, b+0.6*eps]])
            W = np.linalg.norm(weights(nodes, 0.5))
            assert abs(eps*W - math.sqrt(2)*abs(C)) < 20*eps
            checks += 1
    W = np.linalg.norm(w, axis=1)
    for T in (6.0, 9.0, 12.0, 18.0):
        tail = float(np.mean(W > T))
        ratio = T*T*tail / K
        print(f"threshold={T:g} tail={tail:.9g} t^2*tail={T*T*tail:.9g} ratio_to_constant={ratio:.5g}")
        # Random observations are intentionally tested with a generous tolerance.
        assert 0.80 < ratio < 1.20
        checks += 1
    # The exceptional central linear interpolant is a convex combination.
    p = np.column_stack([rng.random(100000)/2, 0.5+rng.random(100000)/2])
    pw = weights(p, 0.5)
    assert np.min(pw) >= -1e-12
    assert np.max(np.linalg.norm(pw, axis=1)) <= 1 + 1e-12
    checks += 2
    print(f"closed_form_tail_constant={K:.15f}")
    print(f"checks_passed={checks}; Monte Carlo checks are diagnostics, not an infinite proof")


if __name__ == '__main__':
    main()
