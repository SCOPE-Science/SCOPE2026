"""Verify the linear model L(x)=Mx mod 1 for the rigidity proof.

M = companion of x^3+x^2-1. Checks:
 1. det=1, hyperbolic, irreducible (no rational root), 1 real stable + complex unstable pair.
 2. Conformal structure of L|E^u (rotation-dilation) -- backbone of quadrilateral step.
 3. Quadrilateral telescoping identity for an explicit coboundary Phi = u o L - u.
 4. Matching-function identity rho_f/rho_g = P-ratio for synthetic data.
Writes linear_model.json.
"""
import numpy as np
import json, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "linear_model.json")
M = np.array([[0, 1, 0], [0, 0, 1], [1, 0, -1]], float)
res = {}

# ---- 1. spectrum / hyperbolicity / irreducibility ----
w, V = np.linalg.eig(M)
res["det"] = float(np.linalg.det(M))
res["eigenvalues"] = [[float(v.real), float(v.imag)] for v in w]
res["moduli"] = [float(abs(v)) for v in w]
poly = np.poly(M)  # monic char poly coefficients
res["charpoly"] = [float(c) for c in poly]
p1 = float(np.polyval(poly, 1.0)); pm1 = float(np.polyval(poly, -1.0))
res["p(1)"] = p1; res["p(-1)"] = pm1  # both nonzero => no rational root => irreducible cubic
mods = np.abs(w)
is_ = int(np.argmin(mods))
lam_s = float(w[is_].real)
iu = [i for i in range(3) if i != is_]
mu = complex(w[iu[0]])
res["lambda_s"] = lam_s
res["mu_abs"] = float(abs(mu)); res["mu_arg_over_2pi"] = float(np.angle(mu) / (2 * np.pi))
assert abs(res["det"]) == 1.0
assert lam_s < 1.0 and abs(mu) > 1.0
assert abs(p1) > 0.5 and abs(pm1) > 0.5
# hyperbolicity: nothing on unit circle
assert all(abs(m - 1.0) > 1e-6 for m in mods)

# ---- splitting ----
vs = V[:, is_].real
e1 = V[:, iu[0]].real; e2 = V[:, iu[0]].imag
res["stable_dir"] = [float(x) for x in vs]
# left eigenvectors for projections
wl, VL = np.linalg.eig(M.T)
js = int(np.argmin(np.abs(wl)))
zs = VL[:, js].real; zs = zs / (zs @ vs)
res["left_stable_pairing"] = float(zs @ vs)

# ---- 2. complex-pair (conformal) structure of L|E^u ----
# Intrinsically: L|Eu has a complex-conjugate eigenvalue pair (open condition),
# i.e. it is a real rotation-dilation: trace^2-4det<0, det>0. It is conformal
# w.r.t. the adapted Hermitian metric, NOT w.r.t. an arbitrary Euclidean basis.
# We verify the intrinsic signature and record the Euclidean gram for honesty.
Q, _ = np.linalg.qr(np.column_stack([e1, e2]))
B = Q  # 3x2 isometry onto Eu
M2 = B.T @ M @ B  # 2x2 representing L|Eu in an orthonormal basis
tr2, det2 = float(np.trace(M2)), float(np.linalg.det(M2))
res["Eu_trace"] = tr2; res["Eu_det"] = det2
res["Eu_discriminant"] = tr2 ** 2 - 4 * det2  # <0 <=> complex pair (conformal type)
assert det2 > 0 and (tr2 ** 2 - 4 * det2) < 0
S = M2.T @ M2
res["Eu_gram_ratio_diag"] = float(S[0, 0] / S[1, 1])
res["Eu_gram_offdiag_normed"] = float(S[0, 1] / np.sqrt(S[0, 0] * S[1, 1]))
r = float(np.sqrt(det2))  # |mu|: conformal factor (|det M2| = r^2)
R = M2 / r
res["conformal_factor_r"] = r
res["rotation_det"] = float(np.linalg.det(R))
# NOTE (corrected in WORKLOG): no Euclidean-orthogonality assertion here; the
# conformal structure is intrinsic (discriminant<0), not Euclidean.

# ---- helpers on torus ----
def Lmap(x):
    return np.mod(M @ x, 1.0)

rng = np.random.default_rng(0)
p = rng.random(3)
u = (B @ np.array([0.01, -0.004]))          # small unstable displacement
s = 0.01 * vs / np.linalg.norm(vs)          # small stable displacement
x = np.mod(p + u, 1.0); z = np.mod(p + s, 1.0); wpt = np.mod(p + u + s, 1.0)
# quadrilateral closes exactly (linear): w = corner Wu(z) cap Ws(x)
res["quad_closure_err"] = float(np.linalg.norm(np.mod(x + s, 1.0) - wpt))

