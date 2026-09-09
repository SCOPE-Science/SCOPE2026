"""Exact Nill-criterion audit over a committed panel of reflexive 3-polytopes.

Stdlib only (fractions.Fraction). For each committed vertex set:
  - exact facet enumeration via supporting triples,
  - reflexivity certificate (all facet levels == 1, unique interior lattice point 0),
  - lattice-point census, Demazure roots (= facet relative-interior lattice points),
  - semisimple/unipotent split, reductive verdict (Nill Prop 2.2),
  - exact rational polytope barycenter via origin-fan determinant triangulation
    with independent fan-from-vertex cross-check; dual-polytope barycenter likewise.

Run: python3 verify_panel.py
Exits nonzero on any failed certificate. Prints summary table + witness lines.
"""
from fractions import Fraction
from math import gcd, atan2
import sys

def sub(a, b): return (a[0]-b[0], a[1]-b[1], a[2]-b[2])
def dot(a, b): return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
def cross(a, b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def det3(a, b, c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1]) - a[1]*(b[0]*c[2]-b[2]*c[0])
            + a[2]*(b[0]*c[1]-b[1]*c[0]))

def facets_of(V):
    """Return sorted list of outward (n, L): dot(n,x)<=L on V, n primitive int."""
    planes = {}
    n = len(V)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                cr = cross(sub(V[j], V[i]), sub(V[k], V[i]))
                if cr == (0, 0, 0):
                    continue
                g = gcd(gcd(abs(cr[0]), abs(cr[1])), abs(cr[2]))
                np_ = (cr[0]//g, cr[1]//g, cr[2]//g)
                L = dot(np_, V[i])
                ds = [dot(np_, v) for v in V]
                if all(d <= L for d in ds):
                    key = (np_, L)
                elif all(d >= L for d in ds):
                    key = ((-np_[0], -np_[1], -np_[2]), -L)
                else:
                    continue
                planes[key] = True
    return sorted(planes.keys())

def lattice_points(V, facets):
    lo = [min(v[i] for v in V) for i in range(3)]
    hi = [max(v[i] for v in V) for i in range(3)]
    pts = []
    for x in range(lo[0], hi[0]+1):
        for y in range(lo[1], hi[1]+1):
            for z in range(lo[2], hi[2]+1):
                p = (x, y, z)
                if all(dot(n, p) <= L for (n, L) in facets):
                    pts.append(p)
    return pts

def order_facet_verts(fv, n):
    """Cyclic order of coplanar verts via angle sort (floats for order only)."""
    cx = Fraction(sum(v[0] for v in fv), len(fv))
    cy = Fraction(sum(v[1] for v in fv), len(fv))
    cz = Fraction(sum(v[2] for v in fv), len(fv))
    u = (Fraction(fv[0][0])-cx, Fraction(fv[0][1])-cy, Fraction(fv[0][2])-cz)
    w = cross(n, (float(u[0]), float(u[1]), float(u[2])))
    def ang(v):
        d = (float(Fraction(v[0])-cx), float(Fraction(v[1])-cy), float(Fraction(v[2])-cz))
        return atan2(d[0]*w[0]+d[1]*w[1]+d[2]*w[2],
                     d[0]*float(u[0])+d[1]*float(u[1])+d[2]*float(u[2]))
    return sorted(fv, key=ang)

def barycenter(apex, facets, V):
    """Exact centroid via fan triangulation from apex. Returns (bary, vol6)."""
    num = [Fraction(0), Fraction(0), Fraction(0)]
    den = Fraction(0)
    for (n, L) in facets:
        fv = [v for v in V if dot(n, v) == L]
        if apex in fv:
            continue
        if len(fv) < 3:
            raise AssertionError("degenerate facet")
        fo = order_facet_verts(fv, n)
        for i in range(1, len(fo)-1):
            t = (fo[0], fo[i], fo[i+1])
            d = det3(sub(t[0], apex), sub(t[1], apex), sub(t[2], apex))
            vol = Fraction(abs(d), 6)
            if vol == 0:
                continue
            for k in range(3):
                num[k] += vol * (Fraction(apex[k]) + Fraction(t[0][k])
                                 + Fraction(t[1][k]) + Fraction(t[2][k])) / 4
            den += vol
    if den == 0:
        raise AssertionError("zero volume")
    return ([num[k]/den for k in range(3)], den)

FAIL = []
def check(name, cond, msg):
    print(("PASS " if cond else "FAIL ") + name + ": " + msg)
    if not cond:
        FAIL.append(name)

# ---------------- committed panel (vertex lists frozen) ----------------
E1 = [1, 0, 0]
PANEL = {
    "cube": [(x, y, z) for x in (-1, 1) for y in (-1, 1) for z in (-1, 1)],
    "octahedron": [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)],
    "E3": [(1,0,0),(0,1,0),(0,0,1),(-1,-1,-1)],
    "E3star": [(-1,-1,-1),(3,-1,-1),(-1,3,-1),(-1,-1,3)],
    "W_nill": [(1,0,0),(1,3,0),(1,0,3),(-5,-6,-3)],
    "prismQ": [(t, q[0], q[1]) for t in (-1, 1)
               for q in ((1,0),(0,1),(-1,-1),(0,-1))],
    "prismH": [(t, q[0], q[1]) for t in (-1, 1)
               for q in ((1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1))],
}

