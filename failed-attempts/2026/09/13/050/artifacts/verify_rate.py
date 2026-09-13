"""Numpy-only check: 3-state MFG, O(r) vanishing-discount rate.
Policy iteration for discounted HJB + linear solve for invariant law; ergodic via rho-iteration."""
import numpy as np

d = 3
a_min, a_max = 0.5, 2.0
c0 = 1.0
b = np.array([0.6, -0.2, -0.4])  # breaks symmetry -> nontrivial u, m

def pol_and_H(V):
    DV = V[None, :] - V[:, None]
    G = np.zeros((d, d)); H = np.zeros(d)
    for x in range(d):
        for y in range(d):
            if y == x: continue
            p = DV[x, y]
            a = min(a_max, max(a_min, 1.0 - p))
            G[x, y] = a
            H[x] += -a * p - 0.5 * (a - 1.0) ** 2 + b[x]/d
        G[x, x] = -np.sum(G[x, :])
    return G, H

def stat_dist(G):
    A = G.T.copy(); A[-1, :] = 1.0
    b = np.zeros(d); b[-1] = 1.0
    return np.linalg.solve(A, b)

def solve_disc(r, iters=200):
    V = np.zeros(d); m = np.ones(d) / d
    for _ in range(iters):
        G, H = pol_and_H(V)
        # V = -(H + c0 m)/(r) damped fixed point
        Vn = -(H + c0 * m + b/d) / r
        Vn = Vn - np.mean(Vn) + np.mean(V)  # stabilize level via damping below
        V = 0.5 * V + 0.5 * (Vn - np.mean(Vn) + np.mean(V))
        # recompute with new V then update m
        G, _ = pol_and_H(V)
        m = stat_dist(G)
        # correct level: enforce HJB mean
        _, H = pol_and_H(V)
        V = V - np.mean(r * V + H + c0 * m + b/d) / r * 0.5
    return V, m

def solve_erg(iters=500):
    u = np.zeros(d); m = np.ones(d) / d; lam = 0.0
    for _ in range(iters):
        G, H = pol_and_H(u)
        lam = -np.mean(H + c0 * m + b/d)
        # value iteration step: u <- u + (lam + H + c0 m)/k damped, mean-zero
        u = u + 0.1 * (lam + H + c0 * m + b/d)
        u = u - np.mean(u)
        G, _ = pol_and_H(u)
        m = stat_dist(G)
    G, H = pol_and_H(u)
    lam = float(-np.dot(m, H + c0 * m + b/d))
    return u, m, lam

u_b, m_b, lam_b = solve_erg()
print("ergodic: u=", np.round(u_b, 5), "m=", np.round(m_b, 5), "lam=", round(lam_b, 5))
ok = True
prev = None
for r in [0.4, 0.2, 0.1, 0.05, 0.025]:
    V, m = solve_disc(r)
    em = float(np.linalg.norm(m - m_b)); ev = float(np.linalg.norm(r * V - lam_b))
    print(f"r={r:.3f} |m-mbar|={em:.6f} /r={em/r:.4f} |rV-lam|={ev:.6f} /r={ev/r:.4f}")
    if not (np.all(m > 0.01) and em / r < 10 and ev / r < 10):
        ok = False
print("O(r) consistent:", ok)
