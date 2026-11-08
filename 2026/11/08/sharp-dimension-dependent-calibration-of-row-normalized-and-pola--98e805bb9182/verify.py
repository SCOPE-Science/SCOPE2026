"""Numerical and symbolic cross-checks for sharp coherence-conditioned polar alignment.

This verifier checks finite instances and explicit extremizers. It is not a
replacement for the universal spectral and concavity arguments in the proof.
"""
import math
import numpy as np


def gram_extremizer(m, R):
    delta = (m - 1) / R
    lambda_star = (m + math.sqrt(m)) / 2
    lam = min(1 + delta, lambda_star)
    rho = (lam - 1) / (m - 1)
    return (1 - rho) * np.eye(m) + rho * np.ones((m, m)), lam


def min_efficiency(m, R):
    g, lam = gram_extremizer(m, R)
    return m / (lam + math.sqrt((m - 1) * lam * (m - lam)))


def max_polar_error(m, R):
    delta = (m - 1) / R
    return max(math.sqrt(1 + delta) - 1,
               1 - math.sqrt(max(0, 1 - delta)))


def metrics_from_gram(g):
    m = len(g)
    lambdas = np.linalg.eigvalsh(g)
    assert lambdas[0] > 0
    r_min = min((m - 1) / sum(abs(g[i, j]) for j in range(m) if j != i)
                if sum(abs(g[i, j]) for j in range(m) if j != i) > 0
                else float('inf') for i in range(m))
    lam = float(lambdas[-1])
    efficiency = m / (math.sqrt(lam) * np.sqrt(lambdas).sum())
    gap = max(abs(np.sqrt(lambdas) - 1))
    return r_min, efficiency, gap


def verify():
    checks = 0
    rng = np.random.default_rng(20261101)
    for m in range(2, 22):
        for R in [1.001, 1.02, 1.3, 1.7, 2., 3.,
                  max(2., math.sqrt(m)), m/2+1, m, 2*m, 20*m, 100*m]:
            g, lam = gram_extremizer(m, R)
            r, e, gap = metrics_from_gram(g)
            assert r >= R - 2e-9, (m, R, r)
            checks += 1
            assert abs(e - min_efficiency(m, R)) < 2e-12, (m, R, e)
            checks += 1
            assert gap <= max_polar_error(m, R) + 1e-10
            checks += 1
            # Near-equality of upper polar bound via the positive equicorrelation.
            delta = (m - 1) / R
            if math.sqrt(1+delta)-1 >= 1-math.sqrt(max(0,1-delta)):
                # Saturate the row budget: efficient-alignment extremizer may
                # instead use a lower coherence at the interior optimum.
                pos = (1-1/R)*np.eye(m) + np.ones((m,m))/R
                _, _, gp = metrics_from_gram(pos)
                assert abs(gp - max_polar_error(m, R)) < 3e-12
                checks += 1
            # Negative equicorrelation gives the lower spectral boundary if delta < 1.
            if delta < 1:
                neg = (1 + 1/R) * np.eye(m) - (1/R) * np.ones((m, m))
                r2, e2, gap2 = metrics_from_gram(neg)
                assert abs(r2 - R) < 2e-8
                assert abs(gap2 - max_polar_error(m, R)) < 2e-12
                checks += 2
            else:
                # If delta >= 1, the negative spectral edge is a singular
                # *limit*: every individual witness remains full rank.
                eps = 1e-8
                theta = (1-eps)/(m-1)
                near = (1+theta)*np.eye(m)-theta*np.ones((m,m))
                rr,ee,gg = metrics_from_gram(near)
                assert rr + 1e-9 >= R
                checks += 1
                assert gg >= 1-math.sqrt(eps)-1e-5
                checks += 1
    # Random unit-row full-rank examples compared with exact minimax at their own r_min.
    for m in [2, 3, 4, 7, 11, 20]:
        for _ in range(500):
            V = rng.standard_normal((m, m+3))
            V /= np.linalg.norm(V, axis=1)[:, None]
            g = V @ V.T
            r, e, gap = metrics_from_gram(g)
            assert e + 1e-10 >= min_efficiency(m, r), (m, r, e)
            checks += 1
            assert gap <= max_polar_error(m, r) + 1e-10, (m, r, gap)
            checks += 1
            # SVD-based direct polar comparison (critical nonstandard identity).
            u, s, vt = np.linalg.svd(V, full_matrices=False)
            Q = u @ vt
            assert abs(np.linalg.norm(V-Q,2)-gap) < 1e-10
            checks += 1
    # Exact rational tr(G), eigenvalue equalities for m=q^2 and R=q.
    from fractions import Fraction
    for q in range(2, 101):
        m = q*q
        rho = Fraction(1,q)
        lam1 = Fraction(1)+(m-1)*rho
        lam2 = Fraction(1)-rho
        assert lam1 + (m-1)*lam2 == m
        checks += 1
        assert lam1 > lam2 > 0
        checks += 1
        assert (m-1)*rho == Fraction(m-1,q)
        checks += 1
        if q>=3:
            assert lam1 <= Fraction(m,2)+Fraction(q,2)
            checks += 1
    print('PASS:',checks,'finite, spectral, rational and extremal checks')
    for m,R in [(16,4),(256,16),(4096,64)]:
        # Formula only (avoid O(m^3) eigendecomposition on large m)
        lam=min(1+(m-1)/R,(m+math.sqrt(m))/2)
        rho=(lam-1)/(m-1)
        eff=min_efficiency(m,R)
        print('m=%d R=%g lam_max=%.12g eff=%.12g spectral_RN=%.12g' % (m,R,lam,eff,math.sqrt(lam)))

if __name__ == '__main__':
    verify()
