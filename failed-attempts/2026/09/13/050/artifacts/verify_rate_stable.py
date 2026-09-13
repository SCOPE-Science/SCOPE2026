"""Stable branch-tracking check: ergodic solve + discounted solves via damped
fixed point with continuation r=0.4 -> 0.025 (numpy only). Prints O(r) ratios."""
import numpy as np

d = 3
a_min, a_max = 0.5, 2.0
c0 = 1.0
b = np.array([0.6, -0.2, -0.4])

def pol(V):
    DV = V[None, :] - V[:, None]
    G = np.zeros((d, d)); H = np.zeros(d); L = np.zeros(d)
    for x in range(d):
        for y in range(d):
            if y == x: continue
            p = DV[x, y]
            a = min(a_max, max(a_min, 1.0 - p))
            G[x, y] = a
            H[x] += -a * p - 0.5 * (a - 1.0) ** 2
            L[x] += 0.5 * (a - 1.0) ** 2
        G[x, x] = -np.sum(G[x, :])
    return G, H, L

def stat_dist(G):
    A = G.T.copy(); A[-1, :] = 1.0
    bb = np.zeros(d); bb[-1] = 1.0
    return np.linalg.solve(A, bb)

def solve_erg(it=300):
    u = np.zeros(d); m = np.ones(d) / d
    for _ in range(it):
        G, H, L = pol(u)
        m_new = stat_dist(G)
        m = 0.5 * m + 0.5 * m_new
        Fv = c0 * m + b / d
        lam = -float(np.dot(m, H + Fv))
        rhs = -(H + Fv + lam)
        rhs = rhs - np.dot(m, rhs)
        A = -G + np.outer(np.ones(d), m)
        u = np.linalg.solve(A, rhs) - np.mean(np.linalg.solve(A, rhs))
    G, H, _ = pol(u)
    m = stat_dist(G)
    lam = -float(np.dot(m, H + c0 * m + b / d))
    return u, m, lam

def solve_disc(r, V0, m0, it=300, damp=0.2):
    V, m = V0.copy(), m0.copy()
    for _ in range(it):
        G, H, L = pol(V)
        Fv = c0 * m + b / d
        V_new = np.linalg.solve(r * np.eye(d) - G, L - Fv)
        V = (1 - damp) * V + damp * V_new
        G2, _, _ = pol(V)
        m = (1 - damp) * m + damp * stat_dist(G2)
    return V, m

ub, mb, lamb = solve_erg()
print("ergodic: u=", np.round(ub, 4), "m=", np.round(mb, 4), "lam=", round(lamb, 4))
Vw, mw = np.zeros(d), np.ones(d) / d
for r in [0.4, 0.2, 0.1, 0.05, 0.025]:
    Vw, mw = solve_disc(r, Vw, mw)
    em = float(np.linalg.norm(mw - mb)); ev = float(np.linalg.norm(r * Vw - lamb))
    print(f"r={r:.3f} m_r={np.round(mw,4)} |m-mbar|={em:.6f} /r={em/r:.4f} |rV-lam|={ev:.6f} /r={ev/r:.4f}")
