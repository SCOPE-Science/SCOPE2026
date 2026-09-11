"""Lane-1020 target ledger: Chapman-Enskog quasimode viability at k=e1.

Normalization (explicit, standard math-PDE):
  M(v) = (2pi)^-3/2 exp(-|v|^2/2) (unit density, unit temperature),
  linearization f = M(1+h), inner product <f,g> = int f gbar M dv dx/(2pi)^3,
  cutoff hard-sphere kernel B(|u|,cos) = |u| with Grad cutoff b = 1
  (angular integral 4pi folded in; effective diameter d_eff = 2).
Fiber generator at k = e1: G_k = L - i*v1 on L^2(M dv).

Contents:
  A. Exact Gaussian Euler block: acoustic vectors, micro-flux norms
     (exact integer-moment arithmetic -- no quadrature error).
  B. Exact collision-frequency identities: nu(0), nu-bar (closed form),
     Gauss-Hermite spot checks.
  C. First-Sonine hard-sphere transport coefficients + Navier-Stokes
     branch locations at |k|=1 + distance to window [-0.03,-0.01].
  D. Relaxation-model cross-check (flux^2/nu-bar) vs true Sonine values.
  E. Residual-floor estimate + recovery tests (widened budget / window).
Writes output/artifacts/quasimode_ledger.json
"""
import json
import numpy as np
from numpy.polynomial.hermite import hermgauss

OUT = "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1020/output/artifacts/quasimode_ledger.json"

# ---------- A. Euler block (exact moments) ----------
s = np.sqrt(2.0 / 3.0)
c = np.sqrt(5.0 / 3.0)
n0 = np.sqrt(10.0 / 3.0)
a, b, e_coeff = 1.0 / n0, c / n0, (s / n0) / np.sqrt(6.0)
# phi0 = a + b*v1 + e_coeff*(|v|^2-3); N^2 = a^2+3b^2+14e^2+4ae (derived in worklog)
N2 = a * a + 3 * b * b + 14 * e_coeff * e_coeff + 4 * a * e_coeff
hyd = b * b + (a + 2 * e_coeff) ** 2 + (2.0 / 3.0) * b * b
flux2_ac = N2 - hyd
# optimal-lambda pure-hydro residual needs m1 = E[phi0^2 v1]
# phi0^2 v1: odd terms survive: 2ab v1^2 + 2be v1^2(S-3) + (a^2+.. odd vanish)
# E = 2ab*1 + 2be*2 = 2ab + 4be
m1 = 2 * a * b + 4 * b * e_coeff
lam_opt_imag = -m1  # <phi0,G phi0> = -i*m1
pure_hydro_best_res2 = N2 - m1 * m1  # min_lam ||G phi0 - lam phi0||^2

# shear pure packet phi0 = v2: ||P^perp v1 v2||^2 = E[v1^2 v2^2] = 1
flux2_shear = 1.0
shear_pure_res_at_window_edge = np.sqrt(0.03 ** 2 + 1.0)

# ---------- B. collision frequency ----------
nu_0_exact = 4.0 * np.sqrt(8.0 * np.pi)      # 4pi * E|w|
nu_bar_exact = 16.0 * np.sqrt(np.pi)          # 4pi * 4/sqrt(pi)


def E_maxw(f, n=30):
    x, w = hermgauss(n)
    X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
    W = (w[:, None, None] * w[None, :, None] * w[None, None, :]) / (np.pi ** 1.5)
    return float(np.sum(W * f(np.sqrt(2) * X, np.sqrt(2) * Y, np.sqrt(2) * Z)))


def nu_of_v(v, n=30):
    f = lambda X, Y, Z: 4.0 * np.pi * np.sqrt((X - v) ** 2 + Y ** 2 + Z ** 2)
    return E_maxw(f, n)


nu0_num = nu_of_v(0.0)
nu1_num = nu_of_v(1.0)
nu2_num = nu_of_v(2.0)

# ---------- C. transport coefficients / branches ----------
mu1 = 5.0 / (64.0 * np.sqrt(np.pi))   # first-Sonine HS viscosity, d_eff = 2
Gamma_ac = 7.0 / 6.0 * mu1            # Stokes-Kirchhoff temporal damping
shear_branch = -mu1                   # transverse NS damping at |k|=1
acoustic_branch_re = -Gamma_ac
entropy_branch = -mu1 / (2.0 / 3.0)   # -kappa/(rho cp), Pr = 2/3
d_shear = abs(shear_branch - (-0.03))
d_ac = abs(acoustic_branch_re - (-0.03))
d_entr = abs(entropy_branch - (-0.03))

# Grad transverse 2x2 check: lam^2 + nu_s lam + k^2 = 0
nu_sig = 1.0 / mu1
k = 1.0
disc = nu_sig ** 2 - 4 * k * k
lam_slow = (-nu_sig + np.sqrt(disc)) / 2.0
lam_fast = (-nu_sig - np.sqrt(disc)) / 2.0

