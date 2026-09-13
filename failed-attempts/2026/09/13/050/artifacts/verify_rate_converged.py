"""Converged reference check: exact policy iteration for ergodic + discounted
finite-state MFG (3-state instance). Shows |m_r-mbar|+|rV_r-lam| -> 0 with
bounded ratios (O(r) illustration). Numpy only."""
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
            if y == x:
                continue
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

def solve_erg(tol=1e-12, maxit=1000):
    u = np.zeros(d)
    for _ in range(maxit):
        G, H, L = pol(u)
        m = stat_dist(G)
        Fv = c0 * m + b / d
        lam = -float(np.dot(m, H + Fv))
        rhs = -(H + Fv + lam)
        A = -G + np.outer(np.ones(d), m)
        u_new = np.linalg.solve(A, rhs)
        u_new = u_new - np.mean(u_new)
        if float(np.linalg.norm(u_new - u)) < tol:
            u = u_new
            break
        u = u_new
    G, H, L = pol(u)
    m = stat_dist(G)
    Fv = c0 * m + b / d
    lam = -float(np.dot(m, H + Fv))
    res_hjb = float(np.max(np.abs(H + Fv + lam)))
    res_fp = float(np.max(np.abs(G.T @ m)))
    return u, m, lam, res_hjb, res_fp

def solve_disc(r, V, tol=1e-12, maxit=1000):
    for _ in range(maxit):
        G, H, L = pol(V)
        m = stat_dist(G)
        Fv = c0 * m + b / d
        V_new = np.linalg.solve(r * np.eye(d) - G, L - Fv)
        if float(np.linalg.norm(V_new - V)) < tol:
            V = V_new
            break
        V = V_new
    G, H, L = pol(V)
    m = stat_dist(G)
    Fv = c0 * m + b / d
    res = float(np.max(np.abs(r * V + H + Fv))) + float(np.max(np.abs(G.T @ m)))
    return V, m, res

ub, mb, lamb, rh, rf = solve_erg()
print("ergodic: u=", np.round(ub, 6), "m=", np.round(mb, 6), "lam=", round(float(lamb), 6))
print("ergodic residuals: hjb=%.2e fp=%.2e" % (rh, rf))
print("positivity: min(mb)=%.4f" % float(mb.min()))
V = np.zeros(d)
for r in [0.4, 0.2, 0.1, 0.05, 0.025]:
    V, m, res = solve_disc(r, V)
    em = float(np.linalg.norm(m - mb)); ev = float(np.linalg.norm(r * V - lamb))
    print("r=%.3f |m-mbar|=%.6f /r=%.4f |rV-lam|=%.6f /r=%.4f disc_res=%.1e"
          % (r, em, em / r, ev, ev / r, res))
