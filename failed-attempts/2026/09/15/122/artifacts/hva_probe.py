"""HVA degree-2 K3 probe: construct explicit surfaces, test smoothness,
adelic solubility heuristics, rational-point search, Brauer evaluation.
Pure python + sympy. Heuristic/exploratory: labeled as such in WORKLOG.
"""
import itertools, math, random
from fractions import Fraction

import sympy as sp

x, y, z = sp.symbols('x y z')
MONS = [x**2, y**2, z**2, x*y, x*z, y*z]

def quad(coeffs):
    return sum(c*m for c, m in zip(coeffs, MONS))

def det_sextic(coeffs):
    A, B, C, D, E, F = [quad(c) for c in coeffs]
    M = sp.Matrix([[2*A, B, C], [B, 2*D, E], [C, E, 2*F]])
    d = sp.expand(M.det())
    # d should be divisible by 2
    f = sp.expand(-d/2)
    return f, (A, B, C, D, E, F)

def poly_to_int_coeffs(f):
    # return dict monom->int after clearing denominators
    p = sp.Poly(f, x, y, z)
    coeffs = p.as_dict()
    denoms = []
    for c in coeffs.values():
        q = sp.Rational(c)
        denoms.append(q.q)
    L = 1
    for d in denoms:
        L = L*d//math.gcd(L, d)
    out = {k: int(sp.Rational(v)*L) for k, v in coeffs.items()}
    return out, L

def eval_int(coeffdict, X, Y, Z):
    s = 0
    for (i, j, k), c in coeffdict.items():
        s += c*(X**i)*(Y**j)*(Z**k)
    return s

def f_mod_p_zeros(coeffdict, L, p):
    """zeros of L*fscale... careful: f = F_int / L. Evaluate sign/zeros mod p via F_int * L^{-1}."""
    Linv = pow(L, -1, p)
    pts = []
    for (X, Y, Z) in itertools.product(range(p), repeat=3):
        if X == 0 and Y == 0 and Z == 0:
            continue
        # projective: normalize to canonical rep to avoid triplicates
        v = eval_int(coeffdict, X, Y, Z) % p
        pts.append(((X, Y, Z), (v*Linv) % p))
    return pts

def smooth_fp_test(f, p):
    """Check for singular Fp-points of f=0 in P2(Fp). Returns (n_pts, n_sing). Heuristic only."""
    fx, fy, fz = sp.diff(f, x), sp.diff(f, y), sp.diff(f, z)
    fF = sp.Lambdify = None
    # evaluate via Poly
    Pf = sp.Poly(f, x, y, z)
    Px = sp.Poly(fx, x, y, z)
    Py = sp.Poly(fy, x, y, z)
    Pz = sp.Poly(fz, x, y, z)
    def ev(P, X, Y, Z):
        return int(P.eval({x: X, y: Y, z: Z})) % p
    npts = nsing = 0
    reps = set()
    for X, Y, Z in itertools.product(range(p), repeat=3):
        if (X, Y, Z) == (0, 0, 0):
            continue
        # canonical rep: first nonzero coord = 1 scaled... just dedupe by scaling
        # compute normalized tuple
        tup = (X, Y, Z)
        # skip non-canonical (to count projective points once)
        # find first nonzero; require it == 1 up to scale: enforce by scaling inverse
        for c in tup:
            if c % p != 0:
                inv = pow(c, -1, p)
                tup = tuple((t*inv) % p for t in tup)
                break
        if tup in reps:
            continue
        reps.add(tup)
        X, Y, Z = tup
        if ev(Pf, X, Y, Z) == 0:
            npts += 1
            if ev(Px, X, Y, Z) == 0 and ev(Py, X, Y, Z) == 0 and ev(Pz, X, Y, Z) == 0:
                nsing += 1
    return npts, nsing

def groebner_smoothness_check(f):
    """Rigorous smoothness over C: Groebner basis of (f,fx,fy,fz) contains constant."""
    fx, fy, fz = sp.diff(f, x), sp.diff(f, y), sp.diff(f, z)
    try:
        G = sp.groebner([f, fx, fy, fz], x, y, z, order='grlex')
        for g in G.polys:
            if g.is_number:
                return True, "constant in ideal -> smooth"
        return False, f"no constant; basis len {len(G.polys)}"
    except Exception as e:
        return None, f"groebner failed: {e}"

def is_square_frac(q):
    if q < 0:
        return False
    n, d = q.numerator, q.denominator
    rn, rd = math.isqrt(n), math.isqrt(d)
    return rn*rn == n and rd*rd == d

def rational_point_search(f, H=25, Hden=5):
    """Search w^2=f(x,y,z) for rational points with num,den bounded. Returns list."""
    Pf = sp.Poly(f, x, y, z)
    found = []
    # affine charts z=1, y=1, x=1
    charts = [
        ('z=1', lambda a, b: (Fraction(a[0], a[1]), Fraction(b[0], b[1]), Fraction(1))),
    ]
    nums = list(range(-H, H+1))
    dens = list(range(1, Hden+1))
    vals = sorted(set(Fraction(n, d) for n in nums for d in dens))
    for X in vals:
        for Y in vals:
            v = Pf.eval({x: X, y: Y, z: 1})
            if v >= 0 and is_square_frac(v):
                w = sp.sqrt(v)
                found.append((X, Y, 1, v))
                if len(found) >= 8:
                    return found
    return found

