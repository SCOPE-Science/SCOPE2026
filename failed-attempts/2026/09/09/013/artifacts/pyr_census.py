"""De novo pyramid census: Pyr(Q,h) over lattice triangles/quads in [0,3]^2, h=1..4.
Route A: slice-scaling exact Ehrhart enumeration (all-integer arithmetic).
Writes output/artifacts/census.json and prints summary.
Stdlib only.
"""
import json, math, itertools, time, os

BOX = 3
HEIGHTS = [1, 2, 3, 4]
TMAX = 6
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "census.json")

PTS = [(x, y) for x in range(BOX + 1) for y in range(BOX + 1)]

def cross2(a, b):
    return a[0] * b[1] - a[1] * b[0]

def hull2(points):
    pts = sorted(set(points))
    if len(pts) <= 1:
        return list(pts)
    def cr(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lo = []
    for p in pts:
        while len(lo) >= 2 and cr(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    hi = []
    for p in reversed(pts):
        while len(hi) >= 2 and cr(hi[-2], hi[-1], p) <= 0:
            hi.pop()
        hi.append(p)
    return lo[:-1] + hi[:-1]

def signed_area2(Q):
    s = 0
    n = len(Q)
    for i in range(n):
        x1, y1 = Q[i]
        x2, y2 = Q[(i + 1) % n]
        s += x1 * y2 - x2 * y1
    return s

def ccw(Q):
    Q = list(Q)
    if signed_area2(Q) < 0:
        Q = [Q[0]] + Q[:0:-1]
    return Q

def poly_invariants(Q):
    Q = ccw(Q)
    a2 = abs(signed_area2(Q))
    b = 0
    n = len(Q)
    for i in range(n):
        dx = abs(Q[(i + 1) % n][0] - Q[i][0])
        dy = abs(Q[(i + 1) % n][1] - Q[i][1])
        b += math.gcd(dx, dy)
    i_int = (a2 - b + 2) // 2
    assert (a2 - b + 2) % 2 == 0 and i_int >= 0
    return {"area2": a2, "b": b, "i": i_int, "Q": Q}

def translate_canon(V):
    mx = min(p[0] for p in V)
    my = min(p[1] for p in V)
    return frozenset((p[0] - mx, p[1] - my) for p in V)

def det2_cols(p, q):
    return p[0] * q[1] - p[1] * q[0]

def mat_apply(U, p):
    return (U[0][0] * p[0] + U[0][1] * p[1], U[1][0] * p[0] + U[1][1] * p[1])

def gl2_equiv(A, B):
    """Exact GL(2,Z)+translation equivalence of finite lattice point sets."""
    A = list(A)
    B = list(B)
    if len(A) != len(B):
        return False
    n = len(A)
    Bset_all = set(B)
    for a0 in A:
        Ap = [(p[0] - a0[0], p[1] - a0[1]) for p in A]
        for b0 in B:
            Bp = [(p[0] - b0[0], p[1] - b0[1]) for p in B]
            Bs = set(Bp)
            nzA = [v for v in Ap if v != (0, 0)]
            nzB = [v for v in Bp if v != (0, 0)]
            for P1, P2 in itertools.permutations(nzA, 2):
                dA = det2_cols(P1, P2)
                if dA == 0:
                    continue
                for R1, R2 in itertools.permutations(nzB, 2):
                    dR = det2_cols(R1, R2)
                    if dR == 0 or abs(dR) != abs(dA):
                        continue
                    # U [P1 P2] = [R1 R2] -> U = [R1 R2] adj([P1 P2]) / dA
                    a, b_ = P1[0], P2[0]
                    c, d = P1[1], P2[1]
                    # adj(P) = [[d,-b],[-c,a]]
                    U11 = (R1[0] * d - R2[0] * c)
                    U12 = (-R1[0] * b_ + R2[0] * a)
                    U21 = (R1[1] * d - R2[1] * c)
                    U22 = (-R1[1] * b_ + R2[1] * a)
                    if U11 % dA or U12 % dA or U21 % dA or U22 % dA:
                        continue
                    U = ((U11 // dA, U12 // dA), (U21 // dA, U22 // dA))
                    if abs(U[0][0] * U[1][1] - U[0][1] * U[1][0]) != 1:
                        continue
                    if all(mat_apply(U, v) in Bs for v in Ap):
                        return True
    return False

# ---- 1. enumerate translation types of convex lattice tri/quads in box ----
tri_reps = {}
quad_reps = {}
for comb in itertools.combinations(PTS, 3):
    H = hull2(comb)
    if len(H) == 3:
        key = translate_canon(H)
        if key not in tri_reps:
            tri_reps[key] = H
for comb in itertools.combinations(PTS, 4):
    H = hull2(comb)
    if len(H) == 4:
        key = translate_canon(H)
        if key not in quad_reps:
            quad_reps[key] = H

tri_keys = tri_reps
quad_keys = quad_reps
all_types = [("tri", tri_reps[k]) for k in tri_reps] + [("quad", quad_reps[k]) for k in quad_reps]

# ---- 2. GL(2,Z) dedup for the generation log ----
reps = []  # (kind, vertexset)
for kind, V in all_types:
    Vs = set(map(tuple, V))
    found = None
    for (rk, rv) in reps:
        if rk == kind and gl2_equiv(Vs, rv):
            found = rk
            break
    if found is None:
        reps.append((kind, Vs))

# ---- 3. Ehrhart via slice scaling (all integer) ----
def ehrhart_pyr(Q, h, tmax=TMAX):
    E = [(Q[i], Q[(i + 1) % len(Q)]) for i in range(len(Q))]
    L = []
    for t in range(tmax + 1):
        c = 0
        for z in range(t * h + 1):
            k = t * h - z
            if k == 0:
                c += 1
                continue
            m = (3 * k + h - 1) // h
            for x in range(m + 1):
                hx = h * x
                for y in range(m + 1):
                    hy = h * y
                    ok = True
                    for (a, b) in E:
                        ex = b[0] - a[0]
                        ey = b[1] - a[1]
                        vx = hx - k * a[0]
                        vy = hy - k * a[1]
                        if ex * vy - ey * vx < 0:
                            ok = False
                            break
                    if ok:
                        c += 1
        L.append(c)
    return L

def C2(n):
    return n * (n - 1) * (n - 2) // 6 if n >= 3 else 0

def hstar(L):
    h0 = L[0]
    h1 = L[1] - 4 * h0
    h2 = L[2] - 10 * h0 - 4 * h1
    h3 = L[3] - 20 * h0 - 10 * h1 - 4 * h2
    return [h0, h1, h2, h3]

def Lpred(hs, t):
    return hs[0] * (t + 3) * (t + 2) * (t + 1) // 6 + hs[1] * C2(t + 2) + hs[2] * C2(t + 1) + hs[3] * C2(t)

# ---- 4. lattice width with certified direction bound ----
def det3(M):
    a, b, c = M[0], M[1], M[2]
    return (a[0] * (b[1] * c[2] - b[2] * c[1]) - a[1] * (b[0] * c[2] - b[2] * c[0])
            + a[2] * (b[0] * c[1] - b[1] * c[0]))

def adj3(M):
    (a1, a2, a3), (b1, b2, b3), (c1, c2, c3) = M
    C = [[(b2 * c3 - b3 * c2), -(b1 * c3 - b3 * c1), (b1 * c2 - b2 * c1)],
         [-(a2 * c3 - a3 * c2), (a1 * c3 - a3 * c1), -(a1 * c2 - a2 * c1)],
         [(a2 * b3 - a3 * b2), -(a1 * b3 - a3 * b1), (a1 * b2 - a2 * b1)]]
    return [[C[0][0], C[1][0], C[2][0]],
            [C[0][1], C[1][1], C[2][1]],
            [C[0][2], C[1][2], C[2][2]]]

def lattice_width(V):
    spans = [max(v[i] for v in V) - min(v[i] for v in V) for i in range(3)]
    W0 = min(spans)
    D = [(V[i][0] - V[0][0], V[i][1] - V[0][1], V[i][2] - V[0][2]) for i in range(1, len(V))]
    M = None
    for tri in itertools.combinations(D, 3):
        if det3(tri) != 0:
            M = [list(r) for r in tri]
            break
    assert M is not None, "pyramid must be full-dimensional"
    det = det3(M)
    A = adj3(M)
    rownorm = max(sum(abs(A[i][j]) for j in range(3)) for i in range(3))
    from math import ceil
    B = ceil(rownorm / abs(det) * W0)
    best = None
    bestu = None
    R = range(-B, B + 1)
    dots = {}
    for u1 in R:
        for u2 in R:
            for u3 in R:
                if u1 == 0 and u2 == 0 and u3 == 0:
                    continue
                if math.gcd(math.gcd(abs(u1), abs(u2)), abs(u3)) != 1:
                    continue
                vals = [u1 * v[0] + u2 * v[1] + u3 * v[2] for v in V]
                w = max(vals) - min(vals)
                if best is None or w < best:
                    best = w
                    bestu = (u1, u2, u3)
    assert best is not None and best <= W0
    return {"width": best, "witness": list(bestu), "W0": W0, "B": B}

t0 = time.time()
results = []
class_of = {}
for idx, (rk, rv) in enumerate(reps):
    class_of[(rk, tuple(sorted(rv)))] = idx

# map each translation type to a GL class id (recompute equivalence cheaply)
typeclass = []
for kind, V in all_types:
    Vs = set(map(tuple, V))
    for idx, (rk, rv) in enumerate(reps):
        if rk == kind and gl2_equiv(Vs, rv):
            typeclass.append(idx)
            break

n_dip = 0
for ti, (kind, V) in enumerate(all_types):
    inv = poly_invariants(list(map(tuple, V)))
    Q = inv["Q"]
    for h in HEIGHTS:
        L = ehrhart_pyr(Q, h)
        hs = hstar(L)
        assert L[0] == 1 and hs[0] == 1
        assert all(v >= 0 for v in hs), (Q, h, L, hs)
        assert sum(hs) == h * inv["area2"], (Q, h, L, hs, "volume identity")
        for t in range(4, TMAX + 1):
            assert Lpred(hs, t) == L[t], (Q, h, t, "Ehrhart cross-check")
        P = [(x, y, 0) for (x, y) in Q] + [(0, 0, h)]
        w = lattice_width(P)
        dip = hs[1] - hs[2]
        if dip > 0:
            n_dip += 1
        results.append({
            "Q": Q, "kind": kind, "i": inv["i"], "b": inv["b"], "area2": inv["area2"],
            "h": h, "L": L, "hstar": hs, "dip": dip,
            "width": w["width"], "width_dir": w["witness"], "width_B": w["B"],
            "gl_class": typeclass[ti],
        })

results.sort(key=lambda r: (-r["dip"], r["h"], r["i"]))
best = results[0]
runner = results[1]
gap = best["dip"] - runner["dip"]
el = time.time() - t0

out = {
    "window": {"box": [0, BOX], "kinds": ["tri", "quad"], "heights": HEIGHTS,
               "tmax": TMAX, "note": "Q translated min-corner-to-origin; every convex lattice tri/quad in box is translation-equivalent to exactly one census Q; pyramid classes cover all placements up to horizontal translation"},
    "generation": {"n_trisubsets": len(list(itertools.combinations(range(3), 3))),
                   "n_translation_types_tri": len(tri_keys),
                   "n_translation_types_quad": len(quad_keys),
                   "n_gl_classes_tri": sum(1 for r in reps if r[0] == "tri"),
                   "n_gl_classes_quad": sum(1 for r in reps if r[0] == "quad"),
                   "n_pyramids": len(results),
                   "n_dips_h1_gt_h2": n_dip,
                   "seconds": round(el, 2)},
    "extremal": best,
    "runner_up": runner,
    "runner_gap": gap,
    "results": results,
}
with open(OUT, "w") as f:
    json.dump(out, f)

print("types tri/quad:", len(tri_keys), len(quad_keys))
print("GL classes tri/quad:", sum(1 for r in reps if r[0] == "tri"), sum(1 for r in reps if r[0] == "quad"))
print("pyramids:", len(results), "dips(h1>h2):", n_dip, "time: %.1fs" % el)
print("EXTREMAL Q=%s h=%s h*=%s dip=%s width=%s dir=%s L=%s" % (
    best["Q"], best["h"], best["hstar"], best["dip"], best["width"], best["width_dir"], best["L"]))
print("RUNNER   Q=%s h=%s h*=%s dip=%s width=%s dir=%s L=%s" % (
    runner["Q"], runner["h"], runner["hstar"], runner["dip"], runner["width"], runner["width_dir"], runner["L"]))
print("gap:", gap)
# unimodality audit of extremal + any dips
def unimodal(hs):
    n = len(hs)
    for k in range(n):
        if all(hs[j] <= hs[j + 1] for j in range(k)) and all(hs[j] >= hs[j + 1] for j in range(k, n - 1)):
            return True, k
    return False, None
print("extremal unimodal:", unimodal(best["hstar"]))
for r in results:
    if r["dip"] > 0:
        print("DIP Q=%s h=%s h*=%s unimodal=%s" % (r["Q"], r["h"], r["hstar"], unimodal(r["hstar"])))
# distribution of dips
from collections import Counter
print("dip histogram:", sorted(Counter(r["dip"] for r in results).items()))
print("min dip:", min(r["dip"] for r in results))