# ---- 3. quadrilateral telescoping for coboundary Phi = u0 o L - u0 ----
# STABLE-pair series: sum_k [Phi(L^k p) - Phi(L^k z)] telescopes (exact algebra)
# to [u0(L^N p)-u0(p)] - [u0(L^N z)-u0(z)] -> u0(z)-u0(p) because the stable
# pair contracts geometrically (ratio |lam_s|), so u0(L^N p)-u0(L^N z) -> 0.
# Numerics: iterate the SEPARATION in the linear lift (exact: d_k = lam_s^k s),
# not two mod-1 trajectories (catastrophic cancellation once d_k < 1e-12).
# Evaluate u0 at lifted representatives paired in the same fundamental domain.
def u0(y):
    return np.sin(2 * np.pi * y[0]) * np.cos(2 * np.pi * y[1]) + 0.5 * np.sin(2 * np.pi * y[2])

def Phi(y):
    return u0(Lmap(y)) - u0(y)

base = np.mod(p + 100.0, 1.0)  # representative of p in R^3
dk = s.copy()                   # lifted separation, contracts by lam_s each step
N = 60                          # |lam_s|^60 ~ 1e-7: tail below 1e-6, no precision loss
S_pz = 0.0
Qk = base.copy()
for _ in range(N):
    S_pz += Phi(np.mod(Qk, 1.0)) - Phi(np.mod(Qk + dk, 1.0))
    Qk = M @ Qk                 # linear lift of the orbit (no mod: exact pairing)
    dk = lam_s * dk             # L(Qk+dk)-L(Qk) = lam_s*dk along stable line
res["stable_series_val"] = float(S_pz)
res["stable_series_target"] = float(u0(np.mod(base + s, 1.0)) - u0(np.mod(base, 1.0)))
res["stable_series_err"] = float(abs(res["stable_series_val"] - res["stable_series_target"]))
res["stable_tail_bound"] = float((abs(lam_s) ** N) / (1 - abs(lam_s)) * 8.0)
assert res["stable_series_err"] < 1e-6

# QUADRILATERAL identity (corrected): each stable-leg sum telescopes to the
# u-difference along its leg: S(p,z) -> u(z)-u(p), S(x,w) -> u(w)-u(x).
# Their double difference D = S(p,z) - S(x,w) converges to the CORNER DEFECT
#   D -> [u(z)-u(p)] - [u(w)-u(x)] = [u(x)-u(p)] - [u(w)-u(z)] =: corner_defect,
# which vanishes iff u is affine along the quadrilateral. For the rigidity
# proof this is exactly the point: matching transfer functions make the two
# legs see the same rho, and conformality forces the corner defect to zero
# in the limit of small quadrilaterals, yielding differentiability.
dk1 = s.copy(); dk2 = s.copy()
Qk1 = base.copy(); Qk2 = base + u  # same-branch lift of x (NOT re-modded)
D = 0.0
for _ in range(N):
    D += (Phi(np.mod(Qk1, 1.0)) - Phi(np.mod(Qk1 + dk1, 1.0))) \
         - (Phi(np.mod(Qk2, 1.0)) - Phi(np.mod(Qk2 + dk2, 1.0)))
    Qk1 = M @ Qk1; Qk2 = M @ Qk2; dk1 = lam_s * dk1; dk2 = lam_s * dk2
corner_defect = (u0(np.mod(base + u, 1.0)) - u0(np.mod(base, 1.0))) \
    - (u0(np.mod(base + u + s, 1.0)) - u0(np.mod(base + s, 1.0)))
res["quad_double_diff"] = float(D)
res["corner_defect_closed"] = float(corner_defect)
res["quad_identity_err"] = float(abs(D - corner_defect))
assert res["quad_identity_err"] < 1e-6

# ---- 4. matching-function identity ----
# synthetic stable cocycle a(y) = c + v(Ly)-v(y); rho(p,z) = exp(sum a(L^k z)-a(L^k p))
# Same lifted-pairing technique as section 3 (exact geometric contraction).
def vfun(y):
    return 0.3 * np.cos(2 * np.pi * (y[0] + y[2]))
c0 = np.log(abs(lam_s))
def afun(y):
    return c0 + vfun(Lmap(y)) - vfun(y)
Qk = base.copy(); dk = s.copy()
lr = 0.0
for _ in range(N):
    lr += afun(np.mod(Qk + dk, 1.0)) - afun(np.mod(Qk, 1.0))
    Qk = M @ Qk; dk = lam_s * dk
rho = float(np.exp(lr))
# Sign (verified): lr = sum afun(z_k)-afun(p_k) telescopes with c0 cancelling to
# [v(L^N z)-v(L^N p)] - [v(z)-v(p)] -> v(p)-v(z). So rho -> exp(v(p)-v(z)).
rho_closed = float(np.exp(vfun(np.mod(base, 1.0)) - vfun(np.mod(base + s, 1.0))))
res["rho_series"] = rho; res["rho_closed"] = rho_closed
res["rho_err"] = float(abs(rho - rho_closed))

with open(OUT, "w") as f:
    json.dump(res, f, indent=2)
print(json.dumps(res, indent=2))
print("ALL ASSERTIONS PASSED")