def vp_unit(q, p):
    q = Fraction(q)
    n, d = q.numerator, q.denominator
    va = 0
    nn = abs(n)
    while nn % p == 0 and nn > 0:
        nn //= p; va += 1
    vd = 0
    dd = d
    while dd % p == 0:
        dd //= p; vd += 1
    v = va - vd
    u = Fraction(q) / (Fraction(p) ** v)
    return v, u

def legendre_mod(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p-1)//2, p) == 1 else -1

def hilbert_qp(a, b, p):
    """Hilbert symbol (a,b)_p for a,b in Q* (Fractions), p prime or 'inf'. Returns +1/-1."""
    a = Fraction(a); b = Fraction(b)
    if a == 0 or b == 0:
        raise ValueError("degenerate symbol")
    if p == 'inf':
        return -1 if (a < 0 and b < 0) else 1
    va, ua = vp_unit(a, p); vb, ub = vp_unit(b, p)
    def umod(u):
        return (int(u.numerator % p) * pow(int(u.denominator % p), -1, p)) % p
    if p % 2 == 1:
        e = (va*vb*(p-1)//2) % 2
        la = legendre_mod(umod(ua), p)
        lb = legendre_mod(umod(ub), p)
        t = (lb if va % 2 else 1) * (la if vb % 2 else 1)
        return int((-1)**e * t)
    else:
        # p = 2: (a,b)_2 = (-1)^{e(ua)e(ub)+w(ua)vb+w(ub)va}
        def umod8(u):
            return (int(u.numerator % 8) * pow(int(u.denominator % 8), -1, 8)) % 8
        def e2(u):
            return ((umod8(u) - 1)//2) % 2
        def w2(u):
            return ((umod8(u)**2 - 1)//8) % 2
        s = (e2(ua)*e2(ub) + w2(ua)*(vb % 2) + w2(ub)*(va % 2)) % 2
        return -1 if s else 1

def binv(a, b, p):
    h = hilbert_qp(a, b, p)
    return 0 if h == 1 else 1  # in (1/2)Z/Z as 0 or 1 (=1/2)

def eval_alpha_at_point(coeffs_mats, X, Y, Z, W, pplaces=('inf', 3, 5, 7)):
    """Evaluate alpha=(d1,A) at a rational point; d1=B^2-4AD, A quadric. Returns dict place->inv."""
    f, (A, B, C, D, E, F) = det_sextic(coeffs_mats)
    d1 = sp.expand(B**2 - 4*A*D)
    PA = sp.Poly(A, x, y, z); P1 = sp.Poly(d1, x, y, z)
    a = P1.eval({x: Fraction(X), y: Fraction(Y), z: Fraction(Z)})
    b = PA.eval({x: Fraction(X), y: Fraction(Y), z: Fraction(Z)})
    a = Fraction(a); b = Fraction(b)
    out = {}
    if a == 0 or b == 0:
        return None, "point lies on ramification divisor of quaternion representative"
    for p in pplaces:
        out[p] = (binv(a, b, p), a, b)
    return out, f"a={a} b={b}"

if __name__ == '__main__':
    random.seed(20358)
    print("=== HVA probe ===")
    tested = 0
    for trial in range(6):
        coeffs = [[random.randint(-2, 2) for _ in range(6)] for _ in range(6)]
        # avoid degenerate zero quadrics
        if any(all(c == 0 for c in q) for q in coeffs):
            continue
        f, mats = det_sextic(coeffs)
        if f == 0:
            print(f"trial {trial}: det=0 skip"); continue
        tested += 1
        print(f"--- trial {trial}: quads={coeffs}")
        print("f =", f)
        ok, msg = groebner_smoothness_check(f)
        print("smoothness(C):", ok, msg)
        for p in (5, 7, 13):
            npts, ns = smooth_fp_test(f, p)
            print(f"  mod {p}: pts={npts} sing={ns}")
        # real solubility: sample
        Pf = sp.Poly(f, x, y, z)
        pos = sum(1 for (X, Y) in [(i/3, j/3) for i in range(-9, 10) for j in range(-9, 10)]
                  if float(Pf.eval({x: X, y: Y, z: 1})) > 0)
        print("  real sample positive count:", pos, "-> R-points:", bool(pos))
        pts = rational_point_search(f, H=12, Hden=4)
        print(f"  rational pts found (bounded): {len(pts)}", pts[:3])
        if pts:
            X0, Y0, Z0, v = pts[0][0], pts[0][1], pts[0][2], pts[0][3]
            ev, info = eval_alpha_at_point(coeffs, X0, Y0, Z0, v)
            print("  alpha eval:", info, ev)
    print("done, tested =", tested)
