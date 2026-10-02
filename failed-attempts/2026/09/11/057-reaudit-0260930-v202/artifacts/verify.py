"""Verify the falsity of the Golod claim for facet-glued G9 = S #_F O.

S = 6-vertex stacked 2-sphere on {0..5} (two stackings, keeping facet 012).
O = octahedron boundary on {0,1,2,6,7,8}, opposite pairs (0,6),(1,7),(2,8).
G9 = (S \ {012}) u (O \ {012}), 9 vertices, 14 facets.

Model: R(K) = Lambda[u] (x) k[K], d(u_i)=v_i, multidegree-J piece C(J)
with basis e_L = u_{J\L} v_L for L subset J, L a face. All linear algebra
exact over Q (Fractions). Headline: nonzero Baskakov product of the two
missing-edge classes [{0,6}] * [{1,7}] = [e_{01}] != 0 on K_{0167}=4-cycle.
"""
from fractions import Fraction
from itertools import combinations

# ---------- complex definition ----------
# Stacked 6-vertex sphere S on 0..5 (stack 4 onto 013, then 5 onto 023)
S_FACETS = [(0,1,2),(1,2,3),(0,1,4),(0,3,4),(1,3,4),(0,2,5),(0,3,5),(2,3,5)]
# Octahedron boundary on {0,1,2,6,7,8}, opposite pairs (0,6),(1,7),(2,8)
O_FACETS = [(0,1,2),(0,1,8),(0,2,7),(0,7,8),(1,2,6),(1,6,8),(2,6,7),(6,7,8)]
F = (0,1,2)
G9_FACETS = sorted(set(S_FACETS) - {F} | set(O_FACETS) - {F})
VERTS = list(range(9))
print("G9 facets (%d):" % len(G9_FACETS), G9_FACETS)
assert len(G9_FACETS) == 14

FACET_SET = set(G9_FACETS)
EDGES = sorted({tuple(sorted((a,b))) for f in G9_FACETS
                for a, b in combinations(f, 2)})
FACES = {()} | {(v,) for v in VERTS} | set(EDGES) | set(G9_FACETS)
print("edges:", len(EDGES))

# ---------- sphere checks ----------
# every edge in exactly 2 facets
from collections import Counter
cnt = Counter()
for f in G9_FACETS:
    for a, b in combinations(f, 2):
        cnt[tuple(sorted((a,b)))] += 1
assert set(cnt) == set(EDGES) and all(v == 2 for v in cnt.values()), "not a manifold"
euler = 9 - len(EDGES) + len(G9_FACETS)
print("Euler =", euler); assert euler == 2
# links are cycles
for v in VERTS:
    nb = sorted(u for u in VERTS if u != v and tuple(sorted((u,v))) in FACET_SET or
                tuple(sorted((u,v))) in set(EDGES))
    ledges = [e for e in EDGES if v not in e and tuple(sorted(e + (v,))) in FACET_SET]
    deg = Counter()
    for a, b in ledges:
        deg[a] += 1; deg[b] += 1
    assert set(deg) == set(nb) and all(d == 2 for d in deg.values()), ("link fail", v)
    # connected link
    seen, stack = {nb[0]}, [nb[0]]
    adj = {u: [] for u in nb}
    for a, b in ledges:
        adj[a].append(b); adj[b].append(a)
    while stack:
        x = stack.pop()
        for y in adj[x]:
            if y not in seen:
                seen.add(y); stack.append(y)
    assert seen == set(nb), ("link disconnected", v)
print("manifold S^2: every edge in 2 facets, every link a cycle. OK")

# ---------- exact linear algebra over Q ----------
def mat_rank(M):
    M = [[Fraction(x) for x in row] for row in M]
    m, n = (len(M), len(M[0])) if M else (0, 0)
    r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if M[i][c] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        iv = M[r][c]
        for i in range(m):
            if i != r and M[i][c] != 0:
                f = M[i][c] / iv
                for j in range(c, n):
                    M[i][j] -= f * M[r][j]
        r += 1
    return r

