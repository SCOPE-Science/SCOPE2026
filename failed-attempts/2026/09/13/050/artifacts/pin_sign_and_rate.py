"""Pin duality sign + verify O(r) rate with stable policy iteration (numpy only)."""
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

def DH_of(V):
    # Jacobian-vector not needed; finite-diff gradient of H wrt DV for Bregman check
    DV = V[None, :] - V[:, None]
    Dh = np.zeros((d, d))
    for x in range(d):
        for y in range(d):
            if y == x: continue
            p = DV[x, y]
            a = min(a_max, max(a_min, 1.0 - p))
            Dh[x, y] = -a  # dH/dp edge
    return Dh

def stat_dist(G):
    A = G.T.copy(); A[-1, :] = 1.0
    bb = np.zeros(d); bb[-1] = 1.0
    return np.linalg.solve(A, bb)

# ---- 1. Duality sign check on RANDOM (u1,m1),(u2,m2) ----
rng = np.random.default_rng(0)
u1 = rng.normal(size=d); u2 = rng.normal(size=d)
m1 = rng.random(d); m1 /= m1.sum(); m2 = rng.random(d); m2 /= m2.sum()
G1, H1, _ = pol(u1); G2, H2, _ = pol(u2)
Dh1 = DH_of(u1); Dh2 = DH_of(u2)
w = u1 - u2; mu = m1 - m2
DVw = w[None, :] - w[:, None]
SH = float(np.dot(H1 - H2, mu))
# gaps: B1(x)=H2-H1-Dh1.D(u2-u1), B2(x)=H1-H2-Dh2.D(u1-u2)
B1 = (H2 - H1) - np.sum(Dh1 * (-DVw), axis=1)
B2 = (H1 - H2) - np.sum(Dh2 * (DVw), axis=1)
gaps = float(np.dot(m1, B1) + np.dot(m2, B2))
T = float(np.dot(w, G1.T @ m1 - G2.T @ m2))
print(f"SH={SH:.6f} gaps={gaps:.6f} T={T:.6f}")
print(f"SH+gaps={SH+gaps:.2e} | SH+T+gaps={SH+T+gaps:.2e} | SH-T+gaps={SH-T+gaps:.2e}")
print(f"Bregman nonneg: min(B1)={B1.min():.4f} min(B2)={B2.min():.4f}")

# ---- 2. Policy iteration solvers ----
def solve_disc(r, it=50):
    V = np.zeros(d); m = np.ones(d) / d
    for _ in range(it):
        G, H, L = pol(V)
        Fv = c0 * m + b / d
        V = np.linalg.solve(r * np.eye(d) - G, L - Fv)
        G, _, _ = pol(V)
        m = stat_dist(G)
    return V, m

def solve_erg(it=200):
    u = np.zeros(d); m = np.ones(d) / d; lam = 0.0
    for _ in range(it):
        G, H, L = pol(u)
        Fv = c0 * m + b / d
        m = stat_dist(G)
        lam = -float(np.dot(m, H + Fv))
        rhs = -(H + Fv + lam)
        rhs = rhs - np.dot(m, rhs)  # compatibility (mean-zero vs m)
        A = -G + np.outer(np.ones(d), m)  # pin m.u=0
        u = np.linalg.solve(A, rhs)
        u = u - np.mean(u)
    G, H, _ = pol(u)
    m = stat_dist(G)
    lam = -float(np.dot(m, H + c0 * m + b / d))
    return u, m, lam

ub, mb, lamb = solve_erg()
print("ergodic: u=", np.round(ub, 4), "m=", np.round(mb, 4), "lam=", round(lamb, 4))
print("positivity: min(mb)=", mb.min())
for r in [0.4, 0.2, 0.1, 0.05, 0.025]:
    V, m = solve_disc(r)
    em = float(np.linalg.norm(m - mb)); ev = float(np.linalg.norm(r * V - lamb))
    print(f"r={r:.3f} |m-mbar|={em:.6f} /r={em/r:.4f} |rV-lam|={ev:.6f} /r={ev/r:.4f}")
