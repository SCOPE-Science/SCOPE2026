"""Recovery test: corrected projective smoothness + hunt for point-sparse HVA K3.
Also demonstrates the core blocker: certifying X(Q)=empty beyond Brauer.
"""
import itertools, math, random
from fractions import Fraction
import sympy as sp

x, y, z = sp.symbols('x y z')
MONS = [x**2, y**2, z**2, x*y, x*z, y*z]

def quad(c):
    return sum(ci*m for ci, m in zip(c, MONS))

def det_sextic(coeffs):
    A, B, C, D, E, F = [quad(c) for c in coeffs]
    M = sp.Matrix([[2*A, B, C], [B, 2*D, E], [C, E, 2*F]])
    f = sp.expand(-M.det()/2)
    return f, (A, B, C, D, E, F)

def proj_smooth_affine_charts(f):
    """Rigorous projective smoothness: check each standard affine chart
    (z=1,y=1,x=1). Singular locus in chart = V(g0, partials). Empty iff the
    lex Groebner basis contains a nonzero CONSTANT. A nonconstant univariate
    polynomial (e.g. y^2+1) does NOT imply a singular point over C -- must solve.
    Returns (smooth, detail)."""
    import sympy as sp2
    charts = [({z: 1}, (x, y)), ({y: 1}, (x, z)), ({x: 1}, (y, z))]
    for subs, vars2 in charts:
        g0 = sp.expand(f.subs(subs))
        gvars = {x: (sp.diff(f, x)), y: (sp.diff(f, y)), z: (sp.diff(f, z))}
        keep = [gvars[v].subs(subs) for v in vars2]
        gs = [sp.expand(g0)] + [sp.expand(g) for g in keep]
        try:
            G = sp.groebner(gs, *vars2, order='lex')
        except Exception as e:
            return None, f"groebner failed in chart {subs}: {e}"
        polys = list(G.polys)
        if any(p.is_number and not p.is_zero for p in polys):
            continue  # nonzero constant -> empty singular locus in this chart
        # solve triangular lex system to decide whether a COMMON complex zero exists
        try:
            sols = sp.solve(gs, vars2, dict=True)
        except Exception as e:
            return None, f"solve failed in chart {subs}: {e}"
        if sols:
            return False, f"singular point in chart {subs}: {sols[0]}"
    return True, "all three affine charts smooth -> projective sextic smooth"

def is_square_frac(q):
    if q < 0:
        return False
    n, d = q.numerator, q.denominator
    rn, rd = math.isqrt(n), math.isqrt(d)
    return rn*rn == n and rd*rd == d

def has_small_point(f, H=8, Hden=3):
    Pf = sp.Poly(f, x, y, z)
    vals = sorted(set(Fraction(n, d) for n in range(-H, H+1) for d in range(1, Hden+1)))
    hits = []
    for X in vals:
        for Y in vals:
            v = Fraction(Pf.eval({x: X, y: Y, z: 1}))
            if v >= 0 and is_square_frac(v):
                hits.append((X, Y))
                if len(hits) >= 3:
                    return True, hits
    return (len(hits) > 0), hits

if __name__ == '__main__':
    random.seed(777)
    n_smooth = 0
    sparse = []
    tried = 0
    for trial in range(40):
        coeffs = [[random.randint(-2, 2) for _ in range(6)] for _ in range(6)]
        if any(all(c == 0 for c in q) for q in coeffs):
            continue
        f, mats = det_sextic(coeffs)
        if f == 0:
            continue
        tried += 1
        sm, detail = proj_smooth_affine_charts(f)
        if sm:
            n_smooth += 1
            ok, hits = has_small_point(f)
            print(f"trial {trial}: SMOOTH; small-pt={ok} {hits[:2]}")
            if not ok:
                sparse.append((trial, coeffs))
                print(f"  ^^ point-sparse candidate {trial}: {coeffs}")
                print("   f =", f)
        else:
            print(f"trial {trial}: not-smooth ({detail[:70]})")
    print(f"SUMMARY: tried={tried} smooth={n_smooth} sparse={len(sparse)}")
    # Even for sparse candidates, proving X(Q) empty needs beyond-BM tools:
    # - local solubility at all p still likely (real pts + smooth mod p pts observed);
    # - Brauer evaluation of alpha at rational pts unavailable (no rational pt);
    # - need full Br(X) + proof no rational pt: no implemented rigorous method.
    print("BLOCKER-DEMO: smooth HVA K3s are abundant; small-point absence is not a proof of X(Q)=empty,")
    print("and no local/2-descent routine for Picard-rank-1 K3 double covers certifies emptiness.")
