"""Bounded probe for lane-1731: GUE/GOE finite-matrix model of q = s1 s2 s1 + s1 s2.

Maps: (a) eigenvalue distribution near 0 (Brown-mass signal),
      (b) radial mass exponent fit, (c) max |ev| (bulk edge vs outliers),
      (d) s_min(Q - lam I) grid (resolvent-gap / spectrum signal).
Model: independent Wigner matrices -> free semicirculars (radius 2).
"""
import numpy as np

rng = np.random.default_rng(7)
N = 700

def wigner(n):
    X = rng.standard_normal((n, n))
    return (X + X.T) / np.sqrt(2 * n)  # semicircle radius 2

S1 = wigner(N)
S2 = wigner(N)
# sanity: spectra inside [-2,2] up to fluctuations
print("spec S1 range:", np.linalg.eigvalsh(S1).min(), np.linalg.eigvalsh(S1).max())
Q = S1 @ S2 @ S1 + S1 @ S2
ev = np.linalg.eigvals(Q)
r = np.abs(ev)
print("N =", N)
print("max|ev| =", r.max(), " mean|ev| =", r.mean(), " min|ev| =", r.min())
print("quantiles:", np.quantile(r, [0, .005, .01, .05, .25, .5, .75, .95, .99, 1.0]))
for t in [0.02, 0.05, 0.1, 0.2, 0.5, 1.0]:
    print(f"frac |ev|<{t}:", float(np.mean(r < t)))
# radial exponent fit: log F(r) = a log r + c over t grid
ts = np.array([0.02, 0.03, 0.05, 0.08, 0.12, 0.2, 0.3, 0.5])
Fs = np.array([np.mean(r < t) for t in ts])
A = np.vstack([np.log(ts), np.ones_like(ts)]).T
a, c = np.linalg.lstsq(A, np.log(Fs + 1e-12), rcond=None)[0]
print("radial exponent fit: F(r)~r^a, a =", a)
# resolvent gap probes
for lam in [0j, 0.25, 0.5, 1.0, 2.0, 3.0, 5.0, 8.0, 1j, 2j, 1 + 1j, -1.0]:
    M = Q - lam * np.eye(N)
    s = np.linalg.svd(M, compute_uv=False)
    print(f"lam={lam}: smin={s[-1]:.5f} smax={s[0]:.3f}")
np.save("output/artifacts/ev_lane1731_N700.npy", ev)
print("saved output/artifacts/ev_lane1731_N700.npy")
