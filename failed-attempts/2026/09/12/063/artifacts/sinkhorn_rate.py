"""1D proxy experiment: static-EOT displacement midpoint vs true OT midpoint.

Proxy model (documented limitation): on [0,1] with quadratic cost we compute the
static entropic plan pi_eps via log-domain Sinkhorn, push it forward under
(x+y)/2 to get an approximate entropic midpoint, and compare in W2 (via CDFs)
to the exact OT midpoint ((Id+T)/2)#mu0. The true dynamic Schrodinger bridge
midpoint differs from this proxy by an additional O(sqrt(eps)) diffusive spread,
so both share the same qualitative small-eps power-law behavior for smooth data.
Purpose: bounded recovery test checking whether the EOT-vs-geodesic rate exponent
depends on finer regularity than the coarse (Linf + Fisher) bounds in the target.
"""
import json
import numpy as np

N = 256
xs = np.linspace(0.0, 1.0, N)
dx = xs[1] - xs[0]
C = (xs[:, None] - xs[None, :]) ** 2  # quadratic cost matrix

def to_grid(dens):
    p = np.asarray(dens, dtype=float)
    p = np.maximum(p, 1e-300)
    return p / (p.sum() * dx)

def cdf(p):
    return np.cumsum(p) * dx

def quantile_map(mu0, mu1):
    """Monotone OT map T pushing mu0 to mu1 via CDF inversion."""
    F0, F1 = cdf(mu0), cdf(mu1)
    return np.interp(F0, np.concatenate([[0.0], F1]), np.concatenate([[xs[0]], xs]))

def sinkhorn(mu0, mu1, eps, iters=20000, tol=1e-12):
    log_a, log_b = np.log(mu0), np.log(mu1)
    logK = -C / eps + np.log(dx)  # include quadrature weight in kernel sums
    f = np.zeros(N)
    g = np.zeros(N)
    for _ in range(iters):
        # f <- log mu0 - log(K exp(g)); g <- log mu1 - log(K^T exp(f))
        g = log_b - np.logaddexp.reduce((f[:, None] + logK), axis=0)
        f2 = log_a - np.logaddexp.reduce((g[None, :] + logK), axis=1)
        if np.max(np.abs(f2 - f)) < tol:
            f = f2
            break
        f = f2
    P = np.exp(f[:, None] + g[None, :] + logK) / dx  # density: P*dx*dx sums to 1
    return P

def w2_1d(p, q):
    Fp, Fq = cdf(p), cdf(q)
    # quantile functions on uniform grid of mass
    u = np.linspace(0, 1, 2001)
    Qp = np.interp(u, np.concatenate([[0.0], Fp]), np.concatenate([[xs[0]], xs]))
    Qq = np.interp(u, np.concatenate([[0.0], Fq]), np.concatenate([[xs[0]], xs]))
    return float(np.sqrt(np.trapz((Qp - Qq) ** 2, u)))

def midpoint_of_plan(P):
    mid = np.zeros(N)
    # distribute each (i,j) mass to grid points bracketing (xi+xj)/2
    z = (xs[:, None] + xs[None, :]) / 2.0
    pos = np.clip(z / dx, 0, N - 1 - 1e-12)
    lo = pos.astype(int)
    hi = np.minimum(lo + 1, N - 1)
    w = pos - lo
    np.add.at(mid, lo, P * (1 - w))
    np.add.at(mid, hi, P * w)
    return mid / (mid.sum() * dx)

def run_case(name, mu0, mu1, eps_list):
    T = quantile_map(mu0, mu1)
    z_true = (xs + T) / 2.0
    # exact OT midpoint density via histogram of quantile pushforward
    u = np.linspace(0, 1, 4001)
    F0 = cdf(mu0)
    X = np.interp(u, np.concatenate([[0.0], F0]), np.concatenate([[xs[0]], xs]))
    Z = (X + np.interp(X, xs, T)) / 2.0
    ot_mid, _ = np.histogram(Z, bins=N, range=(0, 1))
    ot_mid = ot_mid / (ot_mid.sum() * dx)
    out = []
    for eps in eps_list:
        P = sinkhorn(mu0, mu1, eps)
        me = midpoint_of_plan(P)
        err = w2_1d(me, ot_mid)
        out.append([eps, err])
        print(f"{name} eps={eps:.4f} W2mid={err:.6f}", flush=True)
    return out

def fit_slope(rows):
    e = np.array([r[0] for r in rows if r[1] > 0])
    v = np.array([r[1] for r in rows if r[1] > 0])
    A = np.vstack([np.log(e), np.ones_like(e)]).T
    slope, intercept = np.linalg.lstsq(A, np.log(v), rcond=None)[0]
    return float(slope), float(intercept)

if __name__ == "__main__":
    mu0 = to_grid(np.ones(N))
    smooth = to_grid(1.0 + 0.45 * np.sin(2 * np.pi * xs) + 0.15 * np.cos(4 * np.pi * xs))
    # rough: Fisher-matched high-frequency wiggle + log cusp, still bounded above/below
    k = 24
    rough = to_grid(1.0 + (0.9 / k) * np.sin(2 * np.pi * k * xs)
                    + 0.25 * (1.0 / np.log(20.0 + 500.0 * np.abs(xs - 0.5))))
    rough = to_grid(np.clip(rough, 0.35, None))
    eps_list = [0.004, 0.008, 0.016, 0.032]
    res = {}
    for name, mu1 in [("smooth", smooth), ("rough", rough)]:
        rows = run_case(name, mu0, mu1, eps_list)
        slope, icept = fit_slope(rows)
        res[name] = {"rows": rows, "loglog_slope": slope, "intercept": icept}
        print(f"{name}: fitted log-log slope = {slope:.3f}")
    with open("results.json", "w") as f:
        json.dump(res, f, indent=2)
    print("wrote results.json")
