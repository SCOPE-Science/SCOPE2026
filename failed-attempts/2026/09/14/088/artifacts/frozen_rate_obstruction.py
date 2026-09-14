"""Frozen-rate obstruction check for 4D cubic energy-critical NLS type-II ansatz.

Target ansatz (tau = T - t):
    u = e^{i gamma(t)} B + eta,  B(x) = lam W(lam x),
    W(r) = (1 + r^2/8)^{-1}, lam = tau^{-p}, p = 1/2 + nu, gamma = al0 log tau.

This script verifies, with reproducible numerics:
 1. W solves ΔW + W^3 = 0 (radial, 4D) to machine precision.
 2. Sizes c1 = ||∇W||, c2 = ||∇ΛW|| (Hdot1 constants in the residual bound).
 3. Truncated L2 Gram matrix G(R) of {W, ΛW} on {|y|<R}:
       G(R) = [[A, B],[B, C]], A=<W,W>_R, B=<W,ΛW>_R, C=<ΛW,ΛW>_R,
    showing the threshold-resonant log structure:
       A ~ +c logR, B ~ -c logR, C ~ +c logR  (rank-1 leading log),
    so det G(R) grows only like logR and cond(G) ~ logR -> infinity.
 4. Exact rescaled modulation speeds a(s)=lam_s/lam, k(s)=gamma_s and the
    1/s non-integrable resonant forcing, plus a normalized secular-growth
    model over a concrete tau window for sample (al0, nu).
 5. Physical-variable residual blow-up rates ||R||_{Hdot1} ~ tau^{-1},
    ||R||_{Hdot2} ~ tau^{-1} lam.

Outputs JSON results to frozen_rate_obstruction_results.json (same directory).
"""
import json
import math
import os

import numpy as np

S3 = 2.0 * math.pi ** 2  # |S^3|

def W(r):
    return 1.0 / (1.0 + r ** 2 / 8.0)

def Wp(r):
    w = W(r)
    return -(r / 4.0) * w ** 2

def Wpp(r):
    w = W(r)
    return -(1.0 / 4.0) * w ** 2 + (r ** 2 / 8.0) * w ** 3

def LamW(r):
    return (1.0 - r ** 2 / 8.0) * W(r) ** 2

def LamWp(r):
    # d/dr [(1 - r^2/8) W^2] = -(r/4) W^2 + (1 - r^2/8) 2 W W'
    w = W(r)
    return -(r / 4.0) * w ** 2 + (1.0 - r ** 2 / 8.0) * 2.0 * w * Wp(r)

def radial_density(f_vals, r):
    return S3 * (f_vals ** 2) * r ** 3

def trapz_log(f, r):
    return float(np.trapz(f, r))

# ---- 1. PDE residual of W -----------------------------------------------
r_check = np.concatenate(([0.0], np.logspace(-8, 8, 200000)))
r_pos = r_check[1:]
lap = Wpp(r_pos) + 3.0 * Wp(r_pos) / r_pos
# limit at r=0: ΔW(0) = 4 W''(0) = 4*(-1/4) = -1
lap0 = 4.0 * (-(1.0 / 4.0) * W(0.0) ** 2)
resid = np.abs(np.concatenate(([lap0 + W(0.0) ** 3], lap + W(r_pos) ** 3)))
pde_max_resid = float(resid.max())

# ---- 2. Hdot1 constants --------------------------------------------------
r = np.concatenate(([0.0], np.logspace(-10, 10, 400000)))
rp = r[1:]
c1sq = trapz_log(radial_density(np.abs(np.concatenate(([Wp(0.0)], Wp(rp)))), r), r)
c2sq = trapz_log(radial_density(np.abs(np.concatenate(([LamWp(0.0)], LamWp(rp)))), r), r)
c1 = math.sqrt(c1sq)
c2 = math.sqrt(c2sq)

# ---- 3. Truncated Gram matrix --------------------------------------------
def truncated(R):
    rr = np.concatenate(([0.0], np.logspace(-10, math.log10(R), 200000)))
    q = rr[1:]
    wv = np.concatenate(([W(0.0)], W(q)))
    lv = np.concatenate(([LamW(0.0)], LamW(q)))
    A = trapz_log(S3 * wv * wv * rr ** 3, rr)
    B = trapz_log(S3 * wv * lv * rr ** 3, rr)
    Cc = trapz_log(S3 * lv * lv * rr ** 3, rr)
    return A, B, Cc

