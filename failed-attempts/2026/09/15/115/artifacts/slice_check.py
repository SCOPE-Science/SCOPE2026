"""Bounded recovery test for lane-20354 (n=2 exhaustive + feasibility count).

Checks:
 (a) dimension / solvability of D(alpha)=rho(sigma),
 (b) slice (=partition) rank of each symmetric trilinear sigma at n=2,
 (c) max_{+-1 f} correlation proxy per alpha (exact brute force, |G|=4),
 (d) feasibility count showing n=3 exhaustive search is out of reach.
"""
import itertools
import numpy as np

n = 2
G = list(range(4))  # F2^2 as 2-bit ints; addition = xor
coords = np.array([[(g >> 0) & 1, (g >> 1) & 1] for g in G], dtype=np.int64)  # 4x2

# ---- basis enumerations ----
# sigma free coeffs: sorted multisets (a<=b<=c) from {0,1}: 4 of them
multisets3 = [(a, b, c) for a in range(n) for b in range(a, n) for c in range(b, n)]
# alpha free coeffs: (sorted 5-tuple) x i6
multisets5 = [t for t in itertools.combinations_with_replacement(range(n), 5)]
print("dim sigma:", len(multisets3), "dim alpha:", len(multisets5) * n)

def build_sigma_tensor(v):
    """v: length-4 coeff vector -> symmetric 2x2x2 tensor S with S[i,j,k]=v[sort]."""
    S = np.zeros((2, 2, 2), dtype=np.int64)
    for idx, (a, b, c) in enumerate(multisets3):
        for (i, j, k) in set(itertools.permutations((a, b, c))):
            S[i, j, k] = v[idx]
    return S % 2

def build_alpha_tensor(w):
    """w: length-12 coeff vector -> 2^6 tensor A symmetric in first 5 slots.
    free index: ((sorted 5-tuple), i6). A[j1..j6] = w[sort(j1..j5), j6]."""
    A = np.zeros((2,) * 6, dtype=np.int64)
    for idx, t in enumerate(multisets5):
        for i6 in range(n):
            val = w[idx * n + i6]
            for p in set(itertools.permutations(t)):
                A[p + (i6,)] = val
    return A % 2

def rho_tensor(S):
    """rho[i1..i6] = sum_{I in C([4],2)} S[ip,iq,i5]*S[ir,is,i6]."""
    R = np.zeros((2,) * 6, dtype=np.int64)
    pairs = list(itertools.combinations(range(4), 2))
    for tup in itertools.product(range(n), repeat=6):
        s = 0
        for (p, q) in pairs:
            rest = [t for t in range(4) if t not in (p, q)]
            r, ss = rest
            s += S[tup[p], tup[q], tup[4]] * S[tup[r], tup[ss], tup[5]]
        R[tup] = s % 2
    return R

def D_tensor(A):
    D = np.zeros((2,) * 6, dtype=np.int64)
    for tup in itertools.product(range(n), repeat=6):
        a = tup[:4] + (tup[4], tup[5])
        b = tup[:4] + (tup[5], tup[4])
        D[tup] = (A[a] + A[b]) % 2
    return D

# ---- build D matrix (64 x 12) over F2 ----
dimA = len(multisets5) * n  # 12
cols = []
for j in range(dimA):
    w = np.zeros(dimA, dtype=np.int64)
    w[j] = 1
    cols.append(D_tensor(build_alpha_tensor(w)).ravel())
M = np.stack(cols, axis=1) % 2  # 64x12
print("D matrix shape:", M.shape, "rank:", np.linalg.matrix_rank(M.astype(float) % 2))

def gf2_col_space_contains(M, b):
    """Check b in col-space of M over F2 via augmented elimination."""
    A = np.concatenate([M.copy(), b.reshape(-1, 1)], axis=1) % 2
    r, c = 0, 0
    piv = [-1] * M.shape[1]
    while r < A.shape[0] and c < M.shape[1]:
        pivrow = -1
        for i in range(r, A.shape[0]):
            if A[i, c]:
                pivrow = i
                break
        if pivrow == -1:
            c += 1
            continue
        A[[r, pivrow]] = A[[pivrow, r]]
        for i in range(A.shape[0]):
            if i != r and A[i, c]:
                A[i] ^= A[r]
        piv[c] = r
        r += 1
        c += 1
    for i in range(r, A.shape[0]):
        if A[i, -1] and not A[i, :-1].any():
            return False
    return True

def slice_rank_sym(S):
    if not S.any():
        return 0
    F = S.reshape(2, 4)  # mode-1 flattening
    # rank over F2 of 2x4: 1 iff all 2x2 minors vanish (rows dependent)
    # rows r0,r1 in F2^4: dependent iff r0==0 or r1==0 or r0==r1
    if (F[0] == 0).all() or (F[1] == 0).all() or (F[0] == F[1]).all():
        return 1
    return 2

