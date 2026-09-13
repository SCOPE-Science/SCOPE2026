"""Broad scan 2: segment directions, extreme boxes, random GL images, random zonotopes."""
import numpy as np
from zonotope import c_roots, mv, vol, facet_data, ratio

n = 4
Z = c_roots(n)
U, A = facet_data(Z)
rng = np.random.default_rng(1)


def show(label, K):
    try:
        R, D, d, a = ratio(K, Z, U, A)
        print(f"{label}: R={R:.6g} Delta={D:.6g} dist={d:.6g} a={a:.6g}")
    except Exception as e:
        print(label, "ERR", e)


print("--- segments: dense sphere scan (N = a^2, b = 0) ---")
best = []
# fibonacci sphere in 4D via gaussian normalization
X = rng.normal(size=(3000, n))
X /= np.linalg.norm(X, axis=1, keepdims=True)
# add structured directions: coordinate planes diagonals, root directions
extra = []
for i in range(n):
    ei = np.zeros(n)
    ei[i] = 1.0
    extra.append(ei)
for i in range(n):
    for j in range(i + 1, n):
        for s in [1, -1]:
            v = np.zeros(n)
            v[i] = 1.0
            v[j] = s
            extra.append(v / np.linalg.norm(v))
for s1 in [1, -1]:
    for s2 in [1, -1]:
        for s3 in [1, -1]:
            v = np.array([1.0, s1, s2, s3])
            extra.append(v / np.linalg.norm(v))
X = np.vstack([X, np.array(extra)])
rs = []
for x in X:
    K = np.column_stack([Z, x.reshape(n, 1)])
    R, D, d, a = ratio(K, Z, U, A)
    rs.append(R)
rs = np.array(rs)
print("seg scan: min R =", rs.min(), " max =", rs.max(), " mean =", rs.mean())
ib = np.argsort(rs)[:8]
for i in ib:
    print("  best x =", np.round(X[i], 4), " R =", rs[i])

print("--- boxes extreme aspect ---")
for cs in [[100, 1, 1, 1], [1000, 1, 1, 1], [100, 100, 1, 1], [1000, 1000, 1, 1],
           [100, 100, 100, 1], [1, 1, 1, 0.01], [1, 1, 1, 0.001], [50, 2, 1, 0.5]]:
    K = np.column_stack([(c * np.eye(n)[:, [i]]) for i, c in enumerate(cs)])
    show(f"box{cs}", K)

print("--- cross-like zonotope conv extremes: thin slabs Z + t*thinbox ---")
for t in [1, 10, 100]:
    slab = np.array([[t, 0, 0, 0]]).T
    K = np.column_stack([Z, slab])
    show(f"Z+{t}*seg(e1)", K)

print("--- random GL images A Z ---")
for s in range(10):
    M = rng.normal(size=(n, n))
    Q, _ = np.linalg.qr(M)
    if np.linalg.det(Q) < 0:
        Q[:, 0] = -Q[:, 0]
    ang = rng.uniform(0.05, 0.6)
    Rm = np.eye(n) + ang * (Q - Q.T)  # near-rotation-ish invertible
    show(f"GL{s}", Rm @ Z)
print("--- pure rotations of Z (Delta>0 since C fixed) ---")
for s in range(6):
    M = rng.normal(size=(n, n))
    Q, _ = np.linalg.qr(M)
    if np.linalg.det(Q) < 0:
        Q[:, 0] = -Q[:, 0]
    show(f"rot{s}", Q @ Z)
print("--- shears det=1 ---")
for s in range(6):
    S = np.eye(n)
    i, j = rng.integers(0, n, 2)
    if i == j:
        j = (j + 1) % n
    S[i, j] = rng.uniform(0.5, 3.0)
    show(f"shear{s}({i},{j})", S @ Z)

print("--- random zonotopes (generators iid gaussian) ---")
for m in [4, 6, 10, 16]:
    for s in range(4):
        G = rng.normal(size=(n, m))
        show(f"rz m={m} #{s}", G)
print("--- random zonotopes (generators uniform cube, spiky) ---")
for s in range(6):
    G = rng.uniform(-1, 1, size=(n, 8)) * np.exp(rng.normal(0, 1.5, (1, 8)))
    show(f"spiky{s}", G)
