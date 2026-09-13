"""Validate pair-projection formula for b2(K)=V(K,K,Z,Z) and facet-sum for b1.

b1(K) = (1/n) sum_F h_K(u_F) A_F ;  b2(K) = C0 sum_{i<j} D_ij Area(P_ij K).
Calibrate C0 at K=Z then test both against exact mv() on random bodies.
"""
import numpy as np
from zonotope import c_roots, mv, vol, facet_data, support_vals

n = 4
Z = c_roots(n)
m = Z.shape[1]
U, A = facet_data(Z)

# --- b1 check ---
rng = np.random.default_rng(7)
print("--- b1 facet-sum vs exact mv(K,Z,Z,Z) ---")
Cn = [Z] * (n - 2)
for s in range(6):
    G = rng.normal(size=(n, 8))
    exact = mv(G, Z, *Cn)
    approx = float(np.sum(A * support_vals(G, U))) / n
    print(f"rz{s}: exact={exact:.8g} facetsum={approx:.8g} relerr={abs(exact-approx)/exact:.2e}")

# --- projection setup for b2 ---
pairs = [(i, j) for i in range(m) for j in range(i + 1, m)]
D = {}
P = {}
for (i, j) in pairs:
    G2 = Z[:, [i, j]]
    d = float(np.sqrt(np.linalg.det(G2.T @ G2)))
    if d < 1e-12:
        continue
    Q, _ = np.linalg.qr(G2)  # Q: n x 2 orthonormal basis of span
    D[(i, j)] = d
    P[(i, j)] = np.eye(n) - Q @ Q.T  # projector onto 2D orth complement
print("nondegenerate pairs:", len(D), "of", len(pairs))


def hull_area_2d(Pt):
    """Convex hull area of 2D points via monotonic chain + shoelace."""
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


def proj_areas(X):
    """X: (N,n) vertices (or sample pts) of K. Returns dict pair->Area(P_ij conv X)."""
    out = {}
    for key, Pp in P.items():
        Y = X @ Pp.T
        # 2D coords in orth-complement basis
        _, _, vt = np.linalg.svd(Pp)
        B = vt[-2:, :].T  # n x 2 basis of range... (P sym, eigvecs)
        # use eigh for symmetric projector
        w, V = np.linalg.eigh(Pp)
        B = V[:, w > 0.5]
        Q2 = Y @ B
        out[key] = hull_area_2d(Q2)
    return out


# calibrate C0 at K=Z: vertices of Z = zonotope vertices = {Z s : s in {+-1}^m}? use subset:
# vertices = all Z s combos filtered (use verts.npz Xv)
d = np.load("verts.npz")
Xv = d["Xv"]
areas_Z = proj_areas(Xv)
S_Z = sum(D[k] * areas_Z[k] for k in D)
V0 = vol(Z)
C0 = V0 / S_Z
print("calibration: S_Z =", S_Z, " V0 =", V0, " C0 =", C0)

print("--- b2 projection-formula vs exact mv(K,K,Z,Z) ---")
Cn2 = [Z] * (n - 2)
tests = []
for s in range(6):
    tests.append((f"rz{s}", rng.normal(size=(n, 8))))
tests.append(("Z", Z))
tests.append(("box", np.column_stack([(c * np.eye(n)[:, [i]]) for i, c in enumerate([2, 1, 1, 1])])))
tests.append(("diagZ", np.diag([2., 1, 1, 1]) @ Z))
for label, G in tests:
    exact = mv(G, G, *Cn2)
    # vertices of zonotope G: enumerate sign combos (2^m too big for m=12... use m<=8 tests or sample)
    mm = G.shape[1]
    if mm <= 10:
        S = np.array(np.meshgrid(*([[-1., 1.]] * mm))).reshape(mm, -1).T
        X = (G @ S.T).T
    else:  # Z itself or diagZ: use stored/pushed verts
        X = Xv if label == "Z" else None
        if X is None:
            # diag image of Z verts
            X = (np.diag([2., 1, 1, 1]) @ Xv.T).T
    approx = C0 * sum(D[k] * v for k, v in proj_areas(X).items())
    print(f"{label}: exact={exact:.8g} proj={approx:.8g} relerr={abs(exact-approx)/max(exact,1e-9):.2e}")
np.savez("projcal.npz", C0=C0)
