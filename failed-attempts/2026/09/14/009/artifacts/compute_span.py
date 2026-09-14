"""Bounded recovery test for lane-1826: rank-9 equivariant valuation classification.

Computes:
 1. dim Sym^9(R^3), S3- and A3-fixed subspace dims (exact orbit counting + SVD check).
 2. 9th moment vectors over dilates (m=0..8) of simplex, cube, octahedron, prism.
 3. Reeve tetrahedra R_k moments (k=1..12) + polynomial-in-k fit.
 4. Combined rank vs ambient 55.
 5. Facet-normal candidate equivariance failure under a shear matrix.
"""
import itertools
import json
import numpy as np
from math import gcd
from functools import reduce

OUT = "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1826/output/artifacts/"

mons = [(a, b, c) for a in range(10) for b in range(10 - a)
        for c in [9 - a - b] if a + b + c == 9]
assert len(mons) == 55
DIM = 55

# ---- 1. stabilizer fixed subspaces (exact orbit counting) ----
def orbit_count(perms):
    seen = set()
    n = 0
    for m in mons:
        if m in seen:
            continue
        n += 1
        stack = [m]
        seen.add(m)
        # orbit under perms acting on exponent triples
        orb = {m}
        for p in perms:
            orb.add(tuple(m[p[i]] for i in range(3)))
        # closure (perms form group, single application suffices, but close anyway)
        changed = True
        while changed:
            changed = False
            for q in list(orb):
                for p in perms:
                    r = tuple(q[p[i]] for i in range(3))
                    if r not in orb:
                        orb.add(r)
                        changed = True
        seen |= orb
    return n

import itertools as it
S3 = list(it.permutations([0, 1, 2]))
A3 = [p for p in S3 if sum(1 for i in range(3) for j in range(i + 1, 3) if p[i] > p[j]) % 2 == 0]
print("S3 size", len(S3), " A3 size", len(A3))
s3d = orbit_count(S3)
a3d = orbit_count(A3)
print("S3-fixed dim =", s3d, " A3-fixed dim =", a3d)

# ---- 2. moment vectors ----
def moment_vector(pts):
    v = np.zeros(DIM)
    for (x, y, z) in pts:
        for i, (a, b, c) in enumerate(mons):
            v[i] += (x ** a) * (y ** b) * (z ** c)
    return v

def pts_simplex(m):
    return [(x, y, z) for x in range(m + 1) for y in range(m + 1 - x)
            for z in range(m + 1 - x - y)]

def pts_cube(m):
    return [(x, y, z) for x in range(m + 1) for y in range(m + 1) for z in range(m + 1)]

def pts_octa(m):
    return [(x, y, z) for x in range(-m, m + 1) for y in range(-m, m + 1)
            for z in range(-m, m + 1) if abs(x) + abs(y) + abs(z) <= m]

def pts_prism(m):
    return [(x, y, z) for x in range(m + 1) for y in range(m + 1 - x) for z in range(m + 1)]

Ms = list(range(9))
M_sim = np.stack([moment_vector(pts_simplex(m)) for m in Ms])
M_cub = np.stack([moment_vector(pts_cube(m)) for m in Ms])
M_oct = np.stack([moment_vector(pts_octa(m)) for m in Ms])
M_pri = np.stack([moment_vector(pts_prism(m)) for m in Ms])
print("ranks: simplex", np.linalg.matrix_rank(M_sim),
      "cube", np.linalg.matrix_rank(M_cub),
      "octa", np.linalg.matrix_rank(M_oct),
      "prism", np.linalg.matrix_rank(M_pri))
D = np.vstack([M_sim, M_cub, M_oct, M_pri])
print("combined dilate rank:", np.linalg.matrix_rank(D))

# ---- 3. Reeve tetrahedra ----
def moment_reeve(k):
    return moment_vector([(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, k)])

