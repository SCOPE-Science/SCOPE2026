#!/usr/bin/env python3
"""Simulation benchmark: n=m=500 balls-in-bins, 20000 trials, seed 1 (numpy only + stdlib).

Generates 20000 x 500 uniform draws via numpy.random.default_rng(1), computes per-trial
max load by bincount, writes sim_summary.csv, prints histogram and Clopper-Pearson 95% CIs
(computed by pure-Python regularized incomplete beta + binary search, no scipy).
Deterministic; runtime < 1 min.
"""
import csv
import math
import numpy as np

SEED = 1
NTRIALS = 20000
NBALLS = 500
NBINS = 500
BATCH = 2000
OUT_CSV = str(__import__("pathlib").Path(__file__).with_name("sim_summary.csv"))

# --- Clopper-Pearson via pure-Python incomplete beta ---
def _betacf(a, b, x):
    MAXIT = 10000
    EPS = 3e-14
    FPMIN = 1e-300
    qab = a + b
    qap = a + 1.0
    qam = a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < FPMIN:
        d = FPMIN
    d = 1.0 / d
    h = d
    for m in range(1, MAXIT + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < FPMIN:
            d = FPMIN
        c = 1.0 + aa / c
        if abs(c) < FPMIN:
            c = FPMIN
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < FPMIN:
            d = FPMIN
        c = 1.0 + aa / c
        if abs(c) < FPMIN:
            c = FPMIN
        d = 1.0 / d
        dell = d * c
        h *= dell
        if abs(dell - 1.0) < EPS:
            break
    return h

def _betai(a, b, x):
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    if x < (a + 1) / (a + b + 2):
        bt = math.exp(math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
                      + a * math.log(x) + b * math.log(1 - x))
        return bt * _betacf(a, b, x) / a
    bt = math.exp(math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
                  + a * math.log(x) + b * math.log(1 - x))
    return 1.0 - bt * _betacf(b, a, 1 - x) / b

def _beta_q(q, a, b):
    lo, hi = 0.0, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if _betai(a, b, mid) < q:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

def clopper_pearson(x, n, alpha=0.05):
    lo = 0.0 if x == 0 else _beta_q(alpha / 2, x, n - x + 1)
    hi = 1.0 if x == n else _beta_q(1 - alpha / 2, x + 1, n - x)
    return lo, hi

def main():
    rng = np.random.default_rng(SEED)
    counts = {}
    n_le5 = 0
    n_in47 = 0
    maxs = np.empty(NTRIALS, dtype=np.int64)
    for s in range(0, NTRIALS, BATCH):
        b = min(BATCH, NTRIALS - s)
        X = rng.integers(0, NBINS, size=(b, NBALLS))
        for i in range(b):
            m = int(np.bincount(X[i], minlength=NBINS).max())
            maxs[s + i] = m
            counts[m] = counts.get(m, 0) + 1
            if m <= 5:
                n_le5 += 1
            if 4 <= m <= 7:
                n_in47 += 1
    print(f"seed={SEED} trials={NTRIALS} balls={NBALLS} bins={NBINS}")
    print("counts:", dict(sorted(counts.items())))
    for k in sorted(counts):
        x = counts[k]
        lo, hi = clopper_pearson(x, NTRIALS)
        print(f"M={k}: x={x} freq={x/NTRIALS:.6f} CP95=[{lo:.6f},{hi:.6f}]")
    lo, hi = clopper_pearson(n_le5, NTRIALS)
    print(f"P(M<=5): {n_le5}/{NTRIALS}={n_le5/NTRIALS:.6f} CP95=[{lo:.6f},{hi:.6f}]")
    lo, hi = clopper_pearson(n_in47, NTRIALS)
    print(f"P(4<=M<=7): {n_in47}/{NTRIALS}={n_in47/NTRIALS:.6f} CP95=[{lo:.6f},{hi:.6f}]")
    with open(OUT_CSV, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["max_load", "count", "freq", "cp95_lo", "cp95_hi"])
        for k in sorted(counts):
            x = counts[k]
            lo, hi = clopper_pearson(x, NTRIALS)
            w.writerow([k, x, f"{x/NTRIALS:.6f}", f"{lo:.6f}", f"{hi:.6f}"])
        w.writerow([])
        w.writerow(["event", "x", "n", "freq", "cp95_lo", "cp95_hi"])
        for name, x in [("M<=5", n_le5), ("4<=M<=7", n_in47)]:
            lo, hi = clopper_pearson(x, NTRIALS)
            w.writerow([name, x, NTRIALS, f"{x/NTRIALS:.6f}", f"{lo:.6f}", f"{hi:.6f}"])
    print("wrote", OUT_CSV)

if __name__ == "__main__":
    main()