def nullspace(M):
    """Basis of ker(M) for m x n matrix (vectors length n)."""
    M = [[Fraction(x) for x in row] for row in M]
    m, n = (len(M), len(M[0])) if M else (0, 0)
    piv = {}
    r = 0
    rowM = [row[:] for row in M]
    for c in range(n):
        p = next((i for i in range(r, m) if rowM[i][c] != 0), None)
        if p is None:
            continue
        rowM[r], rowM[p] = rowM[p], rowM[r]
        iv = rowM[r][c]
        for j in range(n):
            rowM[r][j] /= iv
        for i in range(m):
            if i != r and rowM[i][c] != 0:
                f = rowM[i][c]
                for j in range(n):
                    rowM[i][j] -= f * rowM[r][j]
        piv[c] = r
        r += 1
    free = [c for c in range(n) if c not in piv]
    basis = []
    for f in free:
        v = [Fraction(0)] * n
        v[f] = Fraction(1)
        for c, i in piv.items():
            v[c] = -rowM[i][f]
        basis.append(v)
    return basis

def in_col_space(G, z):
    """Is z (length m) in column space of m x k matrix G?"""
    m = len(G)
    k = len(G[0]) if m else 0
    # augment [G | z], check ranks equal
    A = [list(G[i]) + [z[i]] for i in range(m)]
    G2 = [list(row) for row in G]
    return mat_rank(A) == mat_rank(G2)

def cohom_reps(Dup, Ddn):
    """Representatives of ker(Dup)/im(Ddn). Dup: a x n, Ddn: n x k."""
    n = len(Dup[0]) if Dup else (len(Ddn) if Ddn else 0)
    ker = nullspace(Dup)
    reps = []
    if Ddn and Ddn[0]:
        G = Ddn
    else:
        G = []
    for v in ker:
        # test v mod span(reps, cols of G)
        if G:
            m = len(G)
            B = [list(G[i]) + [r[i] for r in reps] for i in range(m)]
        else:
            m = n
            B = [[r[i] for r in reps] for i in range(m)] if reps else [[Fraction(0)] * 0 for _ in range(m)]
        if not in_col_space(B, v):
            reps.append(v)
    return reps

# ---------- simplicial homology of G9 (sanity: S^2) ----------
def bnd_sign(face, sub):
    # face sorted tuple, sub = face minus one vertex; sign (-1)^position
    j = list(face).index(next(iter(set(face) - set(sub))))
    return Fraction(-1 if j % 2 else 1)

V = [(v,) for v in VERTS]
d1 = [[bnd_sign(e, v) if set(v) <= set(e) else Fraction(0) for e in EDGES] for v in V]
d2 = [[bnd_sign(f, e) if set(e) <= set(f) else Fraction(0) for f in G9_FACETS] for e in EDGES]
r1, r2 = mat_rank(d1), mat_rank(d2)
H0 = 9 - r1; H1 = (len(EDGES) - r1) - r2; H2 = len(G9_FACETS) - r2
print("simplicial homology dims (H0,H1,H2) =", (H0, H1, H2))
assert (H0, H1, H2) == (1, 0, 1)

# ---------- R(K) multidegree pieces ----------
def piece(J, s):
    return sorted([L for L in FACES if len(L) == s and set(L) <= set(J)],
                  key=lambda t: tuple(t))

def diff_mat(J, s):
    """d: grade s -> s+1 within C(J)."""
    dom = piece(J, s); cod = piece(J, s + 1)
    ci = {L: i for i, L in enumerate(cod)}
    A = set(J)
    M = [[Fraction(0)] * len(dom) for _ in cod]
    for c, L in enumerate(dom):
        rest = sorted(A - set(L))
        for i in rest:
            U = tuple(sorted(tuple(L) + (i,)))
            if U in ci:
                pos = sum(1 for a in rest if a < i)
                M[ci[U]][c] = Fraction(1 if pos % 2 == 0 else -1)
    return M

def shuffle_sign(A, C):
    A, C = sorted(A), sorted(C)
    inv = sum(1 for a in A for c in C if a > c)
    return 1 if inv % 2 == 0 else -1

