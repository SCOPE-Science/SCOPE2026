"""H1 of boundary torus + intersection form + H1 classes of SnapPy m/l + carried-slope LP."""
import pickle
import numpy as np
import snappy, flipper

D = pickle.load(open("output/artifacts/track_data.pkl", "rb"))
branches, switches, NV = D["branches"], D["switches"], D["NV"]
NB = len(branches)

M = snappy.Manifold('10_145')
mono = flipper.monodromy_from_bundle(M)
B = mono.bundle(veering=True)
V = snappy.Manifold(B.snappy_string())
data = V._get_tetrahedra_gluing_data()
NT = len(data)

# corner DSU (same order as build_track)
parent2 = {}
def find2(a):
    while parent2[a] != a:
        parent2[a] = parent2[parent2[a]]
        a = parent2[a]
    return a
def union2(a, b):
    ra, rb = find2(a), find2(b)
    if ra != rb:
        parent2[ra] = rb
for i in range(NT):
    for v in range(4):
        for w in range(4):
            if w != v:
                parent2[(i, v, w)] = (i, v, w)
for i, (nbrs, perms) in enumerate(data):
    for j in range(4):
        i2 = nbrs[j]; p = perms[j]
        for v in range(4):
            if v == j:
                continue
            for w in range(4):
                if w == j or w == v:
                    continue
                union2((i, v, w), (i2, p[v], p[w]))
# vid: root -> 0..NV-1 in the SAME deterministic way? build_track used dict insertion order over `corners`
# list: corners appended i,v,w nested order; vid[root] assigned in that order. Reproduce:
vid = {}
for i in range(NT):
    for v in range(4):
        for w in range(4):
            if w != v:
                r = find2((i, v, w))
                if r not in vid:
                    vid[r] = len(vid)
assert len(vid) == NV, len(vid)

def VC(i, v, w):
    return vid[find2((i, v, w))]

bkey = {}
for b, members in enumerate(branches):
    for s in members:
        bkey[s] = b

# d2: triangle boundaries with link orientations (all tets +)
d2 = np.zeros((24, NB), dtype=int)
tidx = {}
for i in range(NT):
    for v in range(4):
        t = (i, v)
        tidx[t] = len(tidx)
        W = sorted(w for w in range(4) if w != v)
        bedges = [((W[1], W[2]), 1), ((W[0], W[2]), -1), ((W[0], W[1]), 1)]
        for j in range(4):
            if j == v:
                continue
            rest = [w for w in W if w != j]
            a, bb = rest
            for ((x, y), s) in bedges:
                if {x, y} == {a, bb}:
                    sgn = s if (x, y) == (a, bb) else -s
                    b = bkey[((i, v), j)]
                    ca, cb = VC(i, v, a), VC(i, v, bb)
                    agree = 1 if ca <= cb else -1
                    d2[tidx[t], b] += sgn * agree
                    break
assert set(d2.sum(axis=1)) == {0}, d2.sum(axis=1)
assert sorted(set((d2 != 0).sum(axis=1))) == [3]

d1 = np.zeros((NV, NB), dtype=int)
for b, members in enumerate(branches):
    ((i1, v1), j1) = members[0]
    W1 = [w for w in range(4) if w != v1 and w != j1]
    a = VC(i1, v1, W1[0]); bb = VC(i1, v1, W1[1])
    if a != bb:
        lo, hi = min(a, bb), max(a, bb)
        d1[lo, b] = -1; d1[hi, b] = 1
assert np.abs(d1 @ d2.T).max() == 0
from numpy.linalg import matrix_rank
r1, r2 = matrix_rank(d1), matrix_rank(d2)
print("rank d1:", r1, "rank d2:", r2, "dim H1:", NB - r1 - r2)
assert NB - r1 - r2 == 2

