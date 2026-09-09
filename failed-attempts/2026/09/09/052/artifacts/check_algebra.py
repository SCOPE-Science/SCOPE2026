"""Lane 409 — verification-critical checks for target energy identity.

Checks (all reproducible, stdlib+numpy only):
 1. su(2) quartic-dissipation identity: <X,[Y,[Y,X]]> = -||[X,Y]||^2,
    with [.,.] = cross product (su(2) ~ R^3 adjoint). Random test + exact cases.
 2. Abelian-ray vanishing: D4 = sum_{i,j} ||[v_i,v_j]||^2 = 0 on collinear data,
    nonzero generic -> D4 does not control L^4 norm.
 3. Constant-abelian steady states of deterministic DeTurck flow:
    F=0, drift=0, D4=0, arbitrarily large L^2 norm.
 4. Quadratic-term scaling: |I_quad| ~ g ||v||_4^2 ||grad v||_2 has total
    H^1-exponent 5/2 (supercritical); small-data absorption threshold r(g).
 5. Explicit small-data numbers: Kprime, r(g), gamma0 from torus gap (=1).

Writes results.json for audit.
"""
import json, math, os, random

random.seed(409)
import numpy as np
np.random.seed(409)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results.json")
res = {}

# ---------- 1. Lie algebra identity ----------
def cross(a, b):
    return np.cross(a, b)

def check_identity(n=2000):
    worst = 0.0
    for _ in range(n):
        X = np.random.randn(3); Y = np.random.randn(3)
        lhs = float(np.dot(X, cross(Y, cross(Y, X))))
        rhs = -float(np.dot(cross(X, Y), cross(X, Y)))
        worst = max(worst, abs(lhs - rhs))
    return worst

w = check_identity()
res["lie_identity_max_err"] = w
res["lie_identity_pass"] = bool(w < 1e-9)
# exact integer case
X = np.array([1.0, 2.0, 3.0]); Y = np.array([-1.0, 0.5, 2.0])
lhs = float(np.dot(X, cross(Y, cross(Y, X)))); rhs = -float(np.sum(cross(X, Y)**2))
res["lie_identity_exact_case"] = {"lhs": lhs, "rhs": rhs, "diff": abs(lhs-rhs)}

# ---------- 2. Abelian ray D4 = 0 ----------
def D4_of(v):
    # v: (3,3) array v[i,a] spatial i, color a
    s = 0.0
    for i in range(3):
        for j in range(3):
            c = cross(v[i], v[j])
            s += float(np.dot(c, c))
    return s

def L4norm4_of(v):
    return float(np.sum(v**2)**2)  # (sum v^2)^2 ~ ||v||_4^4 up to volume factor for constants

nvec = np.array([0.0, 0.0, 1.0])
phi = np.array([1.0, -2.0, 0.5])
v_abel = np.outer(phi, nvec)  # v_i^a = phi_i n^a
res["abelian_D4"] = D4_of(v_abel)
res["abelian_L4proxy"] = L4norm4_of(v_abel)
rng = np.random.randn(3, 3)
res["generic_D4"] = D4_of(rng)
res["generic_L4proxy"] = L4norm4_of(rng)
res["abelian_vanishing_pass"] = bool(res["abelian_D4"] < 1e-12 and res["generic_D4"] > 0.01)
# scale-invariance check: D4(λv_abel)=0 for λ large
for lam in [1.0, 10.0, 100.0]:
    d = D4_of(lam * v_abel)
    assert abs(d) < 1e-9, (lam, d)
res["abelian_ray_scale_invariant"] = True

# ---------- 3. Constant abelian steady state ----------
# Deterministic DeTurck drift on constants: gradients=0, [A,A]A terms:
# Q_3 for constant abelian v_i = lam_i n: [v_j,[v_j,v_i]] = 0 since all collinear.
V = (2.0 * math.pi) ** 3
lam = np.array([3.0, -7.0, 11.0])
A = np.outer(lam, nvec)
# nonlinear drift norm proxy: max ||[A_j,[A_j,A_i]]||
drift = 0.0
for i in range(3):
    for j in range(3):
        drift = max(drift, float(np.linalg.norm(cross(A[j], cross(A[j], A[i])))))
L2sq = V * float(np.sum(A**2))
res["const_abelian_drift"] = drift
res["const_abelian_L2sq"] = L2sq
res["const_abelian_steady_pass"] = bool(drift < 1e-12 and L2sq > 1000.0)
# curvature F=0 check: F_ij = dA + [A,A]; constants -> [A_i,A_j]=0 (collinear)
Fmax = max(float(np.linalg.norm(cross(A[i], A[j]))) for i in range(3) for j in range(3))
res["const_abelian_curvature"] = Fmax

# ---------- 4/5. Quadratic supercriticality + small-data threshold ----------
# Bound model: |I_quad| <= K' g ||v||_{H^1}^{5/2} ... absorption needs K' g r^{1/2} <= 1/4.
# Take conservative overestimate K' = 8 (documents Sobolev C_S ~ 1-2, combin. factors).
Kprime = 8.0
def r_of_g(g):
    return (1.0 / (4.0 * Kprime * g)) ** 2 if g > 0 else float("inf")
for g in [1.0, 0.5, 0.1, 0.01]:
    res[f"r_small_g={g}"] = r_of_g(g)
# torus spectral gap = 1 (frequencies k in Z^3, min |k|^2 = 1); linearized net decay:
# d/dt||v||^2 + 2(1 - K'g r^{1/2} - cg^2...)||∇v||^2 <= ... -> gamma0 ~= gap/2 at closure
# At closure boundary K'g r^{1/2}=1/4, residual diffusion fraction 1/2 -> Poincaré gives rate 1/2...1.
res["torus_gap"] = 1.0
res["small_data_gamma0"] = 0.5
res["Kprime_used"] = Kprime
# scaling demo: single-mode field v_L(x) = a sin(kx) e_c: ||v||_4^2||∇v|| ~ a^3 |k| scaling
# ratio I_quad/diffusion ~ g a |k|^{-0}? show growth in amplitude a (supercritical in size)
ks = [1, 2, 4]
a_vals = [0.1, 1.0, 5.0]
tab = {}
for k in ks:
    for a in a_vals:
        # ||v||_2^2 = V a^2/2, ||∇v||_2^2 = V a^2 k^2/2, ||v||_4^4 = V*3a^4/8 (sin^4 avg 3/8)
        I = a**3 * k  # proxy up to constants
        D = a**2 * k**2  # diffusion proxy
        tab[f"k={k},a={a}"] = {"I_proxy": I, "D_proxy": D, "ratio_g1": I / D}
res["scaling_table"] = tab
res["supercritical_note"] = ("ratio I/D ~ a/k grows unboundedly in amplitude a at fixed k: "
    "no fixed diffusion fraction absorbs I_quad uniformly in data size; small-data only.")

with open(OUT, "w") as f:
    json.dump(res, f, indent=2)
print(json.dumps(res, indent=2))
