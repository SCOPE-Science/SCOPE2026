"""Bounded test: axisymmetric (m=0) Jacobi gap scan for equal-volume S^3 double bubble.

Part A: equilibrium profile table (tan d / tan R = 1/2, cos R = cos d cos rho).
Part B: per-sheet radial Neumann eigenvalue shooting vs Jacobi potentials.
Part C: coupled finite-difference generalized eigenproblem with junction elimination
        and volume projection (junction boundary term B omitted and flagged).
Stdlib + numpy only.
"""
import numpy as np
import json

PI = np.pi
VOL = 2 * PI ** 2


def profile(R):
    dc = float(np.arctan(0.5 * np.tan(R)))
    rho = float(np.arccos(np.cos(R) / np.cos(dc)))
    return dc, rho


def region_vol(R, dc, n=4000):
    h = (R - dc) / n
    t = np.tan(dc)
    s = 0.0
    for i in range(n + 1):
        r = dc + i * h
        w = 1.0 if (i == 0 or i == n) else (4.0 if i % 2 else 2.0)
        s += w * (1.0 + t / np.tan(r)) * (np.sin(r) ** 2)
    cap = PI * (2 * dc - np.sin(2 * dc))
    return cap + 2 * PI * s * h / 3.0


def find_R(vf):
    lo, hi = 0.05, 1.45
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        dc, _ = profile(mid)
        if region_vol(mid, dc) / VOL < vf:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def shoot_neumann(L, lam, nsteps=4000):
    """Integrate u'' + cot_a u' + lam u = 0 on (0,L], u(0)=1,u'(0)=0.
    cot_a(t) = (1/a)cot(t/a) with a = L*3/pi for outer sheets, a=1 separator.
    Here pass a explicitly. Returns u'(L)."""
    raise NotImplementedError


def shoot_neumann_a(L, a, lam, nsteps=6000):
    t0 = 1e-7
    u = 1.0 - lam * t0 * t0 / 4.0
    v = -lam * t0 / 2.0
    h = (L - t0) / nsteps
    t = t0
    for _ in range(nsteps):
        def f(tt, uu, vv):
            c = (1.0 / a) / np.tan(tt / a) if tt / a > 1e-12 else 1.0 / max(tt, 1e-300)
            return vv, -c * vv - lam * uu
        k1u, k1v = f(t, u, v)
        k2u, k2v = f(t + h / 2, u + h * k1u / 2, v + h * k1v / 2)
        k3u, k3v = f(t + h / 2, u + h * k2u / 2, v + h * k2v / 2)
        k4u, k4v = f(t + h, u + h * k3u, v + h * k3v)
        u += h * (k1u + 2 * k2u + 2 * k3u + k4u) / 6.0
        v += h * (k1v + 2 * k2v + 2 * k3v + k4v) / 6.0
        t += h
    return v


def first_neumann(L, a):
    glo = 1e-6
    g = shoot_neumann_a(L, a, glo)
    lam = 0.05
    while lam < 500:
        g2 = shoot_neumann_a(L, a, lam)
        if g2 > 0:
            lo, hi = lam - 0.05 if lam > 0.05 else glo, lam
            glo_val = shoot_neumann_a(L, a, lo)
            for _ in range(50):
                mid = 0.5 * (lo + hi)
                gm = shoot_neumann_a(L, a, mid)
                if gm > 0:
                    hi = mid
                else:
                    lo = mid
            return 0.5 * (lo + hi)
        lam += 0.05 if lam < 5 else 0.5
    return float("nan")


def killing_mode(R, dc, rho, t_out, s_sep):
    """Axial Killing K = x1 d4 - x4 d1 normal components on outer sheet 1 and separator.
    Axis = x1-axis. C+ = (cos d, sin d,0,0). Sheet: S(C+,R), axisymmetric الإسلام..."""
    a = np.sin(R)
    # outer sheet 1: pole P = point on axis beyond C+: P = cos(R-d)... pole at angle (dc+R) on x1-axis? 
    # Points: gamma(zt) = cos R * C+ + sin R * (cos(zt/a) * E + sin(zt/a) * F)
    # with E = axis direction at C+ (unit vector in x1x2-plane perp to C+ pointing +x1-ish),
    # F = (0,0,1,0)-type transverse. Normal n = -sin R C+ + cos R (cos E + sin F).
    E = np.array([-np.sin(dc), np.cos(dc), 0.0, 0.0])
    Cp = np.array([np.cos(dc), np.sin(dc), 0.0, 0.0])
    F = np.array([0.0, 0.0, 1.0, 0.0])
    phi = np.zeros_like(t_out)
    for j, zt in enumerate(t_out):
        th = zt / a
        N = -np.sin(R) * Cp + np.cos(R) * (np.cos(th) * E + np.sin(th) * F)
        X = np.cos(R) * Cp + np.sin(R) * (np.cos(th) * E + np.sin(th) * F)
        K = np.array([X[3], 0.0, 0.0, -X[0]])  # x1 d4 - x4 d1? K^1 = -x4? K = x4*e1... define K = (x4,0,0,-x1)
        # K = x4 d1 - x1 d4 gives rotation; normal comp:
        phi[j] = K @ N
    # separator: disk x1=0: X = (0, sin s cosφ, sin s sinφ, cos s); normal e1; K^1 = x4 = cos s
    return phi, np.cos(s_sep)


