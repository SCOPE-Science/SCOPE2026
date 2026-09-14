"""Multi-K heuristic trend + slope-rule/bijection check for the target law.

Part A: bump rho, K in {1e4,1e6,1e9,1e12,1e15}; F_heur(E)=min_s[(1-s)lnK - s lnlnK
  + s lng + ln M_s(E)]; empirical crossing level of rho(E) at F=0 zeros;
  track g*level vs K (naive annealed theory predicts -> 1/e ~= 0.368).
Part B: double-bump rho (4 crossings of level 1/(4g)) at large K: count F zeros,
  |M_k-E_k|, slope-rule agreement.
Writes JSON to argv[1].
"""
import json
import sys

import numpy as np


def make_grid(N=60001):
    return np.linspace(-1.0, 1.0, N)


def bump_rho(xs):
    y = np.zeros_like(xs)
    m = np.abs(xs) < 1.0
    xx = xs[m]
    y[m] = np.exp(-1.0 / (1.0 - xx ** 2))
    return y / np.trapz(y, xs)


def double_bump_rho(xs):
    # two bumps -> level crossings: up/down/up/down pattern (up to 4)
    y = np.exp(-40.0 * (xs - 0.45) ** 2) + 0.8 * np.exp(-40.0 * (xs + 0.45) ** 2)
    y = y * (np.abs(xs) < 0.999)
    return y / np.trapz(y, xs)


def Ms_table(Es, ss, grid, rho, delta=1e-3):
    """M_s(E) with analytic core; returns (M, rhoE)."""
    M = np.zeros((len(Es), len(ss)))
    rhoE = np.array([float(np.interp(E, grid, rho)) for E in Es])
    d = np.abs(grid)[None, :]  # placeholder, recomputed per E below
    for i, E in enumerate(Es):
        dist = np.abs(grid - E)
        mask = dist > delta
        g = grid[mask]
        base = rho[mask]
        dd = dist[mask]
        for j, s in enumerate(ss):
            outer = np.trapz(base / (dd ** s), g)
            core = rhoE[i] * 2.0 * (delta ** (1.0 - s)) / (1.0 - s)
            M[i, j] = outer + core
    return M, rhoE


def F_field(M, ss, K, g):
    L = float(np.log(K))
    ll = float(np.log(L))
    u = 1.0 - ss
    return (u[None, :] * L - (1.0 - u[None, :]) * ll
            + (1.0 - u[None, :]) * np.log(g) + np.log(M))


def crossing_levels(Es, Fmin, rhoE):
    lv = []
    for i in range(len(Es) - 1):
        if Fmin[i] == 0:
            lv.append(float(rhoE[i]))
        elif Fmin[i] * Fmin[i + 1] < 0:
            w = abs(Fmin[i]) / (abs(Fmin[i]) + abs(Fmin[i + 1]))
            lv.append(float((1 - w) * rhoE[i] + w * rhoE[i + 1]))
    return lv


def zero_positions(Es, Fmin):
    z = []
    for i in range(len(Es) - 1):
        if Fmin[i] * Fmin[i + 1] < 0:
            w = abs(Fmin[i]) / (abs(Fmin[i]) + abs(Fmin[i + 1]))
            z.append(float((1 - w) * Es[i] + w * Es[i + 1]))
    return z


def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else None
    g = 0.5
    grid = make_grid()
    rho = bump_rho(grid)
    Es = np.linspace(-0.9, 0.9, 31)

    partA = []
    for K in [1e4, 1e6, 1e9, 1e12, 1e15]:
        L = float(np.log(K))
        u = np.exp(np.linspace(np.log(0.15 / L), np.log(min(0.9, 7.0 / L)), 60))
        ss = 1.0 - u
        M, rhoE = Ms_table(Es, ss, grid, rho)
        F = F_field(M, ss, K, g)
        Fmin = F.min(axis=1)
        iu = F.argmin(axis=1)
        lv = crossing_levels(Es, Fmin, rhoE)
        med = float(np.median(lv)) if lv else float("nan")
        partA.append({
            "K": K, "lnK": L,
            "empirical_levels": lv,
            "median_level": med,
            "g_times_median": g * med if lv else None,
            "ustar_at_center": float(u[iu[len(Es) // 2]]),
            "one_over_lnK": 1.0 / L,
            "slope_agree": float(np.mean((Fmin > 0) == (rhoE > med))) if lv else None,
        })

    # Part B: double bump, largest K
    rho2 = double_bump_rho(grid)
    K = 1e12
    L = float(np.log(K))
    u = np.exp(np.linspace(np.log(0.15 / L), np.log(min(0.9, 7.0 / L)), 60))
    ss = 1.0 - u
    EsB = np.linspace(-0.95, 0.95, 121)
    M, rhoE = Ms_table(EsB, ss, grid, rho2)
    F = F_field(M, ss, K, g)
    Fmin = F.min(axis=1)
    level = 1.0 / (4 * g)
    # true crossings of rho2(E)=level
    trueE = []
    for i in range(len(EsB) - 1):
        d0 = rhoE[i] - level
        d1 = rhoE[i + 1] - level
        if d0 * d1 < 0:
            w = abs(d0) / (abs(d0) + abs(d1))
            trueE.append(float((1 - w) * EsB[i] + w * EsB[i + 1]))
    Mpos = zero_positions(EsB, Fmin)
    med = float(np.median(crossing_levels(EsB, Fmin, rhoE))) if Mpos else float("nan")
    partB = {
        "K": K, "g": g, "level_1_over_4g": level,
        "true_crossings_E": trueE,
        "F_zero_positions_M": Mpos,
        "n_true": len(trueE), "n_Fzeros": len(Mpos),
        "empirical_median_level": med,
        "slope_agree": float(np.mean((Fmin > 0) == (rhoE > med))) if Mpos else None,
    }

    out = {"g": g, "partA_bump_trend": partA, "partB_doublebump": partB,
           "note": "naive annealed predicts g*level -> 1/e = 0.3679; target claims 1/4 = 0.25"}
    print(json.dumps(out, indent=2))
    if out_path:
        with open(out_path, "w") as f:
            json.dump(out, f, indent=2)


if __name__ == "__main__":
    main()
