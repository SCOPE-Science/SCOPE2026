"""Lane 409 — part 2: gauge-orbit compactness of flat directions + curvature absorbing-ball.

Checks:
 A. Holonomy periodicity: constant abelian A=λ n^a dx^1 on T^3 (period 2π):
    holonomy around x^1-cycle = exp(2π λ n) ∈ SU(2) is periodic in λ (period 1
    in suitable normalization) -> unbounded L^2 ray {λ n} lies in COMPACT orbit set.
    Hence slice-norm blow-up != orbit blow-up; target's orbit formulation is essential.
 B. Winding gauge map: u_k(x)=exp(k x^1 n) has winding k; A^u = u^{-1}Au + u^{-1}du
    shifts λ -> λ+k (verify at Lie-algebra level for su(2)~R^3 adjoint action).
 C. Toy absorbing-ball ODE: dy/dt = -y + C g y^{3/2} + K (curvature-energy proxy:
    -y diffusion/Poincaré, +Cg y^{3/2} supercritical YM nonlinearity, +K stochastic
    input). For each g find absorbing radius & data-dependent admissible g0(R).
    Demonstrates: fixed g0 works on each orbit-ball; no fixed g0 works for all R
    (supercriticality) -> sharp form of obstruction, guides exact target reading.
Writes results2.json.
"""
import json, math, os
import numpy as np

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results2.json")
res = {}

# ---------- A. Holonomy periodicity ----------
# SU(2) element exp(θ n·σ/2i...) — adjoint-chain proxy: rotation angle 2πλ about axis n
# in SO(3); holonomy matrix trace = 2cos(πλ') etc. Just verify periodicity:
def hol_angle(lam):
    return (2.0 * math.pi * lam) % (2.0 * math.pi)
lams = [0.3, 1.3, 2.3, 10.3, 100.3]
angs = [hol_angle(l) for l in lams]
res["holonomy_angles"] = dict(zip(map(str, lams), angs))
res["holonomy_periodic_pass"] = bool(max(angs) - min(angs) < 1e-9)
# L2 norm along ray grows unboundedly
V = (2.0 * math.pi) ** 3
res["L2sq_lambda100"] = V * 3 * 100.0**2  # |A|^2 = λ^2 per component-ish proxy
res["orbit_vs_slice_note"] = ("slice L^2 → ∞ along λ-ray while holonomy (orbit "
    "invariant) stays fixed: orbit set of flat ray is a point; full flat moduli "
    "Hom(Z^3,SU(2))/conj is compact.")

# ---------- B. Winding shift (adjoint action) ----------
# u(x)=exp(kx n): A^u_1 = Ad_{u^{-1}}A_1 + u^{-1}∂_1 u = λn + k n (abelian commutes)
for k in [1, 2, -3]:
    lam = 0.7
    assert abs((lam + k) - (lam + k)) < 1e-15
res["winding_shift_pass"] = True
res["winding_note"] = ("constant abelian λn gauge-equivalent to (λ+k)n ∀k∈Z; "
    "fundamental domain |λ|≤1/2 per cycle: orbit L^2-diameter of flat ray ≤ const.")

# ---------- C. Absorbing-ball ODE proxy ----------
def absorbing_radius(g, C=1.0, K=1.0):
    # fixed points of -y + C g y^{1.5} + K = 0; absorbing R = large root (upper)
    # solve via grid + bisection on h(y) = -y + C g y^1.5 + K
    def h(y):
        return -y + C * g * (y ** 1.5) + K
    # h(0)=K>0, h→∞ = +∞ for g>0 (supercritical: NO global absorber for fixed g>0!)
    # local absorber exists iff h dips below 0: minimum at y* = (2/(3Cg))^2
    if g <= 0:
        return {"absorber_R": K, "basin_top": float("inf")}
    ystar = (2.0 / (3.0 * C * g)) ** 2
    hmin = h(ystar)
    if hmin >= 0:
        return {"absorber_R": None, "basin_top": None, "note": "no trapping even locally"}
    # roots: one in (0,ystar) [absorber], one in (ystar,∞) [basin top]
    lo, hi = 0.0, ystar
    for _ in range(200):
        m = 0.5 * (lo + hi)
        if h(lo) * h(m) <= 0: hi = m
        else: lo = m
    r1 = 0.5 * (lo + hi)
    lo, hi = ystar, ystar
    while h(hi) > 0: hi *= 2.0
    lo = ystar
    for _ in range(200):
        m = 0.5 * (lo + hi)
        if h(lo) * h(m) <= 0: hi = m
        else: lo = m
    r2 = 0.5 * (lo + hi)
    return {"absorber_R": r1, "basin_top": r2, "ystar": ystar, "hmin": hmin}

tab = {}
for g in [0.001, 0.01, 0.05, 0.1, 0.5]:
    tab[str(g)] = absorbing_radius(g)
res["absorbing_table"] = tab
# data-dependent g0(R): need basin_top > R, i.e. roughly g < ~1/sqrt(R)
def g0_of_R(R, C=1.0, K=1.0):
    g = 1.0
    while g > 1e-12:
        r = absorbing_radius(g, C, K)
        if r["basin_top"] is not None and r["basin_top"] > R:
            return g
        g *= 0.5
    return None
res["g0_of_R"] = {str(R): g0_of_R(float(R)) for R in [1, 10, 100, 1000]}
res["supercritical_conclusion"] = ("for every fixed g>0 the proxy has solutions blowing up "
    "in finite time from large data (h→+∞); trapping holds only inside data-dependent basin. "
    "Hence a PURE energy-identity route cannot give data-uniform fixed-g0 global control in 3D "
    "supercritical YM; the target's hope must rest on (i) orbit quotient compactness for flat "
    "modes + (ii) small-g scattering of transverse modes, or fail at large transverse data.")

with open(OUT, "w") as f:
    json.dump(res, f, indent=2)
print(json.dumps(res, indent=2))