results = {}
for name, V in PANEL.items():
    F = facets_of(V)
    check(name+".facets_nonempty", len(F) >= 4, "nfacets=%d" % len(F))
    reflexive = all(L == 1 for (_, L) in F)
    check(name+".reflexive_levels", reflexive,
          "levels=%s" % sorted(set(L for (_, L) in F)))
    pts = lattice_points(V, F)
    interior = [p for p in pts
                if all(dot(n, p) < L for (n, L) in F)]
    check(name+".unique_interior_origin", interior == [(0,0,0)],
          "interior=%s nlat=%d" % (interior, len(pts)))
    # roots: boundary points on exactly one facet
    roots = []
    for p in pts:
        on = [i for i, (n, L) in enumerate(F) if dot(n, p) == L]
        if len(on) == 1:
            roots.append((p, on[0]))
    R = [p for (p, _) in roots]
    S = [p for p in R if (-p[0], -p[1], -p[2]) in R]
    U = [p for p in R if (-p[0], -p[1], -p[2]) not in R]
    reductive = len(U) == 0
    dimaut = len(R) + 3
    # barycenter, two independent fans
    b1, v1 = barycenter((0,0,0), F, V)
    b2, v2 = barycenter(V[0], F, V)
    check(name+".bary_fan_agree", b1 == b2 and v1 == v2,
          "b=%s vol6=%s" % ([str(x) for x in b1], v1))
    # dual polytope audit
    DV = sorted(set(n for (n, _) in F))
    check(name+".dual_integral", all(isinstance(c, int) for v in DV for c in v),
          "ndualverts=%d" % len(DV))
    DF = facets_of(DV)
    dreflex = all(L == 1 for (_, L) in DF)
    check(name+".dual_reflexive", dreflex, "dual nfacets=%d" % len(DF))
    dpts = lattice_points(DV, DF)
    dint = [p for p in dpts if all(dot(n, p) < L for (n, L) in DF)]
    check(name+".dual_interior", dint == [(0,0,0)], "dual nlat=%d" % len(dpts))
    db1, dv1 = barycenter((0,0,0), DF, DV)
    db2, dv2 = barycenter(DV[0], DF, DV)
    check(name+".dual_bary_agree", db1 == db2 and dv1 == dv2,
          "bstar=%s" % [str(x) for x in db1])
    bzero = all(x == 0 for x in b1)
    results[name] = dict(nfac=len(F), nlat=len(pts), vol6=v1, R=len(R),
                         S=len(S), U=len(U), red=reductive, dim=dimaut,
                         bary=b1, bstar=db1, bzero=bzero,
                         dual_nlat=len(dpts), dual_vol6=dv1)
    print("  -> %s: facets=%d lat=%d vol6=%s |R|=%d |S|=%d |U|=%d %s dim=%d b=%s b*=%s" % (
        name, len(F), len(pts), v1, len(R), len(S), len(U),
        "RED" if reductive else "NONRED", dimaut,
        [str(x) for x in b1], [str(x) for x in db1]))

print("\n== Nill cross-checks ==")
c = results
check("nill-ex216", c["W_nill"]["S"] == 4 and c["W_nill"]["U"] == 6
      and not c["W_nill"]["red"], "W: |S|=4 |U|=6 non-reductive reproduced")
check("p3-extremal", c["E3star"]["dim"] == 15 and c["E3star"]["red"],
      "E3*: dim Aut = 15 = d^2+2d sharp (Thm 2.21)")
check("cube-facet-bound", c["cube"]["R"] <= 12 and len(
    set(n for (n, _) in facets_of(PANEL["cube"]))) == 6,
    "|R|=%d <= 12, 6 facets (Cor 3.3: <=2d=6 root facets)" % c["cube"]["R"])
check("sharp-not-necessary", (not c["prismQ"]["bzero"]) and c["prismQ"]["red"],
      "prismQ: b!=0 (%s) yet reductive, |R|=%d dim=%d" % (
          [str(x) for x in c["prismQ"]["bary"]], c["prismQ"]["R"], c["prismQ"]["dim"]))
check("sufficient-bites", (not c["W_nill"]["bzero"]) and not c["W_nill"]["red"],
      "W: b!=0 and non-reductive")
check("suff-confirmed", all(c[k]["red"] for k in PANEL if c[k]["bzero"]),
      "every b=0 panel member reductive (Thm 4.2(2)(i) instances)")

if FAIL:
    print("\nFAILURES: %s" % FAIL)
    sys.exit(1)
print("\nALL VERIFY_OK")