def coupled_gap(R, dc, rho, N=140, M=140):
    a = np.sin(R)
    T = (PI / 3.0) * a
    Vout = 2.0 / a ** 2
    Vsep = 2.0
    # grids (cell-centered FD for -d(w d)/w + V); build stiffness via nodal differences
    t = np.linspace(0, T, N + 1)
    s = np.linspace(0, rho, M + 1)
    wo = a * np.sin(t / a)
    ws = np.sin(s)
    wo[0] = 0.0
    ws[0] = 0.0

    def assemble(L_nodes, w, V):
        n = len(L_nodes) - 1  # intervals; unknowns 0..n (node n = junction end)
        h = L_nodes[1] - L_nodes[0]
        # stiffness K[i,j]: int (u')^2 w, piecewise linear; mass lumped
        K = np.zeros((n + 1, n + 1))
        Wm = np.zeros((n + 1, n + 1))
        for i in range(n):
            wm = 0.5 * (w[i] + w[i + 1])
            e = wm / h
            K[i, i] += e
            K[i, i + 1] -= e
            K[i + 1, i] -= e
            K[i + 1, i + 1] += e
            Wm[i, i] += 0.5 * w[i] * h
            Wm[i + 1, i + 1] += 0.5 * w[i + 1] * h
        # pole regularity: node 0 equation fine with w=0 weights
        return K - V * Wm, Wm

    Ko, Wo = assemble(t, wo, Vout)
    Ks, Ws = assemble(s, ws, Vsep)
    # block system: [outer1 (N+1), outer2 (N+1), sep (M+1)]
    n1 = N + 1
    nall = 2 * n1 + (M + 1)
    K = np.zeros((nall, nall))
    W = np.zeros((nall, nall))
    K[:n1, :n1] = Ko
    K[n1:2 * n1, n1:2 * n1] = Ko
    K[2 * n1:, 2 * n1:] = Ks
    W[:n1, :n1] = Wo
    W[n1:2 * n1, n1:2 * n1] = Wo
    W[2 * n1:, 2 * n1:] = Ws
    # constraints: junction u1[N]+u2[N]-u3[M]=0 (sign conv.; scoping), vol1, vol2
    cJ = np.zeros(nall)
    cJ[N] = 1.0
    cJ[n1 + N] = 1.0
    cJ[-1] = -1.0
    # volume rows: int u w over sheets (lumped weights); sep sign: region1 += sep, region2 -= sep
    do1 = np.diag(Wo).copy()
    dse = np.diag(Ws).copy()
    cV1 = np.zeros(nall)
    cV1[:n1] = do1
    cV1[2 * n1:] = dse
    cV2 = np.zeros(nall)
    cV2[n1:2 * n1] = do1
    cV2[2 * n1:] = -dse
    C = np.vstack([cJ, cV1, cV2])
    # null space via SVD
    U, Sg, Vt = np.linalg.svd(C, full_matrices=True)
    Z = Vt[3:, :].T
    Kr = Z.T @ K @ Z
    Wr = Z.T @ W @ Z
    vals, vecs = np.linalg.eig(np.linalg.solve(Wr, Kr))
    vals = np.sort(np.real(vals))
    # translation-mode correlation: build phi_K vector, project, Rayleigh quotient
    phi_o, phi_s = killing_mode(R, dc, rho, t, s)
    ph = np.concatenate([phi_o, phi_o, phi_s])
    # project onto constraint null space
    coef = Z.T @ (W @ ph)
    G = Z.T @ W @ Z
    alpha = np.linalg.solve(G, coef)
    phn = Z @ alpha
    rq = (phn @ (K @ phn)) / (phn @ (W @ phn))
    return vals[:6], rq


def main():
    out = {"profile": [], "neumann": [], "coupled": []}
    for vf in [0.05, 0.10, 0.15, 0.20, 0.25, 0.30]:
        R = find_R(vf)
        dc, rho = profile(R)
        a = np.sin(R)
        T = (PI / 3.0) * a
        Vout = 2.0 / a ** 2
        out["profile"].append(dict(vf=vf, R=R, d=dc, rho=rho, T=T, a=a,
                                   Vout=Vout, exterior=1 - 2 * vf))
        lam_sep = first_neumann(rho, 1.0)
        lam_out = first_neumann(T, a)
        out["neumann"].append(dict(vf=vf, lam_sep=lam_sep, lam_out=lam_out,
                                   margin_sep=lam_sep - 2.0 - 0.25,
                                   margin_out=lam_out - Vout - 0.25))
        print(f"vf={vf:.2f} R={R:.4f} d={dc:.4f} rho={rho:.4f} a={a:.4f} "
              f"lam_sep={lam_sep:.3f} (m={lam_sep-2.25:.3f}) "
              f"lam_out={lam_out:.3f} (m={lam_out-Vout-0.25:.3f})", flush=True)
    for rec in out["profile"]:
        vals, rq = coupled_gap(rec["R"], rec["d"], rec["rho"])
        out["coupled"].append(dict(vf=rec["vf"], eigs=[float(v) for v in vals],
                                   killing_RQ=float(rq)))
        print(f"vf={rec['vf']:.2f} coupled eigs={np.round(vals,3)} killingRQ={rq:.4f}",
              flush=True)
    with open("output/artifacts/gap_scan_results.json", "w") as f:
        json.dump(out, f, indent=1)
    print("wrote output/artifacts/gap_scan_results.json")


main()