def prod_vec(J1, v1, J2, v2):
    """Product of explicit vectors v1 in C(J1), v2 in C(J2), J1 cap J2 = {}."""
    assert not (set(J1) & set(J2))
    J = tuple(sorted(set(J1) | set(J2)))
    out = {}
    P1 = [L for s in range(5) for L in piece(J1, s)]
    P2 = [L for s in range(5) for L in piece(J2, s)]
    for L, c1 in zip(P1, v1):
        if c1 == 0:
            continue
        for Mf, c2 in zip(P2, v2):
            if c2 == 0:
                continue
            U = tuple(sorted(tuple(L) + tuple(Mf)))
            if len(U) != len(L) + len(Mf):
                continue
            if U not in FACES:
                continue
            sgn = shuffle_sign(set(J1) - set(L), set(J2) - set(Mf))
            out[U] = out.get(U, Fraction(0)) + sgn * c1 * c2
    return J, out

def vec_in_piece(J, s, d):
    P = piece(J, s)
    return [d.get(L, Fraction(0)) for L in P]

def apply_mat(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]

# d^2 = 0 for every multidegree
from itertools import chain
ALLJ = [tuple(sorted(S)) for r in range(10) for S in combinations(VERTS, r)]
for J in ALLJ:
    for s in range(4):
        A = diff_mat(J, s); B = diff_mat(J, s + 1)
        if A and B and A[0] and B[0]:
            n, m, k = len(A[0]), len(A), len(B)
            for c in range(n):
                col = [A[i][c] for i in range(m)]
                img = apply_mat(B, col)
                assert all(x == 0 for x in img), ("d^2 fail", J, s)
print("d^2 = 0 on all 512 multidegree pieces. OK")

# Leibniz check on all disjoint pairs with |I|,|J| <= 3 (exhaustive) + random
import random
random.seed(7)
pairs = []
subs = [tuple(sorted(S)) for r in range(4) for S in combinations(VERTS, r)]
Sset = set(subs)
for I in subs:
    for J in subs:
        if not (set(I) & set(J)):
            pairs.append((I, J))
pairs += [tuple(sorted(random.sample(VERTS, random.randint(0, 9)))),
          tuple(sorted(random.sample(VERTS, random.randint(0, 9))))] * 0
print("Leibniz pairs (small, exhaustive):", len(pairs))
for I, J in pairs:
    K = tuple(sorted(set(I) | set(J)))
    for s1 in range(4):
        for s2 in range(4):
            P1, P2 = piece(I, s1), piece(J, s2)
            if not P1 or not P2:
                continue
            d1m, d2m = diff_mat(I, s1), diff_mat(J, s2)
            dKm = diff_mat(K, s1 + s2)
            PK = piece(K, s1 + s2)
            PK1 = piece(K, s1 + s2 + 1)
            ki = {L: i for i, L in enumerate(PK)}
            ki1 = {L: i for i, L in enumerate(PK1)}
            # test on basis pairs (limit: first few if many)
            for L in P1[:6]:
                for Mf in P2[:6]:
                    if set(L) & set(Mf):
                        continue
                    U = tuple(sorted(tuple(L) + tuple(Mf)))
                    if U not in FACES:
                        continue
                    sgn = shuffle_sign(set(I) - set(L), set(J) - set(Mf))
                    # d(x.y) vs dx.y + (-1)^{|x|} x.dy ; |x| = s1-|I|
                    dl = [Fraction(0)] * len(P1)
                    dl[P1.index(L)] = Fraction(1)
                    dm = [Fraction(0)] * len(P2)
                    dm[P2.index(Mf)] = Fraction(1)
                    dx = apply_mat(d1m, dl) if d1m and d1m[0] else [Fraction(0)] * 0
                    dy = apply_mat(d2m, dm) if d2m and d2m[0] else [Fraction(0)] * 0
                    P1n = piece(I, s1 + 1); P2n = piece(J, s2 + 1)
                    lhs = [Fraction(0)] * len(PK1)
                    rest = sorted(set(K) - set(U))
                    for i in rest:
                        W = tuple(sorted(tuple(U) + (i,)))
                        if W in ki1:
                            pos = sum(1 for a in rest if a < i)
                            lhs[ki1[W]] += (Fraction(1 if pos % 2 == 0 else -1)) * sgn
                    rhs = [Fraction(0)] * len(PK1)
                    for Ln, c in zip(P1n, dx):
                        if c == 0 or set(Ln) & set(Mf):
                            continue
                        W = tuple(sorted(tuple(Ln) + tuple(Mf)))
                        if W in ki1 and len(W) == len(Ln) + len(Mf):
                            rhs[ki1[W]] += c * shuffle_sign(set(I) - set(Ln), set(J) - set(Mf))
                    hx = s1 - len(I)
                    sgnx = 1 if hx % 2 == 0 else -1
                    for Mn, c in zip(P2n, dy):
                        if c == 0 or set(L) & set(Mn):
                            continue
                        W = tuple(sorted(tuple(L) + tuple(Mn)))
                        if W in ki1 and len(W) == len(L) + len(Mn):
                            rhs[ki1[W]] += sgnx * c * shuffle_sign(set(I) - set(L), set(J) - set(Mn))
                    assert lhs == rhs, ("Leibniz fail", I, J, L, Mf)