# ---- enumerate all sigma (16) ----
all_rho = {}
solvable = {}
slices = {}
for code in range(16):
    v = np.array([(code >> i) & 1 for i in range(4)], dtype=np.int64)
    S = build_sigma_tensor(v)
    R = rho_tensor(S)
    b = R.ravel() % 2
    ok = gf2_col_space_contains(M, b)
    solvable[code] = ok
    slices[code] = slice_rank_sym(S)
    all_rho[code] = R

print("solvable count:", sum(solvable.values()), "/16")
print("slice-rank histogram:", {r: sum(1 for c in range(16) if slices[c] == r) for r in (0, 1, 2)})
zero_rho = [c for c in range(16) if not all_rho[c].any()]
print("codes with rho==0:", zero_rho, "their slice ranks:", [slices[c] for c in zero_rho])

# ---- exact max correlation over +-1 f ----
# precompute g_f(a) = E_x Delta^6 f(x,a) for all 16 f, all 4096 a-tuples
atuples = np.array(list(itertools.product(G, repeat=6)), dtype=np.int64)  # 4096x6
xs = np.array(G, dtype=np.int64)
# coefficient table: for each a-tuple and each omega in {0,1}^6, index x+sum omega_i a_i
omegas = np.array(list(itertools.product([0, 1], repeat=6)), dtype=np.int64)  # 64x6
# lin[a, w] = xor-sum of selected a_i = group element (as int 0..3)
lin = np.zeros((len(atuples), 64), dtype=np.int64)
for j, w in enumerate(omegas):
    sel = atuples[:, w.astype(bool)] if w.any() else np.zeros((len(atuples), 0), dtype=np.int64)
    v = np.zeros(len(atuples), dtype=np.int64)
    for k in range(sel.shape[1]):
        v ^= sel[:, k]
    lin[:, j] = v
# f table: 16 x 4 values +-1
fvals = np.array([[1 if (f >> x) & 1 else -1 for x in G] for f in range(16)], dtype=np.int64)
# Delta(x,a) = prod_w f(x xor lin[a,w]); g[f,a] = mean_x
g = np.zeros((16, len(atuples)))
for f in range(16):
    fv = fvals[f]
    for xi, x in enumerate(xs):
        idx = (x ^ lin)  # 4096x64
        g[f] += np.prod(fv[idx], axis=1)
    g[f] /= 4.0
# alpha sign table: 4096 alphas x 4096 a-tuples, (-1)^{alpha(a)}
# alpha evaluation: A tensor flattened in same ravel order (C-order over product(range(2),repeat=6) of *coordinates*? careful)
# Our atuples are group elements; expand each coordinate pair via coords lookup.
Acoords = coords[atuples]  # 4096 x 6 x 2  (bit coords of each of the 6 group args)
alpha_sign = np.zeros((2 ** dimA, len(atuples)))
# alpha evaluation: alpha(a_1..a_6) = sum_{c in {0,1}^6} A[c] prod_i bit(a_i, c_i).
Cidx = np.array(list(itertools.product(range(n), repeat=6)), dtype=np.int64)  # 64x6
# Mon[t, cidx] = prod_i Acoords[t, i, Cidx[cidx, i]]  (4096 x 64), precompute once
Mon = np.ones((len(atuples), 64), dtype=np.int64)
for kk in range(6):
    Mon *= Acoords[:, kk, :][:, Cidx[:, kk]]
for acode in range(2 ** dimA):
    w = np.array([(acode >> j) & 1 for j in range(dimA)], dtype=np.int64)
    A = build_alpha_tensor(w)
    Aval = A[tuple(Cidx[:, k] for k in range(6))]  # 64-vector
    aval = (Mon @ Aval) % 2
    alpha_sign[acode] = np.where(aval == 0, 1.0, -1.0)
corr = np.abs((g @ alpha_sign.T) / len(atuples))  # 16 x 4096
maxcorr = corr.max(axis=0)
print("global maxcorr range over alphas:", float(maxcorr.min()), float(maxcorr.max()))
# per sigma: max over solving alphas of maxcorr
for code in range(16):
    b = all_rho[code].ravel() % 2
    best = -1.0
    nsol = 0
    for acode in range(2 ** dimA):
        w = np.array([(acode >> j) & 1 for j in range(dimA)], dtype=np.int64)
        if ((D_tensor(build_alpha_tensor(w)).ravel() % 2) == b).all():
            nsol += 1
            if maxcorr[acode] > best:
                best = maxcorr[acode]
    print(f"sigma code {code:2d} slice={slices[code]} solvable={solvable[code]} nsol={nsol} best_maxcorr={best:.3f}")
print("n=3 feasibility: dim sigma =", 10, " dim alpha =", 63,
      "-> exhaustive pairs =", 2 ** 10 * 2 ** 63)
