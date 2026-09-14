"""Verification script for lane-1801: triangular vs quadrilateral monotone fibres in dP5.

Checks (exact integer arithmetic unless noted):
 1. T = [(-3,-2),(-1,-2),(2,3)] is a complete primitive CCW fan (triangle).
 2. Q = [(-2,-1),(-1,-1),(1,0),(1,2)] is a complete primitive CCW fan (quadrilateral).
 3. Both anticanonical polytopes {m : m.vi >= -1} have normalized area 5 (degree-5 limits).
 4. Cone data (r,s), T-assignments (d,n), and Picard-rank check rho_smooth = 5 for both.
 5. Maslov-2 hulls conv(rays): vertex-extremality of every ray, normalized area,
    boundary/interior/total lattice points. Areas 10 vs 7 => no GL(2,Z) equivalence.
 6. Hori-Vafa/Pascaleff-Tonkonog potentials and their Newton data.
"""
import math
from fractions import Fraction

def det(a, b):
    return a[0]*b[1]-a[1]*b[0]

def prim(v):
    return math.gcd(abs(v[0]), abs(v[1])) == 1

def check_fan(rays):
    n = len(rays)
    assert all(prim(v) for v in rays), "all rays primitive"
    ds = [det(rays[i], rays[(i+1) % n]) for i in range(n)]
    assert all(d > 0 for d in ds), f"CCW complete fan, dets={ds}"
    return ds

def anti_polytope(rays):
    """Vertices of {m : m.vi >= -1}, one per consecutive pair (exact Fractions).
    Returns None if some vertex violates a constraint (rays not a Fano fan)."""
    n = len(rays)
    verts = []
    for i in range(n):
        v, w = rays[i], rays[(i+1) % n]
        d = det(v, w)
        x = Fraction(-w[1]+v[1], d)
        y = Fraction(-v[0]+w[0], d)
        verts.append((x, y))
    for (x, y) in verts:
        for v in rays:
            if x*v[0]+y*v[1] < -1:
                return None
    return verts

def norm_area(V):
    A = Fraction(0)
    n = len(V)
    for i in range(n):
        A += V[i][0]*V[(i+1) % n][1] - V[(i+1) % n][0]*V[i][1]
    return abs(A)

def cone_s(v, w):
    """Return (r, s): r = det > 0, s = normal-form parameter via u with det(v,u)=1."""
    r = det(v, w)
    assert r > 0
    for ux in range(-14, 15):
        for uy in range(-14, 15):
            if det(v, (ux, uy)) == 1:
                return (r, det(w, (ux, uy)) % r)
    raise AssertionError("no complement (rays too large?)")

def T_witness(r, s):
    """All (d,n,a) with r = d*n^2, gcd(a,n)=1, dna-1 = +/-s^{+-1} mod r."""
    if r == 1:
        return [(1, 1, 1)]
    vals = {s % r, (-s) % r}
    if math.gcd(s, r) == 1:
        si = pow(s, -1, r)
        vals.add(si); vals.add((-si) % r)
    out = []
    for n in range(1, int(math.isqrt(r))+2):
        if r % (n*n) != 0:
            continue
        d = r // (n*n)
        for a in range(1, n+1):
            if math.gcd(a, n) != 1:
                continue
            if (d*n*a - 1) % r in vals:
                out.append((d, n, a))
    return out

def is_vertex(P, k):
    """True iff P[k] is extremal: not in conv of the other points (exact)."""
    # P[k] is a vertex iff it lies strictly outside conv(rest):
    # equivalently, some linear functional strictly maximized at P[k].
    # Brute force: check P[k] not expressed as convex combo on a fine rational
    # grid is inexact; instead use facet test: P[k] is a vertex iff the polygon
    # with P[k] removed has P[k] outside it. Use exact half-plane test against
    # convex hull of rest computed by exact Graham scan.
    rest = [p for j, p in enumerate(P) if j != k]
    H = convex_hull(rest)
    # point strictly outside or on boundary-but-extreme? For our sets, test:
    # P[k] is a vertex of conv(P) iff P[k] not in conv(rest).
    return not point_in_convex(P[k], H)

def convex_hull(pts):
    pts = sorted(set(pts))
    if len(pts) <= 1:
        return pts
    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lo, hi = [], []
    for p in pts:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    for p in reversed(pts):
        while len(hi) >= 2 and cross(hi[-2], hi[-1], p) <= 0:
            hi.pop()
        hi.append(p)
    return lo[:-1] + hi[:-1]

def point_in_convex(p, H):
    """Exact: p in conv(H) (closed), H CCW convex polygon (or degenerate)."""
    m = len(H)
    if m == 0:
        return False
    if m == 1:
        return p == H[0]
    if m == 2:
        (x1, y1), (x2, y2) = H
        return ((x2-x1)*(p[1]-y1) == (y2-y1)*(p[0]-x1)
                and min(x1, x2) <= p[0] <= max(x1, x2)
                and min(y1, y2) <= p[1] <= max(y1, y2))
    # CCW hull: inside iff on left of every edge
    for i in range(m):
        (x1, y1), (x2, y2) = H[i], H[(i+1) % m]
        if (x2-x1)*(p[1]-y1) - (y2-y1)*(p[0]-x1) < 0:
            return False
    return True

