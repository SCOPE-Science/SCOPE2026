"""Tangent Hessian gap at Z_4 via symmetric facet-pair pushes.

K(phi) = {U x <= h + phi} (phi per 48 sides; symmetric: phi[-F]=phi[F]).
b1(phi) = (1/n) sum A (h+phi) [linear exact];
b2(phi) = V(K(phi),K(phi),Z,Z) via calibrated pair-projection on pushed vertices
  X(t) = Minv (b0 + Eb phi) linear in phi (fixed combinatorics, small t).
Delta(t) = b1^2 - b2*b0 quadratic: finite-difference N(phi)=Delta''(0)/2.
D(phi) = sum A (phi - a h)^2 with optimal a (v=0 by symmetry; cross-check v too).
Report generalized eig min N/D over 24-dim symmetric pair-push space (excluding h dir).
"""
import itertools
import numpy as np
from zonotope import c_roots, mv, vol, facet_data, support_vals

n = 4
Z = c_roots(n)
m = Z.shape[1]
U, A = facet_data(Z)
F = len(A)
h = support_vals(Z, U)
V0 = vol(Z)
C0 = float(np.load("projcal.npz")["C0"])
d = np.load("verts.npz", allow_pickle=True)
Xv = d["Xv"]
combos = d["combos"]
Minv = d["Minv"]
NV = len(Xv)

# symmetric pair index: pairs (i,j) with U[j] = -U[i]
pair_of = -np.ones(F, dtype=int)
pairs = []
used = np.zeros(F, bool)
for i in range(F):
    if used[i]:
        continue
    j = None
    for k in range(F):
        if not used[k] and k != i and np.allclose(U[k], -U[i], atol=1e-6):
            j = k
            break
    assert j is not None
    pairs.append((i, j))
    used[i] = used[j] = True
P = len(pairs)
print("symmetric pairs:", P)
assert P == 24

# pair projection data (same as projval)
Dij = {}
Pp = {}
Bmat = {}
keys = []
for i in range(m):
    for j in range(i + 1, m):
        G2 = Z[:, [i, j]]
        dd = float(np.sqrt(np.linalg.det(G2.T @ G2)))
        if dd < 1e-12:
            continue
        Q, _ = np.linalg.qr(G2)
        Pp_ = np.eye(n) - Q @ Q.T
        w, V = np.linalg.eigh(Pp_)
        B = V[:, w > 0.5]
        key = (i, j)
        Dij[key] = dd
        Pp[key] = Pp_
        Bmat[key] = B
        keys.append(key)

# vertex -> active combo rows; vertex position X(phi) = Minv[q] @ (b0 + E phi)
# E[q, k] = 1 if facet k in combos[q]
E = np.zeros((NV, F))
for q in range(NV):
    E[q, combos[q]] = 1.0
b0 = h[combos]  # (NV,4)
X0 = np.einsum("qab,qb->qa", Minv, b0)
print("X0 vs Xv max err:", np.abs(X0 - Xv).max())

# directional derivative dX/ds along phi-direction phivec: Vq = Minv[q] @ E[q]*phivec
# projected 2D-area second variation: A(s) = hull area of (X0 + sV) projected.
# Use exact polygon topology at s=0? Simpler: robust finite differences with small s
# and fixed vertex SET (interior vertices harmless: conv of superset = conv).


def hull_area_2d(Pt):
    Pt = np.unique(np.round(Pt, 9), axis=0)
    if len(Pt) < 3:
        return 0.0
    pts = sorted(map(tuple, Pt))
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lo, hi = [], []
    for p in pts:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    for p in reversed(pts):
        while len(hi) >= 2 and cross(hi[-2], hi[-1], p) <= 0:
            hi.pop()
        hi.append(p)
    H = lo[:-1] + hi[:-1]
    s = 0.0
    for k in range(len(H)):
        x1, y1 = H[k]
        x2, y2 = H[(k + 1) % len(H)]
        s += x1 * y2 - x2 * y1
    return abs(s) / 2


# precompute projected vertex clouds at 0: Y0[key] (NV,2), and direction maps V2[q,key]
Y0 = {}
for key in keys:
    Y0[key] = (X0 @ Pp[key].T) @ Bmat[key]

# symmetric pair-push basis: Phi_r[i]+Phi_r[j] = 1 on pair r. Each basis vector -> Vq.
Phi = np.zeros((P, F))
for r, (i, j) in enumerate(pairs):
    Phi[r, i] = 1.0
    Phi[r, j] = 1.0
# Vq[r, q, a] = sum_t Minv[q,a,t] * Phi[r, combos[q,t]]
Cphi = Phi[:, combos]  # (P, NV, n)
V = np.einsum("qat,rqt->rqa", Minv, Cphi)  # (P, NV, n)
V2 = {}
for key in keys:
    M2 = Pp[key].T @ Bmat[key]  # (n,2)
    V2[key] = V @ M2  # (P,NV,2)


