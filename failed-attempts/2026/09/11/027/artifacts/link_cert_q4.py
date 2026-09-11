#!/usr/bin/env python3
"""Exact certificate: vertex link of the q=4 PGL3 building = incidence graph of PG(2,4).

Constructs PG(2,4) from scratch over GF(4) = GF(2)[w]/(w^2+w+1), builds the
21x21 point-line incidence matrix N, and verifies over the integers:
  * every row/column sum = 5  (5-regular bipartite, 21+21 vertices)
  * N N^T = 4I + J and N^T N = 4I + J  (projective-plane axioms: unique join/meet)
  * the 42-vertex graph is connected.
Consequence (exact, no numerics): with A = [[0,N],[N^T,0]],
A^2 = diag(NN^T, N^TN) has eigenvalues 25 (x2) and 4 (x40);
bipartite symmetry then forces Spec(A) = {+5,-5} simple, {+2 (x20), -2 (x20)}.
Hence normalized second eigenvalue lambda2 = 2/5 = 0.4.
Stdlib only.
"""
import json
from pathlib import Path

OUT = Path(__file__).with_name("link_cert_result.json")

# ---- GF(4) as {0,1,2,3} = {0,1,w,w+1}, add = xor ----
def gf4_add(a, b):
    return a ^ b

def gf4_mul(a, b):
    a0, a1 = a & 1, (a >> 1) & 1
    b0, b1 = b & 1, (b >> 1) & 1
    c1 = (a1 & b1) ^ (a1 & b0) ^ (a0 & b1)   # w-coeff, using w^2 = w+1
    c0 = (a1 & b1) ^ (a0 & b0)               # const coeff
    return (c1 << 1) | c0

def gf4_inv(a):
    assert a != 0
    return {1: 1, 2: 3, 3: 2}[a]  # w * (w+1) = w^2+w = 1

# field sanity
for a in range(4):
    for b in range(4):
        assert gf4_add(a, b) == gf4_add(b, a)
        assert gf4_mul(a, b) == gf4_mul(b, a)
for a in (1, 2, 3):
    assert gf4_mul(a, gf4_inv(a)) == 1
for a in range(4):
    for b in range(4):
        for c in range(4):
            assert gf4_mul(a, gf4_add(b, c)) == gf4_add(gf4_mul(a, b), gf4_mul(a, c))

# ---- points of PG(2,4): 63 nonzero vectors / 3 scalars = 21 ----
seen = set()
pts = []
for x in range(4):
    for y in range(4):
        for z in range(4):
            if x == y == z == 0:
                continue
            v = (x, y, z)
            if v in seen:
                continue
            for c in (1, 2, 3):
                seen.add((gf4_mul(c, x), gf4_mul(c, y), gf4_mul(c, z)))
            first = x if x else (y if y else z)
            inv = gf4_inv(first)
            pts.append((gf4_mul(inv, x), gf4_mul(inv, y), gf4_mul(inv, z)))
assert len(pts) == 21, len(pts)
P = sorted(pts)

def dot(u, v):
    return gf4_add(gf4_add(gf4_mul(u[0], v[0]), gf4_mul(u[1], v[1])), gf4_mul(u[2], v[2]))

n = 21
N = [[0] * n for _ in range(n)]
for i, p in enumerate(P):
    for j, w in enumerate(P):  # line j = orthogonal complement of w
        if dot(w, p) == 0:
            N[i][j] = 1

rs = [sum(r) for r in N]
cs = [sum(N[i][j] for i in range(n)) for j in range(n)]
assert all(v == 5 for v in rs), rs
assert all(v == 5 for v in cs), cs

def mat_mul(A, B):
    nn, mm, kk = len(A), len(B[0]), len(B)
    C = [[0] * mm for _ in range(nn)]
    for i in range(nn):
        for j in range(mm):
            s = 0
            for t in range(kk):
                s += A[i][t] * B[t][j]
            C[i][j] = s
    return C

NT = [list(r) for r in zip(*N)]
Pmat = mat_mul(N, NT)
Qmat = mat_mul(NT, N)
for i in range(n):
    for j in range(n):
        want = 5 if i == j else 1
        assert Pmat[i][j] == want, ("NNT", i, j)
        assert Qmat[i][j] == want, ("NTN", i, j)

# connectivity of the 42-vertex incidence graph
adj = [[] for _ in range(42)]
for i in range(n):
    for j in range(n):
        if N[i][j]:
            adj[i].append(21 + j)
            adj[21 + j].append(i)
reached = {0}
stack = [0]
while stack:
    u = stack.pop()
    for w in adj[u]:
        if w not in reached:
            reached.add(w)
            stack.append(w)
assert len(reached) == 42

out = {
    "q": 4,
    "link_vertices": [21, 21],
    "link_degree": 5,
    "row_sums_all_5": True,
    "col_sums_all_5": True,
    "NNT_equals_4I_plus_J": True,
    "NTN_equals_4I_plus_J": True,
    "connected_42_vertices": True,
    "spectrum": {"+5": 1, "-5": 1, "+2": 20, "-2": 20},
    "normalized_lambda2": 0.4,
    "lambda2_le_0_45": True,
    "garland_one_sided_lt_half": True,
    "vertex_degree_D": 42,
    "triangles_per_vertex": 105,
}
with open(OUT, "w") as f:
    json.dump(out, f, indent=2)
print("LINK CERTIFICATE q=4: OK")
print(json.dumps(out, indent=2))
print("Derived: Spec = {+5,-5} simple, {+2 x20, -2 x20}; normalized lambda2 = 0.4.")