def lattice_census(V):
    """(B, I, total) for lattice polygon V (CCW vertices), exact via enumeration."""
    xs = [p[0] for p in V]; ys = [p[1] for p in V]
    n = len(V)
    def onseg(px, py):
        for i in range(n):
            x1, y1 = V[i]; x2, y2 = V[(i+1) % n]
            if ((x2-x1)*(py-y1) == (y2-y1)*(px-x1)
                    and min(x1, x2) <= px <= max(x1, x2)
                    and min(y1, y2) <= py <= max(y1, y2)):
                return True
        return False
    def inside(px, py):
        inn = False
        for i in range(n):
            x1, y1 = V[i]; x2, y2 = V[(i+1) % n]
            if ((y1 > py) != (y2 > py)) and \
               (px < (x2-x1)*(py-y1)/(y2-y1)+x1 if (y2-y1) != 0 else False):
                inn = not inn
        return inn
    B = I = 0
    for px in range(min(xs)-1, max(xs)+2):
        for py in range(min(ys)-1, max(ys)+2):
            if onseg(px, py):
                B += 1
            elif inside(px, py):
                I += 1
    return B, I, B+I

T = [(-3, -2), (-1, -2), (2, 3)]
Q = [(-2, -1), (-1, -1), (1, 0), (1, 2)]

for name, R in [("TRI", T), ("QUAD", Q)]:
    ds = check_fan(R)
    P = anti_polytope(R)
    assert P is not None, f"{name}: not a Fano fan"
    deg = norm_area(P)
    rss = [cone_s(R[i], R[(i+1) % len(R)]) for i in range(len(R))]
    Topts = [T_witness(r, s) for (r, s) in rss]
    assert all(Topts), f"{name}: non-T cone"
    print(f"{name}: rays={R}")
    print(f"  cone dets={ds}, (r,s)={rss}")
    print(f"  T-options (d,n,a)={Topts}")
    print(f"  anticanonical polytope={[(str(x), str(y)) for (x, y) in P]}, degree={deg}")
    assert deg == 5, f"{name}: degree must be 5"

# Chosen Q-Gorenstein data: TRI d=(1,1,5) [Wahl + smooth + A4]; QUAD d=(1,1,2,3).
# rho_smooth = (#rays - 2) + sum(d_i - 1) must equal 5 = rho(dP5).
tri_d = (1, 1, 5); quad_d = (1, 1, 2, 3)
assert 1 + sum(d-1 for d in tri_d) == 5
assert 2 + sum(d-1 for d in quad_d) == 5
# check each chosen d occurs among T-options (n minimal witness)
for (r, s), opts, d in zip([cone_s(T[i], T[(i+1) % 3]) for i in range(3)],
                            [T_witness(*cone_s(T[i], T[(i+1) % 3])) for i in range(3)], tri_d):
    assert any(o[0] == d for o in opts), ((r, s), opts, d)
for (r, s), opts, d in zip([cone_s(Q[i], Q[(i+1) % 4]) for i in range(4)],
                            [T_witness(*cone_s(Q[i], Q[(i+1) % 4])) for i in range(4)], quad_d):
    assert any(o[0] == d for o in opts), ((r, s), opts, d)
print("rank checks: rho_tri=1+0+0+4=5, rho_quad=2+0+0+1+2=5  OK")

# Hulls in H1(L) = Z^2: vertices = fan rays (neck-stretching lemma, see DRAFT.md).
for name, R in [("TRI-hull", T), ("QUAD-hull", Q)]:
    ext = [is_vertex(R, k) for k in range(len(R))]
    A = norm_area(R)
    B, I, tot = lattice_census(R)
    edge_gcds = [math.gcd(abs(R[(i+1) % len(R)][0]-R[i][0]),
                           abs(R[(i+1) % len(R)][1]-R[i][1])) for i in range(len(R))]
    print(f"{name}: extremal={ext}, norm_area={A}, edge_gcds={edge_gcds}, "
          f"B={B}, I={I}, total={tot}")
    assert all(ext), f"{name}: every ray must be a hull vertex"
assert norm_area(T) == 10 and norm_area(Q) == 7
BT, IT, _ = lattice_census(T); BQ, IQ, _ = lattice_census(Q)
assert (BT, IT) == (8, 2) and (BQ, IQ) == (7, 1)
print("OBSTRUCTION: hull areas 10 vs 7; vertices 3 vs 4; (B,I) (8,2) vs (7,1).")
print("No G in GL(2,Z) carries one hull to the other. L_tri, L_quad not Hamiltonian isotopic.")

# Supporting wall-crossing potentials W = sum z^{ray}.
print("W_tri = x^-3.y^-2 + x^-1.y^-2 + x^2.y^3   (3 terms, Newt area 10)")
print("W_quad = x^-2.y^-1 + x^-1.y^-1 + x + x.y^2  (4 terms, Newt area 7)")
print("ALL CHECKS PASSED")