Ks = list(range(1, 13))
R = np.stack([moment_reeve(k) for k in Ks])
print("reeve rank:", np.linalg.matrix_rank(R))
X = np.vander(Ks, 10, increasing=True)
coef, res, *_ = np.linalg.lstsq(X, R, rcond=None)
nrm = np.linalg.norm(coef, axis=1)
print("reeve poly-coef norms:", np.round(nrm, 4))
print("reeve coef-matrix rank:", np.linalg.matrix_rank(coef))
F = np.vstack([D, R])
tot = np.linalg.matrix_rank(F)
print("TOTAL family rank:", tot, " ambient:", DIM, " residual:", DIM - tot)
np.save(OUT + "moment_family.npy", F)

# ---- 5. facet-normal candidate vs shear ----
def prim(v):
    g = reduce(gcd, [abs(int(round(t))) for t in v])
    return tuple(int(round(t)) // g for t in v)

def facets_lattice(verts):
    """verts: list of 3-tuples (tetrahedron). Returns [(area_lat, primitive outward normal)]."""
    out = []
    cx = sum(v[0] for v in verts) / 4
    cy = sum(v[1] for v in verts) / 4
    cz = sum(v[2] for v in verts) / 4
    faces = [(0, 2, 1), (0, 1, 3), (0, 3, 2), (1, 2, 3)]
    for (i, j, k) in faces:
        a = np.array(verts[i], float)
        b = np.array(verts[j], float)
        c = np.array(verts[k], float)
        n = np.cross(b - a, c - a)  # integer vector
        mid = (a + b + c) / 3
        inward = np.array([cx, cy, cz]) - mid
        if np.dot(n, inward) > 0:
            n = -n
        u = prim(n)
        un = np.linalg.norm(u)
        alat = np.linalg.norm(n) / (2 * un)
        out.append((alat, u))
    return out

def tensor_vec(terms):
    """terms: [(weight, (v1,v2,v3))]; embed v^{otimes9} via monomials."""
    t = np.zeros(DIM)
    for w, v in terms:
        for i, (a, b, c) in enumerate(mons):
            t[i] += w * (v[0] ** a) * (v[1] ** b) * (v[2] ** c)
    return t

T = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
phi = np.array([[1, 1, 0], [0, 1, 0], [0, 0, 1]])
ZT = tensor_vec([(A, u) for A, u in facets_lattice(T)])
phiT = [tuple(phi @ np.array(v)) for v in T]
ZphiT = tensor_vec([(A, u) for A, u in facets_lattice(phiT)])
phi_push = tensor_vec([(A, tuple(phi @ np.array(u))) for A, u in facets_lattice(T)])
print("facet-normal Z(T) norm:", np.linalg.norm(ZT))
print("||Z(phi T) - phi.Z(T)|| =", np.linalg.norm(ZphiT - phi_push))
print("equivariance holds:", np.allclose(ZphiT, phi_push))

summary = {
    "dim_sym9": DIM,
    "S3_fixed_dim": s3d,
    "A3_fixed_dim": a3d,
    "rank_simplex_dilates": int(np.linalg.matrix_rank(M_sim)),
    "rank_cube_dilates": int(np.linalg.matrix_rank(M_cub)),
    "rank_octa_dilates": int(np.linalg.matrix_rank(M_oct)),
    "rank_prism_dilates": int(np.linalg.matrix_rank(M_pri)),
    "rank_dilates_combined": int(np.linalg.matrix_rank(D)),
    "rank_reeve": int(np.linalg.matrix_rank(R)),
    "rank_reeve_coef": int(np.linalg.matrix_rank(coef)),
    "rank_total": int(tot),
    "residual": int(DIM - tot),
    "facet_normal_equiv_error": float(np.linalg.norm(ZphiT - phi_push)),
}
with open(OUT + "span_summary.json", "w") as f:
    json.dump(summary, f, indent=2)
print(json.dumps(summary, indent=2))
