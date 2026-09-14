"""Heuristic check: F_heur(E) = min_s [(1-s)lnK - s lnlnK + s lng + ln M_s(E)],
M_s(E) = int rho(v)|v-E|^{-s} dv, rho = normalized bump on (-1,1).
Checks: (1) zero set of F_heur tracks a level set rho(E)=const/g;
(2) sign pattern matches slope rule (F>0 iff rho above threshold).
Writes JSON summary to stdout and to result file given by argv[1] (optional).
"""
import json
import sys

import numpy as np


def bump_rho(xs):
    y = np.zeros_like(xs)
    m = np.abs(xs) < 1.0
    xx = xs[m]
    y[m] = np.exp(-1.0 / (1.0 - xx ** 2))
    Z = np.trapz(y, xs)
    return y / Z


def moment_Ms(E, s, grid, rho, delta=1e-3):
    # Trapezoid outside (E-delta, E+delta) + analytic core rho(E)*2*delta^{1-s}/(1-s).
    mask = np.abs(grid - E) > delta
    g = grid[mask]
    integrand = rho[mask] / (np.abs(g - E) ** s)
    outer = np.trapz(integrand, g)
    # rho(E) by linear interpolation
    rhoE = float(np.interp(E, grid, rho))
    core = rhoE * 2.0 * (delta ** (1.0 - s)) / (1.0 - s)
    return outer + core, rhoE


def main():
    K = 1e6
    g = 0.5
    lnK = float(np.log(K))
    lnlnK = float(np.log(lnK))
    N = 40001
    grid = np.linspace(-1.0, 1.0, N)
    rho = bump_rho(grid)

    Es = np.linspace(-0.95, 0.95, 77)
    us = np.concatenate([
        np.array([0.005, 0.01, 0.02, 0.03, 0.05, 0.07, 0.1, 0.15, 0.2,
                  0.3, 0.45, 0.6, 0.8, 0.95]),
    ])
    ss = 1.0 - us
    F = np.zeros_like(Es)
    rhoE = np.zeros_like(Es)
    ustar = np.zeros_like(Es)
    for i, E in enumerate(Es):
        best = np.inf
        bu = np.nan
        rE = 0.0
        for u, s in zip(us, ss):
            Ms, rE = moment_Ms(E, s, grid, rho)
            val = u * lnK - (1 - u) * lnlnK + (1 - u) * np.log(g) + np.log(Ms)
            if val < best:
                best = val
                bu = u
        F[i] = best
        rhoE[i] = rE
        ustar[i] = bu

    # Empirical threshold: rho(E) at sign changes of F.
    crossings = []
    for i in range(len(Es) - 1):
        if F[i] == 0:
            crossings.append(float(rhoE[i]))
        elif F[i] * F[i + 1] < 0:
            w = abs(F[i]) / (abs(F[i]) + abs(F[i + 1]))
            crossings.append(float((1 - w) * rhoE[i] + w * rhoE[i + 1]))
    # Slope-rule check: sign(F) vs sign(rho - median crossing level)
    level = float(np.median(crossings)) if crossings else float("nan")
    agree = float(np.mean((F > 0) == (rhoE > level))) if crossings else float("nan")
    out = {
        "K": K,
        "g": g,
        "1/(4g)": 1.0 / (4 * g),
        "1/(e g)": 1.0 / (np.e * g),
        "empirical_crossing_levels": crossings,
        "median_level": level,
        "g_times_median_level": g * level if crossings else None,
        "slope_rule_agreement": agree,
        "min_F": float(F.min()),
        "max_F": float(F.max()),
        "ustar_at_center": float(ustar[len(Es) // 2]),
        "1/lnK": 1.0 / lnK,
    }
    print(json.dumps(out, indent=2))
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            json.dump(out, f, indent=2)


if __name__ == "__main__":
    main()
