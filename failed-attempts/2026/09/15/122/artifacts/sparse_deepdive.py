"""Deep dive on sparse candidates: wider point search, full local-solubility sieve
(mod p^k lifting sketch), alpha-invariant scan, Picard-rank signal.
Goal: turn a sparse candidate into a rigorous X(Q)=empty + BM-survival claim,
or document exactly why it fails.
"""
import itertools, math
from fractions import Fraction
import sympy as sp

x, y, z = sp.symbols('x y z')
MONS = [x**2, y**2, z**2, x*y, x*z, y*z]

CANDS = {
 13: [[1, -2, -2, 1, 2, -1], [0, -2, 1, -1, 0, 1], [1, 0, -2, 1, 1, -2], [-2, -1, 2, 2, 2, 2], [0, -1, 1, 1, 0, -1], [2, -2, 2, -1, 1, 2]],
 35: [[-2, -2, -2, 0, -1, 0], [-1, 2, -2, 0, 0, -1], [0, 1, 1, 2, -2, 2], [0, 0, -1, -1, -2, -1], [1, 1, -2, -2, -1, 1], [0, -2, -1, -2, 0, -1]],
 36: [[-1, -1, 1, 2, -1, 2], [0, -1, 2, 0, -2, 2], [2, -1, 2, -1, -1, 2], [-2, 2, 2, -2, 2, 2], [1, 1, 1, -2, 2, -1], [-1, -1, -2, 1, 2, 1]],
 37: [[2, -1, -2, 0, 1, 1], [-1, -2, -2, -2, 0, 1], [-2, 1, 2, 1, 2, 2], [1, -2, 1, 0, -2, -1], [2, 2, 0, -2, 0, -2], [1, -2, -2, 1, 0, -2]],
 38: [[-2, -1, -1, 0, 0, -1], [-2, 2, -2, -1, 0, -1], [-1, -1, -2, -1, -1, -2], [-2, 0, 1, -2, 2, -1], [2, 2, -1, 2, 2, 2], [-2, 1, -1, -1, 1, 1]],
}

def quad(c):
    return sum(ci*m for ci, m in zip(c, MONS))

def det_sextic(coeffs):
    A, B, C, D, E, F = [quad(c) for c in coeffs]
    M = sp.Matrix([[2*A, B, C], [B, 2*D, E], [C, E, 2*F]])
    f = sp.expand(-M.det()/2)
    return f, (A, B, C, D, E, F)

def is_square_frac(q):
    if q < 0:
        return False
    n, d = q.numerator, q.denominator
    rn, rd = math.isqrt(n), math.isqrt(d)
    return rn*rn == n and rd*rd == d

def wide_search(f, H=60, Hden=12):
    Pf = sp.Poly(f, x, y, z)
    vals = sorted(set(Fraction(n, d) for n in range(-H, H+1) for d in range(1, Hden+1)))
    hits = []
    for X in vals:
        for Y in vals:
            v = Fraction(Pf.eval({x: X, y: Y, z: 1}))
            if v >= 0 and is_square_frac(v):
                hits.append((X, Y, v))
                if len(hits) >= 5:
                    return hits
    return hits

def fp_points_and_smooth_lift(f, p):
    Pf = sp.Poly(f, x, y, z)
    def ev(X, Y, Z):
        return int(Pf.eval({x: X, y: Y, z: Z})) % p
    reps = set(); pts = []
    for X, Y, Z in itertools.product(range(p), repeat=3):
        if (X, Y, Z) == (0, 0, 0):
            continue
        for c in (X, Y, Z):
            if c % p != 0:
                inv = pow(c, -1, p)
                t = tuple((u*inv) % p for u in (X, Y, Z))
                break
        if t in reps:
            continue
        reps.add(t)
        if ev(*t) == 0:
            pts.append(t)
    # smoothness: partials
    fx, fy, fz = sp.diff(f, x), sp.diff(f, y), sp.diff(f, z)
    Px, Py, Pz = sp.Poly(fx, x, y, z), sp.Poly(fy, x, y, z), sp.Poly(fz, x, y, z)
    smooth = []
    for t in pts:
        dx = int(Px.eval({x: t[0], y: t[1], z: t[2]})) % p
        dy = int(Py.eval({x: t[0], y: t[1], z: t[2]})) % p
        dz = int(Pz.eval({x: t[0], y: t[1], z: t[2]})) % p
        smooth.append((t, not (dx == dy == dz == 0)))
    return smooth

if __name__ == '__main__':
    for key, coeffs in CANDS.items():
        f, mats = det_sextic(coeffs)
        print(f"===== candidate {key} =====")
        hits = wide_search(f)
        print(f"  wide search (H=60,Hden=12, z=1 chart): {len(hits)} hits {hits[:3]}")
        # local solubility signals
        Pf = sp.Poly(f, x, y, z)
        pos = sum(1 for (X, Y) in [(i/4, j/4) for i in range(-12, 13) for j in range(-12, 13)]
                  if float(Pf.eval({x: X, y: Y, z: 1})) > 0)
        print(f"  real positive samples: {pos} -> R-pts likely: {bool(pos)}")
        for p in (3, 5, 7, 11):
            sm = fp_points_and_smooth_lift(f, p)
            ns = sum(1 for _, s in sm if s)
            print(f"  mod {p}: branch pts={len(sm)} smooth-liftable={ns}")
        # ramification check for alpha representative
        A, B, C, D, E, Fm = mats
        d1 = sp.expand(B**2 - 4*A*D)
        print(f"  deg d1={sp.Poly(d1, x, y, z).total_degree()} (expect 4), A nonzero: {A != 0}")
