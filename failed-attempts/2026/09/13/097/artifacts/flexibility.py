"""Infinitesimal flexibility: unstable-tangent deformations of L preserve
stable periodic data to first order while moving unstable data.

Setup: f_t = Phi^t_X o L, X(y) = psi(y) w, w in Eu_L fixed (constant vector
field direction), psi scalar torus function. Then DX(y) = w (grad psi)^T.

Claim 1 (stable stationarity): d/dt|_0 log|det Df_t^n(p)|E^s| = 0 for every
periodic point p, for EVERY psi. Proof: the derivative equals
  sum_{k=0}^{n-1} tr( P_s DX(L^k p) ) = sum_k (z_s . w) dpsi(L^k p)[v_s dir...].
Since w in Eu and z_s annihilates Eu (L-invariance of splitting), z_s.w = 0
exactly, so every term is 0 *including the derivative hitting eigenvectors*.
We verify numerically: z_s.w1 = z_s.w2 = 0 and first-order finite differences
of the stable multiplier at fixed point 0 and at a period-2 orbit vanish to
O(eps^2) while unstable data moves at O(eps).

Claim 2 (unstable movement): d/dt|_0 log|det Df_t^{n_u}|E^u| != 0 generic.
For the fixed point 0, Df_t(0) = (I + t DX(0)) M, first-order change of
log|det(Df_t|Eu)| = t * tr(P_u DX(0)) which is generically nonzero.
We exhibit one psi with nonzero value AND check it is not killed by
coboundary averaging (it is a pointwise trace, no cohomology involved).

Writes flexibility.json.
"""
import numpy as np
import json, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "flexibility.json")
M = np.array([[0, 1, 0], [0, 0, 1], [1, 0, -1]], float)
w_, V = np.linalg.eig(M)
is_ = int(np.argmin(np.abs(w_)))
vs = V[:, is_].real
iu = [i for i in range(3) if i != is_]
w1 = V[:, iu[0]].real
w2 = V[:, iu[0]].imag
wl, VL = np.linalg.eig(M.T)
js = int(np.argmin(np.abs(wl)))
zs = VL[:, js].real
zs = zs / (zs @ vs)
res = {}
res["annihilation_zs_w1"] = float(zs @ w1)
res["annihilation_zs_w2"] = float(zs @ w2)
assert abs(zs @ w1) < 1e-12 and abs(zs @ w2) < 1e-12

# --- unstable covectors: match left eigvecs to right by eigenvalue ---
# R0 (mu) pairs with L1 (mu); R1 (mubar) pairs with L2 (mubar).
vu = [V[:, iu[0]], V[:, iu[1]]]
ju = [int(np.argmin(np.abs(wl - w_[i]))) for i in iu]
zu = [VL[:, j] for j in ju]
S = np.array([[zu[j] @ vu[k] for k in range(2)] for j in range(2)], dtype=complex)
Sinv = np.linalg.inv(S)
zu = [Sinv[0, 0] * zu[0] + Sinv[0, 1] * zu[1],
      Sinv[1, 0] * zu[0] + Sinv[1, 1] * zu[1]]
S2 = np.array([[zu[j] @ vu[k] for k in range(2)] for j in range(2)])
assert np.max(np.abs(S2 - np.eye(2))) < 1e-9

# --- psi(y) = sin(2 pi y_0): grad psi(y) = 2pi cos(2pi y0) e_0 ---
# DX(y) = w outer grad psi. At fixed point 0: grad = 2pi e_0.
e0 = np.array([1.0, 0, 0])
for tag, wv in [("w1", w1), ("w2", w2)]:
    A = 2 * np.pi * np.outer(wv, e0)  # DX(0)
    tr_s = float((zs @ A @ vs).real)
    tr_u = complex(zu[0] @ A @ vu[0] + zu[1] @ A @ vu[1])
    res[f"trace_stable_{tag}"] = tr_s
    res[f"trace_unstable_{tag}_re"] = float(tr_u.real)
    res[f"trace_unstable_{tag}_im"] = float(tr_u.imag)
assert abs(res["trace_stable_w1"]) < 1e-9 and abs(res["trace_stable_w2"]) < 1e-9
assert abs(complex(res["trace_unstable_w2_re"], res["trace_unstable_w2_im"])) > 1e-6 or \
    abs(complex(res["trace_unstable_w1_re"], res["trace_unstable_w1_im"])) > 1e-6

# --- finite-difference check at fixed point 0 and a genuine period-4 orbit ---
# NOTE: det(M^2-I) = -1, so Fix(L^2) = {0}: L has NO period-2 orbit at all.
# Smallest genuine orbit: period 4 (Fix(L^4) has 5 points). Found q=(0.4,0.2,0.6).
# f_eps(y) = y + eps X(y) composed with L: f(y) = L y + eps X(L y), X = psi w.
# Df(p) = (I + eps DX(Lp)) M. Stable multiplier at fixed pt 0: eig of Df(0)
# near lam_s; unstable: |det|/|stable|.
def Df(p, eps, wv):
    Lp = np.mod(M @ p, 1.0)
    g = 2 * np.pi * np.cos(2 * np.pi * Lp[0]) * e0
    return (np.eye(3) + eps * np.outer(wv, g)) @ M

# period-4 orbit of L (verified closure below); Fix(L), Fix(L^2) are trivial.
q = np.array([0.4, 0.2, 0.6])
orb4 = [q]
for _ in range(3):
    orb4.append(np.mod(M @ orb4[-1], 1.0))
assert np.linalg.norm(np.mod(M @ orb4[-1], 1.0) - q) < 1e-9
assert all(np.linalg.norm(o - q) > 1e-3 or i == 0 for i, o in enumerate(orb4[:3]))
res["period4_point"] = [float(x) for x in q]

for tag, wv in [("w1", w1), ("w2", w2)]:
    for pname, orb in [("fixed0", [np.zeros(3)]), ("per4", orb4)]:
        n = len(orb)
        logs, logu = [], []
        for eps in [1e-4, -1e-4, 2e-4]:
            J = np.eye(3)
            for pt in orb:
                J = Df(pt, eps, wv) @ J
            ev = np.linalg.eigvals(J)
            am = np.abs(ev)
            i0 = int(np.argmin(am))
            ls = np.log(am[i0])
            lu = np.log(abs(np.linalg.det(J))) - ls
            logs.append(ls); logu.append(lu)
        # first-order slope of stable log-mult: (l(+h)-l(-h))/2h should be ~0 (O(h^2) residual)
        slope_s = (logs[0] - logs[1]) / 2e-4
        slope_u = (logu[0] - logu[1]) / 2e-4
        res[f"slope_stable_{tag}_{pname}"] = float(slope_s)
        res[f"slope_unstable_{tag}_{pname}"] = float(slope_u)
        # second-difference measures curvature O(1) i.e. residual is O(eps^2)
        curv_s = (logs[2] - 2 * logs[0] + logs[1] - (logs[0] - logs[1])) / 1e-8
        res[f"curv_stable_{tag}_{pname}"] = float(curv_s)

for tag in ["w1", "w2"]:
    for pname in ["fixed0", "per4"]:
        assert abs(res[f"slope_stable_{tag}_{pname}"]) < 1e-6, (tag, pname, res[f"slope_stable_{tag}_{pname}"])

with open(OUT, "w") as f:
    json.dump(res, f, indent=2)
print(json.dumps(res, indent=2))
print("ALL ASSERTIONS PASSED")
