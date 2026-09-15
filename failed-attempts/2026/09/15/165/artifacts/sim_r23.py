"""Bounded recovery probe for r=2/3 BRW lower envelope (TARGET EXIT evidence).

Model: deterministic binary branching (m=2) + centred/scaled Weibull(shape=2/3)
displacements.  Z~Weibull(k=2/3): P[Z>t]=exp(-t^{2/3}), sampled as E^{3/2}, E~Exp(1).
X=(Z-mu)/sd has E[X]=0, Var=1, upper tail P[X>x]=a(x)exp(-lambda x^r) with
r=2/3, lambda=sd^{2/3}. Satisfies DGH Assumptions 1-2 (up to the lower-tail /
moment side condition, irrelevant for this probe).

Probe A (trajectories): estimate (M_n - alpha n^{3/2})/sqrt(n log n) and the
N_n analogue + gap M_n^D - N_n over n=4..12, R runs.
Probe B (first-moment route test): for t_n(K)=alpha n^{3/2}-K sqrt(n log n),
estimate E[Z_n], E[Z_n^2], P[Z_n>0]=P[M_n>t_n] across runs; Paley-Zygmund ratio
E^2/E[Z^2] ~ 0 with E large demonstrates the early-big-jump correlation that
blocks the naive many-to-one/second-moment route at r=2/3.
"""
import json
import numpy as np

rng = np.random.default_rng(20414)
k = 2.0 / 3.0
mu = 2.329340332171064  # placeholder overwritten below
from math import gamma as Gamma
mu = Gamma(1 + 1 / k)          # Gamma(2.5)
var = Gamma(1 + 2 / k) - mu ** 2  # Gamma(4)-mu^2
sd = var ** 0.5
lam = sd ** k
m = 2.0
import math
alpha = (math.log(m) / lam) ** (1 / k)
sigma = alpha ** (1 - k) / (lam * k)
print(f"mu={mu:.5f} sd={sd:.5f} lambda={lam:.5f} alpha={alpha:.5f} sigma={sigma:.5f}")

def one_run(nmax):
    pos = np.zeros(1)
    maxjump = -np.inf
    Mn = np.zeros(nmax + 1); Mn[0] = 0.0
    Nn = np.zeros(nmax + 1); Nn[0] = -np.inf
    for n in range(1, nmax + 1):
        E = rng.exponential(size=2 * len(pos))
        Z = E ** (1.0 / k)
        X = (Z - mu) / sd
        maxjump = max(maxjump, float(X.max()))
        pos = np.repeat(pos, 2) + X
        Mn[n] = float(pos.max()); Nn[n] = maxjump
    return Mn, Nn

def probeA(nmax=12, R=1500):
    ratios_M, ratios_N, gaps = [], [], []
    for _ in range(R):
        Mn, Nn = one_run(nmax)
        rM, rN, g = [], [], []
        for n in range(4, nmax + 1):
            den = math.sqrt(n * math.log(n))
            rM.append((Mn[n] - alpha * n ** 1.5) / den)
            rN.append((Nn[n] - alpha * n ** 1.5) / den)
            g.append((Mn[n] - Nn[n]) / den)
        ratios_M.append(rM); ratios_N.append(rN); gaps.append(g)
    return np.array(ratios_M), np.array(ratios_N), np.array(gaps)

def probeB(ns=(6, 8, 10, 12), K=1.0, R=1500):
    out = {}
    for n in ns:
        t = alpha * n ** 1.5 - K * math.sqrt(n * math.log(n))
        counts = np.zeros(R)
        for r in range(R):
            pos = np.zeros(1)
            for _ in range(n):
                E = rng.exponential(size=2 * len(pos))
                X = (E ** (1.0 / k) - mu) / sd
                pos = np.repeat(pos, 2) + X
            counts[r] = np.sum(pos > t)
        EZ, EZ2, P = float(counts.mean()), float((counts ** 2).mean()), float(np.mean(counts > 0))
        out[n] = {"t": t, "E[Z]": EZ, "E[Z^2]": EZ2, "P[max>t]": P,
                  "PZ_ratio": (EZ ** 2 / EZ2) if EZ2 > 0 else 0.0}
    return out

A_M, A_N, G = probeA()
ns = list(range(4, 13))
res = {"params": {"m": m, "r": k, "lambda": lam, "alpha": alpha, "sigma": sigma},
       "probeA": {"n": ns,
                  "mean_ratio_M": [float(v) for v in A_M.mean(0)],
                  "p10_ratio_M": [float(v) for v in np.quantile(A_M, 0.10, axis=0)],
                  "mean_ratio_N": [float(v) for v in A_N.mean(0)],
                  "p10_ratio_N": [float(v) for v in np.quantile(A_N, 0.10, axis=0)],
                  "mean_gap": [float(v) for v in G.mean(0)]},
       "probeB_K1": probeB(K=1.0),
       "probeB_K2": probeB(K=2.0)}
with open("output/artifacts/probe_r23.json", "w") as f:
    json.dump(res, f, indent=1)
print(json.dumps(res, indent=1))
