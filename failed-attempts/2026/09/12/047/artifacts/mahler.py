#!/usr/bin/env python3
"""Volume-product computations for 4-polytopes with <=8 vertices (numpy only).
General-position pipeline (deterministic jitter): facet enumeration via 4-subsets,
fan volume/centroid from vertex 0, polar via 4x4 constraint solves, Hausdorff
upper bounds via Frank-Wolfe point-polytope distances.
"""
import numpy as np, itertools, math, json

TOL = 1e-9

def jitter(P, s=1e-7, seed=0):
    rng = np.random.default_rng(seed)
    sc = float(np.abs(P).max()) or 1.0
    return P + rng.normal(0, s * sc, P.shape)

def facets_simplicial(P):
    """P (m,4) general position. Return list of facet index-tuples (4 each)."""
    m = len(P)
    F = []
    for combo in itertools.combinations(range(m), 4):
        C = list(combo)
        A = P[C]
        c = A.mean(axis=0)
        _, _, Vt = np.linalg.svd(A - c)
        n = Vt[-1]
        s = (P - c) @ n
        if np.all(s <= 1e-7) or np.all(s >= -1e-7):
            F.append(tuple(C))
    return F

def fan_vol_centroid(P, F):
    p0 = P[0]
    V = 0.0
    C = np.zeros(4)
    for f in F:
        if 0 in f:
            continue
        M = np.stack([P[i] - p0 for i in f])
        d = abs(float(np.linalg.det(M)))
        V += d
        C += d * (p0 + sum(P[i] for i in f)) / 5.0
    V /= 24.0
    C /= (24.0 * V)
    return V, C

def polar_vertices(W):
    """W (m,4): polytope containing origin interior. Vertices of polar."""
    m = len(W)
    out = []
    for combo in itertools.combinations(range(m), 4):
        A = W[list(combo)]
        if abs(float(np.linalg.det(A))) < 1e-12:
            continue
        try:
            y = np.linalg.solve(A, np.ones(4))
        except np.linalg.LinAlgError:
            continue
        if np.all(W @ y <= 1 + 1e-6):
            out.append(y)
    keep = []
    for y in out:
        if not any(float(np.linalg.norm(y - z)) < 1e-7 for z in keep):
            keep.append(y)
    return np.stack(keep) if keep else None

def proj_simplex(w):
    u = np.sort(w)[::-1]
    css = np.cumsum(u)
    rho = np.nonzero(u + (1 - css) / (np.arange(len(w)) + 1) > 0)[0][-1]
    th = (css[rho] - 1) / (rho + 1)
    return np.maximum(w - th, 0)

def point_poly_dist(x, P, iters=4000):
    """min |x - W w| over simplex weights, projected gradient."""
    m = len(P)
    G = P @ P.T
    b = P @ x
    L = 2 * float(np.linalg.eigvalsh(G).max()) + 1e-12
    w = np.full(m, 1.0 / m)
    for _ in range(iters):
        w = proj_simplex(w - (2 * (G @ w) - 2 * b) / L)
    return float(np.linalg.norm(x - w @ P))

def hausdorff_ub(A, B):
    d1 = max(point_poly_dist(a, B) for a in A)
    d2 = max(point_poly_dist(b, A) for b in B)
    return max(d1, d2)

def normalize(verts, seed):
    Pj = jitter(np.asarray(verts, float), seed=seed)
    F = facets_simplicial(Pj)
    V, C = fan_vol_centroid(Pj, F)
    Q = Pj - C
    F2 = facets_simplicial(Q)
    V2, C2 = fan_vol_centroid(Q, F2)
    assert abs(V - V2) < 1e-6 * V, (V, V2)
    return Q / V2 ** 0.25, V2, C

def product_of(Qn, pseed):
    Y = polar_vertices(Qn)
    assert Y is not None and len(Y) >= 5
    Yj = jitter(Y, s=1e-7, seed=pseed)
    FY = facets_simplicial(Yj)
    VY, _ = fan_vol_centroid(Yj, FY)
    return VY, len(Y)

def reg_simplex():
    c = (1 - math.sqrt(5)) / 4
    V = np.stack([np.array([1., 0, 0, 0]), np.array([0, 1., 0, 0]),
                  np.array([0, 0, 1., 0]), np.array([0, 0, 0, 1.]),
                  np.array([c, c, c, c])])
    return V - V.mean(axis=0)

BASE = 5 ** 5 / 24 ** 2
res = {"base_exact": BASE}
print("exact base 5^5/24^2 =", BASE, flush=True)

S = reg_simplex()
Sn, Vs, _ = normalize(S, seed=1)
ps, ks = product_of(Sn, 101)
res["simplex_numeric"] = {"product": ps, "polar_nverts": ks, "primal_vol_check": Vs}
print("simplex numeric product =", ps, "polar verts:", ks, flush=True)

