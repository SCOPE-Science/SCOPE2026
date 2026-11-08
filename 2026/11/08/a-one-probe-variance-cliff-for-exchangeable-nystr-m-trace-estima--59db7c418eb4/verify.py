"""Reproduce the projector-rank transition and Gaussian leave-one-out moments.

Run: python verify.py   (requires NumPy)
"""
import math
import numpy as np

rng = np.random.default_rng(20261105)
checks = 0


def close(u, v, atol=1e-8):
    global checks
    checks += 1
    assert abs(u - v) < atol, (u, v)


def nystrom(A, Omega):
    Y = A @ Omega
    return Y @ np.linalg.pinv(Omega.T @ Y, rcond=1e-12) @ Y.T


def fun(B):
    lam, V = np.linalg.eigh((B + B.T) / 2)
    return (V * np.log1p(np.maximum(lam, 0))) @ V.T


# Test the implemented estimator, not merely its simplified geometry.
for r in (2, 3, 4, 6):
    n = r + 2
    lam = 2.0
    a = math.log1p(lam)
    A = np.zeros((n, n)); A[:r, :r] = lam * np.eye(r)
    for probes in (r, r + 1):
        for trial in range(12):
            Omega = rng.standard_normal((n, probes))
            full = fun(nystrom(A, Omega))
            basic = []
            for i in range(probes):
                M = fun(nystrom(A, np.delete(Omega, i, axis=1)))
                val = np.trace(M) + Omega[:, i] @ (full - M) @ Omega[:, i]
                basic.append(val)
                if probes == r:
                    G = Omega[:r, :]
                    other = np.delete(G, i, axis=1)
                    Q, _ = np.linalg.qr(other, mode='reduced')
                    u = G[:, i]
                    resid = np.linalg.norm(u - Q @ (Q.T @ u)) ** 2
                    close(val, a * (r - 1 + resid), atol=2e-8)
                else:
                    close(val, r * a, atol=2e-8)
            if probes == r + 1:
                close(np.mean(basic), r*a, atol=2e-8)

# Exact Gaussian identities underlying the proof: angle moments and Laplace law.
theta = (np.arange(200001) + 0.5) * math.pi / 200001
close(np.mean(np.sin(theta)**2), 0.5, atol=5e-11)
close(np.mean(np.sin(theta)**4), 0.375, atol=5e-11)
for s in (0.2, 0.7, 3.0):
    numerical = np.mean((1 + s*np.sin(theta)**2)**(-2))
    exact = (s+2)/(2*(1+s)**1.5)
    close(numerical, exact, atol=5e-10)

# Independent Monte Carlo calculation from QR leave-one-out geometry.
for r, nsamp in ((2, 35000), (3, 35000), (5, 30000), (8, 18000)):
    vals = np.zeros((nsamp, r))
    for t in range(nsamp):
        G = rng.standard_normal((r, r))
        for i in range(r):
            Q, _ = np.linalg.qr(np.delete(G, i, axis=1), mode='reduced')
            u = G[:, i]
            vals[t, i] = np.linalg.norm(u-Q@(Q.T@u))**2
    avg = np.mean(vals, axis=1)
    empirical_var = np.var(avg)
    error_proxy = np.sum((vals - avg[:, None])**2, axis=1)/(r*(r-1))
    target_var = (r+3)/(2*r)
    target_proxy = 3/(2*r)
    close(np.mean(avg), 1, atol=0.04)
    close(empirical_var, target_var, atol=0.055)
    close(np.mean(error_proxy), target_proxy, atol=0.06)
    close(np.cov(vals[:, 0], vals[:, 1], bias=True)[0, 1], 0.5, atol=0.055)
    if r == 2:
        for s in (0.5, 1):
            close(np.mean(np.exp(-s*avg)), (s+2)/(2*(1+s)**1.5), atol=0.014)
    print(f'rank={r} var={empirical_var:.6f} target={target_var:.6f}; mean_proxy={error_proxy.mean():.6f} target={target_proxy:.6f}')

print(f'PASS {checks} deterministic/Monte-Carlo assertions')
