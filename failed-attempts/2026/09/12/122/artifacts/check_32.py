"""Explicit 3x2-periodic Kasteleyn characteristic polynomial + genus/obstruction check.

Bipartite square lattice, fundamental domain 3 (x) by 2 (y).
Black sites B[m,n], white sites W[m,n], m in 0..2, n in 0..1.
Edges with generic positive weights:
  east  B[m,n]-W[m+1,n] weight H[m,n]
  west  B[m,n]-W[m-1,n] weight H[m-1,n]  (same edge, other endpoint)
  north B[m,n]-W[m,n+1] weight V[m,n]
  south B[m,n]-W[m,n-1] weight V[m,n-1]
Kasteleyn signs: +E,+N,-W,-S (standard), magnetic twists z (x-cycle), w (y-cycle).
K is 6x6. P(z,w) = det K(z,w), a Laurent polynomial.
We extract monomials, Newton polygon, interior lattice points (= genus of smooth model),
and compare uniform weights (reducible, genus 0/nodal) vs generic perturbation (genus 2).
"""
import itertools, json
import numpy as np
import sympy as sp

MX, MY = 3, 2
def idx(m, n):
    return (m % MX) * MY + (n % MY)

def build_K(H, V):
    z, w = sp.symbols('z w')
    N = MX * MY
    K = sp.zeros(N, N)
    for m in range(MX):
        for n in range(MY):
            r = idx(m, n)
            # east: B[m,n] -> W[m+1,n]
            c = idx(m + 1, n)
            ph = z if m == MX - 1 else 1   # crossing x-boundary
            K[r, c] += H[m, n] * ph
            # west: B[m,n] -> W[m-1,n] (same undirected edge family H[m-1,n])
            c = idx(m - 1, n)
            ph = 1 / z if m == 0 else 1
            K[r, c] += -H[(m - 1) % MX, n] * ph
            # north: B[m,n] -> W[m,n+1]
            c = idx(m, n + 1)
            ph = w if n == MY - 1 else 1
            K[r, c] += V[m, n] * ph * sp.I  # Kasteleyn phase on vertical
            # south: B[m,n] -> W[m,n-1]
            c = idx(m, n - 1)
            ph = 1 / w if n == 0 else 1
            K[r, c] += -V[m, (n - 1) % MY] * ph * sp.I
    return K, z, w

def laurent_monomials(det_expr, z, w):
    # multiply by z^a w^b to clear denominators, then read Poly
    det_expr = sp.expand(det_expr)
    # find min powers by sampling: convert via x=1/z substitution is messy; instead
    # multiply by z^6 w^6 (safe upper bound) then shift down
    Z = sp.Symbol('Z')
    W = sp.Symbol('W')
    e = sp.expand(det_expr.subs({z: Z, w: W}))
    # clear denominators: multiply by Z^6*W^6
    e2 = sp.expand(e * Z**6 * W**6)
    poly = sp.Poly(e2, Z, W)
    terms = {}
    for mon, coeff in poly.as_dict().items():
        if coeff != 0:
            terms[(mon[0] - 6, mon[1] - 6)] = complex(coeff)
    return terms

def newton_genus(terms):
    pts = list(terms.keys())
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    # bounding box lattice-point interior count via Pick on convex hull
    # convex hull (monotone chain)
    P = sorted(set(pts))
    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lower, upper = [], []
    for p in P:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(P):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    hull = lower[:-1] + upper[:-1]
    import math
    # area (shoelace)
    A = 0
    for i in range(len(hull)):
        x1, y1 = hull[i]; x2, y2 = hull[(i+1) % len(hull)]
        A += x1*y2 - x2*y1
    A = abs(A) / 2
    # boundary lattice points
    B = 0
    for i in range(len(hull)):
        x1, y1 = hull[i]; x2, y2 = hull[(i+1) % len(hull)]
        B += math.gcd(abs(x2-x1), abs(y2-y1))
    I = int(round(A - B/2 + 1))  # Pick's theorem
    return hull, A, B, I

rng = np.random.default_rng(1422)
H_gen = { (m,n): float(0.5 + rng.random()*2.0) for m in range(MX) for n in range(MY)}
V_gen = { (m,n): float(0.5 + rng.random()*2.0) for m in range(MX) for n in range(MY)}
H_uni = { (m,n): 1.0 for m in range(MX) for n in range(MY)}
V_uni = { (m,n): 1.0 for m in range(MX) for n in range(MY)}

out = {"weights_generic": {"H": {str(k): v for k,v in H_gen.items()},
                            "V": {str(k): v for k,v in V_gen.items()}}}
for tag, H, V in [("uniform", H_uni, V_uni), ("generic", H_gen, V_gen)]:
    K, z, w = build_K(H, V)
    d = sp.factor(K.det())
    terms = laurent_monomials(d, z, w)
    hull, A, B, I = newton_genus(terms)
    # evaluate P on unit torus: check Harnack real-root structure / zeros
    f = sp.lambdify((z, w), K.det(), modules="numpy")
    th = np.linspace(0, 2*np.pi, 181)
    Z = np.exp(1j*th); W = np.exp(1j*th)
    ZZ, WW = np.meshgrid(Z, W)
    Pv = f(ZZ, WW)
    out[tag] = {
        "monomials": {str(k): [v.real, v.imag] for k,v in terms.items()},
        "n_terms": len(terms),
        "hull": hull, "area": A, "boundary_pts": B, "interior_pts_genus": I,
        "max_abs_on_torus": float(np.max(np.abs(Pv))),
        "min_abs_on_torus": float(np.min(np.abs(Pv))),
    }

# Discriminant-in-z test at w=1: number of distinct z-roots (branch-point nondegeneracy proxy)
for tag, H, V in [("uniform", H_uni, V_uni), ("generic", H_gen, V_gen)]:
    K, z, w = build_K(H, V)
    p = sp.Poly(sp.expand(K.det().subs(w, 1) * z**6), z)
    roots = np.roots(np.array(p.all_coeffs(), dtype=complex))
    # count distinct (tol 1e-6) and min separation
    sep = min(abs(a-b) for a,b in itertools.combinations(roots, 2))
    out[tag]["z_roots_at_w1"] = [[float(x.real), float(x.imag)] for x in roots]
    out[tag]["min_root_separation"] = float(sep)

with open("output/artifacts/check_32_result.json", "w") as f:
    json.dump(out, f, indent=1)
print(json.dumps({k: ({kk: vv for kk, vv in v.items() if kk != 'monomials' and kk != 'z_roots_at_w1'} if isinstance(v, dict) else v) for k,v in out.items()}, indent=1))
print("generic monomials:", sorted(out["generic"]["monomials"].keys()))
print("uniform monomials:", sorted(out["uniform"]["monomials"].keys()))