def quad_forms(c, s=0.02):
    """Return (N, Dden) with N = Delta''(0)/2 coefficient, Dden = dist''(0)/2 coeff."""
    L = float(np.sum(A * (Phi.T @ c))) / n
    Yp, Ym, Y2p, Y2m = {}, {}, {}, {}
    Ap = Am = A2p = A2m = 0.0
    for key in keys:
        Vc = np.einsum("r,rqa->qa", c, V2[key])  # (NV,2)
        Yc0 = Y0[key]
        Ap += Dij[key] * hull_area_2d(Yc0 + s * Vc)
        Am += Dij[key] * hull_area_2d(Yc0 - s * Vc)
        A2p += Dij[key] * hull_area_2d(Yc0 + 2 * s * Vc)
        A2m += Dij[key] * hull_area_2d(Yc0 - 2 * s * Vc)
    b2_0 = C0 * sum(Dij[k] * hull_area_2d(Y0[k]) for k in keys)
    bp = C0 * Ap
    bm = C0 * Am
    b2p = C0 * A2p
    b2m = C0 * A2m
    # second derivative of b2 at 0 (4th-order FD for robustness)
    B2c = (-b2p + 16 * bp - 30 * b2_0 + 16 * bm - b2m) / (12 * s * s)
    Nq = L * L - V0 * B2c
    phi = Phi.T @ c
    a = float(np.sum(A * phi * h)) / float(np.sum(A * h * h))
    Dd = float(np.sum(A * (phi - a * h) ** 2))
    return Nq, Dd, L, B2c, b2_0


# check b2_0 == V0
Nq0, Dd0, L0, B2c0, b20 = quad_forms(np.zeros(P))
print("b2(0) =", b20, " V0 =", V0)

# Hessian matrices over pair basis via polarization (use s grid + symmetrize)
S = 0.05
HN = np.zeros((P, P))
HD = np.zeros((P, P))
Nv = np.zeros(P)
Dv = np.zeros(P)
for r in range(P):
    e = np.zeros(P)
    e[r] = 1.0
    Nq, Dd, *_ = quad_forms(e, s=S)
    Nv[r] = Nq
    Dv[r] = Dd
for r in range(P):
    for q in range(r, P):
        er = np.zeros(P)
        eq = np.zeros(P)
        er[r] = 1.0
        eq[q] = 1.0
        Npq, Dpq, *_ = quad_forms(er + eq, s=S)
        HN[r, q] = HN[q, r] = (Npq - Nv[r] - Nv[q]) / 2
        HD[r, q] = HD[q, r] = (Dpq - Dv[r] - Dv[q]) / 2
for r in range(P):
    HN[r, r] = Nv[r]
    HD[r, r] = Dv[r]
np.savez("hess.npz", HN=HN, HD=HD, Phi=Phi, pairs=np.array(pairs))

# generalized eigenvalues on subspace orthogonal (HD) to h-mode; h in pair coords:
hpair = np.array([h[i] + h[j] for (i, j) in pairs]) / 2  # phi = c_r on both sides
# restrict: eig(HN, HD) with regularization; drop near-null HD modes
wD, VD = np.linalg.eigh(HD)
print("HD eig min/max:", wD.min(), wD.max())
keep = wD > 1e-6 * wD.max()
print("kept HD modes:", keep.sum(), "of", P)
HNr = VD[:, keep].T @ HN @ VD[:, keep]
wDr = wD[keep]
HNs = HNr / np.sqrt(wDr[:, None] * wDr[None, :])
lam, Uu = np.linalg.eigh(HNs)
print("generalized eigs N/D (sorted):", np.round(lam, 3))
# exclude h-mode: overlap of each mode with h direction
Hp = VD[:, keep] @ (Uu / np.sqrt(wDr)[:, None])
hvec = (Phi.T @ np.ones(P)) * 0 + (h.copy())
# h projected coeffs in pair basis:
hc = np.array([(h[i] + h[j]) / 2 for (i, j) in pairs])
hn = hc / np.linalg.norm(hc)
ov = (Hp * np.sqrt(np.diag(HD) if False else 1)).T @ hn if False else (Hp.T @ (HD @ hn))
print("mode-h overlaps:", np.round(ov / np.sqrt((hn @ HD @ hn) * np.diag(Uu.T @ Uu)), 3))
print("per-basis N, D:")
for r in range(P):
    print(f"  pair{r} {pairs[r]}: N={Nv[r]:.6g} D={Dv[r]:.6g} N/D={Nv[r]/Dv[r] if Dv[r]>0 else float('inf'):.6g}")
print("min over basis:", (Nv / np.maximum(Dv, 1e-300)).min())
