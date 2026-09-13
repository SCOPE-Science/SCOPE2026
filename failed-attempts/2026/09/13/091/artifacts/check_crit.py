# Exact check (integers/Fractions only): balanced 18-term degree-1 Newton-hull model.
# Triangle V = (6,0),(0,6),(-6,-6): edges have lattice lengths 6,6,6 (gcd), matching
# Vianna Thm 5.1 edge lengths (n1*p,n2*q,n3*r) = (6,6,6) for ((2,3),(3,2),(6,1)).
# HONEST SCOPE: this is the unit-count (all n_beta = 1) model on the 18 boundary
# lattice points, GL(2,Z)-equivalent to any (6,6,6) lattice triangle. It is NOT
# claimed to be the true open-GW W_T0 (true counts may differ); it isolates exactly
# what CAN be verified: a balanced hull admits an exact positive-real critical point.
from fractions import Fraction as Q
from math import gcd

V1, V2, V3 = (6, 0), (0, 6), (-6, -6)

def edge_pts(A, B):
    # lattice points on segment A->B inclusive of A, exclusive of B
    dx, dz = B[0]-A[0], B[1]-A[1]
    g = gcd(abs(dx), abs(dz))
    assert g == 6, (A, B, g)
    return [(A[0]+dx*k//g, A[1]+dz*k//g) for k in range(g)]

pts = edge_pts(V1, V2) + edge_pts(V2, V3) + edge_pts(V3, V1)
assert len(pts) == 18 and len(set(pts)) == 18
print("distinct boundary monomials:", len(pts))

# log-gradient at (1,1) = sum of exponent vectors (all weights 1)
sx = sum(a for (a, b) in pts)
sy = sum(b for (a, b) in pts)
print("log-grad at (1,1) =", (sx, sy))
assert sx == 0 and sy == 0

# log-Hessian at critical point = sum v v^T
H11 = sum(a*a for (a, b) in pts)
H12 = sum(a*b for (a, b) in pts)
H22 = sum(b*b for (a, b) in pts)
det = H11*H22 - H12*H12
print("H_log = [[%s,%s],[%s,%s]], det = %s" % (H11, H12, H12, H22, det))
assert det != 0
print("W(1,1) =", len(pts))
print("OK: balanced 18-term model has exact nondegenerate positive-real critical point at (1,1).")
print("ROLE IN DRAFT: exhibits exact satisfiability of hypothesis (H-mono) on this Newton")
print("triangle (open det != 0 condition); true open-GW coefficients enter only via (H-mono).")