Rs = [1e1, 1e2, 1e3, 1e4, 1e5, 1e6]
gram = []
logR = np.log(Rs)
for R in Rs:
    A, B, Cc = truncated(R)
    M = np.array([[A, B], [B, Cc]])
    ev = np.linalg.eigvalsh(M)
    det = A * Cc - B * B
    cond = ev[1] / ev[0] if ev[0] > 0 else float("inf")
    gram.append({"R": R, "A": A, "B": B, "C": Cc, "det": det,
                 "eig_min": float(ev[0]), "eig_max": float(ev[1]),
                 "cond": float(cond), "det_over_logR": det / math.log(R)})

# log-slopes of A, -B, C from last two radii
def slope(key, sign=1.0):
    y1 = sign * gram[-2][key]
    y2 = sign * gram[-1][key]
    return (y2 - y1) / (logR[-1] - logR[-2])

c_theory = 128.0 * math.pi ** 2  # 64 |S^3| tail coefficient
slopes = {"A": slope("A"), "minusB": slope("B", -1.0), "C": slope("C")}

# ---- 4. Rescaled modulation speeds + secular model ------------------------
def secular(al0, nu, tau0=1e-3, tau1=1e-9):
    p = 0.5 + nu
    # exact: s(tau) = tau^{-2nu}/(2nu); a = p tau^{2nu} = p/(2nu s); k = -al0/(2nu s)
    coef_a = p / (2.0 * nu)
    coef_k = -al0 / (2.0 * nu)
    growth = 2.0 * nu * math.log(tau0 / tau1)  # log(s1/s0)
    return {"al0": al0, "nu": nu, "p": p, "coef_a": coef_a, "coef_k": coef_k,
            "log_s_ratio": growth,
            "Dz_scaling": coef_a * growth,   # normalized resonant response, scaling mode
            "Dz_phase": coef_k * growth}     # normalized resonant response, phase mode

samples = [secular(1.0, 2.0), secular(0.0, 1.5), secular(-2.5, 3.0), secular(1.0, 1.1)]

# ---- 5. Physical residual sample values -----------------------------------
def residual_sizes(al0, nu, tau):
    p = 0.5 + nu
    lam = tau ** (-p)
    h1 = (abs(al0) * c1 + p * c2) / tau
    # Hdot2 seminorm constants
    rr = np.concatenate(([0.0], np.logspace(-10, 10, 400000)))
    q = rr[1:]
    dW = np.concatenate(([(lap0)], lap if False else np.concatenate(([lap0], Wpp(q) + 3.0 * Wp(q) / q))))
    # ΔW = -W^3 exactly; use it directly for a clean constant
    wv = np.concatenate(([W(0.0)], W(q)))
    dW = -(wv ** 3)
    dLam = None
    # ΔΛW via L+: L+(ΛW)=0 => -ΔΛW - 3W^2 ΛW = 0 => ΔΛW = -3 W^2 ΛW
    lv = np.concatenate(([LamW(0.0)], LamW(q)))
    dLam = -3.0 * (wv ** 2) * lv
    k1 = math.sqrt(trapz_log(S3 * dW * dW * rr ** 3, rr))
    k2 = math.sqrt(trapz_log(S3 * dLam * dLam * rr ** 3, rr))
    h2 = (abs(al0) * k1 + p * k2) * lam / tau
    return {"tau": tau, "lam": lam, "Hdot1": h1, "Hdot2": h2,
            "k1": k1, "k2": k2}

res_samples = [residual_sizes(1.0, 2.0, 1e-3), residual_sizes(1.0, 2.0, 1e-6),
               residual_sizes(0.0, 1.5, 1e-6)]

results = {
    "pde_max_resid_W": pde_max_resid,
    "Hdot1_W": c1,
    "Hdot1_LamW": c2,
    "tail_coeff_theory": c_theory,
    "log_slopes": slopes,
    "gram": gram,
    "secular_model": samples,
    "residual_samples": res_samples,
}
out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "frozen_rate_obstruction_results.json")
with open(out, "w") as f:
    json.dump(results, f, indent=2)

print("PDE max resid |ΔW+W^3| =", pde_max_resid)
print("||∇W|| =", c1, " ||∇ΛW|| =", c2)
print("tail coeff theory =", c_theory, " slopes =", slopes)
for g in gram:
    print("R=%.0e A=%.4f B=%.4f C=%.4f det=%.4f det/logR=%.4f cond=%.3f"
          % (g["R"], g["A"], g["B"], g["C"], g["det"], g["det_over_logR"], g["cond"]))
for s in samples:
    print("al0=%s nu=%s Dz_scaling=%.3f Dz_phase=%.3f" % (s["al0"], s["nu"], s["Dz_scaling"], s["Dz_phase"]))
for q in res_samples:
    print("tau=%.0e lam=%.2e ||R||_H1=%.2e ||R||_H2=%.2e" % (q["tau"], q["lam"], q["Hdot1"], q["Hdot2"]))
print("wrote", out)
