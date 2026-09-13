"""Build veering boundary train track for 10_145 (flipper veering triangulation).

Outputs (pickle):
  side_classes: list of 36 branches; each = tuple of two side keys ((i,v),j)
  switches: list of 24 (L, s1, s2) branch ids  [w_L = w_s1 + w_s2]
  edge_classes: boundary edge class data, vertex classes, triangles
  homology: H1 basis cycles (as edge-class chains), intersection form,
            meridian/longitude classes in H1 basis (SnapPy basis of V),
            Zung picture coords calibration.
Convention notes inside.
"""
import pickle, itertools
import snappy, flipper
import numpy as np

M = snappy.Manifold('10_145')
mono = flipper.monodromy_from_bundle(M)
B = mono.bundle(veering=True)
V = snappy.Manifold(B.snappy_string())
data = V._get_tetrahedra_gluing_data()
NT = len(data)
WSTAR = {0:2, 1:3, 2:0, 3:1}  # pi-corner direction; large side j=w*(v)

def find(parent, a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a
def union(parent, a, b):
    ra, rb = find(parent, a), find(parent, b)
    if ra != rb:
        parent[ra] = rb

# --- side (branch) classes ---
parent = {}
sides = []
for i in range(NT):
    for v in range(4):
        for j in range(4):
            if j != v:
                s = ((i, v), j)
                parent[s] = s
                sides.append(s)
for i, (nbrs, perms) in enumerate(data):
    for j in range(4):
        i2 = nbrs[j]; p = perms[j]
        for v in range(4):
            if v != j:
                union(parent, ((i, v), j), ((i2, p[v]), p[j]))
bid = {}
branches = []
for s in sides:
    r = find(parent, s)
    if r not in bid:
        bid[r] = len(bid)
        branches.append([])
    branches[bid[r]].append(s)
NB = len(bid)
assert NB == 36, NB
assert all(len(c) == 2 for c in branches)

def B_id(side):
    return bid[find(parent, side)]

switches = []
for i in range(NT):
    for v in range(4):
        L = B_id(((i, v), WSTAR[v]))
        S = [B_id(((i, v), j)) for j in range(4) if j != v and j != WSTAR[v]]
        switches.append((L, S[0], S[1]))

# --- vertex classes of corners (i,v,w) ---
cparent = {}
corners = []
for i in range(NT):
    for v in range(4):
        for w in range(4):
            if w != v:
                c = (i, v, w)
                cparent[c] = c
                corners.append(c)
for i, (nbrs, perms) in enumerate(data):
    for j in range(4):
        i2 = nbrs[j]; p = perms[j]
        for v in range(4):
            if v == j:
                continue
            for w in range(4):
                if w == j or w == v:
                    continue
                union(cparent, (i, v, w), (i2, p[v], p[w]))
vid = {}
for c in corners:
    r = find(cparent, c)
    if r not in vid:
        vid[r] = len(vid)
NV = len(vid)
print("branches:", NB, "switches:", len(switches), "vertices:", NV)

# --- oriented chain complex: orient each branch arbitrarily, compute d ---
# Corner (i,v,w): vertex vid. Side ((i,v),j): connects corners w1,w2 (w1,w2 != v,j).
# Orient side from corner w_first to w_second with a fixed rule: from smaller to larger w? Need corner vertex ids.
branch_ends = []
for b, members in enumerate(branches):
    (s1, s2) = members  # each side ((i,v),j)
    ends = set()
    for ((i, v), j) in [s1, s2]:
        pass
    # endpoints within triangle (i,v): corners (i,v,w), w not in (v,j)
    def tri_ends(member):
        ((i, v), j) = member
        ws = [w for w in range(4) if w != v and w != j]
        return [vid[find(cparent, (i, v, w))] for w in ws]
    e1 = tri_ends(s1)
    e2 = tri_ends(s2)
    branch_ends.append((e1, e2))
# vertex degrees / incidences for H1: build incidence matrix NV x NB with orientation:
# orient branch b from e1[0]... but the two sides are glued; the branch is a single edge with 2 endpoints.
# The endpoints of branch b: glue corner (s1 side) to corner (s2 side): pairing: side s1's two corners pair with
# side s2's two corners via the gluing map. From union construction: ((i,v),j) glued to ((i2,p[v]),p[j]); corners map
# (i,v,w)->(i2,p[v],p[w]). So branch endpoints: pick w_a,w_b corners of s1; their partners in s2.
    # (implemented below in homology section via explicit pairing)

# Explicit endpoint pairing per branch:
branch_vpair = []
for b, members in enumerate(branches):
    ((i1, v1), j1), ((i2, v2), j2) = members
    # corners of side1: w in W1 = {w != v1, j1}; partner of (i1,v1,w) under gluing:
    # The gluing identifying side1 with side2 came from some face pairing; recover by vertex-class equality:
    W1 = [w for w in range(4) if w != v1 and w != j1]
    W2 = [w for w in range(4) if w != v2 and w != j2]
    # partner of corner (i1,v1,w) is the corner in {(i2,v2,w2)} with same vertex class
    pairs = []
    used = set()
    for w in W1:
        c1 = vid[find(cparent, (i1, v1, w))]
        for w2 in W2:
            if w2 in used:
                continue
            if vid[find(cparent, (i2, v2, w2))] == c1:
                pairs.append((c1, w, w2))
                used.add(w2)
                break
    assert len(pairs) == 2, (b, members, W1, W2)
    # branch endpoints: the two vertex classes
    ends = sorted(set(p[0] for p in pairs))
    # For a loop edge both ends same — handle generally below
    branch_vpair.append((members, pairs))

with open("output/artifacts/track_data.pkl", "wb") as f:
    pickle.dump({
        "branches": branches, "switches": switches, "NV": NV,
        "branch_vpair": [(m, p) for (m, p) in branch_vpair],
        "gluing_data": data,
    }, f)
print("saved track_data.pkl")
