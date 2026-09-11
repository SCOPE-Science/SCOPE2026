"""Refined S=2 study: solve on two grids, tighten residual, refined scan for ALL
equatorial-symmetric MOTS roots (inner+outer), expand scan window, report
peq(scan), barrier minima between/within roots, areas of each root, and a
Kerr-comparison quantity. Goal: decide whether S=2 MOTS census is resolved
enough to trust D sign."""
import numpy as np, math, sys, json
import puncture_mots as PM
from puncture_mots import solve_u, make_interp, shoot, mots_area, sphere_H

Uc, psi, Mfall, res = solve_u(2.0, verbose=False)
P, Pr, Pt = make_interp(psi, Uc)
print("Mfall=", Mfall, "res=", res, "umax=", Uc.max(), flush=True)

# dense wide scan
hs0 = np.linspace(0.1, 2.5, 97)
peq = []
for h0 in hs0:
    try:
        h, p, ts, hsa, psa = shoot(float(h0), P, Pr, Pt, nstp=1200)
        peq.append(p if np.isfinite(p) else np.nan)
    except Exception:
        peq.append(np.nan)
peq = np.array(peq)
for h0, p in zip(hs0, peq):
    print(f"h0={h0:.3f} peq={p:+.5f}", flush=True)
roots = []
for i in range(len(hs0)-1):
    fa, fb = peq[i], peq[i+1]
    if np.isfinite(fa) and np.isfinite(fb) and fa*fb < 0:
        a, b = hs0[i], hs0[i+1]
        fa0 = shoot(a, P, Pr, Pt, nstp=1200)[1]
        for _ in range(40):
            m = .5*(a+b)
            pm = shoot(m, P, Pr, Pt, nstp=1200)[1]
            if fa0*pm <= 0: b = m
            else: a, fa0 = m, pm
        roots.append(.5*(a+b))
print("roots:", roots, flush=True)
for h0 in roots:
    h, p, ts, hsa, psa = shoot(h0, P, Pr, Pt, nstp=6000)
    A = mots_area(ts, hsa, psa, P)
    D = A/(8*math.pi*2.0)-1
    print(f"root h0={h0:.5f} peq={p:.2e} A={A:.4f} D={D:+.4f} hmin={hsa.min():.4f} hmax={hsa.max():.4f}", flush=True)
# barrier: coordinate-sphere H between roots and outside
for r in [0.3, 0.5, 0.6, 0.8, 1.0, 1.5, 2.0, 4.0]:
    m, mn = sphere_H(r, P, Pr)
    print(f"sphere r={r}: Hmean={m:.4f} Hmin={mn:.4f}", flush=True)
