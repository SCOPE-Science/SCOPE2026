"""Focused quenched threshold refinement with error bars.

rho(x)=(15/16)(1-x^2)^2, g=1. Target zero: rho=1/4 <-> E=0.696.
Bare two-sided zero: rho=1/(2e)=0.184 <-> E=0.745.
For K in {128,256}, E near threshold, 3 seeds, N=6000 pool, s up to 0.99:
report F_min mean+-sd across seeds. Also resonance diagnostic
P(|G| > K) per (K,E) as delocalization-side cross-check.
Writes JSON to argv[1].
"""
import json
import sys

import numpy as np

GRID = np.linspace(-1.0, 1.0, 20001)
CDF = (15.0 / 16.0) * (GRID - 2 * GRID ** 3 / 3 + GRID ** 5 / 5 + 8.0 / 15.0)
CDF /= CDF[-1]


def rho_fn(x):
    return (15.0 / 16.0) * (1.0 - x ** 2) ** 2 * (np.abs(x) < 1.0)


def run_KE(K, E, g, N, iters, seed, s_grid, eta=1e-9):
    rng = np.random.default_rng(seed)
    t = g / (K * np.log(K))
    G = 1.0 / (np.interp(rng.random(N), CDF, GRID) - E - 1j * eta)
    for _ in range(iters):
        S = G[rng.integers(0, N, size=(N, K))].sum(axis=1)
        G = 1.0 / (np.interp(rng.random(N), CDF, GRID) - E - 1j * eta - t ** 2 * S)
    a = np.abs(G)
    Fs = np.array([float(np.log(K) + s * np.log(t) + np.log(np.mean(a ** s)))
                   for s in s_grid])
    j = int(np.argmin(Fs))
    return float(Fs[j]), float(s_grid[j]), float(np.mean(a > K))


def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else None
    g = 1.0
    s_grid = np.array([0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.93, 0.95, 0.97, 0.985, 0.99])
    rows = []
    for K in [128, 256]:
        for E in [0.60, 0.65, 0.696, 0.72, 0.745, 0.78]:
            vals, sstars, res = [], [], []
            for seed in [11, 22, 33]:
                Fm, ss, rp = run_KE(K, E, g, N=6000, iters=10, seed=seed,
                                    s_grid=s_grid)
                vals.append(Fm)
                sstars.append(ss)
                res.append(rp)
            rE = float(rho_fn(E))
            row = {"K": K, "E": E, "rhoE": rE,
                   "F_min_mean": float(np.mean(vals)),
                   "F_min_sd": float(np.std(vals, ddof=1)),
                   "F_min_vals": vals,
                   "s_star": sstars,
                   "resprob_mean": float(np.mean(res)),
                   "ln_4g_rho": float(np.log(4 * g * rE)),
                   "ln_2eg_rho": float(np.log(2 * np.e * g * rE))}
            rows.append(row)
            print(f"K={K} E={E:.3f} rho={rE:.4f} Fmin={row['F_min_mean']:+.3f}+-{row['F_min_sd']:.3f} "
                  f"ln4g={row['ln_4g_rho']:+.3f} ln2eg={row['ln_2eg_rho']:+.3f} "
                  f"P(|G|>K)={row['resprob_mean']:.2e}", flush=True)
    # linear-interpolated empirical zero per K
    zeros = {}
    for K in [128, 256]:
        sub = sorted([r for r in rows if r["K"] == K], key=lambda r: r["E"])
        z = None
        for a, b in zip(sub, sub[1:]):
            if a["F_min_mean"] * b["F_min_mean"] < 0:
                w = abs(a["F_min_mean"]) / (abs(a["F_min_mean"]) + abs(b["F_min_mean"]))
                z = (1 - w) * a["E"] + w * b["E"]
        zeros[str(K)] = z
    out = {"rows": rows, "empirical_zero_E": zeros,
           "targets": {"E_target_1over4g": 0.696, "E_bare_1over2eg": 0.745}}
    print(json.dumps({"empirical_zero_E": zeros}, indent=2))
    if out_path:
        with open(out_path, "w") as f:
            json.dump(out, f, indent=2)


if __name__ == "__main__":
    main()
