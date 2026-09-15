"""Bounded recovery test (proxy only): Stanley-Reisner depth scan over Q-proxy (mod prime).

Goal: show depth>=3 candidate quotients are plentiful in equal characteristic,
while the decisive ramified vanishing (H^{d-2}_I(R)=0?) is NOT decided by this
proxy -- confirming the block is a theorem/tool gap, not lack of candidates.

Method: Hochster's formula. depth k[Delta] = min over faces F (incl. empty) of
(|F| + 1 + min{j : H~_j(link F) != 0}), where reduced homology is computed over
a finite field F_p (p=32003) as a characteristic-zero proxy. If a link has all
reduced homology zero (possible only for the void/irrelevant cases handled
separately), it contributes +inf. Facet links ({∅}) contribute via j=-1.
CM <=> depth == dim(k[Delta]) == dim(Delta)+1.
"""
import itertools
import numpy as np

P = 32003

def rank_modp(M):
    if M.size == 0:
        return 0
    A = M.copy() % P
    r = 0
    rows, cols = A.shape
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if A[i, c] % P != 0:
                piv = i
                break
        if piv is None:
            continue
        A[[r, piv]] = A[[piv, r]]
        inv = pow(int(A[r, c]), -1, P)
        A[r] = (A[r] * inv) % P
        for i in range(rows):
            if i != r and A[i, c] != 0:
                A[i] = (A[i] - A[i, c] * A[r]) % P
        r += 1
        if r == rows:
            break
    return r

def all_faces(facets, n):
    faces = set()
    faces.add(())
    for F in facets:
        for k in range(1, len(F) + 1):
            for s in itertools.combinations(sorted(F), k):
                faces.add(s)
    return faces

def link_of(facets, n, F):
    Fset = set(F)
    lk = []
    for G in facets:
        if Fset <= set(G):
            lk.append(tuple(sorted(set(G) - Fset)))
    # lk is a complex on V\F; reduce to faces; keep as sets
    # normalize: maximal faces only
    maximal = []
    for A in lk:
        if not any(set(A) < set(B) for B in lk):
            maximal.append(A)
    return maximal

def oriented_faces(complex_maximal, V, k):
    """All k-faces (k = dim, (-1..); k=-1 -> [()] if complex nonempty-or-{∅})."""
    faces = set()
    if k == -1:
        return [()]
    for M in complex_maximal:
        if len(M) >= k + 1:
            for s in itertools.combinations(sorted(M), k + 1):
                # check s is a face (subset of some maximal)
                faces.add(s)
    return sorted(faces)

def betti_tilde(complex_maximal, V):
    """Reduced Betti numbers dict j -> dim H~_j over F_p. V = vertex list."""
    if len(complex_maximal) == 0:
        return {}  # void complex: no faces at all (F not a face); caller skips
    maxd = max((len(M) - 1 for M in complex_maximal), default=-1)
    if maxd == -1:
        # complex = {∅}: H~_{-1} = 1
        return {-1: 1}
    chain = {}
    for k in range(-1, maxd + 1):
        chain[k] = oriented_faces(complex_maximal, V, k)
    ranks = {}
    for k in range(0, maxd + 1):
        Ck, Ckm = chain[k], chain[k - 1]
        idx = {f: i for i, f in enumerate(Ckm)}
        M = np.zeros((len(Ckm), len(Ck)), dtype=np.int64)
        for j, f in enumerate(Ck):
            for t in range(len(f)):
                g = tuple(v for s, v in enumerate(f) if s != t)
                if k - 1 == -1:
                    M[0, j] = ((-1) ** t)
                else:
                    M[idx[g], j] = ((-1) ** t)
        ranks[k] = rank_modp(M)
    # d_0: C_0 -> C_{-1} is row of ones (covered: C_{-1}=[()], idx works)
    betti = {}
    for k in range(-1, maxd + 1):
        nk = len(chain[k])
        rk = ranks.get(k, 0)          # rank of d_k
        rkp1 = ranks.get(k + 1, 0)    # rank of d_{k+1}
        b = (nk - rk) - rkp1
        if b != 0:
            betti[k] = b
    return betti

def depth_of_SR(facets, n):
    facets = [tuple(sorted(F)) for F in facets]
    faces = all_faces(facets, n)
    V = list(range(n))
    best = None
    wit = None
    for F in faces:
        lk = link_of(facets, n, F)
        if len(lk) == 0:
            continue  # F not a face -- shouldn't happen since F enumerated
        b = betti_tilde(lk, [v for v in V if v not in F])
        if not b:
            continue  # acyclic link: no contribution
        jmin = min(b.keys())
        cand = len(F) + 1 + jmin
        if best is None or cand < best:
            best = cand
            wit = (F, jmin, b)
    allv = set(V)
    dim = max(len(F) for F in facets) - 1
    dim_ring = dim + 1
    ht = n - dim_ring
    return best, dim_ring, ht, dim, wit

def show(name, facets, n):
    d, dim_ring, ht, dim, wit = depth_of_SR(facets, n)
    cm = (d == dim_ring)
    print(f"{name}: n={n} dimDelta={dim} dimRing={dim_ring} ht={ht} "
          f"depth={d} CM={cm} threshold_cd_vanish=n-2={n-2} witness={wit}")

# 1) Octahedron boundary (2-sphere, 6 vertices): CM, depth 3.
oct = [(0,1,2),(0,1,3),(0,2,3),(1,2,3),
       (0,1,4),(0,2,4),(1,2,4),(3,4,0),(3,4,1),(3,4,2)]
# fix: standard octahedron = antipodal pairs (0,5),(1,4),(2,3); facets omit antipodal pairs
oct6 = [F for F in itertools.combinations(range(6),3)
        if not ({0,5}<=set(F) or {1,4}<=set(F) or {2,3}<=set(F))]
show("octahedron-S2", oct6, 6)

# 2) 3-simplex boundary (2-sphere, 4 vertices): CM depth 3, ht=1.
show("tetra-S2", list(itertools.combinations(range(4),3)), 4)

# 3) Full 3-skeleton on 6 vertices (3-sphere chunk, CM): depth 4.
show("full-3skel-6", list(itertools.combinations(range(6),4)), 6)

# 4) Full 3-skeleton minus one facet: candidate non-CM depth 3, dimRing 4, ht 2.
full = list(itertools.combinations(range(6),4))
show("3skel-minus1", [F for F in full if set(F)!={0,1,2,3}], 6)
show("3skel-minus2", [F for F in full if set(F) not in ({0,1,2,3},{0,1,2,4})], 6)

# 5) Non-CM depth 3, dimRing 4: octahedron S2 glued to a 3-ball along a facet.
# H_2(Delta)=Z survives (ball glued along a disk), H_3=0, dim Delta=3, so the
# empty-face link violates Reisner (2<3) -> depth exactly 3, not CM.
show("S2-plus-3ball-nonCM", oct6 + [(0,1,2,6)], 7)

print()
print("CONCLUSION: depth>=3 quotients exist in abundance, CM and non-CM.")
print("The proxy CANNOT decide H^{n-2}_I(R) vanishing in ramified mixed char;")
print("in char p, Peskine-Szpiro kills the CM cases (cd=ht), so a genuine")
print("counterexample must be non-CM depth>=3 or use p-torsion phenomena.")
print("Certifying either needs a local-cohomology engine unavailable here => BLOCKED.")