# E2: single-vertex truncation of simplex -> 8 vertices
S0 = S.copy()
v0 = S0[4].copy()
tr = []
for ti, t in enumerate([0.02, 0.05, 0.08, 0.12, 0.16, 0.2, 0.3, 0.4, 0.5, 0.6]):
    W = np.stack([S0[i] for i in range(4)] + [(1 - t) * v0 + t * S0[i] for i in range(4)])
    Wn, V, _ = normalize(W, seed=10 + ti)
    p, k = product_of(Wn, 1000 + ti)
    d = hausdorff_ub(Wn, Sn)
    exc = p - BASE
    tr.append({"t": t, "product": p, "excess": exc, "d_ub": d,
               "margin": exc - 0.1 * d * d, "polar_nverts": k})
    print(f"trunc t={t:.2f} prod={p:.6f} excess={exc:.6f} d_ub={d:.4f} "
          f"margin={exc - 0.1*d*d:.6f} kpol={k}", flush=True)
res["truncation"] = tr

# E2b: vertex split v0 -> v0 +/- eps*u (6 vertices), second-order probe
rng = np.random.default_rng(3)
sp = []
for si in range(6):
    u = rng.normal(0, 1, 4); u /= np.linalg.norm(u)
    eps = [0.05, 0.1, 0.2][si % 3]
    W = np.stack([S0[i] for i in range(4)] + [v0 + eps * u, v0 - eps * u])
    Wn, V, _ = normalize(W, seed=50 + si)
    p, k = product_of(Wn, 2000 + si)
    d = hausdorff_ub(Wn, Sn)
    exc = p - BASE
    sp.append({"eps": eps, "product": p, "excess": exc, "d_ub": d,
               "margin": exc - 0.1 * d * d})
    print(f"split trial={si} eps={eps} prod={p:.6f} excess={exc:.6f} d_ub={d:.4f} "
          f"margin={exc - 0.1*d*d:.6f}", flush=True)
res["vertex_split"] = sp

# E3: structured bodies
fam = {}
X = np.stack([np.eye(4)[i] * s for i in range(4) for s in (1., -1.)])
Wn, _, _ = normalize(X, seed=70); p, k = product_of(Wn, 3001)
fam["cross8"] = {"product": p, "polar_nverts": k}
print("cross product =", p, flush=True)
u3 = np.stack([np.array([1., 1, 1]), np.array([1., -1, -1]),
               np.array([-1., 1, -1]), np.array([-1., -1, 1.])])
pr = np.stack([np.append(x, 0.) for x in u3] + [np.append(x, 2.) for x in u3])
Wn, _, _ = normalize(pr, seed=71); p, k = product_of(Wn, 3002)
fam["tetra_prism"] = {"product": p}
print("tetra-prism product =", p, flush=True)
oc = np.stack([np.eye(3)[i] * s for i in range(3) for s in (1., -1.)])
bi = np.stack([np.append(x, 0.) for x in oc]
              + [np.array([0., 0, 0, 1.5]), np.array([0., 0, 0, -1.5])])
Wn, _, _ = normalize(bi, seed=72); p, k = product_of(Wn, 3003)
fam["bipyr_octahedron"] = {"product": p}
print("bipyramid/octahedron product =", p, flush=True)
Fc = S0[:4].mean(axis=0)
e4 = S0[4] - Fc
for s in [0.05, 0.2, 0.5]:
    apex = S0[4] + s * e4
    W = np.stack(list(S0) + [apex])
    Wn, _, _ = normalize(W, seed=80 + int(s * 100)); p, k = product_of(Wn, 3100 + int(s * 100))
    d = hausdorff_ub(Wn, Sn)
    fam[f"stacked_{s}"] = {"product": p, "d_ub": d, "margin": (p - BASE) - 0.1 * d * d}
    print(f"stacked s={s} prod={p:.6f} d_ub={d:.4f} margin={(p-BASE)-0.1*d*d:.6f}", flush=True)
res["families"] = fam

# E4: random searches (bounded recovery test for disproof route)
def run_random(N, gen, label):
    below = 0; vals = []; minrec = None
    for j in range(N):
        A = gen(j)
        try:
            Wn, _, _ = normalize(A, seed=10000 + j)
            p, _ = product_of(Wn, 50000 + j)
        except Exception:
            continue
        vals.append(p)
        if p < BASE:
            below += 1
        if minrec is None or p < minrec[0]:
            minrec = (p, j)
    vals = np.array(vals)
    out = {"N": N, "kept": len(vals), "min": float(vals.min()), "mean": float(vals.mean()),
           "min_excess": float(vals.min()) - BASE, "n_below_base": below,
           "q": [float(q) for q in np.quantile(vals, [0.0, 0.01, 0.05, 0.5])]}
    print(f"{label}: kept={len(vals)} min={vals.min():.6f} mean={vals.mean():.6f} "
          f"below_base={below} min_excess={float(vals.min())-BASE:.6f}", flush=True)
    return out

r1 = np.random.default_rng(7)
res["random_gauss8"] = run_random(800, lambda j: r1.normal(0, 1, (8, 4)), "gauss8")
r2 = np.random.default_rng(11)
Sref = S.copy()
res["random_near_simplex"] = run_random(
    800, lambda j: Sref + r2.normal(0, 0.15, (5, 4)), "near_simplex")
r3 = np.random.default_rng(13)
res["random_gauss6"] = run_random(400, lambda j: r3.normal(0, 1, (6, 4)), "gauss6")

with open("output/artifacts/results.json", "w") as f:
    json.dump(res, f, indent=1)
print("wrote output/artifacts/results.json", flush=True)