print("Leibniz rule verified on all small disjoint pairs. OK")

# ---------- missing edges ----------
EDGSET = set(EDGES)
MISSING = [tuple(sorted(p)) for p in combinations(VERTS, 2) if tuple(sorted(p)) not in EDGSET]
print("missing edges (%d):" % len(MISSING), MISSING)
assert (0, 6) in MISSING and (1, 7) in MISSING
assert (0, 1) in EDGSET and (1, 6) in EDGSET and (6, 7) in EDGSET and (0, 7) in EDGSET
# no S-side facet can sit inside {0,1,6,7}: S-facets use only {0..5}
for f in S_FACETS:
    assert not set(f) <= {0, 1, 6, 7}
# no facet of G9 inside {0,1,6,7}
assert not [f for f in G9_FACETS if set(f) <= {0, 1, 6, 7}]
print("K_{0167} = hollow 4-cycle 0-1-6-7-0 confirmed.")

# ---------- headline nonzero product ----------
I, Jp = (0, 6), (1, 7)
K = (0, 1, 6, 7)
# class a = [e_0] in C(I) grade 1; check closed, nontrivial
dI = diff_mat(I, 1)   # grade1 -> grade2
PI1 = piece(I, 1)
a = [Fraction(1 if L == (0,) else 0) for L in PI1]
assert all(x == 0 for x in apply_mat(dI, a)), "a not closed"
assert not in_col_space(diff_mat(I, 0), a), "a exact?!"
# class b = [e_1] in C(Jp)
dJ = diff_mat(Jp, 1)
PJ1 = piece(Jp, 1)
b = [Fraction(1 if L == (1,) else 0) for L in PJ1]
assert all(x == 0 for x in apply_mat(dJ, b)), "b not closed"
assert not in_col_space(diff_mat(Jp, 0), b), "b exact?!"
# product
PIfull = [L for s in range(5) for L in piece(I, s)]
PJfull = [L for s in range(5) for L in piece(Jp, s)]
av = [Fraction(1 if L == (0,) else 0) for L in PIfull]
bv = [Fraction(1 if L == (1,) else 0) for L in PJfull]
Jprod, pd = prod_vec(I, av, Jp, bv)
assert Jprod == K and pd == {(0, 1): Fraction(1)}, pd
print("product e_0 . e_1 =", pd)
# closed in C(K)?
pv = vec_in_piece(K, 2, pd)
assert all(x == 0 for x in apply_mat(diff_mat(K, 2), pv)), "product not closed"
# exact in C(K)? solve d_{grade1} x = pv
G = diff_mat(K, 1)
exact = in_col_space(G, pv)
print("product cocycle e_{01} exact?", exact)
assert not exact, "product vanished - target would survive"
# hand-checkable certificate: image equations sum to 0 = 1
print("image of d: vertices -> edges:")
for v, row in zip(piece(K, 1), list(zip(*G))):
    print("  d e_%d =" % v[0], " + ".join(
        "%s%se_%d%d" % (("+" if c > 0 else "-"), ("" if abs(c) == 1 else "%s*" % abs(c)), L[0], L[1])
        for L, c in zip(piece(K, 2), row) if c != 0))
