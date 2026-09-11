"""Target probe (numpy only): metric setup, Lip checks, trivial regime, h=2 symmetric bound.

Repro: python3 output/artifacts/target_probe.py  (numpy only; vertices precomputed once)
"""
import numpy as np
from itertools import combinations

def lca_len(a, b):
    k = 0
    for x, y in zip(a, b):
        if x == y:
            k += 1
        else:
            break
    return k

def gdist(a, b):
    return len(a) + len(b) - 2 * lca_len(a, b)

def leaves(h):
    return [tuple(int(x) for x in format(i, f"0{h}b")) for i in range(2 ** h)]

def S_points(h):
    return [()] + leaves(h)

def dM(a, b):
    return gdist(a, b) ** 0.5

def lip_of(h, f):
    pts = S_points(h)
    m = 0.0
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            m = max(m, abs(f[pts[i]] - f[pts[j]]) / dM(pts[i], pts[j]))
    return m

print("== Lip checks ==", flush=True)
for h in (2, 3):
    L = leaves(h)
    c = (h / 2) ** 0.5
    f = {p: 0.0 for p in S_points(h)}
    for lf in L:
        f[lf] = c if lf[0] == 0 else -c
    print(f"h={h} top-bipartition lip={lip_of(h, f):.6f} (<=1 ok)", flush=True)
    f2 = {p: 0.0 for p in S_points(h)}
    for k, lf in enumerate(L):
        f2[lf] = 0.70710678 if (k * 2654435761) % 2 == 0 else -0.70710678
    print(f"h={h} pseudo-random-sign lip={lip_of(h, f2):.6f} (<=1 ok)", flush=True)
    f3 = {p: 0.0 for p in S_points(h)}
    for lf in L:
        f3[lf] = h ** 0.5
    print(f"h={h} radial-all lip={lip_of(h, f3):.6f} (<=1 ok)", flush=True)

print("== trivial regime ==", flush=True)
for h in (1, 3, 7, 255, 256, 1023):
    v = float(np.log2(h + 1)) / 8
    print(f"h={h}: (1/8)log2(h+1)={v:.4f} {'(trivial,<=1)' if v <= 1 else '(nontrivial)'}", flush=True)

print("== h=2 symmetric single-scale bound ==", flush=True)
r = ()
L = leaves(2)
n = 5
pts = [r] + L
D = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        D[i, j] = dM(pts[i], pts[j])
rows = []
for i in range(4):
    e = np.zeros(4); e[i] = 1.0
    rows.append((e, D[0, 1 + i])); rows.append((-e, D[0, 1 + i]))
for i in range(4):
    for j in range(i + 1, 4):
        e = np.zeros(4); e[i] = 1.0; e[j] = -1.0
        rows.append((e, D[1 + i, 1 + j])); rows.append((-e, D[1 + i, 1 + j]))
A = np.stack([a for a, _ in rows]); b = np.array([v for _, v in rows])
verts = []
seen = set()
for combo in combinations(range(len(rows)), 4):
    M = A[list(combo), :]
    if abs(np.linalg.det(M)) < 1e-9:
        continue
    x = np.linalg.solve(M, b[list(combo)])
    if np.all(A @ x <= b + 1e-7):
        key = tuple(np.round(x, 8))
        if key not in seen:
            seen.add(key); verts.append(x)
V = np.array(verts)
print(f"polytope vertices: {len(V)}", flush=True)

def fnorm(m):
    m = np.asarray(m, float)
    return float(np.max(V @ m))

e00 = np.array([1., 0, 0, 0])
print("sanity ||d00|| =", round(fnorm(e00), 6), " expect ", round(2 ** 0.5, 6), flush=True)

def Lreq(a, b_):
    phi = np.array([a, a, b_, b_])
    n0 = fnorm(phi)
    n1 = fnorm(e00 - phi)
    n2 = fnorm(np.array([0, 0, 1., 0]) - phi)
    return max(n0, n1, n2 / 3 ** 0.5)

grid = np.linspace(-0.5, 1.5, 41)
best = (1e9, None)
for a in grid:
    for b_ in grid:
        v = Lreq(a, b_)
        if v < best[0]:
            best = (v, (round(float(a), 4), round(float(b_), 4)))
print("min symmetric required L =", round(best[0], 4), " at (a,b)=", best[1], flush=True)
print("=> necessary condition E_2 >=", round(best[0], 4), " (O(1); no log signal)", flush=True)
