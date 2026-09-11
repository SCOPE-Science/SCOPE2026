"""Screening + audit tools for tolerance-1 rainbow Tverberg 4x4 in R^3.
Float screening (numpy) with early exit; integer-exact verifier separate.
"""
import numpy as np, itertools, sys, time, json

COMB12 = np.array(list(itertools.combinations(range(12), 3)), dtype=int)
TOL = 1e-7

def tet_planes(T):
    A = np.empty((4, 3)); bb = np.empty(4)
    for i in range(4):
        idx = [j for j in range(4) if j != i]
        P = T[idx]
        n = np.cross(P[1] - P[0], P[2] - P[0]).astype(float)
        if n @ (T[i] - P[0]) > 0:
            n = -n
        A[i] = n; bb[i] = n @ P[0]
    return A, bb

def batch_hits(SA, Sb):
    """SA:(B,12,3), Sb:(B,12) -> bool array (B,) triple intersection nonempty."""
    B = SA.shape[0]
    M = SA[:, COMB12]          # (B,220,3,3)
    rhs = Sb[:, COMB12]        # (B,220,3)
    det = np.linalg.det(M)
    valid = np.abs(det) > 1e-13
    feas = np.zeros((B, 220), dtype=bool)
    if valid.any():
        bi, vi = np.where(valid)
        X = np.linalg.solve(M[bi, vi], rhs[bi, vi])
        diff = np.einsum('kd,ked->ke', X, SA[bi]) - Sb[bi]
        feas[bi, vi] = (diff <= TOL).all(axis=1)
    return feas.any(axis=1)

def build_tets(P, rem):
    """rem: list of 4 lists of point indices. Returns dict tetkey->(A,b), tetkey=(i0,i1,i2,i3)."""
    tets = {}
    for t in itertools.product(*rem):
        T = P[np.array(t)]
        if abs(np.linalg.det(np.column_stack([T[1:] - T[0]]))) < 1e-12:
            # degenerate tet: mark volume 0
            pass
        tets[t] = tet_planes(T)
    return tets

def partitions_for_deletion(rem, dep):
    """Yield triples of tetkeys, canonical unordered (2304). Order triples by key-color point."""
    key = (dep + 1) % 4
    others = [c for c in range(4) if c not in (dep, key)]
    o1, o2 = others
    deppts = rem[dep]
    for keysub in itertools.combinations(rem[key], 3):
        for p1 in itertools.permutations(rem[o1], 3):
            for p2 in itertools.permutations(rem[o2], 3):
                ks = []
                for j in range(3):
                    d = {dep: deppts[j], key: keysub[j], o1: p1[j], o2: p2[j]}
                    ks.append((d[0], d[1], d[2], d[3]))
                yield ks

def deletion_count(P, cols, dep, delidx, cap=None, chunk=512):
    """Count rainbow-triple partitions (cap: early stop). Returns (count_capped, exhaustive)."""
    rem = [list(c) for c in cols]
    rem[dep] = [i for i in rem[dep] if i != delidx]
    tets = build_tets(P, rem)
    SA, Sb = [], []
    count = 0
    total = 0
    for ks in partitions_for_deletion(rem, dep):
        total += 1
        A12 = np.vstack([tets[k][0] for k in ks])
        b12 = np.concatenate([tets[k][1] for k in ks])
        SA.append(A12); Sb.append(b12)
        if len(SA) == chunk:
            h = batch_hits(np.array(SA), np.array(Sb))
            count += int(h.sum())
            SA, Sb = [], []
            if cap is not None and count >= cap:
                return count, False
    if SA:
        h = batch_hits(np.array(SA), np.array(Sb))
        count += int(h.sum())
    return count, True

def audit_config(P, cols, cap=1):
    """For each of 16 deletions: capped count. Returns list of (dep,delidx,count,exhaustive)."""
    out = []
    for dep in range(4):
        for delidx in cols[dep]:
            c, ex = deletion_count(P, cols, dep, delidx, cap=cap)
            out.append((dep, delidx, c, ex))
    return out

# ---------------- generators ----------------
def gen_rand_cube(rng, L=10.0):
    return rng.uniform(0, L, size=(16, 3))

def gen_int_box(rng, L=8):
    return rng.integers(0, L + 1, size=(16, 3)).astype(float)

def gen_near_planar(rng, eps=0.05, L=10.0):
    P = rng.uniform(0, L, size=(16, 3)); P[:, 2] = eps * rng.normal(size=16); return P

def gen_grid_422(rng, noise=0.15):
    base = np.array([[x, y, z] for x in [0, 3, 6, 9] for y in [0, 3] for z in [0, 3]], float)
    return base + rng.normal(scale=noise, size=base.shape)

def gen_moment(rng, noise=0.0):
    t = np.arange(1, 17, dtype=float)
    P = np.column_stack([t, t**2 / 16.0, t**3 / 256.0])
    if noise: P += rng.normal(scale=noise, size=P.shape)
    return P

def gen_clustered(rng, spread=0.35, R=6.0):
    centers = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], float) * R / 2
    P = np.zeros((16, 3))
    for c in range(4):
        for k in range(4):
            P[4 * c + k] = centers[k] + rng.normal(scale=spread, size=3)
    return P

def gen_two_planes(rng, L=10.0, H=5.0):
    P = rng.uniform(0, L, size=(16, 3)); P[:8, 2] = rng.normal(scale=0.1, size=8); P[8:, 2] = H + rng.normal(scale=0.1, size=8)
    return P

def gen_three_clusters(rng, spread=0.4, R=7.0):
    centers = np.array([[R, 0, 0], [0, R, 0], [0, 0, R]], float)
    P = np.zeros((16, 3))
    assign = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0]
    for i, a in enumerate(assign):
        P[i] = centers[a] + rng.normal(scale=spread, size=3)
    return P

def default_cols():
    return [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

def shuffled_cols(rng):
    idx = rng.permutation(16)
    return [sorted(idx[4 * c:4 * c + 4].tolist()) for c in range(4)]

if __name__ == '__main__':
    rng = np.random.default_rng(12345)
    cols = default_cols()
    ncfg = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    gens = {'cube': gen_rand_cube, 'planar': gen_near_planar, 'grid': gen_grid_422,
            'moment': gen_moment, 'cluster': gen_clustered, 'twoplane': gen_two_planes,
            'threecl': gen_three_clusters, 'intbox': gen_int_box}
    for name, g in gens.items():
        nkills = 0; mincount = None; t0 = time.time()
        for t in range(ncfg):
            P = g(rng)
            res = audit_config(P, cols, cap=1)
            kills = [r for r in res if r[2] == 0]
            if kills:
                nkills += 1
                print(f'HIT {name} trial {t}: killing deletions={[(k[0], k[1]) for k in kills]}', flush=True)
                np.save(f'/tmp/blocker_{name}_{t}.npy', P)
        print(f'{name}: {ncfg} trials, {nkills} with killing deletion, {time.time()-t0:.1f}s', flush=True)
