"""Quenched cavity population dynamics: locate empirical FM threshold.

rho(x) = (15/16)(1-x^2)^2 on (-1,1) (C^1, satisfies target hypotheses shape).
g = 1, t = g/(K lnK). Target threshold: rho(E) = 1/(4g) = 0.25 <-> E = +-0.696.
Bare two-sided prediction: rho = 1/(2eg) = 0.184 <-> E = +-0.745.
Bare one-sided prediction: rho = 1/(eg) = 0.368 <-> E = +-0.60.

For each (K, E): iterate cavity pool G <- 1/(V - E - i eta - t^2 sum_{K} G),
compute m_s = mean|G|^s, F(s) = lnK + s ln t + ln m_s, report min_s F(s).
Direction: F_min < 0 rigorously implies localization (one-step FM bound);
F_min > 0 is consistent-with (not proof of) delocalization.

Writes JSON to argv[1].
"""
import json
import sys

import numpy as np

rng = np.random.default_rng(20113)


def rho_fn(x):
    return (15.0 / 16.0) * (1.0 - x ** 2) ** 2 * (np.abs(x) < 1.0)


def sample_V(n):
    # inverse-CDF via table: CDF(x) = (15/16)(x - 2x^3/3 + x^5/5 + 8/15)
    grid = np.linspace(-1.0, 1.0, 20001)
    cdf = (15.0 / 16.0) * (grid - 2 * grid ** 3 / 3 + grid ** 5 / 5 + 8.0 / 15.0)
    cdf /= cdf[-1]
    u = rng.random(n)
    return np.interp(u, cdf, grid)


def run_KE(K, E, g=1.0, N=2500, iters=8, eta=1e-9, s_grid=None):
    if s_grid is None:
        s_grid = np.linspace(0.5, 0.97, 24)
    t = g / (K * np.log(K))
    lnt = np.log(t)
    G = 1.0 / (sample_V(N) - E - 1j * eta)  # init: bare law
    for _ in range(iters):
        S = G[rng.integers(0, N, size=(N, K))].sum(axis=1)
        G = 1.0 / (sample_V(N) - E - 1j * eta - t ** 2 * S)
    absG = np.abs(G)
    Fs = []
    for s in s_grid:
        ms = float(np.mean(absG ** s))
        Fs.append(float(np.log(K) + s * lnt + np.log(ms)))
    Fs = np.array(Fs)
    j = int(np.argmin(Fs))
    return {
        "F_min": float(Fs[j]),
        "s_star": float(s_grid[j]),
        "F_at_s_grid": [float(v) for v in Fs],
        "mean_absG": float(np.mean(absG)),
        "median_ImG": float(np.median(G.imag)),
    }


def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else None
    g = 1.0
    Ks = [64, 128, 256, 512]
    Es = [0.0, 0.2, 0.4, 0.55, 0.696, 0.75, 0.8, 0.9]
    s_grid = np.linspace(0.5, 0.97, 24)
    rows = []
    for K in Ks:
        for E in Es:
            r = run_KE(K, E, g=g, s_grid=s_grid)
            rE = float(rho_fn(E))
            r.update({
                "K": K, "E": E, "g": g,
                "rhoE": rE,
                "ln_4g_rho": float(np.log(4 * g * rE)) if rE > 0 else None,
                "ln_2eg_rho": float(np.log(2 * np.e * g * rE)) if rE > 0 else None,
                "one_over_lnK": 1.0 / np.log(K),
            })
            rows.append(r)
            print(f"K={K} E={E:.3f} rho={rE:.4f} Fmin={r['F_min']:+.3f} "
                  f"(s*={r['s_star']:.2f}) ln4grho={r['ln_4g_rho']:+.3f} "
                  f"ln2egrho={r['ln_2eg_rho']:+.3f}", flush=True)
    out = {"rows": rows, "note": ("F_min<0 => localized (rigorous direction); "
                                  "compare empirical zero vs ln(4g rho) [target] "
                                  "vs ln(2eg rho) [bare two-sided]")}
    print(json.dumps({"summary": [(r["K"], r["E"], round(r["F_min"], 3)) for r in rows]}))
    if out_path:
        with open(out_path, "w") as f:
            json.dump(out, f, indent=2)


if __name__ == "__main__":
    main()
