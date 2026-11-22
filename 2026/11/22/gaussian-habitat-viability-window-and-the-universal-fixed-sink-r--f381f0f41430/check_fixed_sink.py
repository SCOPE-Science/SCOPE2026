"""Supplementary numerical checks for fixed-sink random-habitat eigenvalue asymptotics.

Run: python check_fixed_sink.py
Requires numpy and scipy. Numerical checks supplement, not replace, the proof.
"""
import itertools
import math
import numpy as np
from scipy.sparse import csr_matrix, diags
from scipy.sparse.linalg import eigsh


def laplacian(adj):
    return np.diag(np.sum(adj, axis=1)) - adj


def low_eigenvalue(inner, sink_count):
    return float(np.linalg.eigvalsh(laplacian(inner) + np.diag(sink_count))[0])


def finite_sandwich():
    tested = 0
    # Exhaust all 4-vertex internal graphs and 3^4 nonnegative integer
    # boundary-degree vectors; assert the deterministic eigenvalue bracket
    # when its gap hypothesis is satisfied.
    for mask in range(1 << 6):
        A = np.zeros((4, 4), dtype=float)
        for j, (u, v) in enumerate(itertools.combinations(range(4), 2)):
            if (mask >> j) & 1:
                A[u, v] = A[v, u] = 1
        gap = np.linalg.eigvalsh(laplacian(A))[1]
        for ztuple in itertools.product(range(3), repeat=4):
            z = np.array(ztuple, dtype=float)
            s = float(z.max())
            if gap <= s + 1e-12:
                continue
            bar = float(z.mean())
            lam = low_eigenvalue(A, z)
            assert bar - s * s / (gap - s) - 1e-10 <= lam <= bar + 1e-10
            tested += 1
    return tested


def er_trial(n, s, p, rng):
    m = n - s
    upper = np.triu(rng.random((m, m)) < p, 1)
    adj = upper | upper.T
    z = rng.binomial(s, p, size=m)
    ii, jj = np.nonzero(adj)
    A = csr_matrix((np.ones(len(ii)), (ii, jj)), shape=(m, m))
    L = diags(np.asarray(A.sum(axis=1)).ravel().astype(float) + z) - A
    eigen = float(eigsh(L, k=1, which="SA", tol=1e-10, maxiter=4000, return_eigenvectors=False)[0])
    bar = float(z.mean())
    assert eigen <= bar + 1e-8
    return eigen, bar


def schur_complement_check():
    # Exact block identity up to floating-point error: bar(z)-lambda=b^T K^{-1}b.
    rng = np.random.default_rng(4372)
    validated = 0
    for m in (12, 20, 36):
        for _ in range(20):
            p = 0.45
            A = np.triu((rng.random((m, m)) < p).astype(float), 1)
            A += A.T
            z = rng.binomial(3, p, size=m).astype(float)
            L = laplacian(A) + np.diag(z)
            lam = np.linalg.eigvalsh(L)[0]
            e = np.ones(m) / math.sqrt(m)
            Q = np.eye(m) - np.outer(e, e)
            bar = float(np.mean(z))
            b = Q @ (z * e)
            eigval, eigvec = np.linalg.eigh(Q @ L @ Q)
            # q=0 produces one zero artificial eigenvalue; invert only Q range.
            projection = np.abs(eigvec.T @ e)
            good = projection < 1e-6
            eigval = eigval[good]
            eigvec = eigvec[:, good]
            # Need separation of smallest eigenvalue from Q spectrum.
            if min(eigval) <= lam + 1e-9:
                continue
            rhs = sum(((eigvec.T @ b)**2) / (eigval - lam))
            assert abs((bar - lam) - rhs) < 5e-8
            validated += 1
    return validated


def sample_check():
    rng = np.random.default_rng(20261116)
    s = 2
    p = 0.4
    values = []
    for n in (96, 192, 384):
        diffs = []
        centered = []
        for _ in range(72):
            eigen, bar = er_trial(n, s, p, rng)
            diffs.append((n-s) * (bar - eigen))
            centered.append(math.sqrt(n) * (eigen - s * p))
        mean_correction = float(np.mean(diffs))
        variance_fluctuation = float(np.var(centered, ddof=1))
        values.append((n, round(mean_correction, 6), round(variance_fluctuation, 6)))
        assert 0 < mean_correction < s * s / p + 0.5
        assert 0 < variance_fluctuation < 5
    return values


if __name__ == '__main__':
    count = finite_sandwich()
    schur = schur_complement_check()
    trials = sample_check()
    print('Finite eigenvalue brackets checked:', count)
    print('Schur complement identities checked:', schur)
    print('Erdos-Renyi instances checked:', 72 * len(trials))
    print('n, sample mean of (n-s)(boundary mean - eigenvalue), sample variance of sqrt(n)(eigenvalue - sp)')
    for item in trials:
        print(*item)
    print('Predicted correction:', 2 * (1 - 0.4))
    print('Predicted Gaussian variance:', 2 * 0.4 * (1 - 0.4))
    print('PASS (numerical diagnostics, not an infinite-size certificate)')
