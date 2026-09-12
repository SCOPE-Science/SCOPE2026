#!/usr/bin/env python3
"""Corrected volume-product pipeline (numpy only).
Volume via cone decomposition from interior point (mean of vertices, strictly
interior for full-dimensional hulls) over simplicial facets of jittered body.
Self-tests against exact cube / cross-polytope / simplex volumes included.
"""
import numpy as np, itertools, math, json

def jitter(P, s=1e-7, seed=0):
    rng = np.random.default_rng(seed)
    sc = float(np.abs(P).max()) or 1.0
    return np.asarray(P, float) + rng.normal(0, s * sc, np.shape(P))

def facets_simplicial(P, tol=1e-7):
    m = len(P)
    F = []
    for combo in itertools.combinations(range(m), 4):
        C = list(combo)
        A = P[C]
        c = A.mean(axis=0)
        _, _, Vt = np.linalg.svd(A - c)
        n = Vt[-1]
        s = (P - c) @ n
        if np.all(s <= tol) or np.all(s >= -tol):
            F.append(tuple(C))
    return F

def vol_centroid_cone(P, F):
    """Exact (up to jitter) volume+centroid: cone from mean(P) over all facets."""
    o = P.mean(axis=0)
    V = 0.0
    C = np.zeros(4)
    W = 0.0
    for f in F:
        M = P[list(f)] - o
        d = abs(float(np.linalg.det(M)))
        if d == 0:
            continue
        V += d
        TC = (o + P[list(f)].sum(axis=0)) / 5.0
        C += d * TC
        W += d
    V /= 24.0
    C /= W
    return V, C

def polar_vertices(W, tol=1e-6):
    out = []
    for combo in itertools.combinations(range(len(W)), 4):
        A = W[list(combo)]
        if abs(float(np.linalg.det(A))) < 1e-12:
            continue
        try:
            y = np.linalg.solve(A, np.ones(4))
        except np.linalg.LinAlgError:
            continue
        if np.all(W @ y <= 1 + tol):
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

def point_poly_dist(x, P, iters=2000):
    m = len(P)
    G = P @ P.T
    b = P @ x
    L = 2 * float(np.linalg.eigvalsh(G).max()) + 1e-12
    w = np.full(m, 1.0 / m)
    for _ in range(iters):
        w = proj_simplex(w - (2 * (G @ w) - 2 * b) / L)
    return float(np.linalg.norm(x - w @ P))

def hausdorff_ub(A, B):
    return max(max(point_poly_dist(a, B) for a in A),
               max(point_poly_dist(b, A) for b in B))

def normalize(verts, seed):
    Pj = jitter(verts, seed=seed)
    F = facets_simplicial(Pj)
    assert len(F) > 0
    V, C = vol_centroid_cone(Pj, F)
    return (Pj - C) / V ** 0.25, V

def polar_vol(Wn, pseed):
    Y = polar_vertices(Wn)
    assert Y is not None and len(Y) >= 5, "polar degenerate/unbounded"
    Yj = jitter(Y, seed=pseed)
    FY = facets_simplicial(Yj)
    VY, _ = vol_centroid_cone(Yj, FY)
    return VY, len(Y)

def reg_simplex():
    c = (1 - math.sqrt(5)) / 4
    V = np.stack([np.array([1., 0, 0, 0]), np.array([0, 1., 0, 0]),
                  np.array([0, 0, 1., 0]), np.array([0, 0, 0, 1.]),
                  np.array([c, c, c, c])])
    return V - V.mean(axis=0)

res = {}
BASE = 5 ** 5 / 24 ** 2
res["base_exact"] = BASE

# ---- self-tests ----
t = {}
Cb = np.stack([np.array([x, y, z, w], float)
               for x in (-1., 1.) for y in (-1., 1.)
               for z in (-1., 1.) for w in (-1., 1.)])
Vb, _ = vol_centroid_cone(jitter(Cb, seed=5), facets_simplicial(jitter(Cb, seed=5)))
t["cube_vol"] = {"got": Vb, "want": 16.0}
X = np.stack([np.eye(4)[i] * s for i in range(4) for s in (1., -1.)])
Vx, _ = vol_centroid_cone(jitter(X, seed=6), facets_simplicial(jitter(X, seed=6)))
t["cross_vol"] = {"got": Vx, "want": 2.0 / 3.0}
S = reg_simplex()
Vs, _ = vol_centroid_cone(jitter(S, seed=7), facets_simplicial(jitter(S, seed=7)))
t["simplex_vol_consistency"] = {"got": Vs}
Sn, _ = normalize(S, seed=1)
ps, ks = polar_vol(Sn, 101)
t["simplex_product"] = {"got": ps, "want": BASE, "polar_nverts": ks}
Wn, _ = normalize(X, seed=70)
px, kx = polar_vol(Wn, 3001)
t["cross_product"] = {"got": px, "want": 32.0 / 3.0, "polar_nverts": kx}
res["self_tests"] = t
for k, v in t.items():
    print(k, v, flush=True)

