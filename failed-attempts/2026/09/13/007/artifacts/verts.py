"""Step 1: enumerate vertices of Z_4 (H-polytope Ux <= h) + save; verify facet data."""
import itertools
import numpy as np
from zonotope import c_roots, facet_data, support_vals, vol

n = 4
Z = c_roots(n)
U, A = facet_data(Z)
h = support_vals(Z, U)
F = len(h)
print("facets(sides):", F, "Vol:", vol(Z))

combos = np.array(list(itertools.combinations(range(F), n)))
print("num 4-combos:", len(combos))
M = U[combos]          # (N,4,4) rows are normals
b = h[combos]          # (N,4)
dets = np.linalg.det(M)
ok = np.abs(dets) > 1e-9
print("nonsingular:", ok.sum())
X = np.zeros((len(combos), n))
X[ok] = np.linalg.solve(M[ok], b[ok])
# feasibility: U x <= h + tol
tol = 1e-6
viol = (U @ X[ok].T).T - h   # (Nok, F)
maxviol = viol.max(axis=1)
feas = maxviol <= tol * max(1.0, np.abs(h).max())
print("feasible (vertex-defining) combos:", feas.sum())
Xv = X[ok][feas]
print("max violation among kept:", maxviol[feas].max())
# uniqueness: round to 6 decimals
keys = np.round(Xv, 5)
uniq, idx = np.unique(keys, axis=0, return_index=True)
print("unique vertices:", len(uniq))
# per-facet vertex counts (active set)
act = np.abs((U @ Xv.T).T - h) <= 1e-4
counts = act.sum(axis=0)
print("min/max verts per facet:", counts.min(), counts.max())
print("vertex norms min/max:", np.linalg.norm(Xv, axis=1).min(),
      np.linalg.norm(Xv, axis=1).max())
# which combos feasible -> save M^{-1} for linear vertex motion
Mf = M[ok][feas]
Minv = np.linalg.inv(Mf)
np.savez("verts.npz", U=U, A=A, h=h, Xv=Xv, combos=np.array(combos)[ok][feas],
         Minv=Minv)
print("saved verts.npz")
# facet consistency: each facet's vertices should span a 3D face with (n-1)-vol = A
print("total area:", A.sum(), " (1/n)int h dS =", float(U.shape[0] and np.sum(A*h)/n))