# H1 basis: ker d1 mod im d2. Compute integer basis via rational SVD nullspace + lattice rounding.
u, sig, vt = np.linalg.svd(d1)
ker1 = vt[r1:].T  # NB x (NB-r1)
# project out im d2: find basis of ker1 / col(d2). QR approach:
# H1 basis vectors: nullspace of stacked [d1; P] ... use: compute nullspace of d1 over QQ via sympy? Use float + round.
import itertools
# Build projection: Q = orth basis of col(d2); restrict ker1 to Q^perp.
q, _ = np.linalg.qr(d2.T)  # NB x 24, first r2 cols span im d2
Q = q[:, :r2]
proj = np.eye(NB) - Q @ Q.T
red = proj @ ker1  # NB x 25, rank 2
uu, ss, vvt = np.linalg.svd(red)
print("reduced sing vals:", np.round(ss, 8))
h1f = uu[:, :2]  # orthonormal basis of H1 in edge coords
# Round to small integer vectors: LLL-ish by scaling + rounding, then verify cycle+independent mod boundaries.
best = None
for scale in range(1, 40):
    for combo in [np.array([1.0, 0.0]), np.array([0.0, 1.0])]:
        pass
# integerize each basis vector separately via continued scaling search
h1int = []
for k in range(2):
    vec = h1f[:, k]
    found = None
    for scale in range(1, 400):
        r = np.round(vec * scale).astype(int)
        if np.linalg.norm(r) == 0:
            continue
        # must be a cycle: d1 r == 0
        if np.abs(d1 @ r).max() != 0:
            continue
        # direction must match vec
        if np.dot(r, vec) < 0:
            r = -r
        err = np.linalg.norm(r / np.linalg.norm(r) - vec / np.linalg.norm(vec))
        if err < 1e-6:
            found = r
            break
    assert found is not None, (k, vec)
    h1int.append(found)
    print(f"h1[{k}]:", found, "d1 check:", np.abs(d1 @ found).max())
H = np.stack(h1int)  # 2 x NB
print("H1 basis independence mod d2 (rank of stacked [H; d2]):",
      matrix_rank(np.vstack([H, d2]).astype(float)), "(expect 24+... im d2 rank 23 + 2 = 25)")

