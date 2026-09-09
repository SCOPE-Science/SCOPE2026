"""Consolidation verifier: replays every positive structural claim from archived artifacts only.
Prints VERIFY lines; exits nonzero on any failure."""
import numpy as np, json, math, sys

def load_mat(path):
    toks = open(path).read().split()
    r, c = int(toks[0]), int(toks[1])
    vals = list(map(int, toks[2:]))
    assert len(vals) == r * c
    return np.array(vals, dtype=np.int64).reshape(r, c)

# 1. archived matrix
A = load_mat('output/artifacts/no3way-04-04-04.mat')
assert A.shape == (48, 64)
assert set(np.unique(A)) <= {0, 1}
assert (A.sum(axis=0) == 3).all() and (A.sum(axis=1) == 4).all()
print("VERIFY matrix 48x64 0/1 colsum=3 rowsum=4 OK")

# 2. canonical margins: every archived row equals a canonical pairwise-margin row
C = np.zeros((48, 64), dtype=np.int64)
for i in range(4):
    for j in range(4):
        for k in range(4):
            cc = i + 4 * j + 16 * k
            C[i + 4 * j, cc] = 1
            C[16 + i + 4 * k, cc] = 1
            C[32 + j + 4 * k, cc] = 1
for r in range(48):
    assert any((A[r] == C[s]).all() for s in range(48)), r
print("VERIFY all 48 archived rows are canonical pairwise margins OK")

# 3. rank 37 + saturation gcd statement (recompute gcd from archived A37/rowbasis)
AR = np.load('output/artifacts/A37.npy')
LN = np.load('output/artifacts/leftnull.npy')
assert AR.shape == (37, 64) and LN.shape == (11, 48)
assert np.abs(LN @ A).max() == 0
print("VERIFY left-nullspace 11-dim certificate LN@A=0 OK")

def bareiss_det(B):
    n = len(B); M = [row[:] for row in B]; prev = 1
    for k in range(n - 1):
        if M[k][k] == 0:
            for i in range(k + 1, n):
                if M[i][k] != 0:
                    M[k], M[i] = M[i], M[k]; break
            else:
                return 0
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                M[i][j] = (M[i][j] * M[k][k] - M[i][k] * M[k][j]) // prev
            M[i][k] = 0
        prev = M[k][k]
    return M[n - 1][n - 1]

# witness minor: det of sigma_best must be +-2 (archived)
sig = json.load(open('output/artifacts/sigma_best.json'))
d = bareiss_det([[int(AR[r, c]) for c in sig['cols']] for r in range(37)])
assert d == sig['det'] == -2, (d, sig['det'])
print("VERIFY archived sigma det=-2 (non-unimodular simplex) OK")

# gcd-of-minors: verify the logged nonsingular witness + gcd=1 claim on a small archived sample
import random
random.seed(444)
g = 0; nz = 0
for t in range(120):
    cols = random.sample(range(64), 37)
    dd = bareiss_det([[int(AR[r, c]) for c in cols] for r in range(37)])
    if dd != 0:
        nz += 1
        g = abs(dd) if g == 0 else math.gcd(g, abs(dd))
logged = open('output/artifacts/saturation.txt').read()
assert f"nonsingular={nz}/120" in logged and f"gcd={g}" in logged, (logged, nz, g)
assert g == 1
print(f"VERIFY saturation gcd=1 replayed (nonsingular={nz}/120) OK")

# 4. R2/R3 collision-free census replay
R2 = np.load('output/artifacts/R2_distinct.npy'); R3 = np.load('output/artifacts/R3_distinct.npy')
assert R2.shape == (2080, 48) and len(np.unique(R2, axis=0)) == 2080
assert R3.shape == (45760, 48) and len(np.unique(R3, axis=0)) == 45760
print("VERIFY R2=2080/2080, R3=45760/45760 collision-free OK")

# 5. R3 midpoint-convexity exhaustive replay
S3 = set(map(tuple, R3.tolist()))
P = (R3 % 2).astype(np.uint8)
Up, invp, cntp = np.unique(P, axis=0, return_inverse=True, return_counts=True)
tot = sum(int(c) * (int(c) - 1) // 2 for c in cntp)
assert tot == 129024, tot
for gg in range(len(Up)):
    if cntp[gg] < 2:
        continue
    G = R3[invp == gg]
    for a in range(len(G)):
        M = (G[a] + G[a + 1:]) // 2
        for row in M:
            assert tuple(row.tolist()) in S3
print("VERIFY R3 midpoint-convexity exhaustive (129024 pairs) OK")

# 6. empty-simplex certificate replay (no archived column in conv(sigma) besides sigma)
import sympy as sp
cols = sig['cols']
Bm = sp.Matrix([[int(AR[r, c]) for c in cols] for r in range(37)])
Binv = Bm.inv()
n_inside = 0
for j in range(64):
    if j in set(cols):
        continue
    lam = Binv * sp.Matrix([int(x) for x in AR[:, j]])
    if all(x >= 0 for x in lam):
        n_inside += 1
assert n_inside == 0, n_inside
assert json.load(open('output/artifacts/emptiness.json')) == {"interior": []}
print("VERIFY sigma is an empty simplex (0 interior columns) OK")
print("ALL VERIFY_OK")