print("e01 = d(sum c_v e_v) needs c0+c1=1,c0+c7=0,c1+c6=0,c6+c7=0 -> 0=1. NONEXACT.")

# ---------- wider scan: all disjoint missing-edge pairs ----------
nonzero = []
for A in MISSING:
    for B in MISSING:
        if set(A) & set(B):
            continue
        U = tuple(sorted(set(A) | set(B)))
        aI = [L for s in range(5) for L in piece(A, s)]
        bJ = [L for s in range(5) for L in piece(B, s)]
        for la in A:
            for lb in B:
                va = [Fraction(1 if L == (la,) else 0) for L in aI]
                vb = [Fraction(1 if L == (lb,) else 0) for L in bJ]
                # closed?
                if any(x != 0 for x in apply_mat(diff_mat(A, 1), [va[i] for i in range(len(piece(A,1)))][:0] or [Fraction(0)]*len(piece(A,2)))):
                    pass
                _, p = prod_vec(A, va, B, vb)
                if not p:
                    continue  # zero cochain => zero class
                s = len(next(iter(p)))
                pv2 = vec_in_piece(U, s, p)
                if any(x != 0 for x in apply_mat(diff_mat(U, s), pv2)):
                    raise SystemExit(("product not closed?!", A, B))
                if not in_col_space(diff_mat(U, s - 1), pv2):
                    nonzero.append((A, la, B, lb, U, dict(p)))
print("nonzero products among disjoint missing-edge pairs:", len(nonzero))
for n in nonzero[:12]:
    print("  [%s via %s] x [%s via %s] -> %s : %s" % (n[0], n[1], n[2], n[3], n[4], n[5]))

# ---------- Hochster Betti snapshot ----------
tot = 0
betti = {}
for J in ALLJ:
    for s in range(4):
        P = piece(J, s)
        if not P:
            continue
        Dup = diff_mat(J, s)
        Ddn = diff_mat(J, s - 1) if s > 0 else [[Fraction(0)] * 0 for _ in P]
        ker_dim = len(P) - (mat_rank(Dup) if Dup and Dup[0] else 0)
        im_dim = mat_rank(Ddn) if Ddn and Ddn[0] else 0
        dk = ker_dim - im_dim
        assert dk >= 0, ("negative homology?!", J, s)
        if dk and (J or s):
            tot += dk
            betti[(J, s)] = dk
print("total Tor^+ dim over Q =", tot)
# Tor bidegrees: cohomological degree = |J| - s... (s = #v-part)
pairs = sorted({(len(J), s) for (J, s) in betti})
print("nonzero Tor multidegree count:", len(betti), "; (|J|,s) cells:", pairs)

# ---------- top-class (Poincare) search: missing edge x complementary cycle ----------
found = []
FULL = tuple(VERTS)
for A in MISSING:
    C = tuple(sorted(set(VERTS) - set(A)))
    reps = cohom_reps(diff_mat(C, 2), diff_mat(C, 1))
    aI = [L for s in range(5) for L in piece(A, s)]
    for la in A:
        va = [Fraction(1 if L == (la,) else 0) for L in aI]
        for r in reps:
            full_dict_rep = {L: c for L, c in zip(piece(C, 2), r) if c != 0}
            # embed r into full C(C) vector
            Cfull = [L for s in range(5) for L in piece(C, s)]
            vr = [full_dict_rep.get(L, Fraction(0)) for L in Cfull]
            _, p = prod_vec(A, va, C, vr)
            if not p:
                continue
            s = len(next(iter(p)))
            pvF = vec_in_piece(FULL, s, p)
            if any(x != 0 for x in apply_mat(diff_mat(FULL, s), pvF)):
                continue
            if not in_col_space(diff_mat(FULL, s - 1), pvF):
                found.append((A, la, dict(p)))
                break
        if found and found[-1][0] == A:
            break
print("Poincare dual pairs into top class:", len(found))
for f in found[:6]:
    print("  edge", f[0], "via", f[1], "x complementary cycle ->", f[2])

print("VERIFY_OK")
