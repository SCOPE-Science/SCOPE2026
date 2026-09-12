import numpy as np, itertools

P = 998244353

# Fourier q-indices: (g1,g2,g3,g4) in (Z2xZ2)^4 summing to 0 (XOR=0). 64 vars.
G = np.array([[a, b, c, d] for a in range(4) for b in range(4)
              for c in range(4) for d in range(4) if a ^ b ^ c ^ d == 0],
             dtype=np.uint8)
NV = 64
POS = {tuple(g): i for i, g in enumerate(G.tolist())}
g1 = G[:, 0].astype(np.int64); g2 = G[:, 1].astype(np.int64)
g3 = G[:, 2].astype(np.int64); g4 = G[:, 3].astype(np.int64)
G1G4 = (g1 ^ g4); G1G2 = (g1 ^ g2)


def sample_Q(R, seed):
    """Random points on K3P 4-sunlet variety (shared edge params + mixing delta).

    Trees: T1 (keep retic edge c4->c1=er2): internal labels er2:g1, e34:g1^g4, e23:g2.
           T2 (keep retic edge c2->c1=er1): internal labels er1:g1, e23:g1^g2, e34:g4.
    q_g = delta*m1(g) + (1-delta)*m2(g), pendant params shared, a^0=1 normalized.
    """
    rng = np.random.default_rng(seed)
    pend = rng.integers(1, P, size=(R, 4, 4)).astype(np.int64); pend[:, :, 0] = 1
    e23 = rng.integers(1, P, size=(R, 4)).astype(np.int64); e23[:, 0] = 1
    e34 = rng.integers(1, P, size=(R, 4)).astype(np.int64); e34[:, 0] = 1
    er1 = rng.integers(1, P, size=(R, 4)).astype(np.int64); er1[:, 0] = 1
    er2 = rng.integers(1, P, size=(R, 4)).astype(np.int64); er2[:, 0] = 1
    delta = rng.integers(0, P, size=(R,)).astype(np.int64)
    omd = (1 - delta) % P
    Q = np.empty((R, NV), dtype=np.int64)
    for j in range(NV):
        lp = (pend[:, 0, g1[j]] * pend[:, 1, g2[j]]) % P
        lp = (lp * pend[:, 2, g3[j]]) % P
        lp = (lp * pend[:, 3, g4[j]]) % P
        m1 = (lp * er2[:, g1[j]]) % P
        m1 = (m1 * e34[:, G1G4[j]]) % P
        m1 = (m1 * e23[:, g2[j]]) % P
        m2 = (lp * er1[:, g1[j]]) % P
        m2 = (m2 * e23[:, G1G2[j]]) % P
        m2 = (m2 * e34[:, g4[j]]) % P
        Q[:, j] = (delta * m1 + omd * m2) % P
    return Q


def enum_monomials(d):
    return np.array(list(itertools.combinations_with_replacement(range(NV), d)),
                    dtype=np.int32)


def grades_of(cols):
    """Leafwise-XOR grade packed as int key s0|s1*4|s2*16|s3*64."""
    S = np.bitwise_xor.reduce(G[cols], axis=1).astype(np.int64)
    return (S[:, 0] + S[:, 1] * 4 + S[:, 2] * 16 + S[:, 3] * 64)


def eval_block(Q, cols):
    """Evaluate monomials (cols: M x d) on rows Q (R x 64) -> (R x M). Chunked."""
    R, M = Q.shape[0], cols.shape[0]
    E = np.empty((R, M), dtype=np.int64)
    CH = 2000
    for s in range(0, M, CH):
        c = cols[s:s + CH]
        E[:, s:s + CH] = np.prod(Q[:, c], axis=2) % P
    return E


def jordan_null(E):
    """Kernel basis of E (R x N) mod P via Gauss-Jordan. Returns (K x N)."""
    R, N = E.shape
    M = E.copy() % P
    pivcol = np.full(N, -1, dtype=np.int64)
    r = 0
    for c in range(N):
        if r >= R:
            break
        sub = M[r:, c]
        nz = np.flatnonzero(sub)
        if nz.size == 0:
            continue
        i = r + int(nz[0])
        if i != r:
            M[[r, i]] = M[[i, r]]
        inv = pow(int(M[r, c]), P - 2, P)
        if inv != 1:
            M[r] = (M[r] * inv) % P
        f = M[:, c].copy(); f[r] = 0
        nzr = np.flatnonzero(f)
        if nzr.size:
            M[nzr] = (M[nzr] - (f[nzr, None] * M[r][None, :]) % P) % P
        pivcol[c] = r
        r += 1
    free = np.flatnonzero(pivcol == -1)
    K = free.size
    B = np.zeros((K, N), dtype=np.int64)
    B[:, free] = np.eye(K, dtype=np.int64)
    for c in range(N):
        if pivcol[c] >= 0:
            B[:, c] = (-M[pivcol[c], free]) % P
    return B


def row_rank(A):
    """Row rank of A (m x N) mod P via forward elimination."""
    R, N = A.shape
    M = A.copy() % P
    r = 0
    for c in range(N):
        if r >= R:
            break
        nz = np.flatnonzero(M[r:, c])
        if nz.size == 0:
            continue
        i = r + int(nz[0])
        if i != r:
            M[[r, i]] = M[[i, r]]
        inv = pow(int(M[r, c]), P - 2, P)
        if inv != 1:
            M[r] = (M[r] * inv) % P
        for k in range(r + 1, R):
            if M[k, c] != 0:
                M[k] = (M[k] - (M[k, c] * M[r]) % P) % P
        r += 1
    return r
