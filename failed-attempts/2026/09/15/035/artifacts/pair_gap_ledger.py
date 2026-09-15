"""Reproducible ledger for lane-20232 target-block analysis.
Computes (i) GUE small-gap CDF (Wigner surmise) and pair mass int W,
(ii) Fejer bandlimited concentration (Delta=1,2), (iii) cluster counterexample.
Uses only numpy (no scipy).
"""
import numpy as np

def W(u):
    u = np.asarray(u, float)
    out = np.ones_like(u)
    nz = np.abs(u) > 1e-12
    s = np.sin(np.pi * u[nz]) / (np.pi * u[nz])
    out[nz] = 1 - s ** 2
    out[~nz] = 0.0
    return out

def p_gue(s):
    return 32 / np.pi ** 2 * s ** 2 * np.exp(-4 * s ** 2 / np.pi)

def phi_fejer(u, Delta):
    u = np.asarray(u, float)
    x = np.pi * Delta * u
    out = np.ones_like(u) * float(Delta)
    nz = np.abs(x) > 1e-12
    out[nz] = Delta * (np.sin(x[nz]) / x[nz]) ** 2
    return out

print("== (i) GUE signal ==")
for lam in [0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
    g = np.linspace(0, lam, 20001)
    cdf = np.trapz(p_gue(g), g)
    u = np.linspace(-lam, lam, 40001)
    pm = np.trapz(W(u), u)
    print("lam=%.1f WignerCDF~%.5f pairmass=%.5f poisson=%.3f" % (lam, cdf, pm, 2 * lam))

print("== (ii) Fejer concentration ==")
for Delta in [1.0, 2.0]:
    U = np.linspace(-20, 20, 320001)
    du = U[1] - U[0]
    ph = phi_fejer(U, Delta)
    print("Delta=%s total=%.6f (expect ~1)" % (Delta, np.sum(ph) * du))
    for lam in [0.5, 0.7, 0.9]:
        m = np.abs(U) <= lam
        pin = np.sum(ph[m]) * du
        gin = np.sum(ph[m] * W(U[m])) * du
        tail = np.sum(ph[~m]) * du
        print(" lam=%.1f poisson_in=%.4f gue_in=%.4f tail=%.4f" % (lam, pin, gin, tail))

print("== (iii) cluster counterexample ==")
N = 10000; a = 0.7; eps = 0.01; K = 200
xs = np.arange(K + 1) * eps
cnt = 0
for i in range(K + 1):
    cnt += np.sum(np.abs(xs - xs[i]) <= a + 1e-12) - 1
print("S/N=%.4f I_close=%d I_close/N=%.4f I_close/(2S)=%.3f" % (K / N, cnt, cnt / N, cnt / (2 * K)))
print("GUE-expected I_close/N at lam=0.7 ~0.52; cluster gives %.3f with only 2pct small consecutive gaps" % (cnt / N,))
