"""D4 representation-theoretic census for lane-1923 target (lambda=2w2, mu=0).
Self-contained: Weyl group, Kostant partition DP, Weyl dimension, coweight-interval census.
D4 nodes ordered 0..3 = 1,2,3,4 with node 1 (index1) central.
"""
import numpy as np
from collections import deque

C = np.array([[2,-1,0,0],[-1,2,-1,-1],[0,-1,2,0],[0,-1,0,2]], dtype=int)
Cinv = np.linalg.inv(C)
POS_ALPHA = [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),
             (1,1,0,0),(0,1,1,0),(0,1,0,1),
             (1,1,1,0),(1,1,0,1),(0,1,1,1),
             (1,2,1,1),(1,1,1,1)]
assert len(POS_ALPHA) == 12

def weyl_group():
    mats = []
    for i in range(4):
        M = np.eye(4, dtype=int)
        for j in range(4):
            M[j, i] = -C[i, j] if j != i else -1
        mats.append(M)
    els = [np.eye(4, dtype=int)]
    seen = {els[0].tobytes()}
    q = deque([els[0]])
    while q:
        g = q.popleft()
        for M in mats:
            for h in (M @ g, g @ M):
                b = h.tobytes()
                if b not in seen:
                    seen.add(b); els.append(h); q.append(h)
    return els

ELS = weyl_group()
DETS = [round(float(np.linalg.det(g))) for g in ELS]
assert len(ELS) == 192, len(ELS)

def ip(a, b):
    return float(np.array(a, float) @ Cinv @ np.array(b, float))

# ---- Kostant partition table ----
B = (7, 10, 7, 7)
def kostant_table():
    import numpy as np
    dp = np.zeros(B, dtype=np.int64)
    dp[0, 0, 0, 0] = 1
    for r in POS_ALPHA:
        for a in range(B[0]):
            for b in range(B[1]):
                for c in range(B[2]):
                    for d in range(B[3]):
                        pa, pb, pc, pd = a-r[0], b-r[1], c-r[2], d-r[3]
                        if pa >= 0 and pb >= 0 and pc >= 0 and pd >= 0:
                            dp[a, b, c, d] += dp[pa, pb, pc, pd]
    return dp
DP = kostant_table()

def to_alpha_int(dyn):
    v = Cinv.dot(np.array(dyn, float))
    r = [int(round(x)) for x in v]
    assert all(abs(x - y) < 1e-6 for x, y in zip(v, r)), (dyn, v)
    return r

def weight_mult(lam, target):
    lamrho = tuple(np.array(lam) + np.array((1, 1, 1, 1)))
    total = 0
    for g, det in zip(ELS, DETS):
        img = tuple(g.dot(np.array(lamrho)).tolist())
        diff = np.array(img) - (np.array(target) + np.array((1, 1, 1, 1)))
        ad = Cinv.dot(diff.astype(float))
        ra = [int(round(x)) for x in ad]
        if any(abs(x - y) > 1e-6 for x, y in zip(ad, ra)):
            continue
        if any(r < 0 for r in ra):
            continue
        assert all(r < b for r, b in zip(ra, B)), ra
        total += det * int(DP[ra[0], ra[1], ra[2], ra[3]])
    return total

def weyl_dim(lam):
    lpr = tuple(np.array(lam) + 1)
    num = den = 1.0
    for al in POS_ALPHA:
        num *= ip(lpr, al); den *= ip((1, 1, 1, 1), al)
    return num / den

if __name__ == "__main__":
    lam = (0, 2, 0, 0)
    print("|W| =", len(ELS))
    print("dim V(2w2) =", weyl_dim(lam))
    print("zero-weight mult V(2w2) =", weight_mult(lam, (0, 0, 0, 0)))
    # dominant weights <= lam
    doms = []
    for k1 in range(5):
        for k2 in range(7):
            for k3 in range(5):
                for k4 in range(5):
                    mu = (lam[0]-(2*k1-k2), lam[1]-(-k1+2*k2-k3-k4),
                          lam[2]-(-k2+2*k3), lam[3]-(-k2+2*k4))
                    if all(m >= 0 for m in mu):
                        doms.append((mu, (k1, k2, k3, k4)))
    print("dominant weights <= 2w2:", len(doms))
    for mu, k in sorted(doms, key=lambda t: -sum(t[1])):
        print("  ", mu, "mult =", weight_mult(lam, mu))
    # T-fixed-point census of slice: coweights nu with 0<=nu<=lam (coroot-lattice cone order)
    lam_al = to_alpha_int(lam)
    n_all = 0; fixed = []
    for a in range(lam_al[0]+1):
        for b in range(lam_al[1]+1):
            for c in range(lam_al[2]+1):
                for d in range(lam_al[3]+1):
                    nu_al = (a, b, c, d)
                    nu_dyn = tuple((C.dot(np.array(nu_al))).tolist())
                    rem = tuple(np.array(lam_al) - np.array(nu_al))
                    # nu dominant-lattice? nu in coroot lattice automatically; need nu>=0 in coroot cone (true)
                    # and lam-nu in coroot cone (true by box). Record Dynkin labels.
                    n_all += 1
                    fixed.append((nu_dyn, nu_al))
    print("coweights nu with 0<=nu<=2w2 in coroot order:", n_all)
    # tensor-square adjoint zero-weight multiplicity (generic-parameter product crystal weight count)
    # V(w2): weights = 24 roots (m1) + 0 (m4)
    print("generic (V(w2)^2) zero-weight mult =", 24*1*1 + 4*4)
