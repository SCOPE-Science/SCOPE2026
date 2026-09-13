"""Converged reference check (repaired illustration): reduced-Newton ergodic
solve + exact policy iteration for discounted finite-state MFG (3-state).
Shows |m_r-mbar|+|rV_r-lam| -> 0 with bounded ratios. Numpy only."""
import numpy as np

d = 3
a_min, a_max = 0.5, 2.0
c0 = 1.0
b = np.array([0.6, -0.2, -0.4])

def pol(V):
    DV = V[None, :] - V[:, None]
    G = np.zeros((d, d)); H = np.zeros(d)
    for x in range(d):
        for y in range(d):
            if y == x:
                continue
            p = DV[x, y]
            a = min(a_max, max(a_min, 1.0 - p))
            G[x, y] = a
            H[x] += -a * p - 0.5 * (a - 1.0) ** 2
        G[x, x] = -np.sum(G[x, :])
    return G, H

def stat_dist(G):
    A = G.T.copy(); A[-1, :] = 1.0
    bb = np.zeros(d); bb[-1] = 1.0
    return np.linalg.solve(A, bb)

def unpack(w):
    u = np.zeros(d); u[:d - 1] = w[:d - 1]; u[d - 1] = -np.sum(w[:d - 1])
    m = np.zeros(d); m[:d - 1] = w[d - 1:2 * (d - 1)]; m[d - 1] = 1 - np.sum(w[d - 1:2 * (d - 1)])
    return u, m, w[-1]

def egs(w):
    u, m, lam = unpack(w)
    G, H = pol(u)
    return np.concatenate([H + c0 * m + b / d + lam, (G.T @ m)[:d - 1]])

w = np.array([0.0, 0.0, 1 / 3, 1 / 3, 0.0])
for _ in range(60):
    e = egs(w)
    if float(np.linalg.norm(e)) < 1e-14:
        break
    J = np.zeros((len(e), len(w))); eps = 1e-8
    for j in range(len(w)):
        dw = np.zeros(len(w)); dw[j] = eps
        J[:, j] = (egs(w + dw) - egs(w - dw)) / (2 * eps)
    w = w + np.linalg.solve(J, -e)

u, m, lam = unpack(w)
G, H = pol(u)
print("ergodic: u=", np.round(u, 6), "m=", np.round(m, 6), "lam=", round(float(lam), 6))
print("ergodic residual=%.1e fp=%.1e min(m)=%.4f"
      % (float(np.max(np.abs(H + c0 * m + b / d + lam))),
         float(np.max(np.abs(G.T @ m))), float(m.min())))

def solve_disc(r, V):
    for _ in range(1000):
        G, H = pol(V)
        mm = stat_dist(G)
        Vn = np.linalg.solve(r * np.eye(d) - G, 0.5 * np.ones(d) - (c0 * mm + b / d) + (H + 0.5 * np.ones(d) - H))
        # exact policy evaluation: (rI - G)V = L - F with L = running cost part
        # recompute L consistently:
        DV = V[None, :] - V[:, None]
        L = np.zeros(d)
        for x in range(d):
            for y in range(d):
                if y == x:
                    continue
                p = DV[x, y]
                a = min(a_max, max(a_min, 1.0 - p))
                L[x] += 0.5 * (a - 1.0) ** 2
        Vn = np.linalg.solve(r * np.eye(d) - G, L - (c0 * mm + b / d))
        if float(np.linalg.norm(Vn - V)) < 1e-13:
            V = Vn
            break
        V = Vn
    G, H = pol(V); mm = stat_dist(G)
    DV = V[None, :] - V[:, None]
    L = np.zeros(d)
    for x in range(d):
        for y in range(d):
            if y == x:
                continue
            p = DV[x, y]
            a = min(a_max, max(a_min, 1.0 - p))
            L[x] += 0.5 * (a - 1.0) ** 2
    res = float(np.max(np.abs(r * V + H + c0 * mm + b / d))) + float(np.max(np.abs(G.T @ mm)))
    return V, mm, res

V = np.zeros(d)
for r in [0.4, 0.2, 0.1, 0.05, 0.025, 0.0125]:
    V, mm, res = solve_disc(r, V)
    em = float(np.linalg.norm(mm - m)); ev = float(np.linalg.norm(r * V - lam))
    print("r=%.4f |m-mbar|=%.6f /r=%.4f |rV-lam|=%.6f /r=%.4f dres=%.1e"
          % (r, em, em / r, ev, ev / r, res))
