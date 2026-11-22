#!/usr/bin/env python3
"""Independent finite Laplace-domain checks for the semi-Markov row inversion theorem."""
import numpy as np


def laplace_kernels(n, s, rng):
    """Proper joint exit/sojourn laws: destination-weighted Gamma(k,scale)."""
    w = rng.uniform(0.1, 1.0, (n, n))
    np.fill_diagonal(w, 0.0)
    w /= w.sum(axis=1)[:, None]
    shapes = rng.integers(1, 5, size=(n, n))
    scales = rng.uniform(0.3, 2.0, size=(n, n))
    return w * (1.0 + scales * s) ** (-shapes)


def predict_and_invert(Q, s):
    n = Q.shape[0]
    S = list(range(1, n))
    d = (1 - Q.sum(axis=1)) / s
    P = np.linalg.solve(np.eye(n)-Q, np.diag(d))
    Y = P[0, S]
    R = Q[np.ix_(S, S)]
    r = Q[S, 0]
    B = np.linalg.solve(np.eye(n-1)-R, np.diag(d[S]))
    h = np.linalg.solve(np.eye(n-1)-R, r)
    z = np.linalg.solve(B.T, Y)
    recovered = z / (1 + z @ h)
    calculated = (Q[0, S] @ B) / (1 - Q[0, S] @ h)
    assert np.allclose(Y, calculated, atol=1e-11, rtol=1e-11)
    assert np.allclose(recovered, Q[0, S], atol=1e-11, rtol=1e-11)
    assert 1 - Q[0, S] @ h > 0
    return Y


def line_distance(x0, x1, x2):
    v = x1-x0
    return np.linalg.norm(x2-x0-np.dot(x2-x0, v)/np.dot(v,v)*v)


def run():
    rng = np.random.default_rng(5261904)
    checks = 0
    for n in (3, 4, 5, 7):
        for s in (0.07, 0.35, 1.1, 2.7, 8.0):
            qbase = laplace_kernels(n, s, rng)
            predict_and_invert(qbase, s)
            checks += 1
            qother = laplace_kernels(n, s, rng)
            x = []
            for theta in (0., 0.25, 0.6, 1.):
                q = qbase.copy()
                q[0, :] = (1-theta)*qbase[0, :] + theta*qother[0, :]
                x.append(predict_and_invert(q, s))
                checks += 1
            assert line_distance(x[0], x[3], x[1]) < 1e-10
            assert line_distance(x[0], x[3], x[2]) < 1e-10
            checks += 2
    # Explicit non-collinear perturbation when three distinct destinations exist.
    n, s = 4, 0.7
    a = laplace_kernels(n, s, rng)
    b = laplace_kernels(n, s, rng)
    c = laplace_kernels(n, s, rng)
    ys = []
    for row in (a[0], b[0], c[0]):
        t = a.copy()
        t[0] = row
        ys.append(predict_and_invert(t, s))
        checks += 1
    assert line_distance(*ys) > 1e-7
    checks += 1
    # Projective transformations preserve the rank of homogeneous point arrays.
    for n in (3, 4, 6):
        for s in (0.2, 1.4, 4.0):
            base = laplace_kernels(n, s, rng)
            qs, ps = [], []
            for j in range(n+2):
                Q = base.copy()
                Q[0] = laplace_kernels(n, s, rng)[0]
                qs.append(np.r_[Q[0, 1:], 1.0])
                ps.append(np.r_[predict_and_invert(Q, s), 1.0])
                checks += 1
            assert np.linalg.matrix_rank(np.array(qs)) == np.linalg.matrix_rank(np.array(ps))
            checks += 1
    print(f"PASS: {checks} numerical checks; max residual <1e-10; affine and nonaffine examples distinguished")

if __name__ == '__main__':
    run()
