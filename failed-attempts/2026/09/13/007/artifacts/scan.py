"""Scan deficit/distance ratio over zonotope families near C_n reference (n=4)."""
import numpy as np
from zonotope import c_roots, mv, vol, facet_data, ratio, support_vals

n = 4
Z = c_roots(n)
print("generators:", Z.shape)
V0 = vol(Z)
print("Vol(Z) =", V0)

U, A = facet_data(Z)
print("num facet sides:", len(A))
print("total area:", A.sum())
print("check (1/n) int h dS =", float(np.sum(A * support_vals(Z, U))) / n, " vs Vol =", V0)
hnorm = np.sqrt(np.sum(A * support_vals(Z, U) ** 2))
print("num unique unoriented normals:", len(A) // 2)
# show unoriented normals and areas + hZ values
seen = {}
for u, a in zip(U, A):
    key = tuple(np.round(u / np.linalg.norm(u), 4))
    ckey = tuple(sorted([key, tuple(-np.array(key))])[0])
    seen.setdefault(ckey, []).append(a)
for k, v in sorted(seen.items(), key=lambda t: -np.mean(t[1])):
    print("normal:", k, "area(x2):", v, "hZ:", support_vals(Z, np.array([np.array(k)])))

# sanity: self ratio input K=Z -> Delta=0, dist=0
R, D, d, a = ratio(Z, Z, U, A)
print("self: R=", R, "Delta=", D, "dist=", d, "a=", a)

rng = np.random.default_rng(0)

def scan(name, Ks):
    print("=== " + name + " ===")
    for label, K in Ks:
        R, D, d, a = ratio(K, Z, U, A)
        print(f"{label}: R={R:.6g} Delta={D:.6g} dist={d:.6g} a={a:.6g}")

# F1: diagonal scalings diag(t,1,1,1)
scan("diag(t,1,1,1)", [(f"t={t}", np.diag([t, 1, 1, 1]) @ Z) for t in [1.2, 2, 4, 8, 16]])
# F2: diag(t,t,1,1)
scan("diag(t,t,1,1)", [(f"t={t}", np.diag([t, t, 1, 1]) @ Z) for t in [1.2, 2, 4, 8, 16]])
# F3: diag(t,t,t,1)
scan("diag(t,t,t,1)", [(f"t={t}", np.diag([t, t, t, 1]) @ Z) for t in [1.2, 2, 4, 8, 16]])
# F4: extra segment
for xi, x in [("e1", np.array([1, 0, 0, 0])), ("diag", np.array([1, 1, 1, 1]) / 2),
              ("e1+e2", np.array([1, 1, 0, 0]) / np.sqrt(2))]:
    Ks = []
    for t in [0.5, 1, 2, 4]:
        K = np.column_stack([Z, (t * x).reshape(n, 1)])
        Ks.append((f"t={t}", K))
    scan("Z + t*seg(" + xi + ")", Ks)
# F5: single generator weight t (scale first generator column)
scan("gen0 x t", [(f"t={t}", np.column_stack(
    [(Z[:, 0] * t).reshape(n, 1), Z[:, 1:]])) for t in [0.2, 0.05, 3, 8]])
# F6: random positive weights on generators
Ks = []
for s in range(8):
    w = np.exp(rng.normal(0, 1.0, Z.shape[1]))
    Ks.append((f"rw{s}", Z * w.reshape(1, -1)))
scan("random weights", Ks)
# F7: boxes sum c_i [-e_i,e_i]
Ks = []
for cs in [[2, 1, 1, 1], [4, 1, 1, 1], [8, 1, 1, 1], [4, 4, 1, 1]]:
    K = np.column_stack([(c * np.eye(n)[:, [i]]) for i, c in enumerate(cs)])
    Ks.append((str(cs), K))
scan("boxes", Ks)
