"""Numpy-only synthesis of a common augmented LKF with 2nd-order Bessel-Legendre
bound for the Yan-Ozbay 2-mode benchmark (constant delays h1=0.3, h2=0.6).

LMI per mode i: Phi_i(alpha,h_i) < 0, P,Q,R > 0, with
  Phi = E'PD + D'PE + 2a E'PE + diag(Q,-e^{-2ah}Q,0,0)
        + G'(h^2 R)G - e^{-2ah}(C0'RC0 + 3 C1'RC1 + 5 C2'RC2)
zeta = [x(t); x(t-h); v1; v2], v1=(1/h)int x, v2=(1/h^2)int int x (each n=2).
See DRAFT.md for the derivation. This script is the bounded recovery/synthesis test.
"""
import numpy as np, json

A1 = np.array([[-2., 0.], [0., -0.9]]); Ab1 = np.array([[-1., 0.], [-0.5, -1.]])
A2 = np.array([[-1., 0.5], [0., -1.]]); Ab2 = np.array([[-1., 0.], [0.1, -1.]])
H1, H2 = 0.3, 0.6
I2 = np.eye(2); Z2 = np.zeros((2, 2))

def build_Phi(A, Ab, h, a, P, Q, R):
    E = np.block([[I2, Z2, Z2, Z2],
                  [Z2, Z2, I2, Z2],
                  [Z2, Z2, Z2, I2]])                      # 6x8
    D = np.block([[A, Ab, Z2, Z2],
                  [(1/h)*I2, -(1/h)*I2, Z2, Z2],
                  [(1/h)*I2, Z2, -(1/h)*I2, Z2]])          # 6x8
    G = np.block([A, Ab, Z2, Z2])                          # 2x8
    C0 = np.block([I2, -I2, Z2, Z2])
    C1 = np.block([I2, I2, -2*I2, Z2])
    C2 = np.block([I2, -I2, 6*I2, -12*I2])
    e = np.exp(-2*a*h)
    Phi = E.T @ P @ D + D.T @ P @ E + 2*a*(E.T @ P @ E)
    Phi += np.block([[Q, Z2, Z2, Z2],
                     [Z2, -e*Q, Z2, Z2],
                     [Z2, Z2, Z2, Z2],
                     [Z2, Z2, Z2, Z2]])
    Phi += (h**2) * (G.T @ R @ G)
    Phi -= e * (C0.T @ R @ C0 + 3*(C1.T @ R @ C1) + 5*(C2.T @ R @ C2))
    return 0.5*(Phi + Phi.T)

def unpack(th):
    # th: 27 params. P=MM'+eps (6x6, M lower-tri: 21), Q=NN'+eps (3), R=LL'+eps (3)
    M = np.zeros((6, 6)); idx = 0
    for r in range(6):
        for c in range(r+1):
            M[r, c] = th[idx]; idx += 1
    def sym2(v):
        L = np.array([[v[0], 0.], [v[1], v[2]]]); return L
    N = sym2(th[21:24]); L = sym2(th[24:27])
    eps = 1e-6
    return M@M.T + eps*np.eye(6), N@N.T + eps*I2, L@L.T + eps*I2

def maxeig_sym(M):
    return float(np.linalg.eigvalsh(M)[-1])

def objective(th, a):
    P, Q, R = unpack(th)
    f1 = maxeig_sym(build_Phi(A1, Ab1, H1, a, P, Q, R))
    f2 = maxeig_sym(build_Phi(A2, Ab2, H2, a, P, Q, R))
    return max(f1, f2), f1, f2

def search(a, iters=30000, sigma0=0.12, seed=0):
    rng = np.random.default_rng(seed)
    best = None; bestf = np.inf
    th = np.zeros(27)
    th[0], th[7], th[13], th[18], th[22] = 1.0, 1.0, 1.0, 1.0, 1.0  # near-identity start
    th[21] = 0.7; th[23] = 0.7; th[24] = 0.3; th[26] = 0.3
    cur = th.copy(); curf, _, _ = objective(cur, a)
    for it in range(iters):
        sig = sigma0 * (1.0 - it/iters) + 0.002
        prop = cur + sig * rng.standard_normal(27)
        f, _, _ = objective(prop, a)
        if f < curf:
            cur, curf = prop, f
            if f < bestf:
                bestf, best = f, prop.copy()
        if bestf < -1e-6:
            pass
    return best, bestf

if __name__ == "__main__":
    import sys
    alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 0.3
    seed0 = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    out = sys.argv[3] if len(sys.argv) > 3 else "output/artifacts/synth_result.json"
    best_over, fover = None, np.inf
    for s in range(6):
        b, f = search(alpha, iters=25000, sigma0=0.12, seed=seed0*100+s)
        print(f"restart {s}: best maxeig = {f:.6f}", flush=True)
        if f < fover:
            fover, best_over = f, b
    P, Q, R = unpack(best_over)
    f, f1, f2 = objective(best_over, alpha)
    res = {"alpha": alpha, "maxeig": f, "mode1": f1, "mode2": f2,
           "minP": float(np.linalg.eigvalsh(P)[0]),
           "minQ": float(np.linalg.eigvalsh(Q)[0]),
           "minR": float(np.linalg.eigvalsh(R)[0]),
           "P": P.tolist(), "Q": Q.tolist(), "R": R.tolist()}
    with open(out, "w") as fh:
        json.dump(res, fh)
    print(f"ALPHA={alpha} OVERALL={f:.6f} M1={f1:.6f} M2={f2:.6f} "
          f"minP={res['minP']:.3e} minQ={res['minQ']:.3e} minR={res['minR']:.3e}")
    print("FEASIBLE" if (f < -1e-6 and res['minP'] > 0 and res['minQ'] > 0 and res['minR'] > 0) else "NOT_FEASIBLE")
