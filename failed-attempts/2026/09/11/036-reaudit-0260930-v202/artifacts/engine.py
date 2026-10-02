"""Engine for lane 745 target: 3-uniform clutter Hochster regularity over Q and F2.

Conventions:
  H: list of 3-subsets of {0..n-1} as int bitmasks.
  Delta(H): independence complex; W-face iff no edge e with e subset of F.
  Hochster: beta_{i,W}(S/I) = dim H~_{|W|-i-1}(Delta_W).
  reg(S/I;k) = max{h+1 : exists W with H~_h(Delta_W;k) != 0} (h>=1 matters; h=0 gives 1).
  tau = min vertex-cover size. nu_ind = 1 iff every disjoint edge pair is
    "witnessed" by a third edge contained in the pair union (and E nonempty).
  2-collage: C subset of E with every edge sharing >=2 vertices with some c in C;
    Ha-Woodroofe cap: reg(S/I) <= 2|C| for 3-uniform.
"""
import itertools
import numpy as np

# ---------------- basic combinatorics ----------------

def popcount(m):
    return bin(m).count("1")

def submasks(w):
    s = w
    while True:
        yield s
        if s == 0:
            break
        s = (s - 1) & w

def mask_of(S):
    m = 0
    for v in S:
        m |= 1 << v
    return m

def edges_of(triples):
    return [mask_of(t) for t in triples]

# ---------------- tau / nu ----------------

def min_cover(E, n):
    """Min |C| with every edge meeting C (e & cm != 0)."""
    for k in range(n + 1):
        for C in itertools.combinations(range(n), k):
            cm = mask_of(C)
            if all((e & cm) != 0 for e in E):
                return k
    return n

def has_cover_of_size(E, n, k):
    for C in itertools.combinations(range(n), k):
        cm = mask_of(C)
        if all((e & cm) != 0 for e in E):
            return True, C
    return False, None

def disjoint_pairs(E):
    out = []
    for i in range(len(E)):
        for j in range(i + 1, len(E)):
            if E[i] & E[j] == 0:
                out.append((i, j))
    return out

def unwitnessed_disjoint_pairs(E):
    """Disjoint pairs (i,j) with NO third edge contained in E[i]|E[j]."""
    bad = []
    for (i, j) in disjoint_pairs(E):
        u = E[i] | E[j]
        wit = [k for k in range(len(E))
               if k != i and k != j and (E[k] | u) == u]
        if not wit:
            bad.append((i, j))
    return bad

def induced_nu_is_one(E):
    return len(E) > 0 and len(unwitnessed_disjoint_pairs(E)) == 0

# ---------------- 2-collage ----------------

def min_2collage(E):
    """Min |C|, C subset of edge indices, s.t. every edge shares >=2 verts with some c."""
    m = len(E)
    share2 = [[popcount(E[i] & E[j]) >= 2 for j in range(m)] for i in range(m)]
    for k in range(m + 1):
        for C in itertools.combinations(range(m), k):
            if all(any(share2[i][c] for c in C) for i in range(m)):
                return k, C
    return m, tuple(range(m))

# ---------------- face precompute ----------------

def face_array(E, n):
    """face[S] True iff no edge e subset of S, for all S in 0..2^n-1."""
    N = 1 << n
    S = np.arange(N, dtype=np.int64)
    ok = np.ones(N, dtype=bool)
    for e in E:
        ok &= ((S & np.int64(e)) != np.int64(e))
    return ok

# ---------------- homology ----------------

def faces_by_dim(W, face, n):
    """Return dict dim -> list of masks (nonempty faces of Delta_W)."""
    by = {}
    for F in submasks(W):
        if F == 0:
            continue
        if face[F]:
            d = popcount(F) - 1
            by.setdefault(d, []).append(F)
    return by

def boundary_matrix(by, d, signed=True):
    """Return (rows=n_{d-1}, cols=n_d) array of partial_d.
    signed=True: entries (-1)^i (correct over Z / odd characteristic).
    signed=False: 0/1 entries (valid only over GF(2)). None if trivial."""
    if d not in by or (d - 1) not in by:
        return None
    low = by[d - 1]
    high = by[d]
    idx = {F: r for r, F in enumerate(low)}
    A = np.zeros((len(low), len(high)), dtype=np.int64)
    for j, F in enumerate(high):
        verts = []
        g = F
        while g:
            lsb = g & (-g)
            verts.append(lsb)
            g ^= lsb
        for i, lsb in enumerate(verts):
            G = F ^ lsb
            A[idx[G], j] = -1 if (signed and (i % 2 == 1)) else 1
    return A

