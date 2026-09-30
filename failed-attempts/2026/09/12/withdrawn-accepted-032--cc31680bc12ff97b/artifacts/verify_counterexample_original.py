"""Verify the explicit counterexample disproving the target stability inequality.

P = [-1,1]^4, Q = [-1.2,1.2] x [-0.9,0.9]^3 in R^4.
Checks: class membership, identical normalized cone-volume measures (W2=0),
and min-translation Hausdorff distance = 0.2 > 20*0^{1/4} = 0.
Uses only numpy (analytic formulas + vertex enumeration).
"""
import itertools
import numpy as np

aP = np.array([1.0, 1.0, 1.0, 1.0])
aQ = np.array([1.2, 0.9, 0.9, 0.9])

# --- 1. Class membership: (1/2)B^4 subset P, Q subset 2B^4 ---
# (1/2)B^4 subset box iff min half-side >= 1/2; box subset 2B^4 iff vertex norm <= 2.
assert aP.min() >= 0.5 and aQ.min() >= 0.5, "inner ball fails"
vnormP = float(np.sqrt((aP ** 2).sum()))
vnormQ = float(np.sqrt((aQ ** 2).sum()))
assert vnormP <= 2.0 + 1e-12 and vnormQ <= 2.0 + 1e-12, "outer ball fails"
print(f"min half-sides: P={aP.min()}, Q={aQ.min()} (>=0.5 OK)")
print(f"vertex norms: P={vnormP:.6f}, Q={vnormQ:.6f} (<=2 OK)")
print("facets: 8 each (<=12 OK); centroid 0 by central symmetry OK")

# --- 2. Cone-volume weights: facet {x_i=+-a_i} has (n-1)-vol 2^3*prod_{j!=i} a_j,
#     height a_i, cone-vol |F|*h/4 = 2*prod(a); total 16*prod(a); each facet 1/8.
for name, a in (("P", aP), ("Q", aQ)):
    prod = float(np.prod(a))
    cvol = 2.0 * prod
    total = 8.0 * cvol
    assert abs(total - 16.0 * prod) < 1e-12
    w = cvol / total
    assert abs(w - 1.0 / 8.0) < 1e-15, (name, w)
    print(f"{name}: prod={prod:.4f}, per-facet cone-vol={cvol:.4f}, "
          f"total vol={total:.4f} (=16*prod OK), weight={w:.6f} (=1/8 OK)")

print("V_P = V_Q = (1/8) sum over {+-e_i}; identity coupling gives W_2 = 0 <= 1e-3 OK")

# --- 3. Hausdorff distance at t=0 by vertex enumeration ---
vertsP = np.array(list(itertools.product(*[(-v, v) for v in aP])))
vertsQ = np.array(list(itertools.product(*[(-v, v) for v in aQ])))


def point_box_dist(pts, a):
    return np.abs(pts) - a  # signed per-coordinate excess


def dist_to_box(pts, a):
    return np.maximum(point_box_dist(pts, a), 0.0).max(axis=1)


d1 = dist_to_box(vertsP, aQ).max()  # sup_{x in P} dist(x, Q)
d2 = dist_to_box(vertsQ, aP).max()  # sup_{y in Q} dist(y, P)
dH0 = max(d1, d2)
print(f"sup_P dist(.,Q)={d1:.6f} (expect 0.1), sup_Q dist(.,P)={d2:.6f} (expect 0.2)")
print(f"d_H(P,Q) at t=0: {dH0:.6f}")
assert abs(d1 - 0.1) < 1e-9 and abs(d2 - 0.2) < 1e-9 and abs(dH0 - 0.2) < 1e-9

# --- 4. Optimal-translation lower bound via x1-projection (1-Lipschitz) ---
# proj(P)=[-1,1], proj(Q+t)=[-1.2+t1,1.2+t1]; interval Hausdorff = max(|0.2-t1|,|0.2+t1|)=0.2+|t1|.
# Hence min_t d_H(P,Q+t) >= 0.2, attained at t=0 -> equals 0.2.
ts = np.linspace(-1, 1, 41)
lo = np.maximum(np.abs(0.2 - ts), np.abs(-0.2 - ts))
assert np.all(lo >= 0.2 - 1e-12) and abs(lo.min() - 0.2) < 1e-12
print(f"projection lower bound min over grid = {lo.min():.6f}; gives min_t d_H = 0.2")

# --- 5. Inequality check ---
W2, RHS, LHS = 0.0, 20.0 * 0.0 ** 0.25, dH0
print(f"LHS (optimal-translation d_H) = {LHS:.6f}, RHS = 20*W2^(1/4) = {RHS:.6f}")
assert LHS > RHS
print(f"COUNTEREXAMPLE CONFIRMED: {LHS:.4f} <= {RHS:.4f} is FALSE. Target disproved.")