# Intersection form on H1: dual-cocycle method. Need per-branch crossing sign eps.
# Dual edge of branch b connects the two adjacent triangles; orient dual edge from triangle on RIGHT of oriented
# branch to triangle on LEFT (then crossing sign +1 uniformly... sign convention: a.b = sum_e a_e b_e requires
# dual orientation s.t. (branch, dual) is positively oriented at every crossing).
# Determine left/right: branch b members are sides ((i1,v1),j1),((i2,v2),j2) in triangles t1=(i1,v1),t2=(i2,v2).
# Oriented branch direction: by our convention smaller vertex class -> larger. In triangle t1, the side goes from
# corner a1 to corner b1 (one direction); the triangle interior is on one side.
# Compute: in triangle t1 with corners W (sorted, orientation sign + via link), side ((i1,v1),j1) spans rest=(a,bb)
# with boundary direction a->bb times sgn (from d2 code). Branch direction: min(VC)->max(VC).
# Triangle interior relative to branch direction: cross product sign... In the oriented triangle, boundary traverses
# with interior on LEFT (standard: positively oriented boundary has interior left? For CCW triangle, boundary CCW,
# interior left yes). If branch direction agrees with boundary direction in t1, interior of t1 is LEFT of branch;
# else RIGHT. Dual edge should go RIGHT->LEFT: if agree: dual from t2 to t1, i.e., dual orientation t2->t1.
# eps_e: with dual oriented RIGHT->LEFT uniformly, a.b = +sum a_e b_e. So take INTER = +1 on all branches, i.e.,
# intersection matrix in edge coords = Identity restricted to H1? NO — careful: a.b = sum_e a_e * beta_e where beta =
# PD(b) cocycle with beta(dual_e) = b_e. The dual edge basis pairs with primal edge basis with +1 each (by the
# RIGHT->LEFT orientation choice). So intersection form matrix G on H1 basis = H @ H.T (Gram matrix)!?
# That can't be right in general (Gram is PSD; intersection is skew). The subtlety: PD(b) as a COCYCLE has value b_e
# on dual edge e*, but evaluating cup product / intersection needs cap... The identity a.b = sum_e a_e b_e holds for
# PRIMAL cycle a against DUAL cycle b* (transverse): each crossing contributes a_e*b_e*(sign). With uniform +1 signs,
# a . b = a^T b. But a^T b is SYMMETRIC — contradiction with skew-symmetry, UNLESS the formula has an ordering
# subtlety: crossings of a with (dual of b) vs crossings of b with (dual of a) differ by sign; both equal sum a_e b_e?
# They can't both. Resolution: the dual cycle of b crosses branch e exactly |b_e| times, but the SIGN of crossing
# depends on orientations of a and b*_e, giving +a_e b_e; while intersection computed the other way gives -... The
# formula a.b = sum_e eps_e a_e b_e with eps_e=+1 is correct for ONE ordering; skew-symmetry is preserved because...
# sum a_e b_e is symmetric, so this would imply a.b = b.a. Contradiction => the uniform-sign assumption is WRONG:
# eps_e cannot be uniform; it depends on e via the relation between primal and dual orientations (which involves the
# surface orientation + arbitrary primal edge orientations). Correct: eps_e = +/-1 computed locally: eps_e = +1 iff
# (orient(branch_e), orient(dual_e)) is a positively oriented basis of the surface at the crossing.
# With dual_e oriented RIGHT->LEFT (right/left w.r.t. branch orientation), (branch, dual) = (forward, right->left) =
# (east, south...) take branch = +x direction, left = +y. Right->left = -y direction. (+x, -y): negative orientation
# (since (+x,+y) positive). So eps_e = -1 uniformly?! Then a.b = -a^T b — still symmetric. STILL contradictory.
# The real resolution: this "sum over branches" formula double counts / is invalid because a single branch crossing
# isn't transverse in the cell sense... The correct combinatorial intersection needs the actual geometric crossing of
# representatives, not coefficient products. ABANDON Gram idea.
# CORRECT METHOD: represent H1 basis cycles as explicit edge PATHS (they are cycles; decompose into simple loops),
# then compute geometric intersection numbers by counting (with sign) crossings in the triangles: two transverse
# multicurves in general position w.r.t. triangulation: crossings occur inside triangles where arcs cross.
# Put cycle a along edges; perturb cycle b slightly to the left (normal push): crossings appear near vertices...
# Standard simplicial formula: for 1-cocycles alpha, beta (dual to a,b): a.b = <alpha cup beta, [T2]>.
# Implement cup product on the triangulation! Cocycles from cycles via dual graph (need dual edge orientations +
# surface orientation signs — the same eps issue, but cup product handles it systematically).
# Simplest correct: use SAGE-free simplicial cup product with explicit vertex orderings per triangle + cocycle reps.
# Alternative PRAGMATIC route: slopes only need RATIOS. Calibrate using known curves: find carried curves (integer
# weight vectors in switch cone) that are simple loops; identify meridian (slope 0) and longitude (slope -1/6)
# by their topology? Still need slope functional...
# CLEANEST: compute H1 classes of meridian/longitude DIRECTLY as edge chains from SnapPy/flipper peripheral data,
# then for any carried weight vector x that is a SINGLE loop, class(x) = ±(i(x, l') ... ). Hmm still needs pairing.
# Actually with m, l as explicit CHAINS and intersection form computed ONCE via chain-level crossing count
# (perturb one chain off skeleton into general position), every loop's class follows. Chain-level intersection:
# push chain b off the 1-skeleton: each edge-traversal becomes a parallel arc slightly left; crossings with a occur
# near vertices where... this equals a combinatorial formula in (d1, triangle) data. Let me just do transverse
# representatives properly: represent BOTH cycles as train-route-like paths and count signed crossings inside
# triangles after perturbing to general position (arcs connecting side midpoints, perturbed endpoints).
# Concretely: cycle = closed walk on oriented edges. Realize as union of arcs in triangles connecting side-midpoints.
# Perturb: shift endpoints slightly along sides (a left, b right or by different amounts). Inside each triangle,
# arcs are chords between side midpoints (shifted); count signed chord crossings. Sum over triangles. This is exact
# for homologous classes (independent of shifts). Implement with fractions (use epsilon=1/4, 1/5 offsets).
