"""Script C: cone numerics in A_star eigenbasis + inverse (stable) cones.
Df(c2,c3) affine in (c2,c3); Mb = P^T Df P with P orthogonal eigenbasis."""
import math
import numpy as np

A = np.array([[2., 1., 0.], [1., 2., 1.], [0., 1., 1.]])
w, P = np.linalg.eigh(A)
print("eigvals:", w)
es, ew, eu = P[:, 0], P[:, 1], P[:, 2]
alp, bet = 2*math.pi*0.03, 2*math.pi*0.02

def Df(c2, c3):
    return np.array([[2., 1+2*alp*c2, bet*c3],
                     [1., 2+alp*c2, 1+2*bet*c3],
                     [0., 1., 1+bet*c3]])

def Mb(c2, c3):
    return P.T @ Df(c2, c3) @ P

for c2, c3 in [(0, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
    print(f"c=({c2:+d},{c3:+d}) Mb=\n", np.round(Mb(c2, c3), 4))

rng = np.random.default_rng(0)
N = 4000
arr = np.array([Mb(rng.uniform(-1, 1), rng.uniform(-1, 1)) for _ in range(N)])
print("diag ranges: s:", (arr[:, 0, 0].min(), arr[:, 0, 0].max()),
      " w:", (arr[:, 1, 1].min(), arr[:, 1, 1].max()),
      " u:", (arr[:, 2, 2].min(), arr[:, 2, 2].max()))
off = arr.copy()
for i in range(3):
    off[:, i, i] = 0
print("max |offdiag| entrywise:\n", np.abs(off).max(axis=0).round(4))

def cone_check(kappa, trials=120000, inverse=False):
    worst_r, worst_e = 0.0, 1e9
    for _ in range(trials):
        c2, c3 = rng.uniform(-1, 1), rng.uniform(-1, 1)
        M = np.linalg.inv(Mb(c2, c3)) if inverse else Mb(c2, c3)
        th = rng.uniform(0, 2*math.pi)
        sgn = 1 if rng.random() < 0.5 else -1
        v = np.array([kappa*sgn, math.cos(th), math.sin(th)])
        z = M @ v
        r = abs(z[0])/math.hypot(z[1], z[2])
        e = math.hypot(z[1], z[2])
        worst_r = max(worst_r, r)
        worst_e = min(worst_e, e)
    return worst_r, worst_e

for k in [0.3, 0.5, 0.8]:
    r, e = cone_check(k)
    print(f"unstable cone kappa={k}: worst_ratio={r:.3f} (<{k}? {r<k}) worst_exp={e:.3f} (>1? {e>1})")
# stable cone: Df^{-1} expands stable dir; check cone around es under inverse map
Ainv = np.linalg.inv(A)
ws, Ps = np.linalg.eigh(Ainv)  # same vecs, recip eigs
print("Ainv eigs:", ws)
for k in [0.3, 0.5, 0.8]:
    r, e = cone_check(k, inverse=True)
    print(f"stable cone kappa={k}: worst_ratio={r:.3f} (<{k}? {r<k}) worst_exp={e:.3f} (>1? {e>1})")