def rank_gf2(A):
    """A: (r x c) 0/1 array. Rank over GF(2) via python-int bitsets."""
    if A is None or A.size == 0:
        return 0
    r, c = A.shape
    rows = []
    for i in range(r):
        v = 0
        for j in np.nonzero(A[i])[0]:
            v |= 1 << int(j)
        if v:
            rows.append(v)
    rank = 0
    col = 0
    # find max col
    piv = {}
    for v in rows:
        w = v
        for b in sorted(piv, reverse=True):
            if (w >> b) & 1:
                w ^= piv[b]
        if w:
            b = w.bit_length() - 1
            piv[b] = w
            rank += 1
    return rank

def rank_modp(A, p):
    """Exact rank over F_p via vectorized elimination (int64)."""
    if A is None or A.size == 0:
        return 0
    M = (A % p).astype(np.int64)
    r, c = M.shape
    rank = 0
    for j in range(c):
        piv = -1
        for i in range(rank, r):
            if M[i, j] % p != 0:
                piv = i
                break
        if piv < 0:
            continue
        if piv != rank:
            M[[piv, rank]] = M[[rank, piv]]
        inv = pow(int(M[rank, j] % p), -1, p)
        M[rank] = (M[rank] * inv) % p
        for i in range(r):
            if i != rank and M[i, j] % p != 0:
                M[i] = (M[i] - M[i, j] * M[rank]) % p
        rank += 1
        if rank == r:
            break
    return rank

def homology_dims(W, face, n, field="f2", p=1000000007, maxdim=None):
    """Reduced homology dims {h>=1: dim} of Delta_W over field ('f2' or 'qp')."""
    by = faces_by_dim(W, face, n)
    if not by:
        return {}
    top = max(by)
    rk = {}
    for d in range(1, top + 2):
        A = boundary_matrix(by, d)
        if A is None:
            rk[d] = 0
        elif field == "f2":
            rk[d] = rank_gf2(A)
        else:
            rk[d] = rank_modp(A, p)
    out = {}
    for d in range(1, top + 1):
        nd = len(by.get(d, []))
        h = nd - rk.get(d, 0) - rk.get(d + 1, 0)
        if h:
            out[d] = h
    return out

# ---------------- regularity / betti ----------------

def regularity(E, n, field="f2", p=1000000007, minsize=0, verbose_witness=False):
    """reg(S/I) over field; optionally return attaining W list."""
    face = face_array(E, n)
    best = 1
    wit = []
    N = 1 << n
    for W in range(N):
        if popcount(W) < minsize:
            continue
        hdim = homology_dims(W, face, n, field=field, p=p)
        for h in hdim:
            if h + 1 > best:
                best = h + 1
                wit = [(W, h, hdim[h])]
            elif h + 1 == best and h + 1 > 1 and verbose_witness:
                wit.append((W, h, hdim[h]))
    if verbose_witness:
        return best, wit
    return best

def betti_table(E, n, field="f2", p=1000000007):
    """beta[i][j] graded Betti numbers of S/I. Returns dict (i,j)->dim."""
    face = face_array(E, n)
    tab = {}
    N = 1 << n
    for W in range(N):
        m = popcount(W)
        if m == 0:
            continue
        hdim = homology_dims(W, face, n, field=field, p=p)
        for h, d in hdim.items():
            i = m - h - 1
            j = m - i  # = h+1
            if i >= 0:
                tab[(i, j)] = tab.get((i, j), 0) + d
    return tab

def fmt_betti(tab):
    lines = []
    for k in sorted(tab):
        lines.append(f"beta_{k[0]},{k[1]} = {tab[k]}")
    return "\n".join(lines)

def snf_torsion_cert(W, face, n, h):
    """Integer SNF of partial_{h+1} restricted... return SNF diag of boundary maps
    around degree h to certify torsion in H~_h(Delta_W;Z). Uses sympy."""
    from sympy import Matrix
    from sympy.matrices.normalforms import smith_normal_form
    by = faces_by_dim(W, face, n)
    out = {}
    for d in (h, h + 1):
        A = boundary_matrix(by, d)
        if A is None:
            out[d] = []
            continue
        M = Matrix(A.tolist())
        S = smith_normal_form(M, domain=None)
        dg = [abs(int(S[i, i])) for i in range(min(S.shape))]
        out[d] = dg
    return out