# ---------- D. relaxation-model cross-check ----------
Gamma_ac_model = flux2_ac / nu_bar_exact
mu_model = 1.0 / nu_bar_exact

# ---------- E. floor + recovery ----------
tau = 1.0 / nu_sig
trunc_ac = tau * Gamma_ac       # O(Kn)*first-order scale
trunc_shear = tau * mu1
floor_shear = d_shear + trunc_shear
floor_ac = d_ac + trunc_ac
rec_budget = 0.02
rec_window = [-0.06, -0.03]
strength_mult_shear = mu1 / 0.03
strength_mult_ac = Gamma_ac / 0.03

ledger = {
    "normalization": "M unit Maxwellian; B(|u|,cos)=|u|, Grad cutoff b=1 (4pi); T^3=(R/2piZ)^3; k=e1",
    "A_euler_exact": {
        "sound_speed": float(c),
        "acoustic_coeffs_(a,b,e)": [float(a), float(b), float(e_coeff)],
        "N2_v1phi0": float(N2),
        "hydro_proj_norm2": float(hyd),
        "micro_flux2_acoustic": float(flux2_ac),
        "micro_flux_acoustic": float(np.sqrt(flux2_ac)),
        "pure_hydro_best_residual": float(np.sqrt(pure_hydro_best_res2)),
        "pure_hydro_best_Im_lambda": float(lam_opt_imag),
        "micro_flux2_shear": float(flux2_shear),
        "pure_shear_residual_at_Re_-0.03": float(shear_pure_res_at_window_edge),
    },
    "B_collision_frequency": {
        "nu0_exact_4sqrt(8pi)": float(nu_0_exact),
        "nu0_GH30": float(nu0_num),
        "nu1_GH30": float(nu1_num),
        "nu2_GH30": float(nu2_num),
        "nu_bar_exact_16sqrt(pi)": float(nu_bar_exact),
        "mu_model_p_over_nubar": float(mu_model),
    },
    "C_first_sonine_branches_k1": {
        "mu1_5/(64sqrt(pi))": float(mu1),
        "shear_branch_-mu": float(shear_branch),
        "acoustic_branch_-7mu/6": float(acoustic_branch_re),
        "entropy_branch_-mu/Pr": float(entropy_branch),
        "dist_shear_to_window_top": float(d_shear),
        "dist_acoustic_to_window_top": float(d_ac),
        "dist_entropy_to_window_top": float(d_entr),
        "grad_transverse_slow": float(lam_slow),
        "grad_transverse_fast": float(lam_fast),
        "residual_budget": 0.01,
    },
    "D_model_crosscheck": {
        "Gamma_ac_model_flux2/nubar": float(Gamma_ac_model),
        "model_vs_true_acoustic_ratio": float(Gamma_ac_model / Gamma_ac),
        "model_vs_true_shear_ratio": float(mu_model / mu1),
    },
    "E_floor_and_recovery": {
        "Kn_proxy_tau": float(tau),
        "trunc_estimate_acoustic": float(trunc_ac),
        "trunc_estimate_shear": float(trunc_shear),
        "predicted_best_residual_in_window_shear": float(floor_shear),
        "predicted_best_residual_in_window_acoustic": float(floor_ac),
        "recovery_budget_0.02_shear_total": float(floor_shear),
        "recovery_budget_0.02_pass": bool(floor_shear <= rec_budget),
        "recovery_window_widened": rec_window,
        "recovery_window_pass_shear_trunc_only": bool(trunc_shear <= 0.01),
        "strength_multiplier_needed_shear": float(strength_mult_shear),
        "strength_multiplier_needed_acoustic": float(strength_mult_ac),
    },
}

with open(OUT, "w") as f:
    json.dump(ledger, f, indent=2)

print("sound speed c =", c)
print("acoustic micro-flux =", np.sqrt(flux2_ac))
print("pure-hydro best residual =", np.sqrt(pure_hydro_best_res2), " at Im lam =", lam_opt_imag)
print("nu(0) exact/num =", nu_0_exact, nu0_num, " nubar =", nu_bar_exact)
print("nu(1), nu(2) =", nu1_num, nu2_num)
print("mu1 =", mu1, " shear br =", shear_branch, " acoustic br =", acoustic_branch_re)
print("dist shear/ac/entr to window top:", d_shear, d_ac, d_entr)
print("Grad transverse slow/fast:", lam_slow, lam_fast)
print("model-vs-true ratios (ac, shear):", Gamma_ac_model / Gamma_ac, mu_model / mu1)
print("predicted floor in window: shear", floor_shear, " acoustic", floor_ac)
print("ledger written to", OUT)
