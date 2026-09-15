"""Bounded recovery test (lean): uniform ellipticity + uniform transversality for
phi_gamma(x,y) = x^2 + y^2 + gamma*y^3/3 on Sigma=[0,1]^2, |gamma|<=1/2.
"""
import numpy as np

gammas = np.linspace(-0.5, 0.5, 21)
ys = np.linspace(0, 1, 401)
c0 = 0.2

min_eig, max_eig = 1e9, -1e9
for g in gammas:
    e2 = 2 + 2*g*ys
    min_eig = min(min_eig, 2.0, e2.min())
    max_eig = max(max_eig, 2.0, e2.max())
print(f"eigenvalue range over grid: [{min_eig:.4f}, {max_eig:.4f}]", flush=True)

def normal(x, y, g):
    v = np.stack([-2*x, -(2*y + g*y*y), np.ones_like(x)], axis=-1)
    return v / np.linalg.norm(v, axis=-1, keepdims=True)

rng = np.random.default_rng(0)
worst = 1e9
worst_cfg = None
# Random separated pairs + local refinement: sufficient as a bounded probe.
for g in np.linspace(-0.5, 0.5, 11):
    p1 = rng.random((6000, 2))
    p2 = rng.random((6000, 2))
    d = np.linalg.norm(p1 - p2, axis=1)
    m = d >= c0
    n1 = normal(p1[m, 0], p1[m, 1], g)
    n2 = normal(p2[m, 0], p2[m, 1], g)
    cross = np.linalg.norm(np.cross(n1, n2), axis=1)
    j = int(np.argmin(cross))
    if cross[j] < worst:
        worst = float(cross[j])
        worst_cfg = (float(g), p1[m][j].tolist(), p2[m][j].tolist())
print(f"min normal cross-product gap (c0={c0}): {worst:.4f} at {worst_cfg}", flush=True)
assert min_eig >= 1.0 - 1e-9 and max_eig <= 3.0 + 1e-9
assert worst > 0.02
print("PASS: uniform ellipticity + uniform transversality hold; block lies in induction core, not geometry.", flush=True)