# ---- E2: single-vertex truncation (8 verts) ----
S0 = S.copy()
v0 = S0[4].copy()
tr = []
for ti, tt in enumerate([0.02, 0.05, 0.08, 0.12, 0.16, 0.2, 0.3, 0.4, 0.5]):
    W = np.stack([S0[i] for i in range(4)] + [(1 - tt) * v0 + tt * S0[i] for i in range(4)])
    Wn, _ = normalize(W, seed=10 + ti)
    p, k = polar_vol(Wn, 1000 + ti)
    d = hausdorff_ub(Wn, Sn)
    exc = p - BASE
    tr.append({"t": tt, "product": p, "excess": exc, "d_ub": d,
               "margin": exc - 0.1 * d * d, "polar_nverts": k})
    print(f"trunc t={tt:.2f} prod={p:.6f} excess={exc:.6f} d_ub={d:.4f} "
          f"margin={exc - 0.1*d*d:.6f} kpol={k}", flush=True)
res["truncation"] = tr

# ---- E2b: vertex split (6 verts, second-order probe) ----
rng = np.random.default_rng(3)
sp = []
for si in range(6):
    u = rng.normal(0, 1, 4); u /= np.linalg.norm(u)
    eps = [0.05, 0.1, 0.2][si % 3]
    W = np.stack([S0[i] for i in range(4)] + [v0 + eps * u, v0 - eps * u])
    Wn, _ = normalize(W, seed=50 + si)
    p, k = polar_vol(Wn, 2000 + si)
    d = hausdorff_ub(Wn, Sn)
    exc = p - BASE
    sp.append({"eps": eps, "product": p, "excess": exc, "d_ub": d,
               "margin": exc - 0.1 * d * d})
    print(f"split trial={si} eps={eps} prod={p:.6f} excess={exc:.6f} d_ub={d:.4f} "
          f"margin={exc - 0.1*d*d:.6f}", flush=True)
res["vertex_split"] = sp

# ---- E3: structured bodies ----
fam = {}
pr_u = np.stack([np.array([1., 1, 1]), np.array([1., -1, -1]),
                 np.array([-1., 1, -1]), np.array([-1., -1, 1.])])
pr = np.stack([np.append(x, 0.) for x in pr_u] + [np.append(x, 2.) for x in pr_u])
Wn, _ = normalize(pr, seed=71); p, _ = polar_vol(Wn, 3002)
fam["tetra_prism"] = {"product": p}
print("tetra-prism product =", p, flush=True)
oc = np.stack([np.eye(3)[i] * s for i in range(3) for s in (1., -1.)])
bi = np.stack([np.append(x, 0.) for x in oc]
              + [np.array([0., 0, 0, 1.5]), np.array([0., 0, 0, -1.5])])
Wn, _ = normalize(bi, seed=72); p, _ = polar_vol(Wn, 3003)
fam["bipyr_octahedron"] = {"product": p}
print("bipyramid/octahedron product =", p, flush=True)
res["families"] = fam

# ---- E4: bounded recovery test — random search for product below base ----
def run_random(N, gen, label, seed0):
    below = 0; vals = []
    for j in range(N):
        A = gen(j)
        try:
            Wn, _ = normalize(A, seed=seed0 + j)
            p, _ = polar_vol(Wn, seed0 + 40000 + j)
        except Exception:
            continue
        vals.append(p)
        if p < BASE:
            below += 1
    vals = np.array(vals)
    out = {"kept": len(vals), "min": float(vals.min()), "mean": float(vals.mean()),
           "min_excess": float(vals.min()) - BASE, "n_below_base": below}
    print(f"{label}: kept={len(vals)} min={vals.min():.6f} mean={vals.mean():.6f} "
          f"below_base={below}", flush=True)
    return out

r1 = np.random.default_rng(7)
res["random_gauss8"] = run_random(800, lambda j: r1.normal(0, 1, (8, 4)), "gauss8", 10000)
r2 = np.random.default_rng(11)
Sref = S.copy()
res["random_near_simplex"] = run_random(
    800, lambda j: Sref + r2.normal(0, 0.15, (5, 4)), "near_simplex5", 20000)
r3 = np.random.default_rng(13)
res["random_gauss6"] = run_random(400, lambda j: r3.normal(0, 1, (6, 4)), "gauss6", 30000)

with open("output/artifacts/results.json", "w") as f:
    json.dump(res, f, indent=1)
print("wrote output/artifacts/results.json", flush=True)
